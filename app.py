from flask import Flask, render_template, request, jsonify, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import db, User, WeeklyQuest, MarketplaceItem, LeaderboardEntry, DailyQuest
from tracks_data import TRACKS_DATA
from datetime import datetime, timedelta
import os
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'skillspark-secure-session-key-2026')

# Support both SQLite (local) and PostgreSQL (production)
database_url = os.environ.get('DATABASE_URL', 'sqlite:///skillspark.db')
# Fix PostgreSQL URL scheme (psycopg2 vs postgresql)
if database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'index' 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html', tracks=TRACKS_DATA)

@app.route('/track/<track_slug>')
def track_detail(track_slug):
    track = TRACKS_DATA.get(track_slug)
    if not track:
        return redirect(url_for('index'))
    return render_template('track_detail.html', track=track)

@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email', '').strip().lower()
    password = data.get('password', '')

    # Validate email format
    if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
        return jsonify({'error': 'Invalid email format'}), 400

    # Validate password strength
    if len(password) < 8:
        return jsonify({'error': 'Password must be at least 8 characters'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already registered'}), 400

    new_user = User(email=email, password_hash=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()
    login_user(new_user)
    return jsonify({'success': 'Account created'})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email', '').strip().lower()
    password = data.get('password', '')

    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password_hash, password):
        login_user(user)
        return jsonify({'success': 'Logged in'})
    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/api/update_progress', methods=['POST'])
@login_required
def update_progress():
    data = request.get_json()
    if 'path' in data:
        current_user.recommended_path = data['path']
        # Initialize XP for new path if not exists
        xp_data = current_user.xp_data or {}
        if data['path'] not in xp_data:
            xp_data[data['path']] = 0
            current_user.xp_data = xp_data
    if 'explored' in data:
        current_user.last_explored = data['explored']
    db.session.commit()
    return jsonify({'success': True})

@app.route('/api/generate_roadmap', methods=['POST'])
def generate_roadmap():
    data = request.get_json()
    skill = data.get('skill', 'Software Engineering')
    time_per_day = data.get('time', '1')
    budget = data.get('budget', '0')
    
    timeline = f"{max(1, 12 // int(time_per_day))} Weeks"
    
    curriculums = {
        'Software Engineering': {'steps': ["Logic Fundamentals", "Version Control (Git)", "Frontend Architecture", "Database Modeling"], 'tools': "VS Code, GitHub, Vercel" if budget == "0" else "WebStorm, AWS, GitHub Pro"},
        'AI & Machine Learning': {'steps': ["Python & Math Foundations", "Data Wrangling & Scikit-Learn", "Deep Learning Architectures", "LLM Prompting & Model Fine-Tuning"], 'tools': "Google Colab, PyTorch, Hugging Face" if budget == "0" else "AWS SageMaker, OpenAI API, Weights & Biases"},
        'Cybersecurity': {'steps': ["Networking & Linux Internals", "Security Architecture & Cryptography", "Penetration Testing & Exploits", "Incident Response & SIEM Monitoring"], 'tools': "Kali Linux, Wireshark, Nmap" if budget == "0" else "Burp Suite Pro, Splunk, HackTheBox VIP"},
        'Cloud & DevOps': {'steps': ["Linux Administration & Bash", "Docker Containerization", "Kubernetes Orchestration", "CI/CD & Infrastructure as Code (Terraform)"], 'tools': "Docker, GitHub Actions, Minikube" if budget == "0" else "AWS Solutions Architect, Terraform Cloud, Datadog"},
        'Data Science': {'steps': ["Advanced SQL & Relational Querying", "Pandas Exploratory Data Analysis", "Statistical Inference & Machine Learning", "Executive BI Dashboards & Storytelling"], 'tools': "PostgreSQL, Jupyter, PowerBI Desktop" if budget == "0" else "Snowflake, Tableau Cloud, Databricks"},
        'Product Design': {'steps': ["Typography Basics", "Wireframing", "High-Fidelity Prototyping", "Design Systems"], 'tools': "Figma (Free)" if budget == "0" else "Figma Pro, Spline 3D, Adobe CC"},
        'Post-Production': {'steps': ["NLE Timeline Basics", "A-Roll/B-Roll Sync", "Color Correction", "Sound Design"], 'tools': "DaVinci Resolve" if budget == "0" else "Premiere Pro, After Effects"},
        'Audio Engineering': {'steps': ["DAW Navigation", "Beat Sequencing", "EQ & Compression", "Track Mastering"], 'tools': "BandLab, Audacity" if budget == "0" else "Ableton Live, FL Studio, Serum"},
        'Game Development': {'steps': ["Engine Basics", "C#/C++ Scripting", "Level Design", "Publishing"], 'tools': "Unity (Free), Godot" if budget == "0" else "Unreal Engine, Blender, Maya"},
        'Digital Content': {'steps': ["Niche Discovery", "Scriptwriting", "Thumbnail Psychology", "Algorithm Analytics"], 'tools': "CapCut, Canva" if budget == "0" else "Final Cut Pro, Photoshop"}
    }
    
    curriculum = curriculums.get(skill, curriculums['Software Engineering'])
    
    return jsonify({
        'timeline': timeline,
        'steps': curriculum['steps'],
        'tools': curriculum['tools'],
        'investment': 'Free/Open Source' if budget == "0" else 'Premium Tools Advised'
    })

# --- NAYE ROUTES (DASHBOARD & XP) ---

@app.route('/api/user_data', methods=['GET'])
@login_required
def get_user_data():
    """Return user XP and coins data from database for page load sync"""
    path = current_user.recommended_path
    xp_data = current_user.xp_data or {}
    xp_points = xp_data.get(path, 0)

    return jsonify({
        'xp_points': xp_points,
        'total_xp': current_user.total_xp or 0,
        'marketplace_xp': current_user.marketplace_xp or 0,
        'spendable_coins': current_user.spendable_coins or 0,
        'total_coins': current_user.total_coins or 0,
        'path': path
    })

@app.route('/dashboard')
@login_required
def dashboard():
    career_content = {
        'Software Engineering': {
            'tasks': [
                {'title': 'Master Frontend Basics', 'desc': 'Complete an HTML, CSS, and JS crash course.', 'xp': 100},
                {'title': 'Version Control (Git)', 'desc': 'Set up GitHub and push your first repository.', 'xp': 150},
                {'title': 'Build a Web App', 'desc': 'Create and deploy a simple React application.', 'xp': 200},
                {'title': 'Database Integration', 'desc': 'Connect your app to a SQL or NoSQL database.', 'xp': 250},
                {'title': 'Full-Stack Deployment', 'desc': 'Host your app live on Vercel or Render.', 'xp': 300}
            ],
            'resources': [
                {'name': 'FreeCodeCamp', 'url': 'https://freecodecamp.org', 'icon': 'fa-laptop-code'},
                {'name': 'The Odin Project', 'url': 'https://theodinproject.com', 'icon': 'fa-book-open'}
            ]
        },
        'AI & Machine Learning': {
            'tasks': [
                {'title': 'Python & Linear Algebra', 'desc': 'Master NumPy, vector operations, and matrix algebra.', 'xp': 100},
                {'title': 'Exploratory Machine Learning', 'desc': 'Train regression and classification models in Scikit-Learn.', 'xp': 150},
                {'title': 'Deep Neural Networks', 'desc': 'Build a multi-layer perceptron and CNN in PyTorch.', 'xp': 200},
                {'title': 'LLM Integration & Prompt Chains', 'desc': 'Build a Retrieval-Augmented Generation (RAG) agent with LangChain.', 'xp': 250},
                {'title': 'Model Serving & Inference', 'desc': 'Deploy an open-source model endpoint on Hugging Face or Docker.', 'xp': 300}
            ],
            'resources': [
                {'name': 'Fast.ai Practical Deep Learning', 'url': 'https://course.fast.ai', 'icon': 'fa-brain'},
                {'name': 'Hugging Face NLP Course', 'url': 'https://huggingface.co/learn', 'icon': 'fa-microchip'}
            ]
        },
        'Cybersecurity': {
            'tasks': [
                {'title': 'Linux & TCP/IP Networking', 'desc': 'Configure virtual subnets, firewalls, and analyze packet captures.', 'xp': 100},
                {'title': 'Reconnaissance & Port Scanning', 'desc': 'Audit attack surfaces using Nmap, Shodan, and Wireshark.', 'xp': 150},
                {'title': 'Web Application Exploitation', 'desc': 'Identify and exploit OWASP Top 10 vulnerabilities (SQLi, XSS).', 'xp': 200},
                {'title': 'Privilege Escalation', 'desc': 'Crack password hashes and escalate privileges on target Linux/Windows machines.', 'xp': 250},
                {'title': 'Defensive SIEM & Hardening', 'desc': 'Set up log ingestion rules and harden system configurations.', 'xp': 300}
            ],
            'resources': [
                {'name': 'TryHackMe Cyber Defense', 'url': 'https://tryhackme.com', 'icon': 'fa-shield-halved'},
                {'name': 'OverTheWire Wargames', 'url': 'https://overthewire.org', 'icon': 'fa-terminal'}
            ]
        },
        'Cloud & DevOps': {
            'tasks': [
                {'title': 'Linux Administration & Bash', 'desc': 'Automate server tasks with shell scripts and cron jobs.', 'xp': 100},
                {'title': 'Containerization with Docker', 'desc': 'Write multi-stage Dockerfiles and deploy multi-service Docker Compose apps.', 'xp': 150},
                {'title': 'CI/CD Automated Pipelines', 'desc': 'Build automated test-and-deploy pipelines with GitHub Actions.', 'xp': 200},
                {'title': 'Kubernetes Cluster Orchestration', 'desc': 'Deploy pods, services, ingress, and auto-scaling rules.', 'xp': 250},
                {'title': 'Infrastructure as Code (IaC)', 'desc': 'Provision cloud infrastructure declaratively using Terraform.', 'xp': 300}
            ],
            'resources': [
                {'name': 'DevOps Roadmap (roadmap.sh)', 'url': 'https://roadmap.sh/devops', 'icon': 'fa-cloud'},
                {'name': 'Kubernetes Official Interactive Labs', 'url': 'https://kubernetes.io/docs/tutorials', 'icon': 'fa-cubes-stacked'}
            ]
        },
        'Data Science': {
            'tasks': [
                {'title': 'Advanced SQL & Joins', 'desc': 'Write complex CTEs, window functions, and aggregation queries.', 'xp': 100},
                {'title': 'Python Pandas & Data Cleaning', 'desc': 'Clean, transform, and impute real-world messy datasets.', 'xp': 150},
                {'title': 'Statistical Testing & A/B Experiments', 'desc': 'Formulate hypotheses and calculate p-values for feature impact.', 'xp': 200},
                {'title': 'Predictive Modeling & Feature Engineering', 'desc': 'Build XGBoost and random forest models with hyperparameter tuning.', 'xp': 250},
                {'title': 'Executive Dashboard & Storytelling', 'desc': 'Design high-impact KPI dashboards with drill-downs in PowerBI/Tableau.', 'xp': 300}
            ],
            'resources': [
                {'name': 'Kaggle Learn & Datasets', 'url': 'https://kaggle.com/learn', 'icon': 'fa-chart-pie'},
                {'name': 'Mode Analytics SQL Tutorial', 'url': 'https://mode.com/sql-tutorial', 'icon': 'fa-database'}
            ]
        },
        'Product Design': {
            'tasks': [
                {'title': 'UI/UX Theory', 'desc': 'Learn color theory, typography, and layout spacing.', 'xp': 100},
                {'title': 'Low-Fi Wireframing', 'desc': 'Sketch layout concepts for a 3-page mobile app.', 'xp': 150},
                {'title': 'Master Figma Components', 'desc': 'Build a reusable design system (buttons, navbars).', 'xp': 200},
                {'title': 'Interactive Prototyping', 'desc': 'Link your screens together with smooth animations.', 'xp': 250},
                {'title': 'User Testing & Handoff', 'desc': 'Prepare your file for developer handoff.', 'xp': 300}
            ],
            'resources': [
                {'name': 'Figma Community Files', 'url': 'https://figma.com/community', 'icon': 'fa-pen-nib'},
                {'name': 'Laws of UX', 'url': 'https://lawsofux.com', 'icon': 'fa-eye'}
            ]
        },
        'Post-Production': {
            'tasks': [
                {'title': 'NLE Setup & Basics', 'desc': 'Import footage and learn timeline shortcuts.', 'xp': 100},
                {'title': 'The Rough Cut', 'desc': 'Sync A-roll and B-roll to build your narrative.', 'xp': 150},
                {'title': 'Color Correction', 'desc': 'Balance exposure, contrast, and white balance.', 'xp': 200},
                {'title': 'Sound Design', 'desc': 'Add SFX, background music, and audio transitions.', 'xp': 250},
                {'title': 'Final Render', 'desc': 'Export in the correct format and codec for the web.', 'xp': 300}
            ],
            'resources': [
                {'name': 'DaVinci Resolve Training', 'url': 'https://blackmagicdesign.com', 'icon': 'fa-video'},
                {'name': 'Mixkit Free Assets', 'url': 'https://mixkit.co', 'icon': 'fa-film'}
            ]
        },
        'Audio Engineering': {
            'tasks': [
                {'title': 'DAW Workspace Setup', 'desc': 'Configure your audio interface and project BPM.', 'xp': 100},
                {'title': 'Beat Sequencing', 'desc': 'Program a drum pattern and lay down a bassline.', 'xp': 150},
                {'title': 'Recording Vocals/Instruments', 'desc': 'Record a clean take with proper gain staging.', 'xp': 200},
                {'title': 'Mixing (EQ & Compression)', 'desc': 'Balance the frequencies and dynamics of your tracks.', 'xp': 250},
                {'title': 'Mastering', 'desc': 'Bring the track to commercial loudness standards.', 'xp': 300}
            ],
            'resources': [
                {'name': 'BandLab Online DAW', 'url': 'https://bandlab.com', 'icon': 'fa-music'},
                {'name': 'Ableton Learn Music', 'url': 'https://learningmusic.ableton.com', 'icon': 'fa-sliders'}
            ]
        },
        'Game Development': {
            'tasks': [
                {'title': 'Engine Installation', 'desc': 'Download Unity/Unreal and create your first 3D scene.', 'xp': 100},
                {'title': 'Player Controller', 'desc': 'Write code to make a character move and jump.', 'xp': 150},
                {'title': 'Level Design', 'desc': 'Build an environment with lighting and obstacles.', 'xp': 200},
                {'title': 'Enemy Logic (AI)', 'desc': 'Create a basic enemy that chases the player.', 'xp': 250},
                {'title': 'Publish Build', 'desc': 'Compile your game into an executable file.', 'xp': 300}
            ],
            'resources': [
                {'name': 'Unity Learn', 'url': 'https://learn.unity.com', 'icon': 'fa-gamepad'},
                {'name': 'Kenney Free Assets', 'url': 'https://kenney.nl', 'icon': 'fa-cubes'}
            ]
        },
        'Digital Content': {
            'tasks': [
                {'title': 'Niche & Strategy', 'desc': 'Define your target audience and content pillars.', 'xp': 100},
                {'title': 'Scripting & Hooks', 'desc': 'Write an engaging script with a 3-second hook.', 'xp': 150},
                {'title': 'Recording & Lighting', 'desc': 'Film your first video with clear audio and lighting.', 'xp': 200},
                {'title': 'Dynamic Editing', 'desc': 'Add captions, b-roll, and pacing cuts.', 'xp': 250},
                {'title': 'Thumbnail & SEO Upload', 'desc': 'Design a high-CTR thumbnail and optimize titles.', 'xp': 300}
            ],
            'resources': [
                {'name': 'YouTube Creator Academy', 'url': 'https://creatoracademy.youtube.com', 'icon': 'fa-youtube'},
                {'name': 'Canva Design School', 'url': 'https://canva.com', 'icon': 'fa-paintbrush'}
            ]
        }
    }

    path_data = career_content.get(current_user.recommended_path, None)
    track_info = next((t for t in TRACKS_DATA.values() if t['name'].lower() == (current_user.recommended_path or '').lower()), None)

    path = current_user.recommended_path
    xp_data = current_user.xp_data or {}
    xp_points = xp_data.get(path, 0)

    # Naya Ranking System (Target: 1000 XP)
    level = "Novice Explorer"
    if xp_points >= 400:
        level = "Intermediate Builder"
    if xp_points >= 900:
        level = "Advanced Creator"

    return render_template('dashboard.html', level=level, path_data=path_data, track_info=track_info, xp_points=xp_points)

@app.route('/api/add_xp', methods=['POST'])
@login_required
def add_xp():
    data = request.get_json()
    points = data.get('points', 0)
    path = current_user.recommended_path

    xp_data = current_user.xp_data or {}
    xp_data[path] = xp_data.get(path, 0) + points
    current_user.xp_data = xp_data
    db.session.commit()

    return jsonify({
        'success': True,
        'new_xp': xp_data[path],
        'user_id': current_user.id
    })

# --- TRACK-SPECIFIC QUEST TEMPLATES ---
TRACK_QUEST_TEMPLATES = {
    'Software Engineering': [
        {'title': 'Master Git Workflows', 'desc': 'Set up and push your first GitHub repo with branches and commits.', 'icon': 'fa-code-branch', 'difficulty': 'Easy', 'coins': 10},
        {'title': 'Build a React Component', 'desc': 'Create a reusable React component with props and state.', 'icon': 'fa-react', 'difficulty': 'Easy', 'coins': 10},
        {'title': 'Write API Endpoints', 'desc': 'Design and build 3 RESTful API endpoints in Node.js or Flask.', 'icon': 'fa-code', 'difficulty': 'Medium', 'coins': 25},
        {'title': 'Debug Production Issue', 'desc': 'Find and fix a bug in deployed code using DevTools and logs.', 'icon': 'fa-bug', 'difficulty': 'Medium', 'coins': 25},
        {'title': 'Deploy Full-Stack App', 'desc': 'Ship a complete app to production (frontend + backend + database).', 'icon': 'fa-rocket', 'difficulty': 'Hard', 'coins': 50},
        {'title': 'Optimize Performance', 'desc': 'Reduce load time by 50% using caching, compression, or CDN.', 'icon': 'fa-bolt', 'difficulty': 'Hard', 'coins': 50},
    ],
    'AI & Machine Learning': [
        {'title': 'Learn Linear Algebra', 'desc': 'Study vectors, matrices, and eigenvalues with NumPy.', 'icon': 'fa-square-root-variable', 'difficulty': 'Easy', 'coins': 10},
        {'title': 'Build Classification Model', 'desc': 'Train a Scikit-Learn classifier and evaluate accuracy metrics.', 'icon': 'fa-chart-bar', 'difficulty': 'Easy', 'coins': 10},
        {'title': 'Create Neural Network', 'desc': 'Build and train a 3-layer neural network in PyTorch.', 'icon': 'fa-brain', 'difficulty': 'Medium', 'coins': 25},
        {'title': 'Fine-Tune LLM', 'desc': 'Fine-tune a pre-trained model on custom dataset with Hugging Face.', 'icon': 'fa-wand-magic-sparkles', 'difficulty': 'Medium', 'coins': 25},
        {'title': 'Deploy ML Model', 'desc': 'Create production API serving your trained model with FastAPI.', 'icon': 'fa-rocket', 'difficulty': 'Hard', 'coins': 50},
        {'title': 'Build RAG System', 'desc': 'Implement Retrieval-Augmented Generation with LangChain.', 'icon': 'fa-magnifying-glass', 'difficulty': 'Hard', 'coins': 50},
    ],
    'Cybersecurity': [
        {'title': 'Learn Network Basics', 'desc': 'Study TCP/IP, DNS, and packet structure with Wireshark.', 'icon': 'fa-network-wired', 'difficulty': 'Easy', 'coins': 10},
        {'title': 'Scan for Vulnerabilities', 'desc': 'Use Nmap and OpenVAS to identify open ports and services.', 'icon': 'fa-magnifying-glass', 'difficulty': 'Easy', 'coins': 10},
        {'title': 'Crack Password Hash', 'desc': 'Use hashcat to brute-force and crack MD5/SHA hashes ethically.', 'icon': 'fa-key', 'difficulty': 'Medium', 'coins': 25},
        {'title': 'Exploit Web Vulnerability', 'desc': 'Find and exploit SQL injection or XSS in vulnerable web app.', 'icon': 'fa-shield-halved', 'difficulty': 'Medium', 'coins': 25},
        {'title': 'Privilege Escalate', 'desc': 'Escalate from user to root on Linux/Windows target.', 'icon': 'fa-crown', 'difficulty': 'Hard', 'coins': 50},
        {'title': 'Build SIEM Rule', 'desc': 'Create detection rules in Splunk/ELK for suspicious activity.', 'icon': 'fa-eye', 'difficulty': 'Hard', 'coins': 50},
    ],
    'Cloud & DevOps': [
        {'title': 'Learn Bash Scripting', 'desc': 'Write shell scripts to automate server tasks and backups.', 'icon': 'fa-terminal', 'difficulty': 'Easy', 'coins': 10},
        {'title': 'Containerize App', 'desc': 'Create multi-stage Dockerfile and push image to Docker Hub.', 'icon': 'fa-cube', 'difficulty': 'Easy', 'coins': 10},
        {'title': 'Build CI/CD Pipeline', 'desc': 'Set up automated testing and deployment with GitHub Actions.', 'icon': 'fa-arrows-spin', 'difficulty': 'Medium', 'coins': 25},
        {'title': 'Deploy with Kubernetes', 'desc': 'Create and manage pods, services, and ingress on K8s cluster.', 'icon': 'fa-cubes-stacked', 'difficulty': 'Medium', 'coins': 25},
        {'title': 'Infrastructure as Code', 'desc': 'Provision AWS resources with Terraform and version control.', 'icon': 'fa-code', 'difficulty': 'Hard', 'coins': 50},
        {'title': 'Monitor Production', 'desc': 'Set up Prometheus/Grafana monitoring and alerting rules.', 'icon': 'fa-chart-line', 'difficulty': 'Hard', 'coins': 50},
    ],
    'Data Science': [
        {'title': 'Master SQL Queries', 'desc': 'Write complex queries with JOINs, CTEs, and window functions.', 'icon': 'fa-database', 'difficulty': 'Easy', 'coins': 10},
        {'title': 'Clean Real Dataset', 'desc': 'Handle missing values, outliers, and data transformation with Pandas.', 'icon': 'fa-broom', 'difficulty': 'Easy', 'coins': 10},
        {'title': 'Statistical Hypothesis Test', 'desc': 'Design and execute A/B test with statistical significance.', 'icon': 'fa-chart-pie', 'difficulty': 'Medium', 'coins': 25},
        {'title': 'Feature Engineering', 'desc': 'Create 10+ derived features to improve model accuracy.', 'icon': 'fa-wand-magic-sparkles', 'difficulty': 'Medium', 'coins': 25},
        {'title': 'Build Predictive Model', 'desc': 'Train XGBoost model with hyperparameter tuning and validation.', 'icon': 'fa-crystal-ball', 'difficulty': 'Hard', 'coins': 50},
        {'title': 'Create BI Dashboard', 'desc': 'Build interactive Tableau/PowerBI dashboard with KPIs.', 'icon': 'fa-chart-column', 'difficulty': 'Hard', 'coins': 50},
    ],
    'Product Design': [
        {'title': 'Study Color Theory', 'desc': 'Learn color psychology, harmony, and accessibility principles.', 'icon': 'fa-palette', 'difficulty': 'Easy', 'coins': 10},
        {'title': 'Sketch Wireframes', 'desc': 'Create low-fidelity wireframes for 5-page mobile app.', 'icon': 'fa-pen-nib', 'difficulty': 'Easy', 'coins': 10},
        {'title': 'Build Design System', 'desc': 'Create reusable components library in Figma with variants.', 'icon': 'fa-layer-group', 'difficulty': 'Medium', 'coins': 25},
        {'title': 'Design Microinteractions', 'desc': 'Add smooth animations and feedback to UI components.', 'icon': 'fa-sparkles', 'difficulty': 'Medium', 'coins': 25},
        {'title': 'Prototype Interactive Flow', 'desc': 'Create clickable prototype with user flow and transitions.', 'icon': 'fa-arrow-pointer', 'difficulty': 'Hard', 'coins': 50},
        {'title': 'User Test Design', 'desc': 'Conduct user testing session and incorporate feedback.', 'icon': 'fa-users', 'difficulty': 'Hard', 'coins': 50},
    ],
    'Post-Production': [
        {'title': 'Master Timeline Editing', 'desc': 'Learn NLE keyboard shortcuts and cut together a 5-min sequence.', 'icon': 'fa-film', 'difficulty': 'Easy', 'coins': 10},
        {'title': 'Sync Audio & Video', 'desc': 'Synchronize A-roll and B-roll to build narrative flow.', 'icon': 'fa-compact-disc', 'difficulty': 'Easy', 'coins': 10},
        {'title': 'Color Grade Footage', 'desc': 'Use color wheels and curves to grade footage to cinema standard.', 'icon': 'fa-palette', 'difficulty': 'Medium', 'coins': 25},
        {'title': 'Mix Audio', 'desc': 'Balance dialogue, music, and effects with proper levels and EQ.', 'icon': 'fa-sliders', 'difficulty': 'Medium', 'coins': 25},
        {'title': 'Create Motion Graphics', 'desc': 'Build animated titles and lower-thirds with keyframes.', 'icon': 'fa-star', 'difficulty': 'Hard', 'coins': 50},
        {'title': 'Deliver Final Export', 'desc': 'Export to multiple codecs and delivery specs for broadcast.', 'icon': 'fa-download', 'difficulty': 'Hard', 'coins': 50},
    ],
    'Audio Engineering': [
        {'title': 'Setup DAW', 'desc': 'Configure audio interface, routing, and project settings.', 'icon': 'fa-sliders', 'difficulty': 'Easy', 'coins': 10},
        {'title': 'Program Drums', 'desc': 'Sequence drum pattern with velocity variation and quantization.', 'icon': 'fa-drum', 'difficulty': 'Easy', 'coins': 10},
        {'title': 'Record Clean Vocal', 'desc': 'Record vocal track with proper gain staging and microphone technique.', 'icon': 'fa-microphone', 'difficulty': 'Medium', 'coins': 25},
        {'title': 'Mix with EQ & Compression', 'desc': 'Balance frequencies and dynamics on 8+ tracks.', 'icon': 'fa-sliders', 'difficulty': 'Medium', 'coins': 25},
        {'title': 'Master Track', 'desc': 'Bring mix to commercial loudness standards (LUFS compliance).', 'icon': 'fa-volume-high', 'difficulty': 'Hard', 'coins': 50},
        {'title': 'Design Sound Effects', 'desc': 'Create custom SFX from scratch using synthesis and sampling.', 'icon': 'fa-waveform-lines', 'difficulty': 'Hard', 'coins': 50},
    ],
    'Game Development': [
        {'title': 'Learn Game Engine', 'desc': 'Complete tutorials in Unity or Unreal and understand editor.', 'icon': 'fa-gamepad', 'difficulty': 'Easy', 'coins': 10},
        {'title': 'Code Player Controller', 'desc': 'Script character movement, jumping, and collision detection.', 'icon': 'fa-arrow-right', 'difficulty': 'Easy', 'coins': 10},
        {'title': 'Design Level', 'desc': 'Build playable level with terrain, obstacles, and lighting.', 'icon': 'fa-mountain', 'difficulty': 'Medium', 'coins': 25},
        {'title': 'Implement Enemy AI', 'desc': 'Create enemy that patrols, detects player, and attacks.', 'icon': 'fa-robot', 'difficulty': 'Medium', 'coins': 25},
        {'title': 'Build Game Mechanic', 'desc': 'Implement scoring, power-ups, and game state management.', 'icon': 'fa-star', 'difficulty': 'Hard', 'coins': 50},
        {'title': 'Publish Game', 'desc': 'Build executable and publish to Steam or itch.io.', 'icon': 'fa-rocket', 'difficulty': 'Hard', 'coins': 50},
    ],
    'Digital Content': [
        {'title': 'Define Niche', 'desc': 'Research audience, competitors, and content pillars for channel.', 'icon': 'fa-magnifying-glass', 'difficulty': 'Easy', 'coins': 10},
        {'title': 'Write Script', 'desc': 'Write engaging 5-min video script with hook and CTA.', 'icon': 'fa-pen', 'difficulty': 'Easy', 'coins': 10},
        {'title': 'Record Quality Footage', 'desc': 'Film video with proper lighting, audio, and camera work.', 'icon': 'fa-video', 'difficulty': 'Medium', 'coins': 25},
        {'title': 'Edit & Add Effects', 'desc': 'Edit video with captions, B-roll, transitions, and music.', 'icon': 'fa-film', 'difficulty': 'Medium', 'coins': 25},
        {'title': 'Design Thumbnail', 'desc': 'Create high-CTR thumbnail that stands out in feed.', 'icon': 'fa-image', 'difficulty': 'Hard', 'coins': 50},
        {'title': 'Optimize for Algorithm', 'desc': 'Research trending topics and optimize title/description for discovery.', 'icon': 'fa-chart-line', 'difficulty': 'Hard', 'coins': 50},
    ],
}

# --- TRACK-SPECIFIC MARKETPLACE ITEMS ---
TRACK_ITEMS = {
    'Software Engineering': [
        {'name': 'Git Master Badge', 'track': 'Software Engineering', 'rarity': 'rare', 'cost': 150, 'icon': 'fa-code-branch', 'desc': 'Master of version control'},
        {'name': 'React Wizard', 'track': 'Software Engineering', 'rarity': 'epic', 'cost': 250, 'icon': 'fa-wand-magic-sparkles', 'desc': 'Expert in component architecture'},
        {'name': 'Full-Stack Architect', 'track': 'Software Engineering', 'rarity': 'legendary', 'cost': 400, 'icon': 'fa-crown', 'desc': 'End-to-end system designer'},
    ],
    'AI & Machine Learning': [
        {'name': 'Neural Network Architect', 'track': 'AI & Machine Learning', 'rarity': 'rare', 'cost': 150, 'icon': 'fa-brain', 'desc': 'Deep learning expert'},
        {'name': 'LLM Fine-tuner', 'track': 'AI & Machine Learning', 'rarity': 'epic', 'cost': 250, 'icon': 'fa-wand-magic-sparkles', 'desc': 'Large language model specialist'},
        {'name': 'AI Researcher', 'track': 'AI & Machine Learning', 'rarity': 'legendary', 'cost': 400, 'icon': 'fa-crown', 'desc': 'Cutting-edge AI pioneer'},
    ],
    'Cybersecurity': [
        {'name': 'Ethical Hacker', 'track': 'Cybersecurity', 'rarity': 'rare', 'cost': 150, 'icon': 'fa-shield-halved', 'desc': 'Pen-testing champion'},
        {'name': 'Security Architect', 'track': 'Cybersecurity', 'rarity': 'epic', 'cost': 250, 'icon': 'fa-fortress', 'desc': 'System defense expert'},
        {'name': 'Cyber Defender', 'track': 'Cybersecurity', 'rarity': 'legendary', 'cost': 400, 'icon': 'fa-crown', 'desc': 'Guardian of digital infrastructure'},
    ],
    'Cloud & DevOps': [
        {'name': 'DevOps Engineer', 'track': 'Cloud & DevOps', 'rarity': 'rare', 'cost': 150, 'icon': 'fa-gears', 'desc': 'Automation master'},
        {'name': 'Kubernetes Maestro', 'track': 'Cloud & DevOps', 'rarity': 'epic', 'cost': 250, 'icon': 'fa-cubes-stacked', 'desc': 'Container orchestration expert'},
        {'name': 'Cloud Architect', 'track': 'Cloud & DevOps', 'rarity': 'legendary', 'cost': 400, 'icon': 'fa-crown', 'desc': 'Scalable infrastructure designer'},
    ],
    'Data Science': [
        {'name': 'SQL Wizard', 'track': 'Data Science', 'rarity': 'rare', 'cost': 150, 'icon': 'fa-database', 'desc': 'Database query expert'},
        {'name': 'Data Analyst', 'track': 'Data Science', 'rarity': 'epic', 'cost': 250, 'icon': 'fa-chart-pie', 'desc': 'Insight extraction specialist'},
        {'name': 'Data Scientist', 'track': 'Data Science', 'rarity': 'legendary', 'cost': 400, 'icon': 'fa-crown', 'desc': 'Predictive modeling master'},
    ],
    'Product Design': [
        {'name': 'UI Expert', 'track': 'Product Design', 'rarity': 'rare', 'cost': 150, 'icon': 'fa-palette', 'desc': 'Interface design specialist'},
        {'name': 'UX Researcher', 'track': 'Product Design', 'rarity': 'epic', 'cost': 250, 'icon': 'fa-users', 'desc': 'User experience strategist'},
        {'name': 'Design Systems Lead', 'track': 'Product Design', 'rarity': 'legendary', 'cost': 400, 'icon': 'fa-crown', 'desc': 'Design scalability architect'},
    ],
    'Post-Production': [
        {'name': 'Video Editor Pro', 'track': 'Post-Production', 'rarity': 'rare', 'cost': 150, 'icon': 'fa-film', 'desc': 'Timeline master'},
        {'name': 'Colorist', 'track': 'Post-Production', 'rarity': 'epic', 'cost': 250, 'icon': 'fa-palette', 'desc': 'Color grading artist'},
        {'name': 'Post Production Master', 'track': 'Post-Production', 'rarity': 'legendary', 'cost': 400, 'icon': 'fa-crown', 'desc': 'Cinematic finishing specialist'},
    ],
    'Audio Engineering': [
        {'name': 'Sound Designer', 'track': 'Audio Engineering', 'rarity': 'rare', 'cost': 150, 'icon': 'fa-waveform-lines', 'desc': 'Audio effects specialist'},
        {'name': 'Mix Engineer', 'track': 'Audio Engineering', 'rarity': 'epic', 'cost': 250, 'icon': 'fa-sliders', 'desc': 'Mixing console master'},
        {'name': 'Mastering Engineer', 'track': 'Audio Engineering', 'rarity': 'legendary', 'cost': 400, 'icon': 'fa-crown', 'desc': 'Audio quality perfectionist'},
    ],
    'Game Development': [
        {'name': 'Game Programmer', 'track': 'Game Development', 'rarity': 'rare', 'cost': 150, 'icon': 'fa-code', 'desc': 'Game logic expert'},
        {'name': 'Level Designer', 'track': 'Game Development', 'rarity': 'epic', 'cost': 250, 'icon': 'fa-map', 'desc': 'World building specialist'},
        {'name': 'Game Director', 'track': 'Game Development', 'rarity': 'legendary', 'cost': 400, 'icon': 'fa-crown', 'desc': 'Creative game vision lead'},
    ],
    'Digital Content': [
        {'name': 'Content Creator', 'track': 'Digital Content', 'rarity': 'rare', 'cost': 150, 'icon': 'fa-camera', 'desc': 'Media production expert'},
        {'name': 'Video Strategist', 'track': 'Digital Content', 'rarity': 'epic', 'cost': 250, 'icon': 'fa-chart-line', 'desc': 'Growth hacking specialist'},
        {'name': 'Content Creator Influencer', 'track': 'Digital Content', 'rarity': 'legendary', 'cost': 400, 'icon': 'fa-crown', 'desc': 'Audience building master'},
    ],
}

# --- DAILY QUESTS GENERATION ---

def generate_daily_quests(user_id):
    """Generate 4 track-specific daily quests for the user"""
    import random
    from datetime import timedelta

    user = User.query.get(user_id)
    if not user or not user.recommended_path:
        return []

    track = user.recommended_path

    # Delete old quests (older than 24 hours)
    cutoff = datetime.utcnow() - timedelta(hours=24)
    DailyQuest.query.filter(
        DailyQuest.user_id == user_id,
        DailyQuest.created_at < cutoff
    ).delete()
    db.session.commit()

    # Get track-specific templates
    templates = TRACK_QUEST_TEMPLATES.get(track, [])
    if not templates:
        templates = TRACK_QUEST_TEMPLATES.get('Software Engineering', [])

    # Select 4 random quests, balanced by difficulty
    easy_templates = [q for q in templates if q['difficulty'] == 'Easy']
    medium_templates = [q for q in templates if q['difficulty'] == 'Medium']
    hard_templates = [q for q in templates if q['difficulty'] == 'Hard']

    # Pick 1 Easy, 1 Medium, 2 Hard for balance
    selected = []
    if easy_templates:
        selected.append(random.choice(easy_templates))
    if medium_templates:
        selected.append(random.choice(medium_templates))
    if hard_templates:
        selected.extend(random.sample(hard_templates, min(2, len(hard_templates))))

    # Shuffle order
    random.shuffle(selected)

    # Create DailyQuest records
    new_quests = []
    for quest_data in selected:
        daily_quest = DailyQuest(
            user_id=user_id,
            title=quest_data['title'],
            description=quest_data['desc'],
            icon=quest_data['icon'],
            difficulty=quest_data['difficulty'],
            coins_reward=quest_data['coins'],
            created_at=datetime.utcnow()
        )
        db.session.add(daily_quest)
        new_quests.append(daily_quest)

    db.session.commit()
    return new_quests

def seed_marketplace_items():
    """Seed marketplace with track-specific items on first run"""
    if MarketplaceItem.query.first():
        return  # Already seeded

    items_to_add = []
    for track, items in TRACK_ITEMS.items():
        for item_data in items:
            marketplace_item = MarketplaceItem(
                name=item_data['name'],
                description=item_data['desc'],
                xp_cost=item_data['cost'],
                item_type='title',
                icon=item_data['icon'],
                rarity=item_data['rarity'],
                color='#FFD700' if item_data['rarity'] == 'legendary' else '#C0C0C0' if item_data['rarity'] == 'epic' else '#CD7F32'
            )
            items_to_add.append(marketplace_item)

    for item in items_to_add:
        db.session.add(item)
    db.session.commit()

# Seed marketplace on startup
with app.app_context():
    seed_marketplace_items()

@app.route('/api/daily-quests', methods=['GET'])
@login_required
def get_daily_quests():
    from datetime import timedelta

    # Check if user has quests from last 24 hours
    cutoff = datetime.utcnow() - timedelta(hours=24)
    recent_quests = DailyQuest.query.filter(
        DailyQuest.user_id == current_user.id,
        DailyQuest.created_at >= cutoff
    ).all()

    # If no recent quests, generate new ones
    if not recent_quests:
        recent_quests = generate_daily_quests(current_user.id)

    quests_data = [{
        'id': quest.id,
        'title': quest.title,
        'description': quest.description,
        'icon': quest.icon,
        'difficulty': quest.difficulty,
        'coins_reward': quest.coins_reward,
        'completed': quest.completed
    } for quest in recent_quests]

    return jsonify({
        'quests': quests_data,
        'user_coins': current_user.spendable_coins,
        'total_coins': current_user.total_coins
    })

@app.route('/api/daily-quests/complete/<int:quest_id>', methods=['POST'])
@login_required
def complete_daily_quest(quest_id):
    quest = DailyQuest.query.get(quest_id)

    if not quest:
        return jsonify({'error': 'Quest not found'}), 404

    if quest.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403

    if quest.completed:
        return jsonify({'error': 'Quest already completed'}), 400

    # Mark as completed
    quest.completed = True
    quest.completed_at = datetime.utcnow()

    # Add coins
    current_user.spendable_coins = (current_user.spendable_coins or 0) + quest.coins_reward
    current_user.total_coins = (current_user.total_coins or 0) + quest.coins_reward

    db.session.commit()

    return jsonify({
        'success': True,
        'coins_earned': quest.coins_reward,
        'new_spendable_coins': current_user.spendable_coins,
        'new_total_coins': current_user.total_coins
    })

# --- NEW FEATURES: MARKETPLACE, WEEKLY QUESTS, LEADERBOARD ---

@app.route('/api/marketplace/items', methods=['GET'])
@login_required
def get_marketplace_items():
    items = MarketplaceItem.query.all()
    owned_titles = current_user.owned_titles or []

    items_data = [{
        'id': item.id,
        'name': item.name,
        'description': item.description,
        'xp_cost': item.xp_cost,
        'type': item.item_type,
        'icon': item.icon,
        'color': item.color,
        'rarity': item.rarity,
        'owned': item.id in owned_titles
    } for item in items]

    return jsonify({
        'items': items_data,
        'user_coins': current_user.spendable_coins
    })

@app.route('/api/marketplace/purchase/<int:item_id>', methods=['POST'])
@login_required
def purchase_item(item_id):
    # Refresh user from DB to get latest balance (prevents race condition)
    current_user_refreshed = User.query.get(current_user.id)

    item = MarketplaceItem.query.get(item_id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404

    if current_user_refreshed.spendable_coins < item.xp_cost:
        return jsonify({'error': 'Insufficient coins'}), 400

    owned_titles = current_user_refreshed.owned_titles or []
    if item_id in owned_titles:
        return jsonify({'error': 'Already owned'}), 400

    current_user_refreshed.spendable_coins -= item.xp_cost
    owned_titles.append(item_id)
    current_user_refreshed.owned_titles = owned_titles
    db.session.commit()

    return jsonify({
        'success': True,
        'remaining_coins': current_user_refreshed.spendable_coins,
        'owned_items': owned_titles
    })

@app.route('/api/weekly-quests', methods=['GET'])
@login_required
def get_weekly_quests():
    from datetime import datetime, timedelta

    # Get current week's quests
    week_start = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    week_start -= timedelta(days=week_start.weekday())  # Start from Monday

    quests = WeeklyQuest.query.filter(
        WeeklyQuest.week_start >= week_start,
        WeeklyQuest.week_start < week_start + timedelta(days=7)
    ).all()

    user_progress = current_user.weekly_quest_progress or {}

    quests_data = [{
        'id': quest.id,
        'title': quest.title,
        'description': quest.description,
        'xp_reward': quest.xp_reward,
        'difficulty': quest.difficulty,
        'icon': quest.icon,
        'completed': str(quest.id) in user_progress
    } for quest in quests]

    return jsonify({'quests': quests_data})

@app.route('/api/weekly-quests/complete/<int:quest_id>', methods=['POST'])
@login_required
def complete_weekly_quest(quest_id):
    quest = WeeklyQuest.query.get(quest_id)
    if not quest:
        return jsonify({'error': 'Quest not found'}), 404

    user_progress = current_user.weekly_quest_progress or {}

    # Store quest_id as integer (not string) for consistency
    if quest_id in user_progress:
        return jsonify({'error': 'Quest already completed this week'}), 400

    # Add XP
    path = current_user.recommended_path
    xp_data = current_user.xp_data or {}
    xp_data[path] = xp_data.get(path, 0) + quest.xp_reward
    current_user.xp_data = xp_data

    # Track total XP and marketplace XP
    current_user.total_xp = (current_user.total_xp or 0) + quest.xp_reward
    current_user.marketplace_xp = (current_user.marketplace_xp or 0) + quest.xp_reward

    # Mark quest as completed using integer key
    user_progress[quest_id] = True
    current_user.weekly_quest_progress = user_progress

    db.session.commit()

    return jsonify({
        'success': True,
        'xp_earned': quest.xp_reward,
        'new_total_xp': current_user.total_xp,
        'new_marketplace_xp': current_user.marketplace_xp
    })

@app.route('/api/leaderboard', methods=['GET'])
def get_leaderboard():
    track = request.args.get('track', 'Global')

    # Optimize query: only fetch needed columns, not entire User records
    if track == 'Global':
        users = db.session.query(User.email, User.total_xp, User.recommended_path).order_by(User.total_xp.desc()).limit(10).all()
    else:
        users = db.session.query(User.email, User.total_xp, User.recommended_path).filter(User.recommended_path == track).order_by(User.total_xp.desc()).limit(10).all()

    leaderboard = [{
        'rank': idx + 1,
        'email': user.email.split('@')[0],  # Show only username part
        'xp': user.total_xp or 0,
        'path': user.recommended_path
    } for idx, user in enumerate(users)]

    return jsonify({'leaderboard': leaderboard})

@app.route('/api/chatbot/message', methods=['POST'])
@login_required
def chatbot_message():
    """Chatbot using Google Gemini API"""
    import requests

    data = request.get_json()
    user_message = data.get('message', '').strip()
    track = current_user.recommended_path or 'Software Engineering'

    if not user_message:
        return jsonify({'error': 'Empty message'}), 400

    try:
        # Get Gemini API key from environment
        gemini_key = os.environ.get('GEMINI_API_KEY')
        if not gemini_key:
            # Fallback: return generic response if API key not configured
            return jsonify({
                'success': True,
                'response': f"I'm a career guidance chatbot for {track}. How can I help you learn today?",
                'track': track
            })

        # Call Gemini API
        gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={gemini_key}"

        system_prompt = f"""You are a helpful career guidance AI for SkillSpark, an online learning platform.
The user is learning {track}.

Provide:
- Encouraging, supportive responses
- Practical advice for learning and career growth
- Specific resource recommendations when relevant
- Keep responses concise (2-3 sentences max)
- Focus on actionable next steps

Track: {track}
User: {current_user.email}"""

        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": f"{system_prompt}\n\nUser message: {user_message}"
                        }
                    ]
                }
            ]
        }

        headers = {'Content-Type': 'application/json'}

        response = requests.post(gemini_url, json=payload, headers=headers, timeout=5)

        if response.status_code == 200:
            gemini_data = response.json()
            # Extract text from Gemini response
            if 'candidates' in gemini_data and len(gemini_data['candidates']) > 0:
                bot_response = gemini_data['candidates'][0]['content']['parts'][0]['text']
                return jsonify({
                    'success': True,
                    'response': bot_response,
                    'track': track
                })

        # Fallback if response format unexpected
        return jsonify({
            'success': True,
            'response': f"I'm here to help with {track}. What would you like to learn?",
            'track': track
        })

    except requests.exceptions.Timeout:
        return jsonify({
            'success': True,
            'response': "That's a great question! I'm thinking... In the meantime, keep building projects in your track!",
            'track': track
        })
    except Exception as err:
        print(f"Chatbot error: {err}")
        return jsonify({
            'success': True,
            'response': f"I'm ready to help with {track}. Tell me more about what you want to learn!",
            'track': track
        })

@app.route('/marketplace')
@login_required
def marketplace():
    return render_template('marketplace.html')

if __name__ == '__main__':
    app.run(debug=True)