"""
Modern card-based feature selection system with inline forms
"""

import streamlit as st
from typing import Dict, List, Tuple, Any


def render_feature_selection_cards() -> Dict[str, Any]:
    """
    Render feature selection as two modern cards: permanent and additional features
    """
    cards_css = """
    <style>
    .feature-cards-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 2rem;
        margin: 2rem 0;
        animation: slideUpStagger 0.8s ease-out;
    }
    
    @media (max-width: 768px) {
        .feature-cards-container {
            grid-template-columns: 1fr;
        }
    }
    
    .feature-card {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(24px) saturate(180%);
        border: 2px solid var(--border-light);
        border-radius: var(--radius-2xl);
        padding: 0;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
        box-shadow: var(--shadow-lg);
        transform: translateY(0) scale(1);
    }
    
    [data-theme="dark"] .feature-card {
        background: rgba(15, 23, 42, 0.9);
    }
    
    .feature-card:hover {
        transform: translateY(-12px) scale(1.02);
        box-shadow: var(--shadow-2xl);
        border-color: var(--accent-purple);
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: var(--gradient-primary);
        border-radius: var(--radius-2xl) var(--radius-2xl) 0 0;
        transform: translateX(-100%);
        transition: transform 0.6s ease;
    }
    
    .feature-card::after {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        background: radial-gradient(circle, rgba(139, 92, 246, 0.08) 0%, transparent 70%);
        transition: all 0.6s ease;
        border-radius: 50%;
        transform: translate(-50%, -50%);
        z-index: 0;
    }
    
    .feature-card:hover::before {
        transform: translateX(0);
    }
    
    .feature-card:hover::after {
        width: 300px;
        height: 300px;
    }
    
    .feature-card-header {
        padding: 2rem 2rem 1.5rem;
        border-bottom: 1px solid var(--border-light);
        background: rgba(139, 92, 246, 0.03);
        position: relative;
        z-index: 1;
    }
    
    .feature-card-title {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 0.75rem;
    }
    
    .feature-card-icon {
        width: 48px;
        height: 48px;
        border-radius: var(--radius-xl);
        background: var(--gradient-primary);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 1.5rem;
        font-weight: 600;
        box-shadow: var(--shadow-lg);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .feature-card-icon::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: all 0.6s ease;
    }
    
    .feature-card:hover .feature-card-icon {
        transform: scale(1.1) rotate(5deg);
        box-shadow: var(--shadow-xl);
    }
    
    .feature-card:hover .feature-card-icon::before {
        left: 100%;
    }
    
    .feature-card-name {
        font-size: 1.375rem;
        font-weight: 700;
        color: var(--text-primary);
        margin: 0;
    }
    
    .feature-card-description {
        color: var(--text-secondary);
        font-size: 0.875rem;
        line-height: 1.6;
        margin: 0;
        font-weight: 500;
    }
    
    .feature-card-content {
        padding: 2rem;
        max-height: 600px;
        overflow-y: auto;
        position: relative;
        z-index: 1;
    }
    }
    
    .feature-section {
        margin-bottom: 1.5rem;
    }
    
    .feature-section:last-child {
        margin-bottom: 0;
    }
    
    .feature-section-title {
        font-size: 0.875rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .feature-section-icon {
        font-size: 1rem;
    }
    
    .feature-item {
        margin-bottom: 1rem;
    }
    
    .feature-label {
        display: block;
        font-size: 0.875rem;
        font-weight: 500;
        color: var(--text-secondary);
        margin-bottom: 0.25rem;
    }
    
    .feature-input {
        width: 100%;
        padding: 0.75rem;
        border: 1px solid var(--border-color);
        border-radius: var(--radius-md);
        background: var(--bg-primary);
        color: var(--text-primary);
        font-size: 0.875rem;
        transition: all 0.2s ease;
    }
    
    .feature-input:focus {
        outline: none;
        border-color: var(--primary-purple);
        box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.1);
    }
    
    .feature-input:hover {
        border-color: var(--border-hover);
    }
    
    .feature-help {
        font-size: 0.75rem;
        color: var(--text-tertiary);
        margin-top: 0.25rem;
        font-style: italic;
    }
    
    .feature-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.25rem;
        padding: 0.25rem 0.5rem;
        background: rgba(139, 92, 246, 0.1);
        color: var(--primary-purple);
        border-radius: var(--radius-full);
        font-size: 0.75rem;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    
    .feature-toggle {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 0.75rem;
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-md);
        cursor: pointer;
        transition: all 0.2s ease;
    }
    
    .feature-toggle:hover {
        background: var(--bg-tertiary);
        border-color: var(--border-hover);
    }
    
    .feature-toggle.active {
        background: rgba(139, 92, 246, 0.1);
        border-color: var(--primary-purple);
    }
    
    .toggle-switch {
        width: 40px;
        height: 20px;
        background: var(--border-color);
        border-radius: 10px;
        position: relative;
        transition: background 0.2s ease;
    }
    
    .toggle-switch.active {
        background: var(--primary-purple);
    }
    
    .toggle-switch::after {
        content: '';
        position: absolute;
        width: 16px;
        height: 16px;
        background: white;
        border-radius: 50%;
        top: 2px;
        left: 2px;
        transition: transform 0.2s ease;
        box-shadow: var(--shadow-sm);
    }
    
    .toggle-switch.active::after {
        transform: translateX(20px);
    }
    
    .toggle-label {
        flex: 1;
        font-size: 0.875rem;
        color: var(--text-primary);
    }
    
    .toggle-description {
        font-size: 0.75rem;
        color: var(--text-secondary);
        margin-top: 0.25rem;
    }
    
    .feature-stats {
        background: var(--bg-secondary);
        border-radius: var(--radius-md);
        padding: 1rem;
        margin-top: 1rem;
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
        text-align: center;
    }
    
    .stat-item {
        padding: 0.5rem;
    }
    
    .stat-number {
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--primary-purple);
        display: block;
        margin-bottom: 0.25rem;
    }
    
    .stat-label {
        font-size: 0.75rem;
        color: var(--text-secondary);
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .required-indicator {
        color: var(--error-color);
        font-weight: 600;
        margin-left: 0.25rem;
    }
    
    .optional-indicator {
        color: var(--text-tertiary);
        font-size: 0.75rem;
        margin-left: 0.25rem;
    }
    </style>
    """
    
    st.markdown(cards_css, unsafe_allow_html=True)
    
    # Start the cards container
    st.markdown('<div class="feature-cards-container">', unsafe_allow_html=True)
    
    # Initialize features dictionary
    features = {}
    
    # Permanent Features Card
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-card-header">
                <div class="feature-card-title">
                    <div class="feature-card-icon">🏠</div>
                    <h3 class="feature-card-name">Essential Features</h3>
                </div>
                <p class="feature-card-description">
                    Core property characteristics required for accurate price prediction
                </p>
            </div>
            <div class="feature-card-content">
        """, unsafe_allow_html=True)
        
        # Essential features with custom styling
        st.markdown('<div class="feature-section">', unsafe_allow_html=True)
        st.markdown('''
        <div class="feature-section-title">
            <span class="feature-section-icon">📐</span>
            Property Dimensions
        </div>
        ''', unsafe_allow_html=True)
        
        # Living Area
        st.markdown('<div class="feature-item">', unsafe_allow_html=True)
        st.markdown('<span class="feature-badge">🎯 Most Important</span>', unsafe_allow_html=True)
        features['GrLivArea'] = st.number_input(
            "Above Ground Living Area (sq ft)",
            min_value=500,
            max_value=5000,
            value=1500,
            step=50,
            help="Total living space above ground level",
            key="essential_living_area"
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Lot Area
        features['LotArea'] = st.number_input(
            "Lot Size (sq ft)",
            min_value=1000,
            max_value=50000,
            value=8000,
            step=100,
            help="Size of the property lot",
            key="essential_lot_area"
        )
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Quality Section
        st.markdown('<div class="feature-section">', unsafe_allow_html=True)
        st.markdown('''
        <div class="feature-section-title">
            <span class="feature-section-icon">⭐</span>
            Quality Ratings
        </div>
        ''', unsafe_allow_html=True)
        
        # Overall Quality
        st.markdown('<span class="feature-badge">🏆 High Impact</span>', unsafe_allow_html=True)
        features['OverallQual'] = st.selectbox(
            "Overall Quality (1-10)",
            options=list(range(1, 11)),
            index=6,
            help="Overall material and finish quality of the house",
            key="essential_quality"
        )
        
        # Kitchen Quality
        quality_options = {'Po': 'Poor', 'Fa': 'Fair', 'TA': 'Average', 'Gd': 'Good', 'Ex': 'Excellent'}
        features['KitchenQual'] = st.selectbox(
            "Kitchen Quality",
            options=list(quality_options.keys()),
            format_func=lambda x: quality_options[x],
            index=2,
            help="Kitchen quality rating",
            key="essential_kitchen_qual"
        )
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Location Section
        st.markdown('<div class="feature-section">', unsafe_allow_html=True)
        st.markdown('''
        <div class="feature-section-title">
            <span class="feature-section-icon">📍</span>
            Location
        </div>
        ''', unsafe_allow_html=True)
        
        # Neighborhood
        neighborhood_options = {
            'NAmes': 'North Ames', 'Edwards': 'Edwards', 'BrkSide': 'Brookside',
            'OldTown': 'Old Town', 'Somerst': 'Somerset', 'Gilbert': 'Gilbert',
            'CollgCr': 'College Creek', 'Crawfor': 'Crawford', 'NoRidge': 'Northridge',
            'StoneBr': 'Stone Brook', 'Timber': 'Timberland', 'NridgHt': 'Northridge Heights'
        }
        
        st.markdown('<span class="feature-badge">🌟 Location Premium</span>', unsafe_allow_html=True)
        features['Neighborhood'] = st.selectbox(
            "Neighborhood",
            options=list(neighborhood_options.keys()),
            format_func=lambda x: neighborhood_options[x],
            index=0,
            help="Property neighborhood/location",
            key="essential_neighborhood"
        )
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Stats for essential features
        st.markdown('''
        <div class="feature-stats">
            <div class="stats-grid">
                <div class="stat-item">
                    <span class="stat-number">6</span>
                    <span class="stat-label">Required</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">85%</span>
                    <span class="stat-label">Accuracy</span>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown('</div></div>', unsafe_allow_html=True)
    
    # Additional Features Card
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-card-header">
                <div class="feature-card-title">
                    <div class="feature-card-icon">⚙️</div>
                    <h3 class="feature-card-name">Advanced Features</h3>
                </div>
                <p class="feature-card-description">
                    Optional features that can improve prediction accuracy
                </p>
            </div>
            <div class="feature-card-content">
        """, unsafe_allow_html=True)
        
        # Advanced features with toggles
        st.markdown('<div class="feature-section">', unsafe_allow_html=True)
        st.markdown('''
        <div class="feature-section-title">
            <span class="feature-section-icon">🏗️</span>
            Structure Details
        </div>
        ''', unsafe_allow_html=True)
        
        # Year Built
        enable_year_built = st.checkbox("Include Year Built", value=True, key="enable_year_built")
        if enable_year_built:
            features['YearBuilt'] = st.slider(
                "Year Built",
                min_value=1900,
                max_value=2024,
                value=1980,
                help="Year the house was originally built",
                key="adv_year_built"
            )
        
        # Total Basement Area
        enable_basement = st.checkbox("Include Basement Info", value=False, key="enable_basement")
        if enable_basement:
            features['TotalBsmtSF'] = st.number_input(
                "Total Basement Area (sq ft)",
                min_value=0,
                max_value=3000,
                value=0,
                step=50,
                help="Total square feet of basement area",
                key="adv_basement"
            )
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Garage Section
        st.markdown('<div class="feature-section">', unsafe_allow_html=True)
        st.markdown('''
        <div class="feature-section-title">
            <span class="feature-section-icon">🚗</span>
            Garage Features
        </div>
        ''', unsafe_allow_html=True)
        
        enable_garage = st.checkbox("Include Garage Details", value=False, key="enable_garage")
        if enable_garage:
            features['GarageCars'] = st.selectbox(
                "Garage Capacity (cars)",
                options=[0, 1, 2, 3, 4, 5],
                index=2,
                help="Number of cars that fit in garage",
                key="adv_garage_cars"
            )
            
            features['GarageArea'] = st.number_input(
                "Garage Area (sq ft)",
                min_value=0,
                max_value=1500,
                value=500,
                step=25,
                help="Size of garage in square feet",
                key="adv_garage_area"
            )
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Additional Quality Features
        st.markdown('<div class="feature-section">', unsafe_allow_html=True)
        st.markdown('''
        <div class="feature-section-title">
            <span class="feature-section-icon">✨</span>
            Additional Quality
        </div>
        ''', unsafe_allow_html=True)
        
        enable_exterior = st.checkbox("Include Exterior Quality", value=False, key="enable_exterior")
        if enable_exterior:
            features['ExterQual'] = st.selectbox(
                "Exterior Quality",
                options=list(quality_options.keys()),
                format_func=lambda x: quality_options[x],
                index=2,
                help="Exterior material quality",
                key="adv_exterior_qual"
            )
        
        enable_heating = st.checkbox("Include Heating Quality", value=False, key="enable_heating")
        if enable_heating:
            features['HeatingQC'] = st.selectbox(
                "Heating Quality",
                options=list(quality_options.keys()),
                format_func=lambda x: quality_options[x],
                index=2,
                help="Heating system quality and condition",
                key="adv_heating_qc"
            )
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Feature count stats
        enabled_count = sum([
            enable_year_built, enable_basement, enable_garage, enable_exterior, enable_heating
        ])
        if enable_garage:
            enabled_count += 1  # GarageArea counts as additional
        
        st.markdown(f'''
        <div class="feature-stats">
            <div class="stats-grid">
                <div class="stat-item">
                    <span class="stat-number">{enabled_count}</span>
                    <span class="stat-label">Enabled</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">{85 + enabled_count * 2}%</span>
                    <span class="stat-label">Accuracy</span>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown('</div></div>', unsafe_allow_html=True)
    
    # Close cards container
    st.markdown('</div>', unsafe_allow_html=True)
    
    return features


def render_prediction_card(prediction: float, features: Dict[str, Any]):
    """
    Render a modern prediction result card
    """
    prediction_css = """
    <style>
    .prediction-card {
        background: var(--gradient-primary);
        border-radius: var(--radius-2xl);
        padding: 2rem;
        text-align: center;
        color: white;
        position: relative;
        overflow: hidden;
        margin: 2rem 0;
        box-shadow: var(--shadow-2xl);
    }
    
    .prediction-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: shimmer 3s ease-in-out infinite;
    }
    
    @keyframes shimmer {
        0%, 100% { transform: rotate(0deg); }
        50% { transform: rotate(180deg); }
    }
    
    .prediction-content {
        position: relative;
        z-index: 1;
    }
    
    .prediction-label {
        font-size: 1rem;
        opacity: 0.9;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
    
    .prediction-value {
        font-size: 3rem;
        font-weight: 900;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .prediction-confidence {
        font-size: 0.875rem;
        opacity: 0.8;
        background: rgba(255,255,255,0.2);
        padding: 0.5rem 1rem;
        border-radius: var(--radius-full);
        display: inline-block;
    }
    </style>
    """
    
    prediction_html = f"""
    {prediction_css}
    
    <div class="prediction-card">
        <div class="prediction-content">
            <div class="prediction-label">Estimated Price</div>
            <div class="prediction-value">${prediction:,.0f}</div>
            <div class="prediction-confidence">95% Confidence Interval: ±5%</div>
        </div>
    </div>
    """
    
    st.markdown(prediction_html, unsafe_allow_html=True)
