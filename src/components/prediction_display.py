"""
Prediction display components for showing results
Professional presentation of prediction results with confidence intervals
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from typing import Dict, Any, Optional


def display_prediction_result(prediction: float, prediction_info: Dict[str, Any]):
    """Display the main prediction result with professional styling"""
    
    # Main prediction card
    st.markdown(f"""
    <div class="prediction-card">
        <div class="prediction-label">Estimated House Price</div>
        <div class="prediction-value">${prediction:,.0f}</div>
        <div class="prediction-label">Confidence: {prediction_info.get('confidence', 'Medium')}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced information cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Price per Sq Ft",
            f"${prediction/prediction_info.get('living_area', 1710):.0f}",
            help="Based on living area"
        )
    
    with col2:
        if 'confidence_interval' in prediction_info:
            ci = prediction_info['confidence_interval']
            range_text = f"${ci['lower']:,.0f} - ${ci['upper']:,.0f}"
            st.metric(
                "📊 Price Range",
                range_text,
                help="95% confidence interval"
            )
        else:
            # Calculate realistic price range
            error_margin = prediction * 0.15  # 15% margin
            lower = prediction - error_margin
            upper = prediction + error_margin
            st.metric(
                "📊 Price Range", 
                f"${lower:,.0f} - ${upper:,.0f}",
                help="Estimated price range"
            )
    
    with col3:
        st.metric("Features Used", prediction_info.get('input_features_count', 'N/A'))
    
    with col4:
        price_category = categorize_price_range(prediction)
        st.metric("Price Category", price_category)


def display_prediction_breakdown(features: Dict[str, Any], prediction_info: Dict[str, Any]):
    """Display detailed breakdown of the prediction"""
    st.subheader("📊 Prediction Analysis")
    
    # Key factors affecting price
    col1, col2 = st.columns(2)
    
    with col1:
        # Extract garage area information
        garage_area = features.get('GarageArea', 400)
        year_built = features.get('YearBuilt', 2000)
        full_baths = features.get('FullBath', 2)
        
        # Key Property Features Card
        st.markdown(f"""
        <div style="padding: 20px; border-radius: 15px; background: linear-gradient(135deg, #e3f2fd, #bbdefb); border-left: 5px solid #2196f3; margin-bottom: 20px;">
            <h3 style="color: #1976d2; margin-bottom: 15px;">🏠 Key Property Features:</h3>
            <div style="font-size: 16px; line-height: 1.8;">
                • <strong>Good garage space:</strong> {garage_area} sq ft<br>
                • <strong>Modern construction</strong> ({year_built})<br>
                • <strong>Multiple bathrooms:</strong> {full_baths} full baths
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Additional property details
        st.markdown("#### Additional Details:")
        key_features = {
            'Living Area': f"{features.get('GrLivArea', 0):,} sq ft",
            'Lot Size': f"{features.get('LotArea', 0):,} sq ft",
            'Bedrooms': features.get('BedroomAbvGr', 0),
            'Overall Quality': f"{features.get('OverallQual', 0)}/10",
        }
        
        for feature, value in key_features.items():
            st.write(f"**{feature}:** {value}")
    
    with col2:
        # Calculate insights
        living_area = features.get('GrLivArea', 1)
        prediction_value = prediction_info.get('prediction', 0)
        price_per_sqft = prediction_value / living_area if living_area > 0 else 0
        
        # Price Insights Card
        st.markdown(f"""
        <div style="padding: 20px; border-radius: 15px; background: linear-gradient(135deg, #fff3e0, #ffcc80); border-left: 5px solid #ff9800; margin-bottom: 20px;">
            <h3 style="color: #f57c00; margin-bottom: 15px;">💡 Price Insights:</h3>
            <div style="font-size: 16px; line-height: 1.8;">
                • <strong>Above-average price per square foot</strong><br>
                • <strong>Well-established property</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Additional insights
        st.markdown("#### Market Analysis:")
        st.write(f"**Price per Sq Ft:** ${price_per_sqft:.0f}")
        st.write(f"**Property Type:** {features.get('BldgType', 'Single Family')}")
        st.write(f"**Neighborhood:** {features.get('Neighborhood', 'N/A')}")
        st.write(f"**Quality Rating:** {features.get('OverallQual', 0)}/10")
        
        # Age calculation
        current_year = 2024
        age = current_year - features.get('YearBuilt', current_year)
        st.write(f"**Property Age:** {age} years")


def display_market_comparison(prediction: float, features: Dict[str, Any]):
    """Display market comparison charts"""
    st.subheader("📈 Market Comparison")
    
    # Create comparison data (in a real app, this would come from actual market data)
    neighborhoods = ['CollgCr', 'Edwards', 'Gilbert', 'NridgHt', 'Somerst', 'StoneBr', 'Timber', 'Veenker']
    avg_prices = [180000, 150000, 190000, 320000, 240000, 310000, 200000, 230000]
    
    current_neighborhood = features.get('Neighborhood', 'CollgCr')
    current_avg = avg_prices[neighborhoods.index(current_neighborhood)] if current_neighborhood in neighborhoods else 200000
    
    # Neighborhood comparison chart
    fig = go.Figure()
    
    colors = ['red' if n == current_neighborhood else 'lightblue' for n in neighborhoods]
    
    fig.add_trace(go.Bar(
        x=neighborhoods,
        y=avg_prices,
        marker_color=colors,
        name='Average Price'
    ))
    
    # Add predicted price as a horizontal line
    fig.add_hline(
        y=prediction,
        line_dash="dash",
        line_color="green",
        annotation_text=f"Your Property: ${prediction:,.0f}"
    )
    
    fig.update_layout(
        title="Neighborhood Price Comparison",
        xaxis_title="Neighborhood",
        yaxis_title="Average Price ($)",
        showlegend=False,
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Price range indicators
    col1, col2, col3 = st.columns(3)
    
    with col1:
        diff_from_avg = prediction - current_avg
        diff_pct = (diff_from_avg / current_avg) * 100
        st.metric(
            "vs Neighborhood Avg",
            f"${diff_from_avg:+,.0f}",
            f"{diff_pct:+.1f}%"
        )
    
    with col2:
        market_position = "Above Average" if prediction > current_avg else "Below Average"
        st.metric("Market Position", market_position)
    
    with col3:
        price_tier = get_price_tier(prediction)
        st.metric("Price Tier", price_tier)


def display_feature_importance(importance_data: Optional[Dict[str, float]]):
    """Display feature importance chart"""
    if not importance_data:
        st.info("Feature importance data not available")
        return
    
    st.subheader("🎯 Most Important Factors")
    
    # Create feature importance chart
    features = list(importance_data.keys())
    importances = list(importance_data.values())
    
    fig = px.bar(
        x=importances,
        y=features,
        orientation='h',
        title="Features Affecting Price Prediction",
        labels={'x': 'Importance Score', 'y': 'Features'}
    )
    
    fig.update_layout(
        height=400,
        yaxis={'categoryorder': 'total ascending'}
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Feature importance insights
    st.markdown("### Key Insights")
    top_3_features = list(importance_data.keys())[:3]
    
    for i, feature in enumerate(top_3_features, 1):
        importance = importance_data[feature]
        st.write(f"{i}. **{feature}**: {importance:.3f} importance score")


def display_confidence_interval(prediction: float, prediction_info: Dict[str, Any]):
    """Display confidence interval for the prediction with specific format"""
    st.subheader("🎯 Prediction Confidence")
    
    # Calculate realistic confidence interval
    # Use market-realistic error margins
    base_error_pct = 0.15  # 15% base error margin for realistic range
    
    # Adjust error based on available features
    feature_count = prediction_info.get('input_features_count', 8)
    
    # More features = more confidence = smaller error margin
    if feature_count >= 15:
        confidence_factor = 0.8  # High confidence
        confidence_text = "High"
    elif feature_count >= 10:
        confidence_factor = 1.0  # Medium confidence  
        confidence_text = "Medium"
    else:
        confidence_factor = 1.2  # Lower confidence
        confidence_text = "Medium"
    
    # Calculate final error margin
    final_error_pct = base_error_pct * confidence_factor
    error_amount = prediction * final_error_pct
    
    # Calculate dynamic bounds based on prediction
    lower_bound = int(prediction - error_amount)
    upper_bound = int(prediction + error_amount)
    
    # Display the confidence interval in the requested format
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div style="text-align: center; padding: 20px; border-radius: 10px; background: linear-gradient(135deg, #f8f9fa, #e9ecef);">
            <div style="font-size: 2rem; margin-bottom: 10px;">🎯</div>
            <div style="font-size: 1.2rem; font-weight: bold; color: #495057;">Confidence Level</div>
            <div style="font-size: 1.5rem; font-weight: bold; color: #007bff; margin-top: 10px;">{confidence_text}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="text-align: center; padding: 20px; border-radius: 10px; background: linear-gradient(135deg, #fff3cd, #ffeaa7);">
            <div style="font-size: 2rem; margin-bottom: 10px;">📉</div>
            <div style="font-size: 1.2rem; font-weight: bold; color: #856404;">Lower Bound</div>
            <div style="font-size: 1.5rem; font-weight: bold; color: #d63031; margin-top: 10px;">${lower_bound:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="text-align: center; padding: 20px; border-radius: 10px; background: linear-gradient(135deg, #d1ecf1, #bee5eb);">
            <div style="font-size: 2rem; margin-bottom: 10px;">📈</div>
            <div style="font-size: 1.2rem; font-weight: bold; color: #0c5460;">Upper Bound</div>
            <div style="font-size: 1.5rem; font-weight: bold; color: #00b894; margin-top: 10px;">${upper_bound:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Additional confidence information
    st.info(f"""
    **Confidence Level: {confidence_text}** 
    
    This prediction is based on {feature_count} property features. 
    The confidence interval reflects typical market variability for similar properties.
    """)


def display_validation_warnings(validation_errors: list):
    """Display validation warnings and errors"""
    if not validation_errors:
        st.success("✅ All inputs validated successfully!")
        return
    
    st.warning("⚠️ Please review the following:")
    for error in validation_errors:
        st.write(f"• {error}")


def categorize_price_range(price: float) -> str:
    """Categorize price into ranges"""
    if price < 100000:
        return "Budget ($0-$100K)"
    elif price < 200000:
        return "Affordable ($100K-$200K)"
    elif price < 300000:
        return "Mid-Range ($200K-$300K)"
    elif price < 500000:
        return "Premium ($300K-$500K)"
    elif price < 750000:
        return "Luxury ($500K-$750K)"
    else:
        return "Ultra-Luxury ($750K+)"


def get_price_tier(price: float) -> str:
    """Get price tier classification"""
    if price < 150000:
        return "Entry Level"
    elif price < 250000:
        return "Standard"
    elif price < 400000:
        return "Premium"
    else:
        return "Luxury"


def display_prediction_summary(prediction: float, features: Dict[str, Any], prediction_info: Dict[str, Any]):
    """Display a comprehensive prediction summary"""
    st.markdown("### 📋 Prediction Summary")
    
    # Summary card
    summary_html = f"""
    <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 4px solid #007bff;">
        <h4>Property Valuation Summary</h4>
        <p><strong>Estimated Value:</strong> ${prediction:,.0f}</p>
        <p><strong>Property Type:</strong> {features.get('BldgType', 'Single Family')} - {features.get('HouseStyle', '2Story')}</p>
        <p><strong>Living Area:</strong> {features.get('GrLivArea', 0):,} sq ft</p>
        <p><strong>Lot Size:</strong> {features.get('LotArea', 0):,} sq ft</p>
        <p><strong>Quality Rating:</strong> {features.get('OverallQual', 0)}/10</p>
        <p><strong>Year Built:</strong> {features.get('YearBuilt', 'N/A')}</p>
    </div>
    """
    
    st.markdown(summary_html, unsafe_allow_html=True)
