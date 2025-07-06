"""
House Price Prediction Model Integration
Professional model handler following house.py logic exactly
"""

import joblib
import pandas as pd
import numpy as np
import streamlit as st
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import os


class HousePricePredictor:
    """Professional House Price Predictor matching house.py logic exactly"""
    
    def __init__(self, model_path: str = "src/models/house_price_model.joblib"):
        """Initialize the predictor with model loading"""
        self.model = None
        self.scaler = None
        self.model_features = None
        self.scaler_features = None
        self.model_metadata = {}
        self.model_path = model_path
        
        # Load model and related files
        self._load_model()
        self._load_scaler()
        self._load_metadata()
    
    def _load_model(self) -> None:
        """Load the trained model exactly like house.py"""
        try:
            if os.path.exists(self.model_path):
                self.model = joblib.load(self.model_path)
                
                # Get the 21 features the model expects (like house.py)
                if hasattr(self.model, 'feature_names_in_'):
                    self.model_features = list(self.model.feature_names_in_)
                else:
                    # Try to load from CSV file in data directory
                    try:
                        selected_features_df = pd.read_csv('data/selected_features.csv')
                        self.model_features = selected_features_df['selected_features'].tolist()
                    except:
                        # Try alternative path
                        try:
                            selected_features_df = pd.read_csv('src/data/selected_features.csv')
                            self.model_features = selected_features_df['selected_features'].tolist()
                        except:
                            # Fallback to the 21 key features
                            self.model_features = [
                                'MSSubClass', 'MSZoning', 'Neighborhood', 'OverallQual', 'YearRemodAdd',
                                'RoofStyle', 'BsmtQual', 'BsmtExposure', 'HeatingQC', 'CentralAir',
                                '1stFlrSF', 'GrLivArea', 'BsmtFullBath', 'KitchenQual', 'Fireplaces',
                                'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageCars', 'PavedDrive',
                                'SaleCondition'
                            ]
                
                print(f"Model expects: {len(self.model_features)} features")
                    
            else:
                st.error(f"❌ Model file not found: {self.model_path}")
                
        except Exception as e:
            st.error(f"❌ Error loading model: {str(e)}")
    
    def _load_scaler(self) -> None:
        """Load the scaler exactly like house.py"""
        try:
            scaler_path = "src/models/scaler.joblib"
            if os.path.exists(scaler_path):
                self.scaler = joblib.load(scaler_path)
                
                # Get all 82 features the scaler expects (like house.py)
                if hasattr(self.scaler, 'feature_names_in_'):
                    self.scaler_features = list(self.scaler.feature_names_in_)
                    print(f"Scaler expects: {len(self.scaler_features)} features")
                else:
                    # If scaler doesn't have feature names, we'll skip scaling
                    self.scaler_features = None
                    st.warning("⚠️ Scaler feature names not found, will skip scaling")
            else:
                st.warning("⚠️ Scaler file not found, will skip scaling")
                self.scaler = None
                self.scaler_features = None
                
        except Exception as e:
            st.warning(f"⚠️ Error loading scaler: {str(e)}")
            self.scaler = None
            self.scaler_features = None
    
    def _get_default_features(self) -> List[str]:
        """Get default feature names for the Kaggle house prices dataset"""
        return [
            'MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'Street', 'Alley',
            'LotShape', 'LandContour', 'Utilities', 'LotConfig', 'LandSlope',
            'Neighborhood', 'Condition1', 'Condition2', 'BldgType', 'HouseStyle',
            'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd', 'RoofStyle',
            'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType', 'MasVnrArea',
            'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual', 'BsmtCond',
            'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1', 'BsmtFinType2',
            'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'Heating', 'HeatingQC',
            'CentralAir', 'Electrical', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF',
            'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath',
            'BedroomAbvGr', 'KitchenAbvGr', 'KitchenQual', 'TotRmsAbvGrd',
            'Functional', 'Fireplaces', 'FireplaceQu', 'GarageType', 'GarageYrBlt',
            'GarageFinish', 'GarageCars', 'GarageArea', 'GarageQual', 'GarageCond',
            'PavedDrive', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch',
            'ScreenPorch', 'PoolArea', 'PoolQC', 'Fence', 'MiscFeature', 'MiscVal',
            'MoSold', 'YrSold', 'SaleType', 'SaleCondition'
        ]
    
    def _load_metadata(self) -> None:
        """Load model metadata and performance information"""
        # Updated with actual values from the notebook training
        self.model_metadata = {
            'model_type': 'Random Forest Regressor',
            'training_date': '2025-07-02',
            'features_count': 82,  # Total features before selection
            'selected_features_count': 21,  # Features after Lasso selection  
            'performance_metrics': {
                'r2_score': 0.9818,  # Actual R² from notebook
                'mae': 0.0367,       # Actual MAE from notebook (log scale)
                'rmse': 0.0539,      # Actual RMSE from notebook (log scale)
                'mse': 0.0029        # Actual MSE from notebook (log scale)
            },
            'preprocessing_steps': [
                'Missing value handling for categorical and numerical features',
                'Log transformation for skewed features', 
                'Year features converted to age features',
                'Categorical encoding using target mean encoding',
                'Rare category handling (< 1% frequency)',
                'Feature scaling using MinMaxScaler',
                'Feature selection using Lasso (α=0.005)',
                'Final model: Random Forest (100 estimators)'
            ]
        }
    
    def create_full_feature_vector(self, user_inputs: Dict) -> List[float]:
        """Create a full 82-feature vector for the scaler (exactly like house.py)"""
        # Default values for all 82 features (matching house.py exactly)
        default_values = {
            # User provided features (21)
            **user_inputs,
            
            # Additional features with reasonable defaults (61 more) - exactly like house.py
            'LotFrontage': 70.0,
            'LotArea': 8000.0,
            'Street': 1,
            'Alley': 0,
            'LotShape': 3,
            'LandContour': 0,
            'Utilities': 0,
            'LotConfig': 4,
            'LandSlope': 0,
            'Condition1': 2,
            'Condition2': 2,
            'BldgType': 0,
            'HouseStyle': 5,
            'OverallCond': 5,
            'YearBuilt': 30,  # 30 years old
            'RoofMatl': 0,
            'Exterior1st': 12,
            'Exterior2nd': 12,
            'MasVnrType': 1,
            'MasVnrArea': 100.0,
            'ExterQual': 3,
            'ExterCond': 3,
            'Foundation': 2,
            'BsmtCond': 3,
            'BsmtFinType1': 5,
            'BsmtFinSF1': 400.0,
            'BsmtFinType2': 5,
            'BsmtFinSF2': 0.0,
            'BsmtUnfSF': 400.0,
            'TotalBsmtSF': 800.0,
            'Heating': 1,
            'Electrical': 4,
            '2ndFlrSF': 0.0,
            'LowQualFinSF': 0.0,
            'BsmtHalfBath': 0,
            'FullBath': 2,
            'HalfBath': 0,
            'BedroomAbvGr': 3,
            'KitchenAbvGr': 1,
            'TotRmsAbvGrd': 7,
            'Functional': 6,
            'GarageYrBlt': 30,
            'GarageArea': 500.0,
            'GarageQual': 3,
            'GarageCond': 3,
            'WoodDeckSF': 0.0,
            'OpenPorchSF': 0.0,
            'EnclosedPorch': 0.0,
            '3SsnPorch': 0.0,
            'ScreenPorch': 0.0,
            'PoolArea': 0.0,
            'PoolQC': 0,
            'Fence': 0,
            'MiscFeature': 0,
            'MiscVal': 0.0,
            'MoSold': 6,
            'YrSold': 2010,
            'SaleType': 8,
            'LotFrontagenan': 0,
            'MasVnrAreanan': 0,
            'GarageYrBltnan': 0
        }
        
        # Create ordered list matching scaler's expected features
        full_vector = []
        for feature in self.scaler_features:
            full_vector.append(default_values.get(feature, 0.0))
        
        return full_vector
    
    def predict_price(self, features: Dict) -> Tuple[float, Dict]:
        """
        Predict house price exactly like house.py
        
        Args:
            features: Dictionary of feature values
            
        Returns:
            Tuple of (predicted_price, prediction_info)
        """
        if not self.model:
            raise ValueError("Model not loaded")
        
        try:
            print(f"=== PREDICTION DEBUG (Streamlit) ===")
            
            # First, encode categorical features to numeric values like house.py
            encoded_features = {}
            for feature, value in features.items():
                if feature in self.model_features:
                    # Handle categorical encoding manually like house.py
                    if feature == 'MSZoning':
                        mapping = {'C': 0, 'RM': 1, 'RH': 2, 'RL': 3, 'FV': 4}
                        encoded_features[feature] = mapping.get(value, 3)  # Default to RL
                    elif feature == 'Neighborhood':
                        mapping = {
                            'MeadowV': 0, 'IDOTRR': 1, 'BrDale': 2, 'OldTown': 3, 'Edwards': 4,
                            'BrkSide': 5, 'Sawyer': 6, 'Blueste': 7, 'SWISU': 8, 'NAmes': 9,
                            'NPkVill': 10, 'Mitchel': 11, 'SawyerW': 12, 'Gilbert': 13, 'NWAmes': 14,
                            'Blmngtn': 15, 'CollgCr': 16, 'ClearCr': 17, 'Crawfor': 18, 'Veenker': 19,
                            'Somerst': 20, 'Timber': 21, 'StoneBr': 22, 'NoRidge': 23, 'NridgHt': 24
                        }
                        encoded_features[feature] = mapping.get(value, 12)  # Default to average
                    elif feature == 'RoofStyle':
                        mapping = {'Gable': 1, 'Hip': 2, 'Gambrel': 3, 'Mansard': 4, 'Flat': 5, 'Shed': 6}
                        encoded_features[feature] = mapping.get(value, 1)  # Default to Gable
                    elif feature == 'BsmtQual':
                        mapping = {'NA': 0, 'Fa': 1, 'TA': 2, 'Gd': 3, 'Ex': 4}
                        encoded_features[feature] = mapping.get(value, 3)  # Default to Good
                    elif feature == 'BsmtExposure':
                        mapping = {'NA': 0, 'No': 1, 'Mn': 2, 'Av': 3, 'Gd': 4}
                        encoded_features[feature] = mapping.get(value, 2)  # Default to Average
                    elif feature == 'HeatingQC':
                        mapping = {'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5}
                        encoded_features[feature] = mapping.get(value, 4)  # Default to Good
                    elif feature == 'CentralAir':
                        mapping = {'N': 0, 'Y': 1}
                        encoded_features[feature] = mapping.get(value, 1)  # Default to Yes
                    elif feature == 'KitchenQual':
                        mapping = {'Fa': 1, 'TA': 2, 'Gd': 3, 'Ex': 4}
                        encoded_features[feature] = mapping.get(value, 3)  # Default to Good
                    elif feature == 'FireplaceQu':
                        mapping = {'NA': 0, 'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5}
                        encoded_features[feature] = mapping.get(value, 3)  # Default to Average
                    elif feature == 'GarageType':
                        mapping = {'NA': 0, 'Detchd': 1, 'CarPort': 2, 'BuiltIn': 3, 'Attchd': 4}
                        encoded_features[feature] = mapping.get(value, 1)  # Default to Attached
                    elif feature == 'GarageFinish':
                        mapping = {'NA': 0, 'Unf': 1, 'RFn': 2, 'Fin': 3}
                        encoded_features[feature] = mapping.get(value, 2)  # Default to Rough Finished
                    elif feature == 'PavedDrive':
                        mapping = {'N': 0, 'P': 1, 'Y': 2}
                        encoded_features[feature] = mapping.get(value, 2)  # Default to Yes
                    elif feature == 'SaleCondition':
                        mapping = {'AdjLand': 0, 'Abnorml': 1, 'Alloca': 2, 'Family': 3, 'Normal': 4, 'Partial': 5}
                        encoded_features[feature] = mapping.get(value, 4)  # Default to Normal
                    else:
                        # Numeric feature
                        encoded_features[feature] = float(value)
            
            print(f"User provided {len(encoded_features)} features")
            
            if self.scaler_features:
                # Method 1: Use scaler with full 82-feature vector (like house.py)
                print("Using scaler with full feature vector...")
                full_vector = self.create_full_feature_vector(encoded_features)
                full_df = pd.DataFrame([full_vector], columns=self.scaler_features)
                
                # Scale all features
                scaled_full = self.scaler.transform(full_df)
                
                # Extract only the 21 features the model needs
                model_indices = [self.scaler_features.index(f) for f in self.model_features]
                model_input = scaled_full[:, model_indices]
                
            else:
                # Method 2: Skip scaler, use raw values (like house.py fallback)
                print("Skipping scaler, using raw values...")
                model_data = [encoded_features.get(f, 0) for f in self.model_features]
                model_input = np.array([model_data])
            
            # Make prediction
            prediction_log = self.model.predict(model_input)[0]
            prediction = np.exp(prediction_log)
            
            print(f"Predicted price: ${prediction:,.2f}")
            
            # Get prediction info
            prediction_info = self._get_prediction_info(model_input, prediction, encoded_features)
            
            return prediction, prediction_info
            
        except Exception as e:
            st.error(f"Prediction error: {str(e)}")
            import traceback
            traceback.print_exc()
            return 0.0, {'error': str(e)}

    def _get_prediction_info(self, feature_array: np.ndarray, prediction: float, user_inputs: Dict) -> Dict:
        """Get additional information about the prediction"""
        info = {
            'prediction': prediction,
            'formatted_prediction': f"${prediction:,.2f}",
            'confidence': 'Medium',
            'input_features_count': len(user_inputs),
            'missing_features_count': len(self.model_features) - len(user_inputs)
        }
        
        # Add category information
        if prediction < 150000:
            info['category'] = 'Budget (Under $150K)'
            info['category_color'] = '#e67e22'
        elif prediction > 400000:
            info['category'] = 'Premium ($400K+)'
            info['category_color'] = '#9b59b6'
        else:
            info['category'] = 'Mid-range ($150K-$400K)'
            info['category_color'] = '#27ae60'
        
        # Add prediction range if available
        if hasattr(self.model, 'estimators_'):
            # For ensemble models, calculate prediction std
            try:
                predictions = [tree.predict(feature_array)[0] for tree in self.model.estimators_]
                predictions = [np.exp(p) for p in predictions]  # Convert from log scale
                std_dev = np.std(predictions)
                info['std_deviation'] = std_dev
                info['confidence_interval'] = {
                    'lower': max(0, prediction - 1.96 * std_dev),
                    'upper': prediction + 1.96 * std_dev
                }
            except:
                pass
        
        return info
    
    def get_model_info(self) -> Dict:
        """Get comprehensive model information"""
        return {
            'status': 'Loaded' if self.model else 'Not Loaded',
            'metadata': self.model_metadata,
            'feature_count': len(self.model_features) if self.model_features else 0,
            'model_features': self.model_features,
            'scaler_features_count': len(self.scaler_features) if self.scaler_features else 0
        }
    
    def get_feature_importance(self, top_n: int = 10) -> Optional[Dict]:
        """Get feature importance from the model"""
        if not self.model or not hasattr(self.model, 'feature_importances_'):
            return None
        
        if not self.model_features:
            return None
        
        # Get feature importances
        importances = self.model.feature_importances_
        feature_importance = dict(zip(self.model_features, importances))
        
        # Sort by importance
        sorted_features = sorted(feature_importance.items(), key=lambda x: x[1], reverse=True)
        
        return dict(sorted_features[:top_n])
    
    def validate_input(self, features: Dict) -> Tuple[bool, List[str]]:
        """Validate input features"""
        errors = []
        
        # Basic validation for numeric features
        numeric_features = ['LotArea', 'GrLivArea', 'YearBuilt', 'OverallQual', 'OverallCond']
        for feature in numeric_features:
            if feature in features:
                value = features[feature]
                if not isinstance(value, (int, float)) or value < 0:
                    errors.append(f"{feature} must be a positive number")
        
        # Logical validations
        if 'YearBuilt' in features and 'YearRemodAdd' in features:
            if features['YearRemodAdd'] < features['YearBuilt']:
                errors.append("Renovation year cannot be before construction year")
        
        if 'GrLivArea' in features and features['GrLivArea'] > 10000:
            errors.append("Living area seems unusually large (>10,000 sq ft)")
        
        return len(errors) == 0, errors
    
    def get_sample_input(self) -> Dict:
        """Get sample input for testing"""
        return {
            'MSSubClass': 60,
            'MSZoning': 'RL',
            'LotFrontage': 65,
            'LotArea': 8450,
            'Street': 'Pave',
            'Alley': 'NA',
            'LotShape': 'Reg',
            'LandContour': 'Lvl',
            'Utilities': 'AllPub',
            'LotConfig': 'Inside',
            'LandSlope': 'Gtl',
            'Neighborhood': 'CollgCr',
            'Condition1': 'Norm',
            'Condition2': 'Norm',
            'BldgType': '1Fam',
            'HouseStyle': '2Story',
            'OverallQual': 7,
            'OverallCond': 5,
            'YearBuilt': 2003,
            'YearRemodAdd': 2003,
            'RoofStyle': 'Gable',
            'RoofMatl': 'CompShg',
            'Exterior1st': 'VinylSd',
            'Exterior2nd': 'VinylSd',
            'MasVnrType': 'BrkFace',
            'MasVnrArea': 196,
            'ExterQual': 'Gd',
            'ExterCond': 'TA',
            'Foundation': 'PConc',
            'BsmtQual': 'Gd',
            'BsmtCond': 'TA',
            'BsmtExposure': 'No',
            'BsmtFinType1': 'GLQ',
            'BsmtFinSF1': 706,
            'BsmtFinType2': 'Unf',
            'BsmtFinSF2': 0,
            'BsmtUnfSF': 150,
            'TotalBsmtSF': 856,
            'Heating': 'GasA',
            'HeatingQC': 'Ex',
            'CentralAir': 'Y',
            'Electrical': 'SBrkr',
            '1stFlrSF': 856,
            '2ndFlrSF': 854,
            'LowQualFinSF': 0,
            'GrLivArea': 1710,
            'BsmtFullBath': 1,
            'BsmtHalfBath': 0,
            'FullBath': 2,
            'HalfBath': 1,
            'BedroomAbvGr': 3,
            'KitchenAbvGr': 1,
            'KitchenQual': 'Gd',
            'TotRmsAbvGrd': 8,
            'Functional': 'Typ',
            'Fireplaces': 0,
            'FireplaceQu': 'NA',
            'GarageType': 'Attchd',
            'GarageYrBlt': 2003,
            'GarageFinish': 'RFn',
            'GarageCars': 2,
            'GarageArea': 548,
            'GarageQual': 'TA',
            'GarageCond': 'TA',
            'PavedDrive': 'Y',
            'WoodDeckSF': 0,
            'OpenPorchSF': 61,
            'EnclosedPorch': 0,
            '3SsnPorch': 0,
            'ScreenPorch': 0,
            'PoolArea': 0,
            'PoolQC': 'NA',
            'Fence': 'NA',
            'MiscFeature': 'NA',
            'MiscVal': 0,
            'MoSold': 2,
            'YrSold': 2008,
            'SaleType': 'WD',
            'SaleCondition': 'Normal'
        }


def load_predictor() -> HousePricePredictor:
    """Load and return a configured predictor instance"""
    return HousePricePredictor()