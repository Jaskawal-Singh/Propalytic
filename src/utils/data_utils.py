"""
Data processing utilities for the House Price Prediction App
"""

import pandas as pd
import numpy as np
import streamlit as st
from typing import Dict, List, Tuple, Optional


def load_dataset(file_path: str) -> pd.DataFrame:
    """Load dataset from CSV file"""
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return pd.DataFrame()


def get_dataset_info(df: pd.DataFrame) -> Dict:
    """Get basic information about the dataset"""
    return {
        'shape': df.shape,
        'columns': list(df.columns),
        'missing_values': df.isnull().sum().sum(),
        'memory_usage': df.memory_usage(deep=True).sum() / 1024**2,  # MB
        'numeric_columns': list(df.select_dtypes(include=[np.number]).columns),
        'categorical_columns': list(df.select_dtypes(include=['object']).columns)
    }


def preprocess_features(features: Dict) -> np.ndarray:
    """Preprocess input features for model prediction"""
    # Convert dictionary to DataFrame
    df = pd.DataFrame([features])
    
    # Handle any necessary preprocessing
    # (This would match the preprocessing done during model training)
    
    return df.values


def validate_features(features: Dict) -> Tuple[bool, List[str]]:
    """Validate input features"""
    errors = []
    
    # Define validation rules
    validation_rules = {
        'bedrooms': (1, 15, 'Bedrooms must be between 1 and 15'),
        'bathrooms': (0.5, 8, 'Bathrooms must be between 0.5 and 8'),
        'sqft_living': (300, 15000, 'Living area must be between 300 and 15,000 sqft'),
        'sqft_lot': (500, 2000000, 'Lot size must be between 500 and 2,000,000 sqft'),
        'floors': (1, 4, 'Floors must be between 1 and 4'),
        'view': (0, 4, 'View rating must be between 0 and 4'),
        'condition': (1, 5, 'Condition must be between 1 and 5'),
        'grade': (1, 13, 'Grade must be between 1 and 13'),
        'yr_built': (1900, 2025, 'Year built must be between 1900 and 2025'),
        'yr_renovated': (0, 2025, 'Year renovated must be between 0 and 2025'),
    }
    
    for feature, (min_val, max_val, error_msg) in validation_rules.items():
        if feature in features:
            value = features[feature]
            if not (min_val <= value <= max_val):
                errors.append(error_msg)
    
    # Additional logical validations
    if 'sqft_above' in features and 'sqft_living' in features:
        if features['sqft_above'] > features['sqft_living']:
            errors.append('Above ground area cannot be larger than total living area')
    
    if 'yr_renovated' in features and 'yr_built' in features:
        if features['yr_renovated'] > 0 and features['yr_renovated'] < features['yr_built']:
            errors.append('Renovation year cannot be before construction year')
    
    return len(errors) == 0, errors


def get_feature_statistics(df: pd.DataFrame) -> Dict:
    """Get statistical information about features"""
    stats = {}
    
    for column in df.select_dtypes(include=[np.number]).columns:
        stats[column] = {
            'mean': df[column].mean(),
            'median': df[column].median(),
            'std': df[column].std(),
            'min': df[column].min(),
            'max': df[column].max(),
            'q25': df[column].quantile(0.25),
            'q75': df[column].quantile(0.75)
        }
    
    return stats


def detect_outliers(df: pd.DataFrame, column: str, method: str = 'iqr') -> pd.Series:
    """Detect outliers in a column"""
    if method == 'iqr':
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        return (df[column] < lower_bound) | (df[column] > upper_bound)
    
    elif method == 'zscore':
        z_scores = np.abs((df[column] - df[column].mean()) / df[column].std())
        return z_scores > 3
    
    return pd.Series([False] * len(df))


def create_feature_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Create a summary table of features"""
    summary = pd.DataFrame({
        'Feature': df.columns,
        'Type': [str(df[col].dtype) for col in df.columns],
        'Missing': [df[col].isnull().sum() for col in df.columns],
        'Missing %': [df[col].isnull().sum() / len(df) * 100 for col in df.columns],
        'Unique': [df[col].nunique() for col in df.columns]
    })
    
    return summary


def prepare_prediction_input(features: Dict, feature_order: List[str]) -> np.ndarray:
    """Prepare input features in the correct order for model prediction"""
    # Ensure features are in the correct order
    ordered_features = []
    
    for feature in feature_order:
        if feature in features:
            ordered_features.append(features[feature])
        else:
            # Handle missing features with default values
            ordered_features.append(0)
    
    return np.array(ordered_features).reshape(1, -1)


def calculate_price_per_sqft(price: float, sqft: float) -> float:
    """Calculate price per square foot"""
    if sqft > 0:
        return price / sqft
    return 0


def categorize_price_range(price: float) -> str:
    """Categorize price into ranges"""
    if price < 200000:
        return "Budget ($0 - $200K)"
    elif price < 400000:
        return "Moderate ($200K - $400K)"
    elif price < 600000:
        return "Premium ($400K - $600K)"
    elif price < 1000000:
        return "Luxury ($600K - $1M)"
    else:
        return "Ultra-Luxury ($1M+)"


def get_comparable_properties(df: pd.DataFrame, features: Dict, n_similar: int = 5) -> pd.DataFrame:
    """Find similar properties in the dataset"""
    # Simple similarity based on key features
    key_features = ['bedrooms', 'bathrooms', 'sqft_living', 'grade']
    
    similarities = []
    for idx, row in df.iterrows():
        similarity = 0
        for feature in key_features:
            if feature in features and feature in row:
                # Calculate similarity (inverse of difference)
                diff = abs(features[feature] - row[feature])
                if feature == 'sqft_living':
                    diff = diff / 1000  # Normalize
                similarity += 1 / (1 + diff)
        similarities.append(similarity)
    
    # Get top similar properties
    df_copy = df.copy()
    df_copy['similarity'] = similarities
    similar_properties = df_copy.nlargest(n_similar, 'similarity')
    
    return similar_properties[['bedrooms', 'bathrooms', 'sqft_living', 'grade', 'price', 'similarity']]
