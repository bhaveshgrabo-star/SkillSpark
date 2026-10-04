/**
 * ==========================================================================
 * SKILLSPARK 2.0 - CORE PLATFORM JAVASCRIPT
 * ==========================================================================
 */

// --- 1. MODAL SYSTEM ---
const modal = document.getElementById('globalModal');
const modalTitle = document.getElementById('modalTitle');
const modalBody = document.getElementById('modalBody');

function openModal(title, htmlContent) {
    if (!modal) return;
    modalTitle.innerHTML = title;
    modalBody.innerHTML = htmlContent;
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    if (!modal) return;
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
}

function handleOverlayClick(e) {
    if (e.target === modal) {
        closeModal();
    }
}

// Close on Escape key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal && modal.classList.contains('active')) {
        closeModal();
    }
});

// --- 2. CAREER DATA REPOSITORY ---
const skillData = {
    coding: {
        name: "Software Engineering",
        icon: "fa-code",
        colorClass: "icon-blue",
        badge: "High Industry Demand",
        roadmap: [
            "Foundations of Web (HTML5 Semantic Markup, Modern CSS3 Flex/Grid, JS ES6+)",
            "Component-Driven UI (React.js, State Management, Responsive Design)",
            "Backend Systems & REST APIs (Node.js/Express, Authentication, Server-Side Logic)",
            "Database Architecture & Deployment (PostgreSQL/SQL, Git CI/CD, Cloud Hosting)"
        ],
        resources: [
            { n: "The Odin Project (Complete Full-Stack)", l: "https://theodinproject.com", type: "Full Curriculum" },
            { n: "FreeCodeCamp Web Certification", l: "https://freecodecamp.org", type: "Interactive Practice" },
            { n: "Full Stack Open (University of Helsinki)", l: "https://fullstackopen.com", type: "Advanced Guide" }
        ],
        career: "Junior Frontend Engineer &bull; Full-Stack Developer &bull; Software Engineer",
        tools: "VS Code, Git & GitHub, Docker, Postman, Vercel"
    },
    designing: {
        name: "Product Design",
        icon: "fa-layer-group",
        colorClass: "icon-purple",
        badge: "UX & System Architecture",
        roadmap: [
            "Visual Hierarchy & Typography (Color Theory, Accessibility WCAG, Spacing Grids)",
            "Wireframing & Information Architecture (User Journey Maps, Lo-Fi Schematics)",
            "High-Fidelity Components in Figma (Auto-Layout, Variants, Design Tokens)",
            "Interactive Micro-Interactions & Prototyping (Smart Animate, Developer Handoff)"
        ],
        resources: [
            { n: "Figma Community & Official Tutorials", l: "https://figma.com/community", type: "Design Files" },
            { n: "Laws of UX (Psychology Principles)", l: "https://lawsofux.com", type: "Reference Guide" },
            { n: "Google UX Design Professional Certificate", l: "https://grow.google", type: "Course" }
        ],
        career: "UI/UX Designer &bull; Product Designer &bull; Design Systems Architect",
        tools: "Figma, FigJam, Spline 3D, Adobe Creative Cloud, Maze"
    },
    video: {
        name: "Post-Production",
        icon: "fa-video",
        colorClass: "icon-rose",
        badge: "Cinematic Narrative",
        roadmap: [
            "NLE Timeline & Cutting Rhythm (Keyboard Shortcuts, A-Roll/B-Roll Sequencing)",
            "Audio Mixing & Sound Design (Dialogue leveling, Room Tone, Impact FX)",
            "Color Science & Grading (Color Wheels, Curves, Look-Up Tables, Scopes)",
            "Motion Graphics & Titles (Keyframing, Lower Thirds, Dynamic Transitions)"
        ],
        resources: [
            { n: "Blackmagic DaVinci Resolve Official Training", l: "https://blackmagicdesign.com", type: "Free Pro Guide" },
            { n: "Mixkit Free Royalty-Free Stock & FX", l: "https://mixkit.co", type: "Asset Library" },
            { n: "Film Riot Post-Production Guides", l: "https://youtube.com", type: "Video Masterclasses" }
        ],
        career: "Video Editor &bull; Colorist &bull; Motion Graphics Artist &bull; Post Supervisor",
        tools: "DaVinci Resolve Studio, Adobe Premiere Pro, After Effects"
    },
    music: {
        name: "Audio Engineering",
        icon: "fa-sliders",
        colorClass: "icon-amber",
        badge: "Acoustics & DAW Mastery",
        roadmap: [
            "DAW Navigation & MIDI Sequencing (Signal Flow, Tempo, Quantization, Drum Programming)",
            "Recording & Gain Staging (Microphone Techniques, Preamp headroom, Clean Tracking)",
            "Dynamic Mixing (Parametric EQ Sculpting, Compression, Reverb & Delay)",
            "Mastering & Commercial Loudness (Limiting, Stereo Width, LUFS Compliance)"
        ],
        resources: [
            { n: "Ableton: Learning Music & Synths", l: "https://learningmusic.ableton.com", type: "Interactive" },
            { n: "BandLab Online DAW (Free)", l: "https://bandlab.com", type: "Cloud DAW" },
            { n: "SoundGym Audio Ear Training", l: "https://soundgym.co", type: "Ear Training" }
        ],
        career: "Mixing Engineer &bull; Music Producer &bull; Sound Designer &bull; Mastering Engineer",
        tools: "Ableton Live, FL Studio, Logic Pro, Serum Synthesizer, iZotope"
    },
    gaming: {
        name: "Game Development",
        icon: "fa-cube",
        colorClass: "icon-emerald",
        badge: "Real-Time 3D Worlds",
        roadmap: [
            "Game Engine Fundamentals (Scene Hierarchies, Transforms, Game Loops, Prefabs)",
            "Gameplay Scripting (Character Controllers, Movement Physics, Collision Triggers)",
            "Level Architecture & Lighting (Terrain generation, Tilemaps, Post-processing)",
            "Game State & Publishing (Game Over logic, Scoring, Build compilation)"
        ],
        resources: [
            { n: "Unity Learn Pathway (Official)", l: "https://learn.unity.com", type: "Official Tracks" },
            { n: "Godot Engine Documentation", l: "https://docs.godotengine.org", type: "Open Source Docs" },
            { n: "Kenney Game Assets (100% Free Public Domain)", l: "https://kenney.nl", type: "Game Art" }
        ],
        career: "Indie Game Developer &bull; Gameplay Programmer &bull; Level Designer",
        tools: "Unity 3D, Unreal Engine 5, Godot, Blender, GitHub"
    },
    content: {
        name: "Digital Content",
        icon: "fa-chart-line",
        colorClass: "icon-indigo",
        badge: "Audience Architecture",
        roadmap: [
            "Target Demographic & Niche Definition (Pillars, Pain points, Search Volume)",
            "Scripting Frameworks (First 3-Second Visual Hook, Story Arc, Retention Loops)",
            "Production & Visual Polish (Lighting, Fast Pacing, Dynamic Subtitles, Sound Accents)",
            "Analytics & Optimization (Click-Through Rate, Average View Duration, Repurposing)"
        ],
        resources: [
            { n: "YouTube Creators Official Academy", l: "https://creatoracademy.youtube.com", type: "Platform Guide" },
            { n: "Canva Design School for Creators", l: "https://canva.com", type: "Visual Guide" },
            { n: "HubSpot Social Strategy Hub", l: "https://hubspot.com", type: "Growth Playbook" }
        ],
        career: "Content Creator &bull; Creative Director &bull; Social Media Strategist",
        tools: "CapCut Pro, Notion, Canva, OBS Studio, YouTube Analytics"
    },
    ai: {
        name: "AI & Machine Learning",
        icon: "fa-brain",
        colorClass: "icon-purple",
        badge: "Next-Gen Intelligence",
        roadmap: [
            "Mathematics & Numerical Python (NumPy, Linear Algebra, Multivariable Calculus)",
            "Classical Machine Learning (Scikit-Learn, Feature Engineering, Classification)",
            "Deep Learning & PyTorch (Convolutional Networks, Transformers, Backpropagation)",
            "LLMs, Prompt Engineering & RAG (LangChain, Hugging Face Transformers, Fine-Tuning)"
        ],
        resources: [
            { n: "Fast.ai Practical Deep Learning", l: "https://course.fast.ai", type: "Hands-on MOOC" },
            { n: "Hugging Face Deep RL & NLP Course", l: "https://huggingface.co/learn", type: "Interactive" },
            { n: "Andrej Karpathy: Neural Networks Zero to Hero", l: "https://youtube.com", type: "Video Masterclass" }
        ],
        career: "AI Engineer &bull; Machine Learning Specialist &bull; Research Engineer",
        tools: "Google Colab, PyTorch, Hugging Face, Weights & Biases, Ollama"
    },
    security: {
        name: "Cybersecurity",
        icon: "fa-shield-halved",
        colorClass: "icon-rose",
        badge: "Critical Infrastructure Defense",
        roadmap: [
            "Linux Systems & TCP/IP Networking (Subnets, Routing, Protocols, Packet Flow)",
            "Defensive Reconnaissance & Threat Modeling (Wireshark, Nmap, Port Scanning)",
            "Web Security & Ethical Exploitation (OWASP Top 10, Burp Suite, SQLi, XSS)",
            "Privilege Escalation, SIEM & Hardening (Metasploit, Splunk, Incident Response)"
        ],
        resources: [
            { n: "TryHackMe Interactive Cyber Labs", l: "https://tryhackme.com", type: "Hands-on Practice" },
            { n: "HackTheBox Academy & Labs", l: "https://hackthebox.com", type: "Pen-testing Lab" },
            { n: "OverTheWire Bandit Wargames", l: "https://overthewire.org", type: "Linux Security" }
        ],
        career: "Security Analyst &bull; Ethical Hacker / Pen Tester &bull; SOC Analyst",
        tools: "Kali Linux, Wireshark, Burp Suite, Nmap, Metasploit, Ghidra"
    },
    cloud: {
        name: "Cloud & DevOps",
        icon: "fa-cloud",
        colorClass: "icon-blue",
        badge: "High Velocity Infrastructure",
        roadmap: [
            "Linux Server Administration & Bash Automation (POSIX shell, SSH, Systemd, Cron)",
            "Docker Containerization & Multi-Stage Builds (Images, Volumes, Docker Compose)",
            "Automated CI/CD Workflows (GitHub Actions, Automated Testing, Security Linting)",
            "Kubernetes & Infrastructure as Code (Pods, Ingress, Helm, Terraform Provisioning)"
        ],
        resources: [
            { n: "DevOps Roadmap (roadmap.sh/devops)", l: "https://roadmap.sh/devops", type: "Visual Curriculum" },
            { n: "Kubernetes Tutorials & Interactive Docs", l: "https://kubernetes.io/docs/tutorials", type: "Official Labs" },
            { n: "Learn Linux TV", l: "https://youtube.com", type: "Server Administration" }
        ],
        career: "DevOps Engineer &bull; Cloud Architect &bull; Site Reliability Engineer (SRE)",
        tools: "AWS, Docker, Kubernetes, Terraform, GitHub Actions, Prometheus"
    },
    datascience: {
        name: "Data Science",
        icon: "fa-chart-pie",
        colorClass: "icon-emerald",
        badge: "Data Intelligence & Modeling",
        roadmap: [
            "Relational Database Querying (Advanced SQL, CTEs, Window Functions, Indexing)",
            "Python Data Manipulation (Pandas, Polars, Exploratory Data Analysis, Imputation)",
            "Statistical Hypothesis Testing & Experimentation (A/B Testing, Confidence Intervals)",
            "Predictive Modeling & BI Storytelling (XGBoost, Feature Importance, PowerBI Dashboards)"
        ],
        resources: [
            { n: "Kaggle Learn & Hands-on Datasets", l: "https://kaggle.com/learn", type: "Interactive Practice" },
            { n: "Mode Analytics Complete SQL Tutorial", l: "https://mode.com/sql-tutorial", type: "Interactive Guide" },
            { n: "StatQuest with Josh Starmer", l: "https://youtube.com", type: "Visual Statistics" }
        ],
        career: "Data Scientist &bull; Data Analyst &bull; Quantitative Analyst &bull; BI Engineer",
        tools: "PostgreSQL, Jupyter Notebooks, Python, Pandas, PowerBI, Scikit-Learn"
    }
};

// --- 3. SKILL DETAILS MODAL ---
function openSkillModal(key) {
    const data = skillData[key];
    if (!data) return;

    // Send analytics update to backend if logged in
    fetch('/api/update_progress', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ explored: data.name })
    }).catch(() => {});

    const titleHTML = `
        <div style="display: flex; align-items: center; gap: 12px;">
            <div class="card-icon-box ${data.colorClass}" style="width: 38px; height: 38px; font-size: 1.1rem;">
                <i class="fa-solid ${data.icon}"></i>
            </div>
            <div>
                <span style="font-size: 1.25rem; font-weight: 700; color: #fff;">${data.name}</span>
            </div>
        </div>
    `;

    const roadmapHTML = data.roadmap.map((step, idx) => `
        <li>
            <i class="fa-solid fa-circle-check"></i>
            <span><strong>Phase ${idx + 1}:</strong> ${step}</span>
        </li>
    `).join('');

    const resourcesHTML = data.resources.map(r => `
        <a href="${r.l}" target="_blank" class="resource-item" style="margin-bottom: 8px;">
            <div class="resource-item-left">
                <div class="resource-icon-box" style="width: 32px; height: 32px; font-size: 0.9rem;">
                    <i class="fa-solid fa-arrow-up-right-from-square"></i>
                </div>
                <div class="resource-meta">
                    <strong>${r.n}</strong>
                    <span>${r.type}</span>
                </div>
            </div>
            <i class="fa-solid fa-chevron-right" style="color: var(--text-muted); font-size: 0.75rem;"></i>
        </a>
    `).join('');

    const contentHTML = `
        <div>
            <div style="margin-bottom: 20px;">
                <span class="section-badge" style="margin-bottom: 8px;">${data.badge}</span>
                <p style="color: var(--text-secondary); font-size: 0.95rem; margin-top: 6px;">
                    Target Roles: <strong style="color: var(--text-primary);">${data.career}</strong>
                </p>
            </div>

            <div style="margin-bottom: 24px;">
                <h4 style="font-size: 1rem; color: var(--primary); margin-bottom: 12px; text-transform: uppercase; letter-spacing: 0.05em; font-family: var(--font-mono);">
                    <i class="fa-solid fa-timeline" style="margin-right: 6px;"></i> 4-Phase Curriculum
                </h4>
                <ul class="modal-roadmap-list">${roadmapHTML}</ul>
            </div>

            <div style="margin-bottom: 24px;">
                <h4 style="font-size: 1rem; color: var(--secondary); margin-bottom: 12px; text-transform: uppercase; letter-spacing: 0.05em; font-family: var(--font-mono);">
                    <i class="fa-solid fa-gift" style="margin-right: 6px;"></i> Curated Free Learning Hubs
                </h4>
                <div>${resourcesHTML}</div>
            </div>

            <div style="margin-bottom: 28px; background: rgba(255,255,255,0.02); border: 1px solid var(--border-subtle); padding: 16px 20px; border-radius: 12px;">
                <span style="font-size: 0.75rem; text-transform: uppercase; color: var(--text-muted); font-weight: 700; letter-spacing: 0.05em; display: block; margin-bottom: 4px;">
                    Standard Production Toolkit
                </span>
                <p style="color: var(--text-primary); font-size: 0.95rem; font-family: var(--font-mono); margin: 0;">${data.tools}</p>
            </div>

            <div style="border-top: 1px solid var(--border-subtle); padding-top: 20px;">
                <button onclick="setCareerPath('${data.name}')" class="btn btn-primary full-width btn-glow" style="padding: 14px; font-size: 1rem;">
                    <span>Lock In as Active Specialization</span>
                    <i class="fa-solid fa-rocket"></i>
                </button>
            </div>
        </div>
    `;

    openModal(titleHTML, contentHTML);
}

// --- 4. CAREER PATH SELECTION ---
async function setCareerPath(pathName) {
    const navXpBadge = document.querySelector('.xp-badge');
    
    // If not authenticated, prompt login
    if (!navXpBadge) {
        sessionStorage.setItem('pending_path', pathName);
        openAuthModal('signup', `Create an account to lock in <strong>${pathName}</strong> and activate your personalized workspace.`);
        return;
    }

    try {
        const res = await fetch('/api/update_progress', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ path: pathName })
        });
        if (res.ok) {
            window.location.href = '/dashboard';
        }
    } catch (err) {
        console.error("Failed to update path:", err);
    }
}

// --- 5. AUTHENTICATION MODAL (TABS: SIGN IN / SIGN UP) ---
function openAuthModal(defaultMode = 'login', customMessage = null) {
    window.authMode = defaultMode;

    const infoNotice = customMessage 
        ? `<div style="background: rgba(56, 189, 248, 0.1); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 10px; padding: 12px 16px; margin-bottom: 18px; color: var(--primary-light); font-size: 0.88rem;">${customMessage}</div>`
        : '';

    const authHTML = `
        <div style="max-width: 440px; margin: 0 auto;">
            ${infoNotice}
            <div class="auth-tabs">
                <button type="button" class="auth-tab-btn ${window.authMode === 'login' ? 'active' : ''}" id="tab-login" onclick="switchAuthTab('login')">
                    <i class="fa-solid fa-lock" style="margin-right: 6px;"></i> Sign In
                </button>
                <button type="button" class="auth-tab-btn ${window.authMode === 'signup' ? 'active' : ''}" id="tab-signup" onclick="switchAuthTab('signup')">
                    <i class="fa-solid fa-user-plus" style="margin-right: 6px;"></i> Create Account
                </button>
            </div>

            <form id="authForm" onsubmit="handleAuth(event)" style="display: flex; flex-direction: column; gap: 16px;">
                <div>
                    <label style="font-size: 0.82rem; font-weight: 600; text-transform: uppercase; color: var(--text-muted); display: block; margin-bottom: 6px;">
                        Email Address
                    </label>
                    <input type="email" id="authEmail" class="premium-input" placeholder="you@domain.com" required autocomplete="email">
                </div>

                <div>
                    <label style="font-size: 0.82rem; font-weight: 600; text-transform: uppercase; color: var(--text-muted); display: block; margin-bottom: 6px;">
                        Password
                    </label>
                    <input type="password" id="authPass" class="premium-input" placeholder="••••••••" required minlength="6" autocomplete="current-password">
                </div>

                <div id="authError" style="font-size: 0.88rem; text-align: center; min-height: 20px; font-weight: 600;"></div>

                <button type="submit" class="btn btn-primary full-width btn-glow" id="authSubmitBtn" style="padding: 13px; font-size: 0.95rem;">
                    <span id="authBtnText">${window.authMode === 'login' ? 'Sign In to Workspace' : 'Create Free Account'}</span>
                    <i class="fa-solid fa-arrow-right"></i>
                </button>
            </form>
        </div>
    `;

    openModal("Platform Access", authHTML);
}

function switchAuthTab(mode) {
    window.authMode = mode;
    const tabLogin = document.getElementById('tab-login');
    const tabSignup = document.getElementById('tab-signup');
    const btnText = document.getElementById('authBtnText');
    const authError = document.getElementById('authError');

    if (authError) authError.innerText = '';

    if (mode === 'login') {
        tabLogin?.classList.add('active');
        tabSignup?.classList.remove('active');
        if (btnText) btnText.innerText = 'Sign In to Workspace';
    } else {
        tabSignup?.classList.add('active');
        tabLogin?.classList.remove('active');
        if (btnText) btnText.innerText = 'Create Free Account';
    }
}

async function handleAuth(e) {
    e.preventDefault();
    const email = document.getElementById('authEmail').value.trim();
    const password = document.getElementById('authPass').value;
    const messageBox = document.getElementById('authError');
    const submitBtn = document.getElementById('authSubmitBtn');
    const endpoint = window.authMode === 'signup' ? '/api/signup' : '/api/login';

    if (!email || !password) return;

    submitBtn.disabled = true;
    submitBtn.style.opacity = '0.7';
    messageBox.style.color = 'var(--text-muted)';
    messageBox.innerHTML = '<i class="fa-solid fa-circle-notch fa-spin"></i> Authenticating...';

    try {
        const res = await fetch(endpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });
        const data = await res.json();

        if (res.ok) {
            messageBox.style.color = 'var(--accent-emerald)';
            messageBox.innerHTML = window.authMode === 'signup'
                ? '<i class="fa-solid fa-circle-check"></i> Account verified! Logging in...'
                : '<i class="fa-solid fa-circle-check"></i> Success! Loading workspace...';

            // Check if there was a pending path selected before login
            const pendingPath = sessionStorage.getItem('pending_path');
            if (pendingPath) {
                await fetch('/api/update_progress', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ path: pendingPath })
                });
                sessionStorage.removeItem('pending_path');
                setTimeout(() => { window.location.href = '/dashboard'; }, 700);
            } else {
                setTimeout(() => { window.location.reload(); }, 700);
            }
        } else {
            messageBox.style.color = 'var(--accent-rose)';
            messageBox.innerHTML = `<i class="fa-solid fa-circle-exclamation"></i> ${data.error || 'Authentication failed'}`;
            submitBtn.disabled = false;
            submitBtn.style.opacity = '1';
        }
    } catch (err) {
        console.error("Auth request failed:", err);
        messageBox.style.color = 'var(--accent-rose)';
        messageBox.innerHTML = '<i class="fa-solid fa-circle-exclamation"></i> Network error. Please try again.';
        submitBtn.disabled = false;
        submitBtn.style.opacity = '1';
    }
}

// --- 6. PATHFINDER QUIZ ENGINE ---
let quizScores = { coding: 0, designing: 0, video: 0, music: 0, gaming: 0, content: 0, ai: 0, security: 0, cloud: 0, datascience: 0 };
const totalQuestions = 5;

function selectOption(btn, currentQId, nextQId, choice) {
    const parentList = btn.closest('.quiz-options-list');
    if (parentList) {
        parentList.querySelectorAll('.quiz-btn').forEach(b => b.classList.remove('selected'));
    }
    btn.classList.add('selected');

    if (choice && quizScores[choice] !== undefined) {
        quizScores[choice] += 1;
    }

    // Update progress bar
    const currentNum = parseInt(currentQId.replace('q', ''));
    const nextNum = nextQId === 'result' ? totalQuestions : parseInt(nextQId.replace('q', ''));
    const progressFill = document.getElementById('quiz-progress-fill');
    if (progressFill) {
        progressFill.style.width = `${(nextNum / totalQuestions) * 100}%`;
    }

    setTimeout(() => {
        if (nextQId === 'result') {
            finishQuiz();
        } else {
            const currentEl = document.getElementById(currentQId);
            const nextEl = document.getElementById(nextQId);
            if (currentEl) currentEl.classList.remove('active');
            if (nextEl) nextEl.classList.add('active');
        }
    }, 350);
}

const skillToSlug = {
    'Software Engineering': 'software-engineering',
    'AI & Machine Learning': 'ai-machine-learning',
    'Cybersecurity': 'cybersecurity',
    'Cloud & DevOps': 'cloud-devops',
    'Data Science': 'data-science',
    'Product Design': 'product-design',
    'Post-Production': 'post-production',
    'Audio Engineering': 'audio-engineering',
    'Game Development': 'game-development',
    'Digital Content': 'digital-content'
};

function finishQuiz() {
    const lastQ = document.getElementById('q5');
    if (lastQ) lastQ.classList.remove('active');

    // Sort to find top 2 scoring disciplines
    let sortedKeys = Object.keys(quizScores).sort((a, b) => quizScores[b] - quizScores[a]);
    let primaryKey = sortedKeys[0];
    let secondaryKey = sortedKeys[1] || 'coding';

    let primarySkill = skillData[primaryKey] ? skillData[primaryKey].name : "Software Engineering";
    let secondarySkill = skillData[secondaryKey] ? skillData[secondaryKey].name : "AI & Machine Learning";

    const resultText = document.getElementById('result-text');
    const resultBox = document.getElementById('quiz-result');
    const exploreBtn = document.getElementById('quiz-explore-btn');
    const deepdiveLink = document.getElementById('quiz-deepdive-link');

    if (resultText) resultText.innerText = primarySkill;
    if (resultBox) resultBox.style.display = 'block';

    const match1Label = document.getElementById('match-1-label');
    const match1Val = document.getElementById('match-1-val');
    const match1Bar = document.getElementById('match-1-bar');
    const match2Label = document.getElementById('match-2-label');
    const match2Val = document.getElementById('match-2-val');
    const match2Bar = document.getElementById('match-2-bar');

    if (match1Label) match1Label.innerText = primarySkill;
    if (match1Val) match1Val.innerText = '96%';
    if (match1Bar) match1Bar.style.width = '96%';

    if (match2Label) match2Label.innerText = secondarySkill;
    if (match2Val) match2Val.innerText = '82%';
    if (match2Bar) match2Bar.style.width = '82%';

    const slug = skillToSlug[primarySkill] || 'software-engineering';
    if (deepdiveLink) {
        deepdiveLink.href = `/track/${slug}`;
    }

    if (exploreBtn) {
        exploreBtn.onclick = () => setCareerPath(primarySkill);
    }
}

function resetQuiz() {
    quizScores = { coding: 0, designing: 0, video: 0, music: 0, gaming: 0, content: 0, ai: 0, security: 0, cloud: 0, datascience: 0 };
    const resultBox = document.getElementById('quiz-result');
    if (resultBox) resultBox.style.display = 'none';

    document.querySelectorAll('.quiz-btn').forEach(b => b.classList.remove('selected'));
    document.querySelectorAll('.quiz-question').forEach(q => q.classList.remove('active'));

    const q1 = document.getElementById('q1');
    if (q1) q1.classList.add('active');

    const progressFill = document.getElementById('quiz-progress-fill');
    if (progressFill) progressFill.style.width = '20%';
}

// --- 7. AI TRAJECTORY ENGINE ---
const roadmapForm = document.getElementById('roadmapForm');
if (roadmapForm) {
    roadmapForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const btn = document.getElementById('generate-btn');
        const origContent = btn.innerHTML;

        btn.innerHTML = '<i class="fa-solid fa-circle-notch fa-spin"></i> Synthesizing Blueprint...';
        btn.disabled = true;
        btn.style.opacity = '0.75';

        const payload = {
            skill: document.getElementById('gen-skill')?.value || 'Software Engineering',
            time: document.getElementById('gen-time')?.value || '1',
            budget: document.getElementById('gen-budget')?.value || '0'
        };

        try {
            const res = await fetch('/api/generate_roadmap', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            const data = await res.json();

            const resultDiv = document.getElementById('roadmapResult');
            if (resultDiv) {
                resultDiv.style.display = 'block';

                const stepsHtml = (data.steps || []).map((step, i) => `
                    <div class="timeline-step-node">
                        <span class="step-num">Phase ${i + 1}</span>
                        <h5>${step}</h5>
                    </div>
                `).join('');

                resultDiv.innerHTML = `
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; flex-wrap: wrap; gap: 12px;">
                        <div>
                            <span class="section-badge" style="margin-bottom: 4px;">Compiled Output</span>
                            <h3 style="font-size: 1.5rem; margin: 0;">Trajectory Blueprint: <span class="gradient-text">${payload.skill}</span></h3>
                        </div>
                        <button class="btn btn-outline" onclick="setCareerPath('${payload.skill}')" style="font-size: 0.85rem; padding: 7px 16px;">
                            <span>Adopt Blueprint</span> <i class="fa-solid fa-arrow-right"></i>
                        </button>
                    </div>

                    <div class="blueprint-header-grid">
                        <div class="bp-stat-card">
                            <span><i class="fa-regular fa-clock" style="color: var(--secondary);"></i> Expected Velocity</span>
                            <strong>${data.timeline}</strong>
                        </div>
                        <div class="bp-stat-card">
                            <span><i class="fa-solid fa-wrench" style="color: var(--primary);"></i> Recommended Stack</span>
                            <strong>${data.tools}</strong>
                        </div>
                        <div class="bp-stat-card">
                            <span><i class="fa-solid fa-wallet" style="color: var(--accent-emerald);"></i> Tooling Tier</span>
                            <strong>${data.investment}</strong>
                        </div>
                    </div>

                    <h4 style="font-size: 0.95rem; text-transform: uppercase; letter-spacing: 0.08em; color: var(--text-muted); margin-bottom: 14px; font-family: var(--font-mono);">
                        Linear Milestones
                    </h4>
                    <div class="timeline-track">${stepsHtml}</div>
                `;

                // Scroll to result smoothly
                resultDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            }
        } catch (err) {
            console.error("Blueprint generation failed:", err);
        } finally {
            btn.innerHTML = origContent;
            btn.disabled = false;
            btn.style.opacity = '1';
        }
    });
}

// --- 8. DAILY QUESTS ENGINE ---

async function loadDailyQuests() {
    try {
        const res = await fetch('/api/daily-quests');
        if (!res.ok) {
            console.error('Failed to load daily quests');
            return;
        }
        const data = await res.json();
        renderDailyQuestsUI(data.quests);
        updateCoinsDisplay(data.user_coins);
        updateDailyCoinsEarned(data.quests);
    } catch (err) {
        console.error('Error loading daily quests:', err);
    }
}

function renderDailyQuestsUI(quests) {
    const container = document.getElementById('daily-quests-container');
    if (!container) return;

    container.innerHTML = '';

    quests.forEach(quest => {
        const card = document.createElement('div');
        card.className = 'milestone-row spotlight-card';
        card.style.opacity = quest.completed ? '0.6' : '1';

        const difficultyColor = quest.difficulty === 'Easy' ? 'var(--accent-emerald)' :
                               quest.difficulty === 'Medium' ? 'var(--secondary)' :
                               'var(--accent-rose)';

        const buttonState = quest.completed
            ? `<button class="btn btn-secondary" disabled style="white-space: nowrap; flex-shrink: 0;">
                <i class="fa-solid fa-circle-check"></i> Completed
            </button>`
            : `<button class="btn btn-primary" onclick="completeDailyQuest(${quest.id}, ${quest.coins_reward})" style="white-space: nowrap; flex-shrink: 0;">
                <i class="fa-solid fa-star"></i> Complete (+${quest.coins_reward} Coins)
            </button>`;

        card.innerHTML = `
            <div class="milestone-left">
                <div class="milestone-phase-num" style="background: ${difficultyColor};">
                    <i class="fa-solid ${quest.icon}"></i>
                </div>
                <div class="milestone-text">
                    <h4>${quest.title}</h4>
                    <p>${quest.description}</p>
                    <span class="pill" style="font-size: 0.75rem; margin-top: 6px; color: ${difficultyColor}; border-color: ${difficultyColor};">
                        ${quest.difficulty} • ${quest.coins_reward} Coins
                    </span>
                </div>
            </div>
            ${buttonState}
        `;

        container.appendChild(card);
    });
}

async function completeDailyQuest(questId, coinsReward) {
    try {
        const res = await fetch(`/api/daily-quests/complete/${questId}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });

        if (!res.ok) {
            alert('Failed to complete quest');
            return;
        }

        const data = await res.json();
        if (data.success) {
            updateCoinsDisplay(data.new_spendable_coins);
            triggerCoinsToastAnimation(coinsReward);
            loadDailyQuests(); // Reload to reflect completed state
        }
    } catch (err) {
        console.error('Error completing quest:', err);
    }
}

function updateCoinsDisplay(coins) {
    const coinsCounter = document.getElementById('nav-coins-counter');
    if (coinsCounter) {
        coinsCounter.innerText = coins;
        localStorage.setItem('skillspark_current_coins', coins);
    }

    const dashCoinsDisplay = document.getElementById('dashboard-coins-display');
    if (dashCoinsDisplay) {
        dashCoinsDisplay.innerText = coins;
    }
}

function updateDailyCoinsEarned(quests) {
    const completedCoins = quests
        .filter(q => q.completed)
        .reduce((sum, q) => sum + q.coins_reward, 0);

    const dailyCoinsLabel = document.getElementById('daily-coins-earned');
    if (dailyCoinsLabel) {
        dailyCoinsLabel.innerText = `+${completedCoins} COINS TODAY`;
    }
}

function triggerCoinsToastAnimation(amount) {
    const toast = document.getElementById('xp-toast');
    const amountSpan = document.getElementById('toast-xp-amount');

    if (!toast || !amountSpan) return;

    amountSpan.innerText = `+${amount}`;
    toast.className = 'xp-toast-visible';

    setTimeout(() => {
        toast.className = 'xp-toast-hidden';
    }, 3800);
}

// --- 9. MOUSE SPOTLIGHT HOVER EFFECT ---
function initSpotlightCards() {
    const spotlightCards = document.querySelectorAll('.spotlight-card');
    spotlightCards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            card.style.setProperty('--mouse-x', `${x}px`);
            card.style.setProperty('--mouse-y', `${y}px`);
        });
    });
}

// --- 10. SCROLL REVEAL OBSERVER ---
function initScrollReveal() {
    const reveals = document.querySelectorAll('.reveal');
    if (!('IntersectionObserver' in window)) {
        reveals.forEach(el => el.classList.add('active'));
        return;
    }

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    reveals.forEach(el => observer.observe(el));
}

// --- 11. AMBIENT PARTICLES CANVAS ---
const canvas = document.getElementById("particles-js");
if (canvas) {
    const ctx = canvas.getContext("2d");
    let particlesArray = [];
    const dpr = window.devicePixelRatio || 1;

    class Particle {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.size = (Math.random() * 1.5 + 0.5) * dpr;
            this.speedX = (Math.random() - 0.5) * 0.3 * dpr;
            this.speedY = (Math.random() - 0.5) * 0.3 * dpr;
            this.opacity = Math.random() * 0.4 + 0.1;
        }
        update() {
            this.x += this.speedX;
            this.y += this.speedY;
            if (this.x < 0 || this.x > canvas.width) this.speedX *= -1;
            if (this.y < 0 || this.y > canvas.height) this.speedY *= -1;
        }
        draw() {
            ctx.fillStyle = `rgba(56, 189, 248, ${this.opacity})`;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    function initParticles() {
        canvas.width = window.innerWidth * dpr;
        canvas.height = window.innerHeight * dpr;
        canvas.style.width = `${window.innerWidth}px`;
        canvas.style.height = `${window.innerHeight}px`;
        particlesArray = [];
        const count = window.innerWidth < 768 ? 25 : 55;
        for (let i = 0; i < count; i++) {
            particlesArray.push(new Particle());
        }
    }

    function animateParticles() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        particlesArray.forEach(p => {
            p.update();
            p.draw();
        });
        requestAnimationFrame(animateParticles);
    }

    window.addEventListener('resize', initParticles);
    initParticles();
    animateParticles();
}

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', () => {
    initScrollReveal();
});
// --- 11. CHATBOT FUNCTIONALITY ---

let chatbotState = {
    step: 0,
    discipline: null,
    timeCommitment: null,
    budget: null,
    trajectory: null
};

function chatbotSendMessage(userMessage) {
    const input = document.getElementById('chatInput');
    if (input) {
        input.value = userMessage;
        handleChatSubmit(new Event('submit'));
    }
}

function handleChatSubmit(e) {
    e.preventDefault();
    const input = document.getElementById('chatInput');
    const messagesContainer = document.getElementById('chatMessages');
    if (!input || !messagesContainer) return;

    const userMessage = input.value.trim();
    if (!userMessage) return;

    // Add user message
    addChatMessage(userMessage, 'user');
    input.value = '';

    // Process user response and generate bot reply
    setTimeout(() => processChatbotLogic(userMessage, messagesContainer), 500);
}

function addChatMessage(message, sender) {
    const messagesContainer = document.getElementById('chatMessages');
    if (!messagesContainer) return;

    const messageDiv = document.createElement('div');
    messageDiv.className = `chat-message ${sender}-message`;

    const avatar = document.createElement('div');
    avatar.className = `message-avatar ${sender === 'bot' ? 'bot' : 'user'}`;
    avatar.innerHTML = sender === 'bot' ? '<i class="fa-solid fa-microchip"></i>' : '<i class="fa-solid fa-user"></i>';

    const content = document.createElement('div');
    content.className = 'message-content';

    if (Array.isArray(message)) {
        message.forEach(msg => {
            const p = document.createElement('p');
            p.innerHTML = msg;
            content.appendChild(p);
        });
    } else {
        const p = document.createElement('p');
        p.innerHTML = message;
        content.appendChild(p);
    }

    messageDiv.appendChild(avatar);
    messageDiv.appendChild(content);
    messagesContainer.appendChild(messageDiv);

    // Scroll to bottom
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function processChatbotLogic(userInput, container) {
    const lowerInput = userInput.toLowerCase();
    let botResponse = [];
    let nextOptions = [];

    if (chatbotState.step === 0) {
        // First question: What type of problems energize you?
        if (lowerInput.includes('build') || lowerInput.includes('web') || lowerInput.includes('software')) {
            chatbotState.discipline = 'Software Engineering';
            botResponse = [
                "Great! Software Engineering is in high demand. Building scalable apps and backend systems is incredibly rewarding.",
                "Next question: <strong>How much time can you dedicate per day?</strong>"
            ];
            nextOptions = ['1 hour daily (part-time)', '3+ hours daily (accelerated)'];
        } else if (lowerInput.includes('ai') || lowerInput.includes('machine learning') || lowerInput.includes('model') || lowerInput.includes('neural')) {
            chatbotState.discipline = 'AI & Machine Learning';
            botResponse = [
                "Excellent! AI & ML is the frontier. You''ll work with neural networks, LLMs, and cutting-edge AI agents.",
                "Next question: <strong>How much time can you dedicate per day?</strong>"
            ];
            nextOptions = ['1 hour daily (part-time)', '3+ hours daily (accelerated)'];
        } else if (lowerInput.includes('security') || lowerInput.includes('hacking') || lowerInput.includes('cyber') || lowerInput.includes('vulnerab')) {
            chatbotState.discipline = 'Cybersecurity';
            botResponse = [
                "Perfect! Cybersecurity is critical and lucrative. You''ll learn offensive and defensive strategies.",
                "Next question: <strong>How much time can you dedicate per day?</strong>"
            ];
            nextOptions = ['1 hour daily (part-time)', '3+ hours daily (accelerated)'];
        } else if (lowerInput.includes('design') || lowerInput.includes('figma') || lowerInput.includes('ui') || lowerInput.includes('ux')) {
            chatbotState.discipline = 'Product Design';
            botResponse = [
                "Wonderful! Product Design is incredibly creative. You''ll craft beautiful, intuitive user experiences.",
                "Next question: <strong>How much time can you dedicate per day?</strong>"
            ];
            nextOptions = ['1 hour daily (part-time)', '3+ hours daily (accelerated)'];
        } else {
            botResponse = ["I''m not sure which path that aligns with. Let me ask again: <strong>What problems energize you most?</strong>"];
            nextOptions = ['?? Building Software', '?? AI & ML', '?? Security', '?? Design'];
            return addChatMessageWithOptions(botResponse, nextOptions);
        }
        chatbotState.step = 1;
    } else if (chatbotState.step === 1) {
        // Time commitment
        if (lowerInput.includes('1') || lowerInput.includes('hour') || lowerInput.includes('part')) {
            chatbotState.timeCommitment = '1 hour per day';
            botResponse = [
                "Smart! Part-time pace allows for consistent, sustainable learning.",
                "Final question: <strong>What''s your budget for tools and platforms?</strong>"
            ];
            nextOptions = ['$0 (Free & Open Source)', '$100+ (Premium Tools)'];
        } else if (lowerInput.includes('3') || lowerInput.includes('accelerat') || lowerInput.includes('sprint')) {
            chatbotState.timeCommitment = '3+ hours per day';
            botResponse = [
                "Intense! You''ll move fast and build real projects quickly.",
                "Final question: <strong>What''s your budget for tools and platforms?</strong>"
            ];
            nextOptions = ['$0 (Free & Open Source)', '$100+ (Premium Tools)'];
        } else {
            botResponse = ["Please choose your time commitment: <strong>1 hour/day</strong> or <strong>3+ hours/day</strong>?"];
            nextOptions = ['1 hour daily', '3+ hours daily'];
            return addChatMessageWithOptions(botResponse, nextOptions);
        }
        chatbotState.step = 2;
    } else if (chatbotState.step === 2) {
        // Budget
        if (lowerInput.includes('0') || lowerInput.includes('free') || lowerInput.includes('open')) {
            chatbotState.budget = 'Free';
        } else if (lowerInput.includes('100') || lowerInput.includes('premium')) {
            chatbotState.budget = 'Premium';
        } else {
            botResponse = ["Please choose: <strong>$0 (Free)</strong> or <strong>$100+ (Premium)</strong>?"];
            nextOptions = ['$0 Free', '$100+ Premium'];
            return addChatMessageWithOptions(botResponse, nextOptions);
        }

        // Generate trajectory
        const trajectory = generateTrajectory(chatbotState.discipline, chatbotState.timeCommitment, chatbotState.budget);
        botResponse = [
            "<strong>?? Your AI-Generated Trajectory</strong>",
            "<strong>Discipline:</strong> " + chatbotState.discipline,
            "<strong>Timeline:</strong> " + trajectory.timeline,
            "<strong>Tools:</strong> " + trajectory.tools,
            "<strong>Investment:</strong> " + trajectory.investment,
            "Your customized learning blueprint is ready! Ready to start your journey?"
        ];
        nextOptions = ['Activate in Dashboard', 'View Full Syllabus'];
        chatbotState.step = 3;
    }

    addChatMessageWithOptions(botResponse, nextOptions);
}

function addChatMessageWithOptions(messages, options) {
    addChatMessage(messages, 'bot');

    if (options && options.length > 0) {
        setTimeout(() => {
            const messagesContainer = document.getElementById('chatMessages');
            const lastMessage = messagesContainer.lastChild;
            const contentDiv = lastMessage.querySelector('.message-content');

            const optionsDiv = document.createElement('div');
            optionsDiv.className = 'quick-options';
            optionsDiv.style.marginTop = '12px';

            options.forEach(opt => {
                const btn = document.createElement('button');
                btn.className = 'quick-option';
                btn.textContent = opt;
                btn.onclick = (e) => {
                    e.preventDefault();
                    chatbotSendMessage(opt);
                };
                optionsDiv.appendChild(btn);
            });

            contentDiv.appendChild(optionsDiv);
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }, 300);
    }
}

function generateTrajectory(discipline, time, budget) {
    const trajectories = {
        'Software Engineering': {
            timeline: time.includes('1') ? '12 weeks' : '6 weeks',
            tools: budget === 'Free' ? 'VS Code, GitHub, Vercel' : 'WebStorm, AWS, GitHub Pro',
            investment: budget === 'Free' ? 'Free/Open Source' : 'Premium Tools'
        },
        'AI & Machine Learning': {
            timeline: time.includes('1') ? '14 weeks' : '7 weeks',
            tools: budget === 'Free' ? 'Google Colab, PyTorch, Hugging Face' : 'AWS SageMaker, OpenAI API, Weights & Biases',
            investment: budget === 'Free' ? 'Free/Open Source' : 'Premium Tools'
        },
        'Cybersecurity': {
            timeline: time.includes('1') ? '16 weeks' : '8 weeks',
            tools: budget === 'Free' ? 'Kali Linux, Wireshark, Nmap' : 'Burp Suite Pro, Splunk, HackTheBox VIP',
            investment: budget === 'Free' ? 'Free/Open Source' : 'Premium Tools'
        },
        'Product Design': {
            timeline: time.includes('1') ? '10 weeks' : '5 weeks',
            tools: budget === 'Free' ? 'Figma Free, Blender' : 'Figma Pro, Adobe CC, Spline 3D',
            investment: budget === 'Free' ? 'Free/Open Source' : 'Premium Tools'
        }
    };

    return trajectories[discipline] || trajectories['Software Engineering'];
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    initSpotlightCards();
    initScrollReveal();
    loadUserCoins();
});

// --- 12. COINS HEADER SYNC ---
async function loadUserCoins() {
    // Check if user is authenticated by looking for nav-coins-counter element
    const coinsCounter = document.getElementById('nav-coins-counter');
    if (!coinsCounter) return; // User not authenticated

    try {
        // Fetch coins from database on page load
        const res = await fetch('/api/user_data');
        if (res.ok) {
            const data = await res.json();
            coinsCounter.innerText = data.spendable_coins;
            // Update localStorage with fresh data
            localStorage.setItem('skillspark_current_coins', data.spendable_coins);
            localStorage.setItem('skillspark_total_coins', data.total_coins);
        }
    } catch (err) {
        console.error("Failed to load user coins from database:", err);
        // Fallback to localStorage if API call fails
        const storedCoins = localStorage.getItem('skillspark_current_coins');
        if (storedCoins) {
            coinsCounter.innerText = storedCoins;
        }
    }
}

function updateHeaderXP(newXP) {
    const xpCounter = document.getElementById('nav-xp-counter');
    if (xpCounter) {
        xpCounter.innerText = newXP;
        // Persist to localStorage
        localStorage.setItem('skillspark_current_xp', newXP);
    }
}

// --- 13. BACKGROUND PERSISTENCE ---
// Background is now handled via CSS background-attachment: fixed
// This ensures it persists across page refreshes and scrolls
