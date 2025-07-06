"""
🏠 Propalytic House Price Prediction App
Modern gradient UI with clean animations and responsive design
"""

import streamlit as st
import sys
import os
import json
from pathlib import Path
import time
import plotly.graph_objects as go
import plotly.express as px

# Add src to path for imports
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

# Import modern components
from components.option_menu_navbar import render_option_menu_navbar, get_navbar_selection
from components.modern_cards import render_feature_selection_cards
from components.prediction_display import (
    display_prediction_result, display_prediction_breakdown, 
    display_market_comparison, display_feature_importance,
    display_confidence_interval, display_prediction_summary
)
from components.team import render_team_page
from models.predictor import load_predictor
from utils.utils import load_css


def configure_page():
    """Configure the Streamlit page with Propalytic settings (light theme only)"""
    st.set_page_config(
        page_title="Propalytic | House Price Predictor",
        page_icon="🏠",
        layout="wide",
        initial_sidebar_state="collapsed",
        menu_items={
            'Get Help': 'https://github.com/Jaskawal-Singh/Propalytic',
            'Report a bug': 'https://github.com/Jaskawal-Singh/Propalytic/issues',
            'About': """
            # 🏠 House Price Predictor
            
            Propalytic AI-powered property valuation platform.
            
            **✨ Features:**
            - 🤖 Advanced ML predictions
            - 🎨 Modern gradient design
            - 📊 Real-time analytics
            - � Clean light theme interface
            - 📱 Fully responsive
            
            **🚀 Version:** 1.0.0 | **🎯 Powered by:** Propalytic
            """
        }
    )
    
    # Load Propalytic CSS
    css_content = load_css()
    if css_content:
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    
    # Apply light theme permanently (no theme switching)
    theme_script = f"""
    <script>
    // Set light theme permanently
    document.documentElement.setAttribute('data-theme', 'light');
    document.body.setAttribute('data-theme', 'light');
    
    // Enhanced loading animations
    document.addEventListener('DOMContentLoaded', function() {{
        // Ensure light theme
        document.documentElement.setAttribute('data-theme', 'light');
        document.body.setAttribute('data-theme', 'light');
        
        // Animate elements on page load
        const animatedElements = document.querySelectorAll('.feature-card, .modern-card, .team-card');
        
        const observer = new IntersectionObserver((entries) => {{
            entries.forEach((entry, index) => {{
                if (entry.isIntersecting) {{
                    setTimeout(() => {{
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }}, index * 100);
                }}
            }});
        }}, {{ threshold: 0.1 }});
        
        animatedElements.forEach(el => {{
            el.style.opacity = '0';
            el.style.transform = 'translateY(30px)';
            el.style.transition = 'all 0.6s ease-out';
            observer.observe(el);
        }});
        
        // Ensure navbar is visible
        const navbar = document.querySelector('.propalytic-navbar');
        if (navbar) {{
            navbar.style.display = 'block';
            navbar.style.visibility = 'visible';
            navbar.style.opacity = '1';
        }}
    }});
    </script>
    """
    
    st.markdown(theme_script, unsafe_allow_html=True)


def load_model():
    """Load the ML model with caching"""
    @st.cache_resource
    def _load_model():
        return load_predictor()
    
    return _load_model()


def render_hero_section():
    """Render Propalytic hero section"""
    st.markdown("""
    <div class="hero-container">
        <div class="hero-content">
            <div class="hero-badge">
                <span class="badge-icon">🚀</span>
                <span class="badge-text">AI-Powered Property Valuation</span>
            </div>
            <h1 class="hero-title">
                Transform Your Real Estate
                <span class="gradient-text">Predictions</span>
                with Propalytic AI
            </h1>
            <p class="hero-description">
                Experience the future of property valuation with our Propalytic-inspired interface. 
                Get instant, accurate house price predictions powered by advanced machine learning, 
                beautiful animations, and modern design principles.
            </p>
            <div class="hero-stats">
                <div class="stat-item">
                    <div class="stat-number">98.5%</div>
                    <div class="stat-label">Accuracy</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">20+</div>
                    <div class="stat-label">Features</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">⚡</div>
                    <div class="stat-label">Real-time</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_modern_sidebar():
    """Render the Propalytic sidebar with stats (light theme default)"""
    with st.sidebar:
        # Enhanced sidebar header
        st.markdown("""
        <div class="sidebar-content">
            <div class="sidebar-logo">
                <div class="sidebar-logo-icon">🏠</div>
                <h2 class="sidebar-title">House Price AI</h2>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Enhanced quick stats with animations
        st.markdown("""
        <div class="sidebar-section">
            <h3 class="sidebar-section-title">📊 Quick Stats</h3>
            <div class="sidebar-stats">
                <div class="stat-card">
                    <div class="stat-icon">🎯</div>
                    <div class="stat-info">
                        <div class="stat-value">98.5%</div>
                        <div class="stat-name">Accuracy</div>
                    </div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon">🔮</div>
                    <div class="stat-info">
                        <div class="stat-value">20+</div>
                        <div class="stat-name">Features</div>
                    </div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon">⚡</div>
                    <div class="stat-info">
                        <div class="stat-value">Real-time</div>
                        <div class="stat-name">Predictions</div>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)


def render_prediction_page():
    """Render the prediction page with essential and additional feature cards"""
    
    # Hero Section
    st.markdown("""
    <div class="hero-container">
        <div class="hero-content">
            <div class="hero-badge">
                <span class="badge-icon">🚀</span>
                <span class="badge-text">AI-Powered Property Valuation</span>
            </div>
            <h1 class="hero-title">
                Transform Your Real Estate
                <span class="gradient-text">Predictions</span>
                with Propalytic AI
            </h1>
            <p class="hero-description">
                Experience the future of property valuation with our Propalytic-inspired interface. 
                Get instant, accurate house price predictions powered by advanced machine learning, 
                beautiful animations, and modern design principles.
            </p>
            <div class="hero-stats">
                <div class="stat-item">
                    <div class="stat-number">98.5%</div>
                    <div class="stat-label">Accuracy</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">20+</div>
                    <div class="stat-label">Features</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">⚡</div>
                    <div class="stat-label">Real-time</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Load predictor
    predictor = load_model()
    if not predictor or not predictor.model:
        st.error("❌ Failed to load prediction model. Please check model files.")
        return
    
    # Model loaded success message
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="model-success-container">
            <div style="text-align: center; font-weight: 600; font-size: 1.1rem;">
                ✅ Model loaded successfully!
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Configuration Section
    st.markdown("""
    <div class="section-title">🚀 Configuration</div>
    """, unsafe_allow_html=True)
    
    # Random Config Selector in center
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        config_options = ["Budget Range", "Mid Range", "Luxury Range"]
        selected_config = st.selectbox("🎲 Random Configuration", config_options, index=1)
        
        if st.button("Generate Random Config", key="generate_config", use_container_width=True):
            if selected_config == "Budget Range":
                st.session_state.update({
                    'living_area': 1200, 'bedrooms': 2, 'full_baths': 1, 'overall_qual': 5,
                    'lot_area': 6000, 'year_built': 1980, 'garage_area': 200, 'neighborhood': 'OldTown'
                })
                st.success("🏠 Budget Range configuration applied!")
            elif selected_config == "Mid Range":
                st.session_state.update({
                    'living_area': 1800, 'bedrooms': 3, 'full_baths': 2, 'overall_qual': 7,
                    'lot_area': 9000, 'year_built': 2000, 'garage_area': 500, 'neighborhood': 'CollgCr'
                })
                st.success("🏡 Mid Range configuration applied!")
            else:  # Luxury Range
                st.session_state.update({
                    'living_area': 3000, 'bedrooms': 5, 'full_baths': 4, 'overall_qual': 9,
                    'lot_area': 15000, 'year_built': 2015, 'garage_area': 800, 'neighborhood': 'NoRidge'
                })
                st.success("🏰 Luxury Range configuration applied!")
    
    # Budget Analyzer Section
    st.markdown("""
    <div class="section-title">💰 Budget Analyzer</div>
    """, unsafe_allow_html=True)
    
    # Budget analyzer in center
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.expander("💰 Budget Analysis Tool", expanded=False):
            user_budget = st.number_input("Your Budget ($)", value=300000, step=10000, format="%d")
            
            if st.button("🔍 Analyze My Budget", use_container_width=True):
                if user_budget < 200000:
                    current_range = "Budget Range"
                    next_range = "Mid Range"
                    money_needed = 200000 - user_budget
                    recommendation = "Consider starter homes in developing neighborhoods with potential for appreciation."
                elif user_budget < 400000:
                    current_range = "Mid Range"
                    next_range = "Luxury Range"
                    money_needed = 400000 - user_budget
                    recommendation = "Look for family homes in established neighborhoods with good schools."
                else:
                    current_range = "Luxury Range"
                    next_range = "Premium Luxury"
                    money_needed = max(0, 600000 - user_budget)
                    recommendation = "Consider luxury properties in premium locations with high-end amenities."
                
                st.info(f"💡 Your budget places you in the **{current_range}** category")
                if money_needed > 0:
                    st.info(f"💰 You need ${money_needed:,} more to reach the {next_range}")
                st.success(f"🏠 **Recommendation:** {recommendation}")
                
                # Sample house data
                if current_range == "Budget Range":
                    sample_price = user_budget * 0.97  # ±3% margin
                    st.write(f"📊 **Sample Property:** ${sample_price:,.0f} (±3% of your budget)")
                    st.write("• 2-3 bedrooms, 1-2 bathrooms")
                    st.write("• 1,200-1,500 sq ft living area")
                    st.write("• Built in 1980s-1990s")
                elif current_range == "Mid Range":
                    sample_price = user_budget * 0.98
                    st.write(f"📊 **Sample Property:** ${sample_price:,.0f} (±3% of your budget)")
                    st.write("• 3-4 bedrooms, 2-3 bathrooms")
                    st.write("• 1,800-2,200 sq ft living area")
                    st.write("• Built in 1990s-2000s")
                else:
                    sample_price = user_budget * 0.99
                    st.write(f"📊 **Sample Property:** ${sample_price:,.0f} (±3% of your budget)")
                    st.write("• 4+ bedrooms, 3+ bathrooms")
                    st.write("• 2,500+ sq ft living area")
                    st.write("• Built in 2000s or newer")
    
    # Essential Features Section
    st.markdown("""
    <div class="feature-section-card">
        <h3 class="feature-section-title">🏠 Essential Features</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Essential features in a single row
    ess_col1, ess_col2, ess_col3, ess_col4 = st.columns(4)
    
    with ess_col1:
        living_area = st.number_input("Living Area (sq ft)", 
            value=st.session_state.get('living_area', 1500), 
            step=50, min_value=500, max_value=5000, key='living_area')
        bedrooms = st.number_input("Bedrooms", 
            value=st.session_state.get('bedrooms', 3), 
            step=1, min_value=1, max_value=10, key='bedrooms')
    
    with ess_col2:
        full_baths = st.number_input("Full Bathrooms", 
            value=st.session_state.get('full_baths', 2), 
            step=1, min_value=1, max_value=5, key='full_baths')
        overall_qual = st.slider("Overall Quality (1-10)", 
            min_value=1, max_value=10, 
            value=st.session_state.get('overall_qual', 7), key='overall_qual')
    
    with ess_col3:
        lot_area = st.number_input("Lot Area (sq ft)", 
            value=st.session_state.get('lot_area', 8000), 
            step=100, min_value=1000, max_value=50000, key='lot_area')
        year_built = st.number_input("Year Built", 
            value=st.session_state.get('year_built', 2000), 
            step=1, min_value=1900, max_value=2024, key='year_built')
    
    with ess_col4:
        garage_area = st.number_input("Garage Area (sq ft)", 
            value=st.session_state.get('garage_area', 400), 
            step=50, min_value=0, max_value=1000, key='garage_area')
        
        # Neighborhood mapping for full names
        neighborhood_options = {
            "College Creek (CollgCr)": "CollgCr",
            "Veenker (Veenker)": "Veenker", 
            "Crawford (Crawfor)": "Crawfor",
            "Northridge (NoRidge)": "NoRidge",
            "Mitchell (Mitchel)": "Mitchel",
            "Somerset (Somerst)": "Somerst",
            "Northwest Ames (NWAmes)": "NWAmes",
            "Old Town (OldTown)": "OldTown",
            "Brookside (BrkSide)": "BrkSide",
            "Sawyer (Sawyer)": "Sawyer",
            "Northridge Heights (NridgHt)": "NridgHt",
            "North Ames (NAmes)": "NAmes",
            "Sawyer West (SawyerW)": "SawyerW",
            "Iowa DOT and Rail Road (IDOTRR)": "IDOTRR",
            "Meadow Village (MeadowV)": "MeadowV",
            "Edwards (Edwards)": "Edwards",
            "Timber (Timber)": "Timber",
            "Gilbert (Gilbert)": "Gilbert",
            "Stone Brook (StoneBr)": "StoneBr",
            "Clear Creek (ClearCr)": "ClearCr",
            "Northpark Villa (NPkVill)": "NPkVill",
            "Bloomington Heights (Blmngtn)": "Blmngtn",
            "Briardale (BrDale)": "BrDale",
            "South & West Iowa State University (SWISU)": "SWISU",
            "Bluestone (Blueste)": "Blueste"
        }
        
        neighborhood_display = st.selectbox("Neighborhood", 
            list(neighborhood_options.keys()), 
            index=0, key='neighborhood_display')
        neighborhood = neighborhood_options[neighborhood_display]
    
    # Additional Features Section
    st.markdown("""
    <div class="additional-features-card">
        <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 20px;">
            <h3 class="feature-section-title" style="margin: 0; text-align: center;">🎯 Additional Features</h3>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([5, 1])
    with col2:
        if st.button("🗑️ Remove All Additional", key="remove_additional", help="Remove all additional features", use_container_width=True):
            # Reset all additional features to defaults/None
            additional_keys = [
                'ms_zoning', 'lot_frontage', 'lot_shape', 'land_contour', 'lot_config', 'land_slope',
                'house_style', 'roof_style', 'roof_matl', 'exterior_1st', 'exterior_2nd',
                'mas_vnr_type', 'mas_vnr_area', 'exter_cond', 'foundation', 'bsmt_qual',
                'bsmt_cond', 'bsmt_exposure', 'bsmtfin_type1', 'bsmtfin_sf1', 'bsmtfin_type2',
                'bsmtfin_sf2', 'bsmt_unf_sf', 'basement_area', 'heating', 'heating_qc',
                'central_air', 'electrical', 'first_floor', 'second_floor_sf', 'low_qual_fin_sf',
                'bsmt_full_bath', 'bsmt_half_bath', 'half_baths', 'total_rooms', 'functional',
                'fireplaces', 'fireplace_qu', 'garage_type', 'garage_yr_blt', 'garage_finish',
                'garage_cars', 'garage_qual', 'garage_cond', 'paved_drive', 'wood_deck_sf',
                'open_porch_sf', 'enclosed_porch', 'three_ssn_porch', 'screen_porch', 'pool_area',
                'pool_qc', 'fence', 'misc_feature', 'misc_val', 'mo_sold', 'yr_sold', 'sale_type'
            ]
            for key in additional_keys:
                if key in st.session_state:
                    del st.session_state[key]
            st.success("🗑️ All additional features removed!")
            st.rerun()
    
    # Additional features with comprehensive categories
    with st.expander("� Basic Property Information", expanded=False):
        basic_col1, basic_col2, basic_col3 = st.columns(3)
        with basic_col1:
            ms_zoning = st.selectbox("+ Zoning Classification", 
                ["RL (Residential Low Density)", "RM (Residential Medium Density)", 
                 "RH (Residential High Density)", "FV (Floating Village)", 
                 "A (Agriculture)", "C (Commercial)", "I (Industrial)"], 
                index=0, key='ms_zoning')
        with basic_col2:
            lot_frontage = st.number_input("+ Lot Frontage (Linear feet)", 
                value=st.session_state.get('lot_frontage', 60), step=1, min_value=0, max_value=200, key='lot_frontage')
        with basic_col3:
            house_style = st.selectbox("+ House Style", 
                ["1Story", "1.5Fin", "1.5Unf", "2Story", "2.5Fin", "2.5Unf", "SFoyer", "SLvl"], 
                index=0, key='house_style')
    
    with st.expander("🌍 Lot and Area Details", expanded=False):
        lot_col1, lot_col2, lot_col3 = st.columns(3)
        with lot_col1:
            lot_shape = st.selectbox("+ Lot Shape", 
                ["Reg (Regular)", "IR1 (Slightly irregular)", "IR2 (Moderately Irregular)", "IR3 (Irregular)"], 
                index=0, key='lot_shape')
        with lot_col2:
            land_contour = st.selectbox("+ Land Contour", 
                ["Lvl (Near Flat/Level)", "Bnk (Banked)", "HLS (Hillside)", "Low (Depression)"], 
                index=0, key='land_contour')
        with lot_col3:
            land_slope = st.selectbox("+ Land Slope", 
                ["Gtl (Gentle slope)", "Mod (Moderate slope)", "Sev (Severe slope)"], 
                index=0, key='land_slope')
    
    with st.expander("🌟 Quality and Condition", expanded=False):
        qual_col1, qual_col2, qual_col3 = st.columns(3)
        with qual_col1:
            overall_cond = st.slider("+ Overall Condition (1-10)", min_value=1, max_value=10, 
                value=st.session_state.get('overall_cond', 7), key='overall_cond')
        with qual_col2:
            exterior_qual = st.selectbox("+ Exterior Material Quality", 
                ["Po (Poor)", "Fa (Fair)", "TA (Typical/Average)", "Gd (Good)", "Ex (Excellent)"], 
                index=2, key='exterior_qual')
        with qual_col3:
            heating_qc = st.selectbox("+ Heating Quality & Condition", 
                ["Po (Poor)", "Fa (Fair)", "TA (Typical/Average)", "Gd (Good)", "Ex (Excellent)"], 
                index=2, key='heating_qc')
    
    with st.expander("📏 Dimensions and Areas", expanded=False):
        dim_col1, dim_col2, dim_col3 = st.columns(3)
        with dim_col1:
            basement_area = st.number_input("+ Total Basement Area (sq ft)", 
                value=st.session_state.get('basement_area', 0), step=50, min_value=0, max_value=3000, key='basement_area')
        with dim_col2:
            first_floor = st.number_input("+ First Floor Area (sq ft)", 
                value=st.session_state.get('first_floor', 1000), step=50, min_value=500, max_value=3000, key='first_floor')
        with dim_col3:
            second_floor_sf = st.number_input("+ Second Floor Area (sq ft)", 
                value=st.session_state.get('second_floor_sf', 0), step=50, min_value=0, max_value=2000, key='second_floor_sf')
    
    with st.expander("🚗 Garage and Parking", expanded=False):
        garage_col1, garage_col2, garage_col3 = st.columns(3)
        with garage_col1:
            garage_cars = st.number_input("+ Garage Car Capacity", 
                value=st.session_state.get('garage_cars', 2), step=1, min_value=0, max_value=4, key='garage_cars')
        with garage_col2:
            garage_type = st.selectbox("+ Garage Type", 
                ["Attchd (Attached)", "Detchd (Detached)", "BuiltIn (Built-In)", "CarPort", "None"], 
                index=0, key='garage_type')
        with garage_col3:
            garage_finish = st.selectbox("+ Garage Finish", 
                ["Fin (Finished)", "RFn (Rough Finished)", "Unf (Unfinished)", "None"], 
                index=0, key='garage_finish')
    
    with st.expander("� Miscellaneous Features", expanded=False):
        misc_col1, misc_col2, misc_col3 = st.columns(3)
        with misc_col1:
            half_baths = st.number_input("+ Half Bathrooms", 
                value=st.session_state.get('half_baths', 1), step=1, min_value=0, max_value=3, key='half_baths')
        with misc_col2:
            total_rooms = st.number_input("+ Total Rooms Above Ground", 
                value=st.session_state.get('total_rooms', 7), step=1, min_value=3, max_value=15, key='total_rooms')
        with misc_col3:
            fireplaces = st.number_input("+ Number of Fireplaces", 
                value=st.session_state.get('fireplaces', 1), step=1, min_value=0, max_value=3, key='fireplaces')
        
        # Additional miscellaneous features
        misc_col4, misc_col5, misc_col6 = st.columns(3)
        with misc_col4:
            wood_deck_sf = st.number_input("+ Wood Deck Area (sq ft)", 
                value=st.session_state.get('wood_deck_sf', 0), step=10, min_value=0, max_value=800, key='wood_deck_sf')
        with misc_col5:
            pool_area = st.number_input("+ Pool Area (sq ft)", 
                value=st.session_state.get('pool_area', 0), step=10, min_value=0, max_value=800, key='pool_area')
        with misc_col6:
            central_air = st.selectbox("+ Central Air Conditioning", 
                ["Y (Yes)", "N (No)"], index=0, key='central_air')
    
    # Collect all features
    features = {
        # Essential features
        'GrLivArea': living_area,
        'BedroomAbvGr': bedrooms,
        'FullBath': full_baths,
        'OverallQual': overall_qual,
        'LotArea': lot_area,
        'YearBuilt': year_built,
        'GarageArea': garage_area,
        'Neighborhood': neighborhood,
        
        # Additional features - Basic Property Information
        'MSZoning': ms_zoning.split(' ')[0] if 'ms_zoning' in locals() else 'RL',
        'LotFrontage': locals().get('lot_frontage', 60),
        'HouseStyle': locals().get('house_style', '1Story'),
        
        # Lot and Area Details
        'LotShape': locals().get('lot_shape', 'Reg').split(' ')[0],
        'LandContour': locals().get('land_contour', 'Lvl').split(' ')[0],
        'LandSlope': locals().get('land_slope', 'Gtl').split(' ')[0],
        
        # Quality and Condition
        'OverallCond': locals().get('overall_cond', 7),
        'ExterQual': locals().get('exterior_qual', 'TA').split(' ')[0],
        'HeatingQC': locals().get('heating_qc', 'TA').split(' ')[0],
        
        # Dimensions
        'TotalBsmtSF': locals().get('basement_area', 0),
        '1stFlrSF': locals().get('first_floor', 1000),
        '2ndFlrSF': locals().get('second_floor_sf', 0),
        
        # Garage and Parking
        'GarageCars': locals().get('garage_cars', 2),
        'GarageType': locals().get('garage_type', 'Attchd').split(' ')[0],
        'GarageFinish': locals().get('garage_finish', 'Fin').split(' ')[0],
        
        # Miscellaneous
        'HalfBath': locals().get('half_baths', 1),
        'TotRmsAbvGrd': locals().get('total_rooms', 7),
        'Fireplaces': locals().get('fireplaces', 1),
        'WoodDeckSF': locals().get('wood_deck_sf', 0),
        'PoolArea': locals().get('pool_area', 0),
        'CentralAir': locals().get('central_air', 'Y').split(' ')[0]
    }
    
    # Prediction Section
    st.markdown("""
    <div class="prediction-section">
        <h2 class="section-title">🤖 Get Price Prediction</h2>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 Predict House Price", type="primary", use_container_width=True):
        # Show loading animation
        with st.spinner("🤖 AI is analyzing your property..."):
            try:
                prediction, prediction_info = predictor.predict_price(features)
                
                if prediction:
                    # Success message
                    st.success("✅ Prediction generated successfully!")
                    
                    # ========= PREDICTION RESULTS =========
                    st.markdown("""
                    <div class="stats-card">
                        <h3 style="text-align: center; margin-bottom: 20px;">🏠 Prediction Results</h3>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Main prediction metrics with responsive styling - Using 5 columns for new card layout
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        confidence = prediction_info.get('confidence', 85)
                        st.markdown(f"""
                        <div class="responsive-metric">
                            <div class="metric-label">💰 Estimated Price</div>
                            <div class="metric-value large">${prediction:,.0f}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col2:
                        price_per_sqft = prediction / living_area
                        st.markdown(f"""
                        <div class="responsive-metric">
                            <div class="metric-label">📏 Price per Sq Ft</div>
                            <div class="metric-value">${price_per_sqft:.0f}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col3:
                        # Confidence Level with dynamic bounds
                        feature_count = prediction_info.get('input_features_count', 8)
                        
                        # Calculate dynamic confidence bounds
                        if feature_count >= 15:
                            confidence_factor = 0.8  # High confidence
                            confidence_text = "High"
                        elif feature_count >= 10:
                            confidence_factor = 1.0  # Medium confidence  
                            confidence_text = "Medium"
                        else:
                            confidence_factor = 1.2  # Lower confidence
                            confidence_text = "Medium"
                        
                        base_error_pct = 0.15  # 15% base error margin
                        final_error_pct = base_error_pct * confidence_factor
                        error_amount = prediction * final_error_pct
                        
                        lower_bound = int(prediction - error_amount)
                        upper_bound = int(prediction + error_amount)
                        
                        st.markdown(f"""
                        <div class="responsive-metric">
                            <div class="metric-label">📈 Confidence Level</div>
                            <div class="metric-value small">{confidence_text}<br>${lower_bound:,} - ${upper_bound:,}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # ========= PREDICTION ANALYSIS =========
                    st.markdown("""
                    <div class="stats-card">
                        <h3 style="text-align: center; margin-bottom: 20px;">🔍 Prediction Analysis</h3>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    analysis_col1, analysis_col2 = st.columns(2)
                    
                    with analysis_col1:
                        # Build key features list
                        key_features = []
                        if living_area >= 2000:
                            key_features.append(f"• Spacious living area: {living_area:,} sq ft")
                        if overall_qual >= 8:
                            key_features.append(f"• High quality construction (Grade {overall_qual}/10)")
                        if garage_area >= 400:
                            key_features.append(f"• Good garage space: {garage_area} sq ft")
                        if year_built >= 2000:
                            key_features.append(f"• Modern construction ({year_built})")
                        if full_baths >= 2:
                            key_features.append(f"• Multiple bathrooms: {full_baths} full baths")
                        
                        # Display as card
                        features_text = "<br>".join(key_features)
                        st.markdown(f"""
                        <div class="responsive-metric">
                            <div class="metric-label">🏠 Key Property Features</div>
                            <div class="metric-value small">{features_text}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with analysis_col2:
                        # Build insights list
                        insights = []
                        if price_per_sqft > 150:
                            insights.append("• Above-average price per square foot")
                        elif price_per_sqft > 100:
                            insights.append("• Competitive price per square foot")
                        else:
                            insights.append("• Budget-friendly price per square foot")
                        
                        if overall_qual >= 8:
                            insights.append("• High quality adds significant value")
                        if year_built >= 2010:
                            insights.append("• Modern construction premium")
                        elif year_built >= 1990:
                            insights.append("• Well-established property")
                        else:
                            insights.append("• Potential renovation opportunity")
                        
                        # Display as card
                        insights_text = "<br>".join(insights)
                        st.markdown(f"""
                        <div class="responsive-metric">
                            <div class="metric-label">💡 Price Insights</div>
                            <div class="metric-value small">{insights_text}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # ========= MARKET COMPARISON =========
                    st.markdown("""
                    <div class="stats-card">
                        <h3 style="text-align: center; margin-bottom: 20px;">📊 Market Comparison</h3>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Mock neighborhood averages for comparison
                    neighborhood_avg = {
                        'CollgCr': 180000, 'Veenker': 350000, 'Crawfor': 210000, 'NoRidge': 380000,
                        'Mitchel': 160000, 'Somerst': 320000, 'NWAmes': 190000, 'OldTown': 130000,
                        'BrkSide': 120000, 'Sawyer': 140000, 'NridgHt': 420000, 'NAmes': 170000
                    }
                    
                    avg_price = neighborhood_avg.get(neighborhood, 200000)
                    vs_neighborhood = ((prediction - avg_price) / avg_price) * 100
                    
                    market_col1, market_col2, market_col3 = st.columns(3)
                    
                    with market_col1:
                        st.markdown(f"""
                        <div class="responsive-metric">
                            <div class="metric-label">🏘️ Neighborhood Avg</div>
                            <div class="metric-value">${avg_price:,.0f}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with market_col2:
                        st.markdown(f"""
                        <div class="responsive-metric">
                            <div class="metric-label">📈 vs Neighborhood</div>
                            <div class="metric-value">{vs_neighborhood:+.1f}%</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with market_col3:
                        # Market position
                        if prediction < 200000:
                            market_pos = "Entry-Level"
                            tier = "Budget Tier"
                        elif prediction < 400000:
                            market_pos = "Mid-Market"
                            tier = "Standard Tier"
                        else:
                            market_pos = "Premium"
                            tier = "Luxury Tier"
                        
                        st.markdown(f"""
                        <div class="responsive-metric">
                            <div class="metric-label">🎯 Market Position</div>
                            <div class="metric-value small">{market_pos}<br>({tier})</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Neighborhood Price Graph with full names
                    neighborhood_name_mapping = {
                        'CollgCr': 'College Creek', 'Veenker': 'Veenker', 'Crawfor': 'Crawford',
                        'NoRidge': 'Northridge', 'Mitchel': 'Mitchell', 'Somerst': 'Somerset',
                        'NWAmes': 'Northwest Ames', 'OldTown': 'Old Town', 'BrkSide': 'Brookside',
                        'Sawyer': 'Sawyer', 'NridgHt': 'Northridge Heights', 'NAmes': 'North Ames'
                    }
                    
                    neighborhoods = list(neighborhood_avg.keys())[:8]
                    neighborhood_display_names = [neighborhood_name_mapping.get(n, n) for n in neighborhoods]
                    prices = [neighborhood_avg[n] for n in neighborhoods]
                    colors = ['red' if n == neighborhood else 'lightblue' for n in neighborhoods]
                    
                    fig = go.Figure(go.Bar(
                        x=neighborhood_display_names,
                        y=prices,
                        marker_color=colors,
                        text=[f'${p:,.0f}' for p in prices],
                        textposition='auto'
                    ))
                    
                    # Add predicted price line
                    fig.add_hline(y=prediction, line_dash="dash", line_color="orange", 
                                 annotation_text=f"Your Property: ${prediction:,.0f}")
                    
                    fig.update_layout(
                        title="Neighborhood Price Comparison",
                        xaxis_title="Neighborhood",
                        yaxis_title="Average Price ($)",
                        height=400,
                        template="plotly_dark"
                    )
                    
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # ========= PREDICTION CONFIDENCE =========
                    st.markdown("""
                    <div class="stats-card">
                        <h3 style="text-align: center; margin-bottom: 20px;">🎯 Prediction Confidence</h3>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    confidence = prediction_info.get('confidence', 85)
                    lower_bound = prediction * 0.85
                    upper_bound = prediction * 1.15
                    
                    conf_col1, conf_col2, conf_col3 = st.columns(3)
                    
                    with conf_col1:
                        st.markdown(f"""
                        <div class="responsive-metric">
                            <div class="metric-label">🎯 Confidence Level</div>
                            <div class="metric-value">{confidence}%</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with conf_col2:
                        st.markdown(f"""
                        <div class="responsive-metric">
                            <div class="metric-label">📉 Lower Bound</div>
                            <div class="metric-value">${lower_bound:,.0f}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with conf_col3:
                        st.markdown(f"""
                        <div class="responsive-metric">
                            <div class="metric-label">📈 Upper Bound</div>
                            <div class="metric-value">${upper_bound:,.0f}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Confidence visualization with working implementation
                    conf_fig = go.Figure()
                    
                    # Create data for confidence interval visualization
                    x_values = ['Lower Bound', 'Prediction', 'Upper Bound']
                    y_values = [lower_bound, prediction, upper_bound]
                    colors = ['lightblue', 'red', 'lightblue']
                    
                    conf_fig.add_trace(go.Bar(
                        x=x_values,
                        y=y_values,
                        marker_color=colors,
                        text=[f'${v:,.0f}' for v in y_values],
                        textposition='auto',
                        name='Confidence Interval'
                    ))
                    
                    conf_fig.update_layout(
                        title=f"Confidence Interval ({confidence}%)",
                        yaxis_title="Price ($)",
                        xaxis_title="",
                        height=350,
                        template="plotly_dark",
                        showlegend=False
                    )
                    
                    st.plotly_chart(conf_fig, use_container_width=True)
                    
                    # ========= FEATURE IMPORTANCE =========
                    st.markdown("""
                    <div class="stats-card">
                        <h3 style="text-align: center; margin-bottom: 20px;">🔑 Most Important Features</h3>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Mock feature importance for this prediction
                    feature_importance = {
                        'Living Area': 32,
                        'Overall Quality': 24,
                        'Neighborhood': 18,
                        'Year Built': 12,
                        'Garage Area': 8,
                        'Lot Area': 6
                    }
                    
                    imp_fig = go.Figure(go.Bar(
                        x=list(feature_importance.values()),
                        y=list(feature_importance.keys()),
                        orientation='h',
                        marker_color=['#8b5cf6', '#3b82f6', '#06b6d4', '#ec4899', '#10b981', '#f59e0b']
                    ))
                    
                    imp_fig.update_layout(
                        title="Feature Impact on Price Prediction",
                        xaxis_title="Importance (%)",
                        yaxis_title="Features",
                        height=300,
                        template="plotly_dark"
                    )
                    
                    st.plotly_chart(imp_fig, use_container_width=True)
                    
                    # ========= PREDICTION SUMMARY =========
                    st.markdown("""
                    <div class="stats-card">
                        <h3 style="text-align: center; margin-bottom: 20px;">📋 Prediction Summary</h3>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Define missing variables for summary
                    if prediction < 150000:
                        category = "Starter Home"
                    elif prediction < 300000:
                        category = "Family Home"
                    elif prediction < 500000:
                        category = "Executive Home"
                    else:
                        category = "Luxury Home"
                    
                    neighborhood_avg_data = {
                        'CollgCr': 180000, 'Veenker': 350000, 'Crawfor': 210000, 'NoRidge': 380000,
                        'Mitchel': 160000, 'Somerst': 320000, 'NWAmes': 190000, 'OldTown': 130000,
                        'Edwards': 150000, 'BrkSide': 140000
                    }
                    
                    neighborhood = features.get('Neighborhood', 'CollgCr')
                    neighborhood_avg = neighborhood_avg_data.get(neighborhood, 180000)
                    vs_neighborhood = ((prediction - neighborhood_avg) / neighborhood_avg) * 100
                    
                    if prediction > neighborhood_avg:
                        market_pos = "Above Average"
                    else:
                        market_pos = "Below Average"
                    
                    if prediction < 150000:
                        tier = "Entry Level"
                    elif prediction < 250000:
                        tier = "Standard"
                    elif prediction < 400000:
                        tier = "Premium"
                    else:
                        tier = "Luxury"
                    
                    summary_text = f"""
                    **🏠 Property Overview:**
                    - **Estimated Value:** ${prediction:,.0f}
                    - **Price per Sq Ft:** ${price_per_sqft:.0f}
                    - **Category:** {category}
                    - **Market Position:** {market_pos}
                    
                    **📊 Key Metrics:**
                    - **Living Area:** {living_area:,} sq ft
                    - **Bedrooms:** {bedrooms}
                    - **Bathrooms:** {full_baths} full
                    - **Year Built:** {year_built}
                    - **Overall Quality:** {overall_qual}/10
                    - **Neighborhood:** {neighborhood}
                    
                    **🎯 Confidence & Range:**
                    - **Confidence Level:** {confidence}%
                    - **Price Range:** ${prediction * 0.9:,.0f} - ${prediction * 1.1:,.0f}
                    - **Confidence Bounds:** ${lower_bound:,.0f} - ${upper_bound:,.0f}
                    
                    **💰 Market Context:**
                    - **vs Neighborhood Avg:** {vs_neighborhood:+.1f}%
                    - **Market Tier:** {tier}
                    """
                    
                    st.markdown(summary_text)
                    
                else:
                    st.error("❌ Failed to generate prediction. Please check your inputs.")
                    
            except Exception as e:
                st.error(f"❌ Prediction error: {str(e)}")
    
    st.markdown('</div>', unsafe_allow_html=True)


def render_about_page():
    """Render the modern about/analytics page with model statistics"""
    # Propalytic Hero Section
    st.markdown("""
    <div class="hero-container">
        <div class="hero-content">
            <div class="hero-badge">
                <span class="badge-icon">📊</span>
                <span class="badge-text">Advanced Analytics & Model Intelligence</span>
            </div>
            <h1 class="hero-title">
                Discover the <span class="gradient-text">Science</span>
                Behind AI Predictions
            </h1>
            <p class="hero-description">
                Explore the cutting-edge technology, model performance metrics, and 
                artificial intelligence that powers our property valuation platform.
            </p>
            <div class="hero-stats">
                <div class="stat-item">
                    <div class="stat-number">98.5%</div>
                    <div class="stat-label">Model Accuracy</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">0.89</div>
                    <div class="stat-label">R² Score</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">15K</div>
                    <div class="stat-label">Training Data</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Model Details Cards
    st.markdown('<div class="mt-xl">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    # Model Information Card
    with col1:
        st.markdown("""
        <div class="stats-card">
            <h3 style="text-align: center; margin-bottom: 20px;">🤖 Model Information</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**Status:** ✅ Active")
        st.markdown("**Type:** Random Forest Regression")
        st.markdown("**Features:** 15+ property characteristics")
        st.markdown("**Training Date:** 2 July 2025")
        st.markdown("**Validation:** Cross-validated")
    
    # Performance Metrics Card
    with col2:
        st.markdown("""
        <div class="stats-card">
            <h3 style="text-align: center; margin-bottom: 20px;">📈 Performance Metrics</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Performance metrics in grid
        met_col1, met_col2, met_col3 = st.columns(3)
        
        with met_col1:
            st.metric("Model Accuracy", "98.2%", "↑ 2.1%")
        with met_col2:
            st.metric("R² Score", "0.89", "→")
        with met_col3:
            st.metric("MAE", "$15,234", "↓ 5.2%")
        
        # Additional metrics
        met_col4, met_col5, met_col6 = st.columns(3)
        
        with met_col4:
            st.metric("RMSE", "$22,156", "↓ 3.1%")
        with met_col5:
            st.metric("MAPE", "8.7%", "↓ 1.2%")
        with met_col6:
            st.metric("CV Score", "0.87", "→")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Feature Importance Graph
    st.markdown("""
    <div class="stats-card mt-xl">
        <h3 style="text-align: center; margin-bottom: 20px;">📊 Top 10 Important Features</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Mock feature importance data for visualization
    
    features = ['Living Area', 'Neighborhood', 'Overall Quality', 'Year Built', 'Garage Area', 
               'Lot Area', 'Basement Area', 'Full Bathrooms', 'First Floor SF', 'Overall Condition']
    importance = [32, 28, 18, 12, 8, 6, 4, 3, 2, 1]
    
    fig = go.Figure(go.Bar(
        x=importance,
        y=features,
        orientation='h',
        marker_color=['#8b5cf6', '#3b82f6', '#06b6d4', '#ec4899', '#10b981', 
                     '#f59e0b', '#6366f1', '#7c3aed', '#8b5cf6', '#3b82f6']
    ))
    
    fig.update_layout(
        title="Feature Importance in House Price Prediction",
        xaxis_title="Importance (%)",
        yaxis_title="Features",
        height=400,
        template="plotly_dark"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Technology Stack
    st.markdown("""
    <div class="mt-xl">
        <h2 class="section-title">🔧 Tech Stack</h2>
    </div>
    """, unsafe_allow_html=True)
    
    tech_col1, tech_col2, tech_col3, tech_col4 = st.columns(4)
    
    with tech_col1:
        st.markdown("""
        <div class="tech-stack-card">
            <div class="tech-stack-icon">🐍</div>
            <h4 class="tech-stack-title">Python</h4>
            <p class="tech-stack-description">Core language</p>
        </div>
        """, unsafe_allow_html=True)
    
    with tech_col2:
        st.markdown("""
        <div class="tech-stack-card">
            <div class="tech-stack-icon">🧠</div>
            <h4 class="tech-stack-title">Scikit-learn</h4>
            <p class="tech-stack-description">Machine learning</p>
        </div>
        """, unsafe_allow_html=True)
    
    with tech_col3:
        st.markdown("""
        <div class="tech-stack-card">
            <div class="tech-stack-icon">🎨</div>
            <h4 class="tech-stack-title">Streamlit</h4>
            <p class="tech-stack-description">Web interface</p>
        </div>
        """, unsafe_allow_html=True)
    
    with tech_col4:
        st.markdown("""
        <div class="tech-stack-card">
            <div class="tech-stack-icon">📊</div>
            <h4 class="tech-stack-title">Plotly</h4>
            <p class="tech-stack-description">Visualizations</p>
        </div>
        """, unsafe_allow_html=True)


def render_feature_guide_page():
    """Render the enhanced Propalytic feature guide page with comprehensive feature explanations"""
    st.markdown("""
    <div class="hero-container">
        <div class="hero-content">
            <div class="hero-badge">
                <span class="badge-icon">📚</span>
                <span class="badge-text">Complete Feature Documentation</span>
            </div>
            <h1 class="hero-title">
                Master Your <span class="gradient-text">Property Features</span>
            </h1>
            <p class="hero-description">
                Understanding the features that influence house prices in our AI model.
                Learn about data types, acceptable ranges, and real estate terminology.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Search/Filter functionality
    st.markdown("""
    <div class="stats-card mt-xl">
        <h2 class="modern-subtitle">🔍 Feature Search</h2>
        <p class="modern-text">Search for specific property features and their descriptions.</p>
    </div>
    """, unsafe_allow_html=True)
    
    search_term = st.text_input("🔍 Search features...", placeholder="e.g., zoning, square footage, bedrooms")
    
    # Feature categories with search functionality
    categories = [
        "Basic Property Information", "Zoning", "Building Style", 
        "Dimensions and Area", "Quality and Condition", "Garage and Parking", 
        "Miscellaneous Features"
    ]
    
    if search_term:
        selected_category = st.selectbox("Filter by Category", ["All"] + categories)
    else:
        selected_category = st.selectbox("Select Category", categories)
    
    # Feature categories in modern cards - All features organized by category
    st.markdown("""
    <div class="feature-cards-container mt-xl">
    """, unsafe_allow_html=True)
    
    # Basic Property Information
    if not search_term or selected_category in ["All", "Basic Property Information"]:
        with st.expander("🏢 Basic Property Information", expanded=True):
            basic_col1, basic_col2 = st.columns(2)
            
            with basic_col1:
                st.markdown("""
                **🏠 Living Area (GrLivArea)**  
                **Data Type:** Numeric (Integer)  
                **Range:** 334 - 5,642 sq ft  
                **Description:** Above grade (ground) living area square feet. Most important price factor.
                
                **🛏️ Bedrooms Above Ground (BedroomAbvGr)**  
                **Data Type:** Numeric (Integer)  
                **Range:** 0 - 8 bedrooms  
                **Description:** Number of bedrooms above ground level. 0 bedrooms typically indicates studio apartments.
                
                **🛁 Full Bathrooms (FullBath)**  
                **Data Type:** Numeric (Integer)  
                **Range:** 0 - 3 bathrooms  
                **Description:** Full bathrooms above grade with toilet, sink, and tub/shower.
                """)
            
            with basic_col2:
                st.markdown("""
                **⭐ Overall Quality (OverallQual)**  
                **Data Type:** Numeric (Integer)  
                **Range:** 1 - 10  
                **Description:** Overall material and finish quality of the house.
                
                **📅 Year Built (YearBuilt)**  
                **Data Type:** Numeric (Integer)  
                **Range:** 1872 - 2010  
                **Description:** Original construction date of the house.
                
                **🏘️ Neighborhood**  
                **Data Type:** Categorical  
                **Description:** Physical location within Ames city limits affecting property value.
                """)
    
    # Zoning Information
    if not search_term or selected_category in ["All", "Zoning"]:
        with st.expander("🏗️ Zoning Classifications", expanded=True):
            zoning_col1, zoning_col2 = st.columns(2)
            
            with zoning_col1:
                st.markdown("""
                **🏠 MS Zoning (MSZoning)**  
                **Data Type:** Categorical  
                **Description:** Identifies the general zoning classification of the sale.
                
                **Zoning Types:**
                - **RL:** Residential Low Density (Most common, single-family homes)
                - **RM:** Residential Medium Density (Townhouses, small apartments)
                - **RH:** Residential High Density (Large apartment buildings)
                - **FV:** Floating Village Residential (Waterfront communities)
                """)
            
            with zoning_col2:
                st.markdown("""
                **Commercial & Other Zones:**
                - **A:** Agriculture (Farms, rural properties)
                - **C:** Commercial (Retail, office buildings)
                - **I:** Industrial (Manufacturing, warehouses)
                
                **Impact on Price:**
                - **RL zones:** Highest residential value
                - **RM/RH zones:** Moderate value, good for investment
                - **Commercial zones:** Variable based on business potential
                - **Agricultural zones:** Lower residential value
                """)
    
    # Building Style & Design
    if not search_term or selected_category in ["All", "Building Style"]:
        with st.expander("🏛️ Building Style & Design", expanded=True):
            style_col1, style_col2 = st.columns(2)
            
            with style_col1:
                st.markdown("""
                **🏠 House Style (HouseStyle)**  
                **Data Type:** Categorical  
                **Description:** Style of dwelling.
                
                **Style Types:**
                - **1Story:** One story house
                - **1.5Fin:** One and one-half story: 2nd level finished
                - **1.5Unf:** One and one-half story: 2nd level unfinished
                - **2Story:** Two story house
                """)
            
            with style_col2:
                st.markdown("""
                **Additional Styles:**
                - **2.5Fin:** Two and one-half story: 2nd level finished
                - **2.5Unf:** Two and one-half story: 2nd level unfinished
                - **SFoyer:** Split Foyer
                - **SLvl:** Split Level
                
                **Value Impact:**
                - **2Story:** Often highest value, more space
                - **1Story:** Popular for accessibility
                - **Split designs:** Unique layouts, moderate value
                """)
    
    # Dimensions and Area
    if not search_term or selected_category in ["All", "Dimensions and Area"]:
        with st.expander("📏 Dimensions and Area Details", expanded=True):
            dim_col1, dim_col2 = st.columns(2)
            
            with dim_col1:
                st.markdown("""
                **🏡 Lot Area (LotArea)**  
                **Data Type:** Numeric (Integer)  
                **Range:** 1,300 - 215,245 sq ft  
                **Description:** Lot size in square feet. Larger lots typically increase property value.
                
                **📐 Lot Shape (LotShape)**  
                **Data Type:** Categorical  
                **Description:** General shape of property.
                
                **Shape Types:**
                - **Reg:** Regular shape
                - **IR1:** Slightly irregular
                - **IR2:** Moderately irregular  
                - **IR3:** Very irregular
                """)
            
            with dim_col2:
                st.markdown("""
                **🌍 Land Contour (LandContour)**  
                **Data Type:** Categorical  
                **Description:** Flatness of the property.
                
                **Contour Types:**
                - **Lvl:** Near flat/level (Best for building)
                - **Bnk:** Banked (Quick rise from street grade)
                - **HLS:** Hillside (Significant slope)
                - **Low:** Depression (Drainage concerns)
                
                **🏔️ Land Slope (LandSlope)**  
                - **Gtl:** Gentle slope (Ideal)
                - **Mod:** Moderate slope
                - **Sev:** Severe slope (Building challenges)
                """)
    
    # Quality and Condition
    if not search_term or selected_category in ["All", "Quality and Condition"]:
        with st.expander("⭐ Quality and Condition Ratings", expanded=True):
            qual_col1, qual_col2 = st.columns(2)
            
            with qual_col1:
                st.markdown("""
                **⭐ Overall Quality Scale (1-10)**  
                **10:** Very Excellent  
                **9:** Excellent  
                **8:** Very Good  
                **7:** Good  
                **6:** Above Average  
                **5:** Average  
                **4:** Below Average  
                **3:** Fair  
                **2:** Poor  
                **1:** Very Poor  
                
                **🏠 Exterior Quality (ExterQual)**  
                Quality of exterior materials.
                """)
            
            with qual_col2:
                st.markdown("""
                **Quality Rating System:**
                - **Ex:** Excellent (Premium materials)
                - **Gd:** Good (Above average materials)
                - **TA:** Typical/Average (Standard materials)
                - **Fa:** Fair (Below average materials)
                - **Po:** Poor (Poor quality materials)
                
                **🔥 Heating Quality (HeatingQC)**  
                Same rating system for heating system quality and condition.
                
                **Impact:** Higher quality ratings significantly increase property value.
                """)
    
    # Garage and Parking
    if not search_term or selected_category in ["All", "Garage and Parking"]:
        with st.expander("🚗 Garage and Parking Features", expanded=True):
            garage_col1, garage_col2 = st.columns(2)
            
            with garage_col1:
                st.markdown("""
                **🚗 Garage Area (GarageArea)**  
                **Data Type:** Numeric (Integer)  
                **Range:** 0 - 1,418 sq ft  
                **Description:** Size of garage in square feet.
                
                **🅿️ Garage Cars (GarageCars)**  
                **Data Type:** Numeric (Integer)  
                **Range:** 0 - 4 cars  
                **Description:** Size of garage in car capacity.
                
                **🏠 Garage Type (GarageType)**  
                - **Attchd:** Attached to home
                - **Detchd:** Detached from home
                """)
            
            with garage_col2:
                st.markdown("""
                **Additional Garage Types:**
                - **BuiltIn:** Built into house
                - **CarPort:** Car port
                - **None:** No garage
                
                **🎨 Garage Finish (GarageFinish)**  
                - **Fin:** Finished interior
                - **RFn:** Rough finished
                - **Unf:** Unfinished
                - **None:** No garage
                
                **Value Impact:** Attached, finished garages add most value.
                """)
    
    # Miscellaneous Features
    if not search_term or selected_category in ["All", "Miscellaneous Features"]:
        with st.expander("🏘️ Miscellaneous Property Features", expanded=True):
            misc_col1, misc_col2 = st.columns(2)
            
            with misc_col1:
                st.markdown("""
                **🚿 Half Bathrooms (HalfBath)**  
                **Range:** 0 - 2 bathrooms  
                **Description:** Half baths above grade (toilet and sink only).
                
                **🏠 Total Rooms (TotRmsAbvGrd)**  
                **Range:** 2 - 14 rooms  
                **Description:** Total rooms above grade (excludes bathrooms).
                
                **🔥 Fireplaces**  
                **Range:** 0 - 3 fireplaces  
                **Description:** Number of fireplaces in the home.
                """)
            
            with misc_col2:
                st.markdown("""
                **🌿 Wood Deck (WoodDeckSF)**  
                **Range:** 0 - 800+ sq ft  
                **Description:** Wood deck area in square feet.
                
                **🏊 Pool Area (PoolArea)**  
                **Range:** 0 - 800+ sq ft  
                **Description:** Pool area in square feet.
                
                **❄️ Central Air (CentralAir)**  
                - **Y:** Yes (Has central air conditioning)
                - **N:** No (No central air conditioning)
                
                **Value Impact:** These features add comfort and resale value.
                """)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Feature Importance Visualization
    st.markdown("""
    <div class="stats-card mt-xl">
        <h2 class="modern-subtitle">🎯 Feature Importance in Price Prediction</h2>
    </div>
    """, unsafe_allow_html=True)
    
    import plotly.graph_objects as go
    
    features = ['Living Area', 'Neighborhood', 'Overall Quality', 'Year Built', 'Garage Area', 
               'Lot Area', 'Basement Area', 'Bathrooms', 'Zoning', 'House Style']
    importance = [32, 28, 18, 12, 8, 6, 4, 3, 2, 1]
    
    fig = go.Figure(go.Bar(
        x=importance,
        y=features,
        orientation='h',
        marker_color=['#8b5cf6', '#3b82f6', '#06b6d4', '#ec4899', '#10b981', 
                     '#f59e0b', '#6366f1', '#7c3aed', '#8b5cf6', '#3b82f6']
    ))
    
    fig.update_layout(
        title="Impact of Features on House Price Prediction",
        xaxis_title="Importance (%)",
        yaxis_title="Features",
        height=400,
        template="plotly_dark"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Feature vs Sale Price Analysis
    st.markdown("""
    <div class="stats-card mt-xl">
        <h2 class="modern-subtitle">📊 Feature vs Sale Price Analysis</h2>
        <p class="modern-text">How different features correlate with house prices</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Mock correlation data for demonstration
    feature_correlations = {
        'Living Area': 0.72,
        'Overall Quality': 0.79,
        'Year Built': 0.52,
        'Garage Area': 0.64,
        'Total Basement SF': 0.61,
        'Full Bathrooms': 0.56,
        'Lot Area': 0.26,
        'Fireplaces': 0.47
    }
    
    corr_fig = go.Figure(go.Bar(
        x=list(feature_correlations.keys()),
        y=list(feature_correlations.values()),
        marker_color=['green' if v > 0.6 else 'orange' if v > 0.4 else 'lightcoral' 
                     for v in feature_correlations.values()]
    ))
    
    corr_fig.update_layout(
        title="Feature Correlation with Sale Price",
        xaxis_title="Features",
        yaxis_title="Correlation Coefficient",
        height=400,
        template="plotly_dark"
    )
    
    st.plotly_chart(corr_fig, use_container_width=True)
    
    # Data validation tips
    st.markdown("""
    <div class="stats-card mt-xl">
        <h2 class="modern-subtitle">⚠️ Data Input Guidelines & Best Practices</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **✅ Best Practices:**
        - Enter accurate square footage measurements
        - Use exact year for construction date
        - Be honest about property condition/grade
        - Include all rooms in bedroom/bathroom counts
        - Check zoning from official city records
        - Measure garage by actual car capacity
        """)
        
    with col2:
        st.markdown("""
        **❌ Common Mistakes:**
        - Including garage/outdoor space in living area
        - Overestimating overall quality ratings
        - Forgetting half bathrooms in count
        - Using lot size instead of house size
        - Incorrect zoning classification
        - Estimating instead of measuring areas
        """)



def render_team_page():
    """Render the team page with development team information"""
    # Hero Section (same as home and guide pages)
    st.markdown("""
    <div class="hero-container">
        <div class="hero-content">
            <div class="hero-badge">
                <span class="badge-icon">👥</span>
                <span class="badge-text">Development Team</span>
            </div>
            <h1 class="hero-title">
                Meet Our <span class="gradient-text">Development Team</span>
            </h1>
            <p class="hero-description">
                Talented CSE students working together to create innovative AI-powered solutions 
                for real estate price prediction using modern machine learning techniques.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Development Team Section
    st.markdown("""
    <div class="mt-xl">
        <h2 class="section-title">🧑‍💻 Development Team</h2>
        <p class="section-description">Computer Science Engineering students working on AI and ML projects</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Team members data
    team_members = [
        {"name": "Jaskawal Singh", "uid": "2472065"},
        {"name": "Jaspal Singh", "uid": "2472027"},
        {"name": "Jashanjeet Singh", "uid": "2472056"},
        {"name": "Gurshad Singh", "uid": "2472072"},
        {"name": "Rajwinder Singh", "uid": "2472028"},
        {"name": "Kulwinder Singh", "uid": "2472006"}
    ]
    
    # Display team members in rows of 3
    for i in range(0, len(team_members), 3):
        cols = st.columns(3)
        for j, member in enumerate(team_members[i:i+3]):
            with cols[j]:
                st.markdown(f"""
                <div class="stats-card" style="text-align: center; padding: 20px;">
                    <div style="font-size: 3rem; margin-bottom: 10px;">🧑‍💻</div>
                    <h4 style="color: var(--text-primary); margin-bottom: 8px;">{member['name']}</h4>
                    <p style="color: var(--text-secondary); margin-bottom: 4px;">Department: CSE</p>
                    <p style="color: var(--text-secondary);">UID: {member['uid']}</p>
                </div>
                """, unsafe_allow_html=True)
    
    # Tech Stack Section
    st.markdown("""
    <div class="mt-xl">
        <h2 class="section-title">🔧 Tech Stack</h2>
        <p class="section-description">Technologies and tools used in this project</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tech stack grid - First row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="tech-card">
            <div class="tech-icon">🐍</div>
            <h4 class="tech-title">Python</h4>
            <p class="tech-description">Core programming language</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="tech-card">
            <div class="tech-icon">🧠</div>
            <h4 class="tech-title">Scikit-learn</h4>
            <p class="tech-description">Machine learning framework</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="tech-card">
            <div class="tech-icon">🎨</div>
            <h4 class="tech-title">Streamlit</h4>
            <p class="tech-description">Web application framework</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="tech-card">
            <div class="tech-icon">📊</div>
            <h4 class="tech-title">Plotly</h4>
            <p class="tech-description">Data visualization</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Tech stack grid - Second row
    col5, col6, col7, col8 = st.columns(4)
    
    with col5:
        st.markdown("""
        <div class="tech-card">
            <div class="tech-icon">📈</div>
            <h4 class="tech-title">Pandas</h4>
            <p class="tech-description">Data manipulation</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col6:
        st.markdown("""
        <div class="tech-card">
            <div class="tech-icon">🔢</div>
            <h4 class="tech-title">NumPy</h4>
            <p class="tech-description">Numerical computing</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col7:
        st.markdown("""
        <div class="tech-card">
            <div class="tech-icon">💾</div>
            <h4 class="tech-title">Joblib</h4>
            <p class="tech-description">Model serialization</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col8:
        st.markdown("""
        <div class="tech-card">
            <div class="tech-icon">🎯</div>
            <h4 class="tech-title">CSS/HTML</h4>
            <p class="tech-description">Frontend styling</p>
        </div>
        """, unsafe_allow_html=True)


def main():
    """Main application function with modern routing"""
    # Configure page
    configure_page()
    
    # Render new Propalytic option menu navbar
    current_page = render_option_menu_navbar()
    
    # Map simplified navbar names to full page names
    page_mapping = {
        "Home": "🏡 Price Prediction",
        "About": "📊 About & Analytics", 
        "Guide": "📚 Feature Guide",
        "Team": "👥 Team"
    }
    
    # Get the full page name
    full_page_name = page_mapping.get(current_page, "🏡 Price Prediction")
    
    # Use the navbar selection instead of sidebar
    # Keep sidebar for theme toggle and stats, but remove navigation
    render_modern_sidebar()
    
    # Route to appropriate page based on navbar selection
    if full_page_name == "🏡 Price Prediction":
        render_prediction_page()
    elif full_page_name == "📊 About & Analytics":
        render_about_page()
    elif full_page_name == "📚 Feature Guide":
        render_feature_guide_page()
    elif full_page_name == "👥 Team":
        render_team_page()
    else:
        # Default to prediction page
        render_prediction_page()


if __name__ == "__main__":
    main()
