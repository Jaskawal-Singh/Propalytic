"""
Utility functions for the House Price Prediction App
"""

import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path


def load_css(css_file_path: str = "assets/style.css") -> str:
    """Load CSS file and return as string"""
    try:
        css_path = Path(css_file_path)
        if css_path.exists():
            with open(css_path) as f:
                return f.read()
        else:
            st.warning(f"CSS file not found: {css_file_path}")
            return ""
    except Exception as e:
        st.error(f"Error loading CSS: {e}")
        return ""


def format_currency(value: float) -> str:
    """Format number as currency"""
    return f"${value:,.2f}"


def format_number(value: float, decimals: int = 2) -> str:
    """Format number with thousand separators"""
    return f"{value:,.{decimals}f}"


def validate_input_range(value: float, min_val: float, max_val: float, field_name: str) -> bool:
    """Validate if input value is within expected range"""
    if value < min_val or value > max_val:
        st.warning(f"{field_name} seems unusual. Expected range: {min_val:,.0f} - {max_val:,.0f}")
        return False
    return True


def get_feature_descriptions() -> dict:
    """Return descriptions for each feature"""
    return {
        'bedrooms': 'Number of bedrooms in the house',
        'bathrooms': 'Number of bathrooms in the house',
        'sqft_living': 'Square footage of living space',
        'sqft_lot': 'Square footage of the lot',
        'floors': 'Number of floors in the house',
        'waterfront': 'Whether the house has a waterfront view',
        'view': 'Quality of the view (0-4 scale)',
        'condition': 'Overall condition of the house (1-5 scale)',
        'grade': 'Overall grade/quality of construction (1-13 scale)',
        'sqft_above': 'Square footage above ground level',
        'sqft_basement': 'Square footage of basement',
        'yr_built': 'Year the house was built',
        'yr_renovated': 'Year the house was renovated (0 if never)',
        'zipcode': 'Zipcode of the property',
        'lat': 'Latitude coordinate',
        'long': 'Longitude coordinate',
        'sqft_living15': 'Average sqft living of 15 nearest neighbors',
        'sqft_lot15': 'Average sqft lot of 15 nearest neighbors'
    }


def get_feature_ranges() -> dict:
    """Return expected ranges for features for validation"""
    return {
        'bedrooms': (1, 15),
        'bathrooms': (0.5, 8),
        'sqft_living': (300, 13540),
        'sqft_lot': (520, 1651359),
        'floors': (1, 3.5),
        'view': (0, 4),
        'condition': (1, 5),
        'grade': (1, 13),
        'sqft_above': (300, 9410),
        'sqft_basement': (0, 4820),
        'yr_built': (1900, 2025),
        'yr_renovated': (0, 2025),
        'zipcode': (98001, 98199),
        'lat': (47.1559, 47.7776),
        'long': (-122.519, -121.315),
        'sqft_living15': (399, 6210),
        'sqft_lot15': (651, 871200)
    }


def create_input_section(title: str, features: list, col_count: int = 2):
    """Create an input section with organized columns"""
    st.subheader(title)
    cols = st.columns(col_count)
    
    values = {}
    for i, feature in enumerate(features):
        col = cols[i % col_count]
        values[feature] = col
    
    return values


def show_model_info():
    """Display model information in sidebar"""
    st.sidebar.markdown("### 🤖 Model Information")
    
    info_data = {
        "Algorithm": "Random Forest",
        "Features": "21 selected features",
        "Training Data": "House sales dataset",
        "Performance": "Optimized for accuracy"
    }
    
    for key, value in info_data.items():
        st.sidebar.write(f"**{key}:** {value}")


def show_app_info():
    """Display app information in sidebar"""
    st.sidebar.markdown("### ℹ️ About This App")
    st.sidebar.write("""
    This professional house price prediction app uses advanced machine learning 
    to estimate property values based on various features.
    
    **Key Features:**
    - Real-time predictions
    - Professional UI/UX
    - Model analytics
    - Data validation
    """)


def create_metrics_display(metrics: dict):
    """Create a metrics display with cards"""
    cols = st.columns(len(metrics))
    
    for i, (label, value) in enumerate(metrics.items()):
        with cols[i]:
            st.markdown(f"""
            <div class="metric-container">
                <div class="metric-value">{value}</div>
                <div class="metric-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)


def show_prediction_confidence(prediction: float, model_std: float = None):
    """Show prediction with confidence interval"""
    if model_std:
        lower_bound = prediction - (1.96 * model_std)
        upper_bound = prediction + (1.96 * model_std)
        
        st.write(f"**Confidence Interval (95%):**")
        st.write(f"{format_currency(lower_bound)} - {format_currency(upper_bound)}")
    else:
        st.write("*Confidence interval not available*")


def log_prediction(features: dict, prediction: float):
    """Log prediction for analytics (in a real app, this would go to a database)"""
    # In a production app, you would save this to a database
    # For now, we'll just create a simple log
    import datetime
    
    log_entry = {
        'timestamp': datetime.datetime.now().isoformat(),
        'prediction': prediction,
        'features': features
    }
    
    # Could save to file or database here
    # st.write("Prediction logged for analytics")


def get_sample_house_data():
    """Return sample house data for quick testing"""
    return {
        'bedrooms': 3,
        'bathrooms': 2.0,
        'sqft_living': 1800,
        'sqft_lot': 7200,
        'floors': 2.0,
        'waterfront': 0,
        'view': 2,
        'condition': 3,
        'grade': 7,
        'sqft_above': 1800,
        'sqft_basement': 0,
        'yr_built': 1990,
        'yr_renovated': 0,
        'zipcode': 98052,
        'lat': 47.6740,
        'long': -122.1215,
        'sqft_living15': 1690,
        'sqft_lot15': 7503
    }
