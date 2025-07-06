"""
Propalytic navbar using streamlit-option-menu
"""

import streamlit as st
from streamlit_option_menu import option_menu


def render_option_menu_navbar():
    """
    Render Propalytic navbar using streamlit-option-menu
    """
    # Initialize session state for navbar if not exists
    if 'navbar_selected' not in st.session_state:
        st.session_state.navbar_selected = "Home"
    
    # Custom CSS for Propalytic navbar styling
    navbar_css = """
    <style>
    /* Option Menu Propalytic Styling */
    .nav-link {
        font-weight: 500 !important;
        font-size: 14px !important;
        padding: 12px 20px !important;
        border-radius: 12px !important;
        margin: 0 4px !important;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        position: relative !important;
        overflow: hidden !important;
    }
    
    .nav-link::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, #8b5cf6, #3b82f6, #06b6d4);
        opacity: 0;
        transition: all 0.3s ease;
        z-index: -1;
        border-radius: 12px;
    }
    
    .nav-link:hover {
        transform: translateY(-2px) scale(1.05) !important;
        box-shadow: 0 10px 25px rgba(139, 92, 246, 0.3) !important;
        color: white !important;
    }
    
    .nav-link:hover::before {
        opacity: 1 !important;
    }
    
    .nav-link.nav-link-selected {
        background: linear-gradient(135deg, #8b5cf6, #3b82f6, #06b6d4) !important;
        color: white !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 8px 20px rgba(139, 92, 246, 0.4) !important;
    }
    
    /* Main container styling */
    .stOptionMenu > div {
        background: rgba(248, 250, 252, 0.95) !important;
        backdrop-filter: blur(24px) saturate(180%) !important;
        border: 1px solid rgba(226, 232, 240, 0.5) !important;
        border-radius: 16px !important;
        padding: 8px !important;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1) !important;
        position: fixed !important;
        top: 10px !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        z-index: 999999 !important;
        max-width: 90vw !important;
        overflow-x: auto !important;
    }
    
    /* Dark theme support */
    [data-theme="dark"] .stOptionMenu > div {
        background: rgba(15, 23, 42, 0.95) !important;
        border-color: rgba(51, 65, 85, 0.5) !important;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3) !important;
    }
    
    /* Logo styling */
    .navbar-logo {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-right: 20px;
        font-weight: 700;
        font-size: 18px;
        color: var(--text-primary);
        text-decoration: none;
    }
    
    .navbar-logo-icon {
        width: 32px;
        height: 32px;
        background: linear-gradient(135deg, #8b5cf6, #3b82f6);
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 16px;
        animation: logoFloat 6s ease-in-out infinite;
        box-shadow: 0 4px 12px rgba(139, 92, 246, 0.3);
    }
    
    @keyframes logoFloat {
        0%, 100% { 
            transform: translateY(0px) rotate(0deg);
        }
        50% { 
            transform: translateY(-3px) rotate(180deg);
        }
    }
    /* Responsive design */
    @media (max-width: 768px) {
        .stOptionMenu > div {
            position: relative !important;
            top: 0 !important;
            left: 0 !important;
            transform: none !important;
            margin-bottom: 20px !important;
        }
        
        .nav-link {
            font-size: 12px !important;
            padding: 8px 12px !important;
        }
        
        .navbar-logo {
            margin-right: 10px !important;
            font-size: 16px !important;
        }
    }
    
    /* Ensure content doesn't overlap */
    .main .block-container {
        padding-top: 120px !important;
    }
    
    @media (max-width: 768px) {
        .main .block-container {
            padding-top: 20px !important;
        }
    }
    </style>
    """
    
    st.markdown(navbar_css, unsafe_allow_html=True)
    
    # Create container for logo + navbar + theme toggle
    navbar_container = st.container()
    
    with navbar_container:
        # Create columns to center the navbar
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            # Empty space
            st.empty()
        
        with col2:
            # Option menu navbar
            selected_page = option_menu(
                menu_title=None,  # No title
                options=["Home", "About", "Guide", "Team"],
                icons=["house-fill", "graph-up", "book-fill", "people-fill"],
                menu_icon="cast",
                default_index=0 if st.session_state.navbar_selected == "Home" else 
                             1 if st.session_state.navbar_selected == "About" else
                             2 if st.session_state.navbar_selected == "Guide" else
                             3 if st.session_state.navbar_selected == "Team" else 0,
                orientation="horizontal",
                styles={
                    "container": {
                        "padding": "0 !important",
                        "background-color": "transparent",
                        "border": "none"
                    },
                    "nav-link": {
                        "font-weight": "500",
                        "color": "var(--text-secondary)",
                        "background-color": "transparent",
                        "border-radius": "12px",
                        "margin": "0 4px",
                        "padding": "12px 20px",
                        "transition": "all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)",
                        "--hover-color": "white"
                    },
                    "nav-link-selected": {
                        "background": "linear-gradient(135deg, #8b5cf6, #3b82f6, #06b6d4)",
                        "color": "white",
                        "transform": "translateY(-1px)",
                        "box-shadow": "0 8px 20px rgba(139, 92, 246, 0.4)"
                    }
                }
            )
            
            # Update session state when selection changes
            if selected_page != st.session_state.navbar_selected:
                st.session_state.navbar_selected = selected_page
                st.rerun()
        
        with col3:
            # Empty space
            st.empty()

    return selected_page


def get_navbar_selection():
    """Get the current navbar selection"""
    return st.session_state.get('navbar_selected', "Home")
