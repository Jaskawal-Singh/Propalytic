"""
Propalytic-inspired Team page component with enhanced animations
"""

import streamlit as st
from typing import Dict, List


def render_team_page():
    """
    Render the team page with Propalytic design and enhanced animations
    """
    # Enhanced team page CSS
    team_css = """
    <style>
    .team-hero {
        text-align: center;
        padding: 5rem 2rem;
        background: radial-gradient(ellipse at center, rgba(139, 92, 246, 0.08) 0%, transparent 70%);
        border-radius: var(--radius-2xl);
        margin-bottom: 4rem;
        position: relative;
        overflow: hidden;
    }
    
    .team-hero::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: var(--gradient-mesh);
        opacity: 0.3;
        animation: meshRotate 20s linear infinite;
    }
    
    @keyframes meshRotate {
        0% { transform: rotate(0deg) scale(1); }
        100% { transform: rotate(360deg) scale(1.1); }
    }
    
    .team-hero-content {
        position: relative;
        z-index: 1;
    }
    
    .team-title {
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 800;
        background: var(--gradient-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1.5rem;
        animation: titleSlideUp 1s ease-out;
    }
    
    @keyframes titleSlideUp {
        0% { opacity: 0; transform: translateY(30px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    .team-subtitle {
        font-size: 1.375rem;
        color: var(--text-secondary);
        max-width: 700px;
        margin: 0 auto;
        line-height: 1.7;
        animation: fadeInUp 1s ease-out 0.3s both;
    }
    
    @keyframes fadeInUp {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    .team-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 2.5rem;
        margin: 4rem 0;
        animation: gridFadeIn 1.2s ease-out 0.6s both;
    }
    
    @keyframes gridFadeIn {
        0% { opacity: 0; transform: translateY(40px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    .team-card {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(24px) saturate(180%);
        border: 2px solid var(--border-light);
        border-radius: var(--radius-2xl);
        padding: 2.5rem;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
        box-shadow: var(--shadow-lg);
        transform: translateY(0) scale(1);
    }
    
    [data-theme="dark"] .team-card {
        background: rgba(15, 23, 42, 0.9);
    }
    
    .team-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(139, 92, 246, 0.15), transparent);
        transition: left 0.8s ease;
    }
    
    .team-card::after {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        background: radial-gradient(circle, rgba(139, 92, 246, 0.1) 0%, transparent 70%);
        transition: all 0.6s ease;
        border-radius: 50%;
        transform: translate(-50%, -50%);
        z-index: 0;
    }
    
    .team-card:hover::before {
        left: 100%;
    }
    
    .team-card:hover::after {
        width: 300px;
        height: 300px;
    }
    
    .team-card:hover {
        transform: translateY(-12px) scale(1.03);
        box-shadow: var(--shadow-2xl);
        border-color: var(--accent-purple);
    }
        box-shadow: var(--shadow-2xl);
        border-color: var(--primary-purple);
    }
    
    .team-avatar {
        width: 120px;
        height: 120px;
        border-radius: var(--radius-full);
        margin: 0 auto 1.5rem;
        background: var(--gradient-primary);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 3rem;
        color: white;
        position: relative;
        overflow: hidden;
    }
    
    .team-avatar::after {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.3) 0%, transparent 70%);
        animation: shimmer 3s linear infinite;
    }
    
    @keyframes shimmer {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .team-name {
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 0.5rem;
    }
    
    .team-role {
        font-size: 1rem;
        color: var(--primary-purple);
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .team-bio {
        color: var(--text-secondary);
        line-height: 1.6;
        margin-bottom: 1.5rem;
    }
    
    .team-skills {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        justify-content: center;
        margin-bottom: 1.5rem;
    }
    
    .team-skill {
        background: rgba(139, 92, 246, 0.1);
        color: var(--primary-purple);
        padding: 0.25rem 0.75rem;
        border-radius: var(--radius-full);
        font-size: 0.875rem;
        font-weight: 500;
    }
    
    .team-social {
        display: flex;
        justify-content: center;
        gap: 1rem;
    }
    
    .team-social-link {
        width: 40px;
        height: 40px;
        border-radius: var(--radius-full);
        background: var(--bg-tertiary);
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--text-secondary);
        text-decoration: none;
        transition: all 0.2s ease;
        font-size: 1.25rem;
    }
    
    .team-social-link:hover {
        background: var(--primary-purple);
        color: white;
        transform: translateY(-2px);
    }
    
    .stats-section {
        background: var(--gradient-card);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-xl);
        padding: 2rem;
        margin: 3rem 0;
        backdrop-filter: blur(10px);
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 2rem;
        text-align: center;
    }
    
    .stat-item {
        padding: 1rem;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 800;
        background: var(--gradient-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        display: block;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        color: var(--text-secondary);
        font-weight: 500;
    }
    
    .values-section {
        text-align: center;
        margin: 4rem 0;
    }
    
    .values-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }
    
    .value-card {
        background: var(--gradient-card);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-xl);
        padding: 2rem;
        text-align: center;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .value-card:hover {
        transform: translateY(-4px);
        box-shadow: var(--shadow-lg);
    }
    
    .value-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    .value-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 1rem;
    }
    
    .value-description {
        color: var(--text-secondary);
        line-height: 1.6;
    }
    
    @media (max-width: 768px) {
        .team-title {
            font-size: 2rem;
        }
        
        .team-grid {
            grid-template-columns: 1fr;
        }
        
        .stats-grid {
            grid-template-columns: repeat(2, 1fr);
        }
        
        .values-grid {
            grid-template-columns: 1fr;
        }
    }
    </style>
    """
    
    st.markdown(team_css, unsafe_allow_html=True)
    
    # Hero section
    st.markdown("""
    <div class="team-hero">
        <div class="team-hero-content">
            <h1 class="team-title">Meet Our Team</h1>
            <p class="team-subtitle">
                Passionate developers, data scientists, and designers working together to create 
                innovative solutions for the real estate industry.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Team members data
    team_members = [
        {
            "name": "Alex Chen",
            "role": "Lead Data Scientist",
            "avatar": "👨‍💻",
            "bio": "Specialized in machine learning and predictive modeling with 8+ years of experience in real estate analytics.",
            "skills": ["Python", "Machine Learning", "TensorFlow", "Statistical Analysis"],
            "social": {"github": "#", "linkedin": "#", "twitter": "#"}
        },
        {
            "name": "Sarah Johnson",
            "role": "Full-Stack Developer", 
            "avatar": "👩‍💻",
            "bio": "Expert in web development and user experience design, passionate about creating intuitive interfaces.",
            "skills": ["React", "Python", "UI/UX", "Streamlit"],
            "social": {"github": "#", "linkedin": "#", "twitter": "#"}
        },
        {
            "name": "Michael Rodriguez",
            "role": "ML Engineer",
            "avatar": "🧑‍🔬",
            "bio": "Focuses on model optimization and deployment, ensuring our predictions are accurate and reliable.",
            "skills": ["MLOps", "Docker", "AWS", "Model Optimization"],
            "social": {"github": "#", "linkedin": "#", "twitter": "#"}
        },
        {
            "name": "Emily Zhang",
            "role": "Product Designer",
            "avatar": "👩‍🎨", 
            "bio": "Creates beautiful and functional user interfaces with a focus on accessibility and user experience.",
            "skills": ["Figma", "User Research", "Prototyping", "Design Systems"],
            "social": {"github": "#", "linkedin": "#", "dribbble": "#"}
        },
        {
            "name": "David Kim",
            "role": "DevOps Engineer",
            "avatar": "👨‍🔧",
            "bio": "Ensures our applications run smoothly and scale efficiently, managing infrastructure and deployments.",
            "skills": ["Kubernetes", "CI/CD", "Monitoring", "Cloud Architecture"],
            "social": {"github": "#", "linkedin": "#", "twitter": "#"}
        },
        {
            "name": "Lisa Thompson",
            "role": "Data Analyst",
            "avatar": "👩‍📊",
            "bio": "Specializes in real estate market analysis and feature engineering for better model performance.",
            "skills": ["SQL", "Tableau", "R", "Market Analysis"],
            "social": {"github": "#", "linkedin": "#", "twitter": "#"}
        }
    ]
    
    # Team grid
    team_html = '<div class="team-grid">'
    
    for member in team_members:
        skills_html = ''.join([f'<span class="team-skill">{skill}</span>' for skill in member["skills"]])
        
        social_html = ""
        for platform, url in member["social"].items():
            icon = "🔗"
            if platform == "github":
                icon = "📱"
            elif platform == "linkedin":
                icon = "💼"
            elif platform == "twitter":
                icon = "🐦"
            elif platform == "dribbble":
                icon = "🎨"
            
            social_html += f'<a href="{url}" class="team-social-link">{icon}</a>'
        
        team_html += f"""
        <div class="team-card">
            <div class="team-avatar">{member["avatar"]}</div>
            <h3 class="team-name">{member["name"]}</h3>
            <p class="team-role">{member["role"]}</p>
            <p class="team-bio">{member["bio"]}</p>
            <div class="team-skills">
                {skills_html}
            </div>
            <div class="team-social">
                {social_html}
            </div>
        </div>
        """
    
    team_html += '</div>'
    st.markdown(team_html, unsafe_allow_html=True)
    
    # Stats section
    st.markdown("""
    <div class="stats-section">
        <h2 style="text-align: center; margin-bottom: 2rem; color: var(--text-primary);">Team Statistics</h2>
        <div class="stats-grid">
            <div class="stat-item">
                <span class="stat-number">6</span>
                <span class="stat-label">Team Members</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">25+</span>
                <span class="stat-label">Years Combined Experience</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">98%</span>
                <span class="stat-label">Model Accuracy</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">10K+</span>
                <span class="stat-label">Properties Analyzed</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Values section
    values = [
        {
            "icon": "🎯",
            "title": "Accuracy First",
            "description": "We prioritize precision and reliability in every prediction, ensuring our models deliver trustworthy results."
        },
        {
            "icon": "🚀",
            "title": "Innovation",
            "description": "Constantly exploring new technologies and methodologies to improve our prediction algorithms."
        },
        {
            "icon": "🤝",
            "title": "Collaboration",
            "description": "Working together as a unified team to tackle complex challenges and deliver exceptional solutions."
        },
        {
            "icon": "📚",
            "title": "Continuous Learning",
            "description": "Staying updated with the latest trends in machine learning, real estate, and technology."
        }
    ]
    
    st.markdown("""
    <div class="values-section">
        <h2 style="color: var(--text-primary); margin-bottom: 1rem;">Our Values</h2>
        <p style="color: var(--text-secondary); max-width: 600px; margin: 0 auto;">
            These core principles guide everything we do and shape how we approach challenges.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    values_html = '<div class="values-grid">'
    
    for value in values:
        values_html += f"""
        <div class="value-card">
            <span class="value-icon">{value["icon"]}</span>
            <h3 class="value-title">{value["title"]}</h3>
            <p class="value-description">{value["description"]}</p>
        </div>
        """
    
    values_html += '</div>'
    st.markdown(values_html, unsafe_allow_html=True)
    
    # Contact section
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 2rem 0;">
            <h3 style="color: var(--text-primary); margin-bottom: 1rem;">Want to Join Our Team?</h3>
            <p style="color: var(--text-secondary); margin-bottom: 2rem;">
                We're always looking for talented individuals who share our passion for innovation and excellence.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("📧 Contact Us", use_container_width=True, type="primary"):
            st.success("🎉 Thank you for your interest! We'll be in touch soon.")
            st.balloons()
