# ==============================================================================
# SKILLSPARK 2.0 - CANONICAL TRACKS REPOSITORY & COURSE SYLLABI
# ==============================================================================

TRACKS_DATA = {
    'software-engineering': {
        'slug': 'software-engineering',
        'name': 'Software Engineering',
        'tagline': 'Architect distributed web systems, production APIs, and scalable cloud frontends.',
        'icon': 'fa-code',
        'color': '#38bdf8',
        'gradient': 'linear-gradient(135deg, #38bdf8, #2563eb)',
        'badge': 'High Industry Demand',
        'salary': '$95,000 - $185,000 / yr',
        'timeline': '12 - 16 Weeks (Intensive)',
        'prerequisites': 'Basic computer literacy, logical reasoning, curiosity about internet systems.',
        'usp_tag': 'Proof-of-Work: Build & deploy 3 resume-worthy distributed full-stack systems.',
        'overview': 'Stop tutorial-hopping. This specialization takes you through modern TypeScript, React component architectures, Node.js microservices, database normalization, and automated CI/CD deployment pipelines.',
        'phases': [
            {
                'phase': 1,
                'title': 'Frontend Architecture & Modern TypeScript',
                'duration': '3 Weeks',
                'summary': 'Master the DOM, ES6+ asynchronous loops, strict TypeScript typing, and responsive CSS Grid/Flexbox design systems without relying on bloated libraries.',
                'deliverable': 'Interactive Portfolio Dashboard with strict TypeScript typing deployed to Vercel.'
            },
            {
                'phase': 2,
                'title': 'Component State & React Ecosystem',
                'duration': '4 Weeks',
                'summary': 'Understand virtual DOM diffing, custom hooks, optimistic UI updates, client-side routing, and scalable server-state caching using TanStack Query.',
                'deliverable': 'High-performance real-time search & filtering interface with debouncing and virtualized lists.'
            },
            {
                'phase': 3,
                'title': 'Backend REST/GraphQL APIs & Relational Databases',
                'duration': '4 Weeks',
                'summary': 'Build secure RESTful endpoints in Node.js/Express, authenticate with JWT/OAuth2, model relational schemas with PostgreSQL, and write ACID-compliant transactions.',
                'deliverable': 'Secure Multi-Tenant Auth & Billing API with rate limiting and automated unit tests.'
            },
            {
                'phase': 4,
                'title': 'System Design, Caching & Cloud CI/CD',
                'duration': '3 Weeks',
                'summary': 'Implement Redis caching layers, Dockerize microservices, set up automated GitHub Actions deployment pipelines, and analyze time/space algorithmic complexity.',
                'deliverable': 'Production-ready containerized application running with zero downtime on Render/AWS.'
            }
        ],
        'capstones': [
            {
                'title': 'Collaborative Real-Time Workspace (Figma/Notion Hybrid)',
                'difficulty': 'Anchor Capstone (Advanced)',
                'summary': 'A multi-user canvas workspace featuring WebSocket live cursor synchronization, conflict-free state resolution, and persistent document storage.',
                'stack': ['React', 'TypeScript', 'WebSockets / Socket.io', 'PostgreSQL', 'Docker'],
                'key_features': ['Sub-50ms cursor sync latency', 'Optimistic offline edits', 'Role-based workspace permissions']
            },
            {
                'title': 'Scalable E-Commerce & Inventory Microservice',
                'difficulty': 'Full-Stack Capstone (Intermediate)',
                'summary': 'High-concurrency store backend handling atomic inventory decrementing, Stripe Webhooks, order tracking, and Redis inventory caching.',
                'stack': ['Node.js', 'Express', 'Redis', 'PostgreSQL', 'Stripe API'],
                'key_features': ['Race-condition prevention via DB locks', 'Idempotent webhook processing', 'Automated email receipt triggers']
            },
            {
                'title': 'Git Analytics & Developer Velocity Dashboard',
                'difficulty': 'Frontend Mastery Capstone',
                'summary': 'An analytical reporting suite that connects to the GitHub REST API to compute PR turnaround time, commit heatmaps, and team velocity metrics.',
                'stack': ['Next.js', 'Tailwind CSS', 'Chart.js', 'GitHub REST API'],
                'key_features': ['Dark-mode responsive visualization', 'Exportable PDF audit reports', 'OAuth account linking']
            }
        ],
        'interview_prep': [
            {
                'q': 'How does React fiber reconciliation work and why are keys essential in lists?',
                'a': 'Fiber is React\'s incremental rendering engine that breaks reconciliation into interruptible units of work. Keys provide stable element identities across renders, enabling React to reuse existing DOM nodes rather than destroying and recreating subtrees.'
            },
            {
                'q': 'What is the difference between SQL database indexing with B-Trees vs Hash indexes?',
                'a': 'B-Tree indexes maintain sorted keys, making them optimal for equality (=) and range queries (<, >, BETWEEN). Hash indexes provide O(1) lookups for strict equality but cannot assist with range scans or sorting.'
            }
        ]
    },

    'ai-machine-learning': {
        'slug': 'ai-machine-learning',
        'name': 'AI & Machine Learning',
        'tagline': 'Train deep neural networks, fine-tune open-source LLMs, and architect RAG pipelines.',
        'icon': 'fa-brain',
        'color': '#c084fc',
        'gradient': 'linear-gradient(135deg, #c084fc, #6366f1)',
        'badge': 'Next-Gen Frontier',
        'salary': '$120,000 - $220,000 / yr',
        'timeline': '14 - 18 Weeks (Intensive)',
        'prerequisites': 'Basic Python programming, high-school algebra & probability fundamentals.',
        'usp_tag': 'Proof-of-Work: Train custom vision models and deploy an enterprise RAG agent with vector databases.',
        'overview': 'Move past simple prompt wrappers. Learn mathematical foundations of gradient descent, build neural nets in PyTorch from scratch, and deploy real AI agents utilizing vector embeddings and local LLMs.',
        'phases': [
            {
                'phase': 1,
                'title': 'Mathematics & Vectorized Python',
                'duration': '3 Weeks',
                'summary': 'NumPy matrix operations, linear algebra transformations, multivariable calculus gradients, and statistical data visualization with Matplotlib & Seaborn.',
                'deliverable': 'Linear & Logistic Regression implemented from pure mathematical scratch without libraries.'
            },
            {
                'phase': 2,
                'title': 'Classical Machine Learning & Feature Engineering',
                'duration': '4 Weeks',
                'summary': 'Decision trees, Random Forests, XGBoost, PCA dimensionality reduction, cross-validation protocols, and hyperparameter tuning with Optuna.',
                'deliverable': 'High-accuracy tabular classification model submitted to an open Kaggle challenge.'
            },
            {
                'phase': 3,
                'title': 'Deep Neural Networks with PyTorch',
                'duration': '4 Weeks',
                'summary': 'Tensors, autograd, multi-layer perceptrons, Convolutional Networks (CNNs) for vision, and self-attention Transformer mechanisms.',
                'deliverable': 'Custom trained image classifier with data augmentation and real-time inference loop.'
            },
            {
                'phase': 4,
                'title': 'LLMs, Vector Embeddings & Agentic RAG',
                'duration': '4 Weeks',
                'summary': 'Fine-tuning with LoRA/QLoRA, ChromaDB/Pinecone vector embeddings, LangChain/LlamaIndex document parsing, and agentic tool-use loops.',
                'deliverable': 'Production RAG agent capable of answering domain-specific technical questions from raw PDFs.'
            }
        ],
        'capstones': [
            {
                'title': 'Autonomous Enterprise Research RAG Agent',
                'difficulty': 'Anchor Capstone (Advanced)',
                'summary': 'A multi-step research agent that ingests internal corporate documentation, embeds text into a vector database, and synthesizes cited answers with source links.',
                'stack': ['Python', 'LangChain', 'ChromaDB', 'FastAPI', 'Hugging Face Transformers'],
                'key_features': ['Hybrid dense/sparse retrieval (BM25 + Cosine)', 'Hallucination verification step', 'Interactive web interface']
            },
            {
                'title': 'Real-Time Edge Computer Vision Detector',
                'difficulty': 'Applied ML Capstone (Intermediate)',
                'summary': 'A fine-tuned YOLO object detection pipeline optimized with ONNX runtime for real-time video stream inspection in web browsers.',
                'stack': ['PyTorch', 'YOLOv8', 'ONNX Runtime', 'OpenCV', 'Streamlit'],
                'key_features': ['30+ FPS edge inference', 'Custom bounding box labeling pipeline', 'Precision-Recall evaluation curve']
            },
            {
                'title': 'Customer Sentiment & Intent Classification API',
                'difficulty': 'NLP Capstone',
                'summary': 'Fine-tuned DistilBERT transformer classifying customer support tickets into multi-label priorities and emotions with automated webhook dispatch.',
                'stack': ['PyTorch', 'Hugging Face Datasets', 'Docker', 'FastAPI'],
                'key_features': ['94%+ F1 score across 8 classes', 'Sub-20ms batch inference', 'Swagger documentation']
            }
        ],
        'interview_prep': [
            {
                'q': 'How does self-attention in Transformers differ from recurrent mechanisms in RNNs?',
                'a': 'RNNs process tokens sequentially, creating sequential dependency bottlenecks that prevent parallelization during training and struggle with long-range dependencies. Self-attention computes pairwise relationship weights across all tokens concurrently via Query, Key, and Value matrices, enabling massive parallelization and O(1) path length between any two tokens.'
            },
            {
                'q': 'What is the vanishing gradient problem and how do residual connections (ResNet) solve it?',
                'a': 'During backpropagation in deep networks, gradients computed through repeated matrix multiplications with small weights decay exponentially toward zero, preventing earlier layers from learning. Residual connections add skip paths: F(x) + x, ensuring the gradient can propagate directly back through the identity mapping with minimum factor of 1.'
            }
        ]
    },

    'cybersecurity': {
        'slug': 'cybersecurity',
        'name': 'Cybersecurity',
        'tagline': 'Master ethical exploitation, vulnerability assessment, network defense, and SIEM monitoring.',
        'icon': 'fa-shield-halved',
        'color': '#f43f5e',
        'gradient': 'linear-gradient(135deg, #f43f5e, #e11d48)',
        'badge': 'Critical Defense',
        'salary': '$90,000 - $175,000 / yr',
        'timeline': '12 - 16 Weeks (Hands-on Labs)',
        'prerequisites': 'Command-line basics, understanding of how IP addresses and websites communicate.',
        'usp_tag': 'Proof-of-Work: Conduct real vulnerability assessments and build hardened defense architectures.',
        'overview': 'Go beyond theory into practical ethical hacking. Analyze live network traffic with Wireshark, exploit OWASP Top 10 web vulnerabilities in sandboxed labs, and write defensive detection rules in Splunk.',
        'phases': [
            {
                'phase': 1,
                'title': 'Networking Foundations & Linux Administration',
                'duration': '3 Weeks',
                'summary': 'The OSI model, TCP/IP handshake, DNS poisoning, ARP spoofing, Linux permissions, firewall rules with iptables, and packet dissection in Wireshark.',
                'deliverable': 'PCAP forensic analysis report identifying unauthorized exfiltration packets.'
            },
            {
                'phase': 2,
                'title': 'Reconnaissance & Vulnerability Scanning',
                'duration': '4 Weeks',
                'summary': 'Passive/active intelligence gathering (OSINT), port mapping with Nmap, automated CVE scanning, and credential auditing with Hydra & Hashcat.',
                'deliverable': 'Comprehensive external vulnerability audit report of a sandboxed virtual network.'
            },
            {
                'phase': 3,
                'title': 'Web Application Security & OWASP Top 10',
                'duration': '4 Weeks',
                'summary': 'Interception proxies with Burp Suite, SQL injection, Cross-Site Scripting (XSS), CSRF tokens, Server-Side Request Forgery (SSRF), and broken access controls.',
                'deliverable': 'Exploit demonstration & remediation proof for 5 OWASP vulnerabilities.'
            },
            {
                'phase': 4,
                'title': 'Defensive Operations, SIEM & Incident Response',
                'duration': '3 Weeks',
                'summary': 'Security Information and Event Management (SIEM), Snort/Suricata IDS rules, log correlation, Windows Event ID analysis, and incident containment.',
                'deliverable': 'Configured SIEM dashboard detecting automated brute-force attacks in real time.'
            }
        ],
        'capstones': [
            {
                'title': 'Automated Attack Surface & Port Scanner (Python CLI)',
                'difficulty': 'Offensive Tooling Capstone',
                'summary': 'A multi-threaded CLI reconnaissance tool that checks target domains for open ports, outdated SSL certificates, and exposed git directories.',
                'stack': ['Python', 'Asyncio', 'Socket Programming', 'Nmap Scripting Engine'],
                'key_features': ['Async port scanning 10x faster than default sockets', 'Subdomain enumeration', 'JSON audit reports']
            },
            {
                'title': 'Vulnerable Lab Assessment & Hardening Walkthrough',
                'difficulty': 'Full Assessment Capstone',
                'summary': 'Complete black-box penetration test of a vulnerable VM (VulnHub / HackTheBox), obtaining root shell, followed by a defensive remediation guide.',
                'stack': ['Kali Linux', 'Burp Suite', 'Metasploit', 'Bash Scripting'],
                'key_features': ['Step-by-step exploit chain documentation', 'Patch verification', 'Executive summary presentation']
            },
            {
                'title': 'Threat Detection SIEM Lab with Live Telemetry',
                'difficulty': 'Defensive Blue Team Capstone',
                'summary': 'A distributed logging cluster that ingests auth logs, triggers Telegram/Slack alerts upon suspicious sudo escalation, and correlates IP threat intelligence.',
                'stack': ['Wazuh / Splunk', 'Elasticsearch', 'Docker', 'Linux Syslog'],
                'key_features': ['Custom Sigma detection rules', 'Real-time alert dispatch', 'Visual geo-IP attack map']
            }
        ],
        'interview_prep': [
            {
                'q': 'Explain the difference between Symmetric and Asymmetric encryption, and how TLS uses both.',
                'a': 'Symmetric encryption uses a single shared key for both encryption and decryption (fast, efficient for large payloads like AES). Asymmetric uses a public-private key pair (slower, computationally expensive like RSA/ECC). TLS uses asymmetric encryption during the initial handshake to authenticate server identity and securely agree on a session key, then switches to symmetric encryption for fast subsequent data transfer.'
            },
            {
                'q': 'How do you mitigate SQL Injection without breaking application functionality?',
                'a': 'The definitive defense is parameterized queries (prepared statements), where SQL code and user-supplied data are sent in separate packets and parsed independently by the database engine regardless of user input characters. Defense-in-depth also includes least-privilege database user permissions, ORM abstractions, and input validation.'
            }
        ]
    },

    'cloud-devops': {
        'slug': 'cloud-devops',
        'name': 'Cloud & DevOps',
        'tagline': 'Automate zero-downtime infrastructure with Docker, Kubernetes, AWS, and Terraform.',
        'icon': 'fa-cloud',
        'color': '#38bdf8',
        'gradient': 'linear-gradient(135deg, #0284c7, #38bdf8)',
        'badge': 'Enterprise Scale',
        'salary': '$100,000 - $190,000 / yr',
        'timeline': '12 - 16 Weeks',
        'prerequisites': 'Linux command-line basics, general understanding of servers and web hosting.',
        'usp_tag': 'Proof-of-Work: Deploy an auto-scaling Kubernetes cluster configured with declarative Terraform.',
        'overview': 'Bridge software development and IT infrastructure. Learn how the world\'s top engineering teams ship code 50 times a day with automated testing, immutable containers, and declarative cloud architectures.',
        'phases': [
            {
                'phase': 1,
                'title': 'Linux Internals, Bash Automation & Networking',
                'duration': '3 Weeks',
                'summary': 'File descriptors, systemd service management, SSH keys, cron jobs, network sockets, and writing production bash deployment scripts.',
                'deliverable': 'Automated server backup & health monitoring shell script with email alerting.'
            },
            {
                'phase': 2,
                'title': 'Docker Containerization & Multi-Stage Builds',
                'duration': '3 Weeks',
                'summary': 'Writing optimized micro-sized Dockerfiles, image layers, volumes, bridge networks, and multi-service orchestration with Docker Compose.',
                'deliverable': 'Dockerized multi-container full-stack application (Frontend + Backend + PostgreSQL + Redis).'
            },
            {
                'phase': 3,
                'title': 'Kubernetes Cluster Orchestration',
                'duration': '4 Weeks',
                'summary': 'Pods, Deployments, ReplicaSets, Services, Ingress controllers, ConfigMaps, Secrets, persistent volume claims, and rolling zero-downtime updates.',
                'deliverable': 'Production Kubernetes manifests deploying an auto-scaling application on Minikube/EKS.'
            },
            {
                'phase': 4,
                'title': 'Infrastructure as Code (Terraform) & GitHub Actions CI/CD',
                'duration': '4 Weeks',
                'summary': 'Declarative cloud provisioning on AWS, Terraform state management, reusable modules, GitHub Actions matrix testing, and Prometheus/Grafana monitoring.',
                'deliverable': 'End-to-end GitOps pipeline: push to main triggers automated tests, Docker build, and deployment.'
            }
        ],
        'capstones': [
            {
                'title': 'End-to-End GitOps Deployment Pipeline',
                'difficulty': 'Anchor Capstone (Advanced)',
                'summary': 'A complete automated pipeline where committing code to GitHub runs linter/tests, compiles a lightweight Docker container, scans for CVEs, and deploys to Kubernetes.',
                'stack': ['GitHub Actions', 'Docker', 'Kubernetes', 'Trivy Scanner', 'Helm'],
                'key_features': ['Automated vulnerability gating', 'Canary release rollback logic', 'Slack build notifications']
            },
            {
                'title': 'Multi-Tier AWS Cloud Infrastructure with Terraform',
                'difficulty': 'Cloud Infrastructure Capstone',
                'summary': 'Declarative Terraform code provisioning an AWS VPC with public/private subnets, NAT Gateways, an Application Load Balancer, and RDS PostgreSQL.',
                'stack': ['Terraform', 'AWS (VPC, EC2, RDS, ALB)', 'S3 Remote State'],
                'key_features': ['Modular code structure', 'Zero credentials hardcoded', 'Cost estimation output']
            },
            {
                'title': 'Distributed Observability Stack (Prometheus & Grafana)',
                'difficulty': 'SRE Capstone',
                'summary': 'Full metric and log telemetry platform monitoring server CPU, memory, HTTP request latency, and 5xx errors with custom alerting thresholds.',
                'stack': ['Prometheus', 'Grafana', 'Node Exporter', 'Alertmanager'],
                'key_features': ['Pre-built operational dashboard', 'P95/P99 latency tracking', 'Automated anomaly alerts']
            }
        ],
        'interview_prep': [
            {
                'q': 'What happens during a Kubernetes rolling update and how do liveness/readiness probes ensure zero downtime?',
                'a': 'During a rolling update, Kubernetes creates a new pod from the updated deployment specification. The readiness probe continuously checks if the new container is initialized and ready to receive traffic. Only when the readiness probe passes does Kubernetes route ingress traffic to the new pod and subsequently terminate the old pod.'
            },
            {
                'q': 'Why is storing Terraform state in a remote backend with state locking critical for teams?',
                'a': 'Terraform state records the mapping between real cloud resources and declarative code. A remote backend (like AWS S3) ensures all team members operate against a single source of truth. State locking (via DynamoDB) prevents concurrent team applies from corrupting the state file or creating conflicting cloud resources.'
            }
        ]
    },

    'data-science': {
        'slug': 'data-science',
        'name': 'Data Science & Analytics',
        'tagline': 'Turn raw enterprise databases into predictive models, statistical tests, and KPI dashboards.',
        'icon': 'fa-chart-pie',
        'color': '#34d399',
        'gradient': 'linear-gradient(135deg, #059669, #34d399)',
        'badge': 'Data Intelligence',
        'salary': '$90,000 - $170,000 / yr',
        'timeline': '12 - 16 Weeks',
        'prerequisites': 'Comfort with spreadsheets, basic algebra, and curiosity about business metrics.',
        'usp_tag': 'Proof-of-Work: Deliver statistical hypothesis tests and high-impact predictive dashboards.',
        'overview': 'Learn how tech giants use data to make billion-dollar decisions. Master advanced SQL, Python data wrangling with Pandas, statistical hypothesis testing (A/B testing), and executive dashboard storytelling.',
        'phases': [
            {
                'phase': 1,
                'title': 'Advanced SQL & Data Modeling',
                'duration': '3 Weeks',
                'summary': 'Common Table Expressions (CTEs), window functions (ROW_NUMBER, DENSE_RANK, LEAD/LAG), self-joins, indexing, and designing clean analytics schemas.',
                'deliverable': 'Comprehensive business cohort retention analysis written in pure SQL.'
            },
            {
                'phase': 2,
                'title': 'Python Pandas & Exploratory Data Analysis',
                'duration': '4 Weeks',
                'summary': 'Cleaning missing data, vector string operations, datetime manipulation, pivot tables, and statistical distribution plotting with Seaborn & Plotly.',
                'deliverable': 'Jupyter Notebook conducting exploratory data analysis on 500,000+ real e-commerce transactions.'
            },
            {
                'phase': 3,
                'title': 'Statistical Inference & A/B Experimentation',
                'duration': '4 Weeks',
                'summary': 'Central Limit Theorem, hypothesis formulation, t-tests, chi-squared tests, p-value calculation, confidence intervals, and statistical power analysis.',
                'deliverable': 'End-to-end A/B test analysis report with sample size calculations and revenue impact.'
            },
            {
                'phase': 4,
                'title': 'Predictive Modeling & Executive Storytelling',
                'duration': '3 Weeks',
                'summary': 'Feature selection, Logistic Regression, Random Forests, XGBoost, model evaluation (ROC-AUC, Precision/Recall), and building interactive PowerBI/Tableau dashboards.',
                'deliverable': 'Customer Churn Predictor model with interactive probability dashboard for executives.'
            }
        ],
        'capstones': [
            {
                'title': 'Predictive Customer Churn Engine & Prevention Dashboard',
                'difficulty': 'Anchor Capstone (Advanced)',
                'summary': 'A machine learning system that flags high-risk subscription cancellations 30 days in advance, estimating saved recurring revenue.',
                'stack': ['Python', 'Pandas', 'XGBoost', 'Scikit-Learn', 'Streamlit'],
                'key_features': ['SHAP feature explainability', 'Threshold tuning for recall', 'Interactive scenario calculator']
            },
            {
                'title': 'Product A/B Experimentation Suite',
                'difficulty': 'Statistical Capstone',
                'summary': 'A statistical calculation framework evaluating conversion rate differences, calculating minimum detectable effect, and detecting sample ratio mismatch (SRM).',
                'stack': ['Python', 'SciPy', 'Statsmodels', 'Plotly'],
                'key_features': ['Bayesian & Frequentist comparisons', 'Automated outlier filtering', 'Executive summary presentation']
            },
            {
                'title': 'Executive SaaS Growth & Cohort Analysis Dashboard',
                'difficulty': 'BI & Storytelling Capstone',
                'summary': 'High-impact business intelligence dashboard tracking Monthly Recurring Revenue (MRR), Customer Acquisition Cost (CAC), and LTV by marketing channel.',
                'stack': ['PostgreSQL', 'PowerBI / Tableau', 'SQL CTEs'],
                'key_features': ['Dynamic date granularity drilldowns', 'Churn heatmap visualization', 'Automated weekly refresh']
            }
        ],
        'interview_prep': [
            {
                'q': 'How do you detect and handle multicollinearity in regression models?',
                'a': 'Multicollinearity occurs when independent variables are highly correlated, inflating coefficient variances and making interpretation unreliable. Detect it using Variance Inflation Factor (VIF > 5-10 indicates issues) or correlation heatmaps. Remediate by dropping redundant variables, combining correlated features via PCA, or using L2 regularization (Ridge regression).'
            },
            {
                'q': 'What is Sample Ratio Mismatch (SRM) in an A/B test and why does it invalidate results?',
                'a': 'SRM occurs when the observed ratio of traffic between Control and Variant differs significantly from the intended design (e.g. 50/50 target yields 52/48 with p < 0.001 on a Chi-Square test). It indicates systematic assignment bias, technical tracking failure, or bot filtering that breaks randomization, rendering any statistical significance unreliable.'
            }
        ]
    },

    'product-design': {
        'slug': 'product-design',
        'name': 'Product Design (UI/UX)',
        'tagline': 'Craft high-converting user interfaces, cohesive design systems, and rapid prototypes.',
        'icon': 'fa-layer-group',
        'color': '#818cf8',
        'gradient': 'linear-gradient(135deg, #6366f1, #818cf8)',
        'badge': 'Creative Systems',
        'salary': '$80,000 - $160,000 / yr',
        'timeline': '10 - 14 Weeks',
        'prerequisites': 'Keen eye for visual aesthetics, interest in human psychology and interface usability.',
        'usp_tag': 'Proof-of-Work: Ship complete Figma design systems and production-ready interactive mobile app flows.',
        'overview': 'Become the designer engineers love working with. Learn visual hierarchy, typography, WCAG accessibility, user journey mapping, and master Figma auto-layout and interactive smart animations.',
        'phases': [
            {
                'phase': 1,
                'title': 'Design Fundamentals & Figma Fluency',
                'duration': '3 Weeks',
                'summary': 'Color theory, 8pt spatial grid systems, typographic hierarchy, layout contrast, and mastering Figma keyboard shortcuts and vector networks.',
                'deliverable': 'Clean 3-screen landing page design with strict component spacing.'
            },
            {
                'phase': 2,
                'title': 'Information Architecture & Wireframing',
                'duration': '3 Weeks',
                'summary': 'User research interviews, persona mapping, task flows, low-fidelity wireframing, and user testing methodology.',
                'deliverable': 'Complete low-fidelity wireframe prototype for an on-demand service app.'
            },
            {
                'phase': 3,
                'title': 'Advanced Design Systems & Tokens',
                'duration': '4 Weeks',
                'summary': 'Component properties, variants, Figma auto-layout 5.0, variables, design tokens (colors, radii, elevations), and dark-mode theming.',
                'deliverable': 'A published reusable 40+ component design system with interactive button states and modals.'
            },
            {
                'phase': 4,
                'title': 'High-Fidelity Prototyping & Developer Handoff',
                'duration': '3 Weeks',
                'summary': 'Smart Animate transitions, micro-interactions, responsive design constraints, developer documentation, and redlining in Dev Mode.',
                'deliverable': 'Interactive clickable prototype ready for stakeholder presentation and engineering handoff.'
            }
        ],
        'capstones': [
            {
                'title': 'Next-Gen Mobile Banking & Investment App',
                'difficulty': 'Anchor Capstone (Advanced)',
                'summary': 'An end-to-end fintech mobile application featuring portfolio tracking, instant peer-to-peer transfers, biometric authorization, and dark-mode styling.',
                'stack': ['Figma Pro', 'Design Systems', 'Prototyping', 'WCAG 2.1 AA'],
                'key_features': ['Complete component library', 'Figma Smart Animate micro-interactions', 'User testing feedback iterations']
            },
            {
                'title': 'Multi-Brand Enterprise Design System',
                'difficulty': 'Design Systems Capstone',
                'summary': 'A modular component architecture utilizing Figma variables to switch seamlessly between two entirely different brand visual identities with one click.',
                'stack': ['Figma Variables', 'Design Tokens', 'Auto-Layout'],
                'key_features': ['Automated dark/light theme switching', 'Accessible WCAG contrast ratios', 'Developer handoff specs']
            },
            {
                'title': 'Health & Fitness Habit Tracker Case Study',
                'difficulty': 'UX Research Capstone',
                'summary': 'Comprehensive user research case study detailing problem discovery, empathy maps, low-fi iteration, usability testing, and final UI polish.',
                'stack': ['Figma', 'FigJam', 'Maze User Testing'],
                'key_features': ['Documented user research insights', 'Before-and-after redesign metrics', 'Interactive prototype link']
            }
        ],
        'interview_prep': [
            {
                'q': 'How do you balance business conversion goals with user-centric usability?',
                'a': 'By recognizing that sustainable business growth requires solving real user friction rather than exploiting dark patterns. I conduct usability testing to pinpoint drop-offs, align design solutions with core business KPIs (e.g. reducing cart abandonment by streamlining form fields), and validate iterations through rigorous A/B testing.'
            },
            {
                'q': 'How do you structure design tokens to ensure seamless collaboration with frontend engineers?',
                'a': 'I use a 3-tier token structure: Global Tokens (raw values like blue-500: #38bdf8), Semantic/Alias Tokens (purpose-driven like bg-interactive-default: blue-500), and Component-Specific Tokens (like button-primary-bg). This allows designers and engineers to speak the same language and makes theming effortless.'
            }
        ]
    },

    'post-production': {
        'slug': 'post-production',
        'name': 'Post-Production & Video',
        'tagline': 'Direct visual narratives with DaVinci Resolve color grading, pacing cuts, and sound design.',
        'icon': 'fa-video',
        'color': '#fb7185',
        'gradient': 'linear-gradient(135deg, #e11d48, #fb7185)',
        'badge': 'Cinematic Media',
        'salary': '$70,000 - $140,000 / yr',
        'timeline': '10 - 14 Weeks',
        'prerequisites': 'Computer with dedicated GPU, basic understanding of video and audio files.',
        'usp_tag': 'Proof-of-Work: Cut, color grade, and master 3 broadcast-quality narrative and commercial edits.',
        'overview': 'Learn what separates amateur video hobbyists from broadcast editors. Master non-linear timeline assembly, narrative cutting rhythms, node-based color science in DaVinci Resolve, and multi-track audio sound design.',
        'phases': [
            {
                'phase': 1,
                'title': 'NLE Editing Workflows & The Rough Cut',
                'duration': '3 Weeks',
                'summary': 'Keyboard shortcuts, asset organization, bin structures, sync sound, timeline assembly, and narrative pacing techniques.',
                'deliverable': 'A 90-second dynamic dialogue scene cut with seamless continuity and shot matching.'
            },
            {
                'phase': 2,
                'title': 'Cinematic Sound Design & Audio Mixing',
                'duration': '3 Weeks',
                'summary': 'Foley effects, background ambiance, dialogue leveling (-12dB to -6dB), EQ ducking under music, and audio transitional whooshes.',
                'deliverable': 'Multi-track audio soundscape with balanced vocal clarity and immersive stereo atmosphere.'
            },
            {
                'phase': 3,
                'title': 'DaVinci Resolve Color Science & Grading',
                'duration': '4 Weeks',
                'summary': 'Primary balance wheels, RGB parade scopes, curves, hue-vs-saturation, skin tone lines, cinematic LUTs, and power windows.',
                'deliverable': 'Professional color grade matching disparate log footage cameras into a cohesive cinematic palette.'
            },
            {
                'phase': 4,
                'title': 'Motion Graphics, Titles & Web Delivery',
                'duration': '3 Weeks',
                'summary': 'Keyframing, kinetic typography, lower thirds, aspect ratio framing (16:9 vs 9:16), compression codecs, and mastering for YouTube/Cinema.',
                'deliverable': 'Finished 60-second commercial spec ad with animated logo resolve and delivery codecs.'
            }
        ],
        'capstones': [
            {
                'title': 'Cinematic Brand Commercial Spec (30s / 60s)',
                'difficulty': 'Anchor Capstone (Advanced)',
                'summary': 'Complete editing, sound design, color grade, and kinetic title graphics for a high-end luxury or tech product commercial.',
                'stack': ['DaVinci Resolve Studio', 'Premiere Pro', 'Fairlight Audio'],
                'key_features': ['Pacing synchronized to custom soundtrack', 'Color matching across multiple cameras', '1080p and 4K masters']
            },
            {
                'title': 'Narrative Short Film Dramatic Scene Cut',
                'difficulty': 'Storytelling Capstone',
                'summary': 'A multi-angle dramatic conversation scene balancing emotional pauses, eye-trace editing, and invisible cuts that pull the viewer in.',
                'stack': ['DaVinci Resolve', 'Sound Design Library'],
                'key_features': ['Seamless continuity editing', 'Dialogue de-noising and leveling', 'Exportable EDL/XML file']
            },
            {
                'title': 'High-Retention Dynamic Social Reel Campaign',
                'difficulty': 'Commercial Fast-Paced Capstone',
                'summary': 'Three vertical 9:16 short-form videos featuring kinetic captions, zoom transitions, sound effects on every cut, and color popping.',
                'stack': ['CapCut Pro / DaVinci', 'Motion Titles'],
                'key_features': ['Under 3-second hook placement', 'Auto-caption styling', 'High-contrast mobile grading']
            }
        ],
        'interview_prep': [
            {
                'q': 'How do you read waveform and vectorscope monitors to achieve proper skin tone fidelity?',
                'a': 'Waveform monitors display luminance (exposure) across the frame from 0 (crushed black) to 1023 (clipped white); Caucasian skin tones typically sit around 60-70 IRE, while darker tones sit between 40-55 IRE. The vectorscope displays chrominance; the dedicated skin tone indicator line shows where blood flow under human skin sits regardless of ethnicity, requiring hue adjustments until vectors land flush on the line.'
            },
            {
                'q': 'What is J-cutting and L-cutting and why are they fundamental to natural dialogue pacing?',
                'a': 'In a J-cut, the incoming scene\'s audio begins before the visual transition occurs. In an L-cut, the outgoing scene\'s audio continues underneath the incoming visual. In real life, people look at someone before they speak, or watch a listener\'s reaction while the speaker is still talking; split edits mimic natural human perception and eliminate robotic, back-and-forth ping-pong cuts.'
            }
        ]
    },

    'audio-engineering': {
        'slug': 'audio-engineering',
        'name': 'Audio Engineering & Production',
        'tagline': 'Sequence beats, carve pristine acoustic mixes, and master tracks for streaming loudness standards.',
        'icon': 'fa-sliders',
        'color': '#fbbf24',
        'gradient': 'linear-gradient(135deg, #d97706, #fbbf24)',
        'badge': 'Acoustic Precision',
        'salary': '$65,000 - $135,000 / yr',
        'timeline': '10 - 14 Weeks',
        'prerequisites': 'Good pair of monitor headphones or speakers, passion for music production.',
        'usp_tag': 'Proof-of-Work: Mix and master 3 complete multi-track songs to Spotify/Apple commercial loudness standards.',
        'overview': 'Learn the science behind professional music and sound design. Master DAW routing, synthesis, parametric EQ frequency cleanup, dynamic compression, stereo widening, and LUFS loudness mastering.',
        'phases': [
            {
                'phase': 1,
                'title': 'DAW Signal Flow & MIDI Sequencing',
                'duration': '3 Weeks',
                'summary': 'Audio interfaces, buffer sizes, sample rates, MIDI velocity programming, drum sequencing, and subtractive synthesis oscillators.',
                'deliverable': 'Full 4-bar instrumental beat with drum groove, bassline, and lead synth chords.'
            },
            {
                'phase': 2,
                'title': 'Recording Techniques & Gain Staging',
                'duration': '3 Weeks',
                'summary': 'Microphone polar patterns, proximity effect, room acoustic treatment, setting proper preamp headroom (-18dBFS nominal), and vocal comping.',
                'deliverable': 'Clean, unclipped multi-track vocal and instrument recording session.'
            },
            {
                'phase': 3,
                'title': 'The Mix: EQ, Compression & Spatial Effects',
                'duration': '4 Weeks',
                'summary': 'High-pass filtering, resolving kick/bass frequency collisions with sidechaining, serial compression, parallel saturation, reverb pre-delay, and stereo panning.',
                'deliverable': 'A clean, punchy multi-track mix with high separation between instruments and clear vocal presence.'
            },
            {
                'phase': 4,
                'title': 'Mastering & Streaming Compliance',
                'duration': '3 Weeks',
                'summary': 'Mid/Side EQ processing, multi-band compression, true peak limiting, metering with -14 LUFS integrated targets, and dithering for 16-bit/44.1kHz delivery.',
                'deliverable': 'Commercial-ready mastered audio file matching streaming reference tracks.'
            }
        ],
        'capstones': [
            {
                'title': 'Complete Multi-Track Song Mix & Master',
                'difficulty': 'Anchor Capstone (Advanced)',
                'summary': 'Take 24+ raw audio stems, perform surgical frequency carving, dynamic control, reverb depth, and master to -14 LUFS commercial loudness.',
                'stack': ['Ableton Live / FL Studio / Pro Tools', 'FabFilter / Stock EQ', 'LUFS Meter'],
                'key_features': ['Balanced low-end kick and bass interaction', 'Wide stereo image without phase cancellation', 'Side-by-side A/B before/after audio comparison']
            },
            {
                'title': 'Film & Game Spatial Sound Design Portfolio',
                'difficulty': 'Sound Design Capstone',
                'summary': 'Create original synthesized and foley sound effects for a 60-second sci-fi or fantasy game trailer from complete silence.',
                'stack': ['Serum Synthesizer', 'Audio Warp', 'Granular Reverb'],
                'key_features': ['Original laser, impact, and monster sound synthesis', 'Sub-bass impact transient design', 'Clean stereo separation']
            },
            {
                'title': 'Original Electronic/Hip-Hop Beat Production EP',
                'difficulty': 'Production Capstone',
                'summary': 'Produce a 2-track mini EP featuring sequenced rhythm sections, custom chord progressions, vocal chops, and polished arrangement transitions.',
                'stack': ['DAW', 'Drum Synthesis', 'Sampler'],
                'key_features': ['Dynamic tension and release buildup', 'Professional transitions (sweeps, reverses)', 'Radio-ready arrangement']
            }
        ],
        'interview_prep': [
            {
                'q': 'How do you resolve masking between the kick drum and bass guitar in a mix?',
                'a': 'Masking occurs when two instruments compete for the exact same low-frequency spectrum (typically 50-100Hz). I assign primary sub-bass weight to one (e.g. kick at 60Hz, bass at 100Hz) and use complementary EQ to carve a surgical notch where the other dominates. Additionally, sidechain compression ducks the bass by 2-4dB for a few milliseconds whenever the kick transient strikes.'
            },
            {
                'q': 'What is the difference between Peak, RMS, and LUFS audio metering?',
                'a': 'Peak measures the absolute highest instantaneous voltage level in the signal (critical for avoiding digital clipping). RMS (Root Mean Square) calculates the mathematical average power over time. LUFS (Loudness Units Full Scale) incorporates human auditory perception curves (K-weighting), making it the gold standard for perceived volume consistency across streaming platforms.'
            }
        ]
    },

    'game-development': {
        'slug': 'game-development',
        'name': 'Game Development (3D & Indie)',
        'tagline': 'Build playable interactive worlds with Unity, Unreal Engine 5, C# scripting, and game physics.',
        'icon': 'fa-cube',
        'color': '#34d399',
        'gradient': 'linear-gradient(135deg, #059669, #10b981)',
        'badge': 'Real-Time 3D',
        'salary': '$80,000 - $165,000 / yr',
        'timeline': '14 - 18 Weeks',
        'prerequisites': 'Basic coding familiarity, interest in 3D geometry and interactive game loops.',
        'usp_tag': 'Proof-of-Work: Build and compile 3 fully playable indie games runnable in browsers or executable files.',
        'overview': 'Turn your ideas into playable interactive experiences. Learn component architecture, physics engine raycasting, character animation state machines, AI enemy state loops, and compile optimized game builds.',
        'phases': [
            {
                'phase': 1,
                'title': 'Game Engine Basics & C# Programming',
                'duration': '3 Weeks',
                'summary': 'Scene hierarchies, game loops (Update vs FixedUpdate), transforms, vector math, and clean object-oriented C# scripting fundamentals.',
                'deliverable': 'Playable 2D arcade game with score tracking and collision mechanics.'
            },
            {
                'phase': 2,
                'title': '3D Physics & Responsive Character Controllers',
                'duration': '4 Weeks',
                'summary': 'Rigidbodies, colliders, raycasting, character movement with jumping/crouching, ground checks, and Cinemachine third-person camera controls.',
                'deliverable': 'Tight 3D platforming obstacle course with jump momentum and moving platforms.'
            },
            {
                'phase': 3,
                'title': 'AI Enemy Logic & Combat Game Loops',
                'duration': '4 Weeks',
                'summary': 'NavMesh pathfinding, state machines (Idle, Patrol, Chase, Attack), health/damage systems, particle effects, and spatial audio cues.',
                'deliverable': 'Combat arena where the player battles wave-based AI enemies with custom attack patterns.'
            },
            {
                'phase': 4,
                'title': 'Optimization, UI Menus & Game Publishing',
                'duration': '3 Weeks',
                'summary': 'Draw call batching, LOD (Level of Detail), occlusion culling, game save states, pause menus, and compiling for WebGL and Windows.',
                'deliverable': 'Completed indie game build published live on itch.io with playable browser demo.'
            }
        ],
        'capstones': [
            {
                'title': '3D Isometric Rogue-Lite Action Game',
                'difficulty': 'Anchor Capstone (Advanced)',
                'summary': 'A complete isometric dungeon combat game featuring procedural enemy waves, multiple weapon archetypes, dash mechanics, and upgrade progression.',
                'stack': ['Unity 3D / Godot', 'C#', 'NavMesh AI', 'Cinemachine'],
                'key_features': ['Fluid character combat controller', 'Enemy state machine AI', 'WebGL browser build']
            },
            {
                'title': 'Physics-Based Puzzle Platformer',
                'difficulty': 'Gameplay Mechanics Capstone',
                'summary': 'A 3D puzzle game where the player manipulates gravity, switches, and laser reflections to solve increasingly complex physics rooms.',
                'stack': ['Unity 3D', 'Physics Engine', 'C# Scripting'],
                'key_features': ['Custom gravity manipulation mechanics', 'Dynamic lighting and particle triggers', 'Save-game state persistence']
            },
            {
                'title': 'Modular Low-Poly Level Design & Environment Demo',
                'difficulty': 'Level Design Capstone',
                'summary': 'An atmospheric 3D environment crafted with modular asset snapping, post-processing volumetric fog, ambient audio, and interactive discoverables.',
                'stack': ['Blender', 'Unity / Unreal Engine 5', 'Post-Processing'],
                'key_features': ['Optimized draw-calls under 100k polygons', 'Dynamic day/night cycle', 'First-person walking controller']
            }
        ],
        'interview_prep': [
            {
                'q': 'Why should physics calculations always occur in FixedUpdate rather than Update in Unity?',
                'a': 'Update runs once per rendered frame, meaning its time step varies with frame rate fluctuations. FixedUpdate runs on a consistent, discrete internal physics timer (e.g. exactly every 0.02 seconds). Performing physics calculations in Update produces non-deterministic behavior, glitchy collisions, and tunnel-through bugs when frame rates drop.'
            },
            {
                'q': 'How do object pooling patterns prevent stuttering and garbage collection lag in games?',
                'a': 'Repeatedly instantiating and destroying game objects (like bullets or particle effects) frequently allocates and deallocates memory, triggering the C# garbage collector and causing frame rate drops. Object pooling pre-allocates an inactive pool of objects at startup, enabling and recycling them as needed to ensure zero runtime GC allocations.'
            }
        ]
    },

    'digital-content': {
        'slug': 'digital-content',
        'name': 'Digital Content & Audience Growth',
        'tagline': 'Engineer viral retention pacing, CTR thumbnail psychology, and multi-channel audience leverage.',
        'icon': 'fa-chart-line',
        'color': '#818cf8',
        'gradient': 'linear-gradient(135deg, #4f46e5, #818cf8)',
        'badge': 'Creator Economy',
        'salary': '$60,000 - $200,000+ / yr (Uncapped)',
        'timeline': '8 - 12 Weeks',
        'prerequisites': 'Basic familiarity with social video platforms (YouTube, TikTok, X), desire to build personal leverage.',
        'usp_tag': 'Proof-of-Work: Launch a high-retention video channel with verified script hooks and analytics optimization.',
        'overview': 'Stop posting into the void. Understand algorithmic distribution, thumbnail psychological triggers, scriptwriting retention loops, and build an automated media machine that compounds personal career leverage.',
        'phases': [
            {
                'phase': 1,
                'title': 'Niche Positioning & Content Pillars',
                'duration': '2 Weeks',
                'summary': 'Audience pain-point discovery, search volume vs curiosity arbitrage, positioning statements, and competitor gap auditing.',
                'deliverable': 'Comprehensive 30-day content calendar targeting 3 high-affinity audience pillars.'
            },
            {
                'phase': 2,
                'title': 'Scripting Frameworks & The First 3 Seconds',
                'duration': '3 Weeks',
                'summary': 'The Visual Hook + Audio Hook formula, open loops, tension escalations, pattern interrupts, and trimming all verbal filler.',
                'deliverable': 'Three verified video scripts optimized for 60%+ Average View Duration (AVD).'
            },
            {
                'phase': 3,
                'title': 'High-CTR Visual Packaging & Thumbnail Psychology',
                'duration': '3 Weeks',
                'summary': 'Color contrast, eye gaze theory, 3-element composition rule, title curiosity gaps vs clickbait, and A/B thumbnail testing.',
                'deliverable': 'Five high-converting thumbnail variants created in Figma/Photoshop with 10%+ CTR targets.'
            },
            {
                'phase': 4,
                'title': 'Analytics Diagnostics & Cross-Platform Repurposing',
                'duration': '2 Weeks',
                'summary': 'Diagnosing retention graph drop-off spikes, repurposing long-form video into high-yield short clips and text newsletters, and monetization pipelines.',
                'deliverable': 'A published long-form video with 3 repurposed vertical shorts and analytic breakdown.'
            }
        ],
        'capstones': [
            {
                'title': 'High-Retention Video Production & Launch Campaign',
                'difficulty': 'Anchor Capstone (Advanced)',
                'summary': 'Script, film, edit, design thumbnails, and publish an original high-production 8-12 minute video engineered for 50%+ retention.',
                'stack': ['CapCut Pro / Premiere', 'Figma Thumbnails', 'YouTube Studio Analytics'],
                'key_features': ['Documented script retention loops', 'A/B thumbnail testing setup', 'Detailed retention graph post-mortem']
            },
            {
                'title': 'Automated Multi-Channel Content Repurposing Pipeline',
                'difficulty': 'Growth Architecture Capstone',
                'summary': 'A standardized production pipeline turning 1 core weekly piece of long-form thought leadership into 5 vertical shorts, 2 carousel graphics, and 1 newsletter.',
                'stack': ['Notion Media Hub', 'CapCut', 'Buffer / Typefully'],
                'key_features': ['Standard operating procedure (SOP) documentation', 'Repurposing template guidelines', 'Asset staging hub']
            },
            {
                'title': 'Audience Conversion Funnel & Digital Lead Magnet',
                'difficulty': 'Monetization Capstone',
                'summary': 'A complete conversion funnel taking social media viewers through an educational lead magnet, email capture page, and welcome sequence.',
                'stack': ['ConvertKit / Mailchimp', 'Substack / Carrd', 'Notion Guide'],
                'key_features': ['High-converting landing page', '5-day automated welcome email sequence', '100% free value deliverable']
            }
        ],
        'interview_prep': [
            {
                'q': 'How do you diagnose and fix a sharp retention drop-off in the first 15 seconds of a YouTube video?',
                'a': 'A steep early drop indicates a packaging-to-content mismatch. The title and thumbnail promised something that the opening 15 seconds failed to validate. Fix it by immediately confirming the premise within the first 3 seconds, eliminating generic intros and logo animations, and introducing an immediate open loop or high-stakes visual hook.'
            },
            {
                'q': 'What is the curiosity gap in title writing and how do you leverage it without misleading viewers?',
                'a': 'The curiosity gap highlights a discrepancy between what the audience knows and what they want to know, provoking an irresistible psychological itch to resolve it. Ethical implementation creates intriguing contrast (e.g. "Why Senior Engineers Write Less Code") that the video content thoroughly and satisfyingly pays off.'
            }
        ]
    }
}
