"""
Feature mapping and descriptions for House Price Prediction App
Maps technical column names to user-friendly names and provides detailed explanations
"""

from typing import Dict, List, Tuple

# Feature name mapping from technical to user-friendly names
FEATURE_MAPPING = {
    # Basic Property Info
    'MSSubClass': 'Building Class',
    'MSZoning': 'Zoning Classification',
    'LotFrontage': 'Street Frontage (feet)',
    'LotArea': 'Lot Size (sq ft)',
    'Street': 'Road Type',
    'Alley': 'Alley Access',
    'LotShape': 'Lot Shape',
    'LandContour': 'Property Flatness',
    'Utilities': 'Available Utilities',
    'LotConfig': 'Lot Configuration',
    'LandSlope': 'Land Slope',
    'Neighborhood': 'Neighborhood',
    
    # Building Type and Style
    'Condition1': 'Proximity to Main Road',
    'Condition2': 'Secondary Proximity',
    'BldgType': 'Building Type',
    'HouseStyle': 'House Style',
    'OverallQual': 'Overall Quality (1-10)',
    'OverallCond': 'Overall Condition (1-10)',
    'YearBuilt': 'Year Built',
    'YearRemodAdd': 'Year Renovated',
    
    # Roof and Exterior
    'RoofStyle': 'Roof Style',
    'RoofMatl': 'Roof Material',
    'Exterior1st': 'Primary Exterior Material',
    'Exterior2nd': 'Secondary Exterior Material',
    'MasVnrType': 'Masonry Veneer Type',
    'MasVnrArea': 'Masonry Veneer Area (sq ft)',
    'ExterQual': 'Exterior Quality',
    'ExterCond': 'Exterior Condition',
    'Foundation': 'Foundation Type',
    
    # Basement
    'BsmtQual': 'Basement Quality',
    'BsmtCond': 'Basement Condition',
    'BsmtExposure': 'Basement Exposure',
    'BsmtFinType1': 'Basement Finish Type 1',
    'BsmtFinSF1': 'Basement Finished Area 1 (sq ft)',
    'BsmtFinType2': 'Basement Finish Type 2',
    'BsmtFinSF2': 'Basement Finished Area 2 (sq ft)',
    'BsmtUnfSF': 'Basement Unfinished Area (sq ft)',
    'TotalBsmtSF': 'Total Basement Area (sq ft)',
    
    # Heating and Electrical
    'Heating': 'Heating Type',
    'HeatingQC': 'Heating Quality',
    'CentralAir': 'Central Air Conditioning',
    'Electrical': 'Electrical System',
    
    # Floor Areas
    '1stFlrSF': 'First Floor Area (sq ft)',
    '2ndFlrSF': 'Second Floor Area (sq ft)',
    'LowQualFinSF': 'Low Quality Finished Area (sq ft)',
    'GrLivArea': 'Above Ground Living Area (sq ft)',
    
    # Bathrooms and Bedrooms
    'BsmtFullBath': 'Basement Full Bathrooms',
    'BsmtHalfBath': 'Basement Half Bathrooms',
    'FullBath': 'Full Bathrooms Above Ground',
    'HalfBath': 'Half Bathrooms Above Ground',
    'BedroomAbvGr': 'Bedrooms Above Ground',
    'KitchenAbvGr': 'Kitchens Above Ground',
    'KitchenQual': 'Kitchen Quality',
    'TotRmsAbvGrd': 'Total Rooms Above Ground',
    
    # Other Features
    'Functional': 'Home Functionality',
    'Fireplaces': 'Number of Fireplaces',
    'FireplaceQu': 'Fireplace Quality',
    
    # Garage
    'GarageType': 'Garage Type',
    'GarageYrBlt': 'Garage Year Built',
    'GarageFinish': 'Garage Finish',
    'GarageCars': 'Garage Car Capacity',
    'GarageArea': 'Garage Area (sq ft)',
    'GarageQual': 'Garage Quality',
    'GarageCond': 'Garage Condition',
    'PavedDrive': 'Paved Driveway',
    
    # Outdoor Features
    'WoodDeckSF': 'Wood Deck Area (sq ft)',
    'OpenPorchSF': 'Open Porch Area (sq ft)',
    'EnclosedPorch': 'Enclosed Porch Area (sq ft)',
    '3SsnPorch': 'Three Season Porch Area (sq ft)',
    'ScreenPorch': 'Screen Porch Area (sq ft)',
    'PoolArea': 'Pool Area (sq ft)',
    'PoolQC': 'Pool Quality',
    'Fence': 'Fence Quality',
    'MiscFeature': 'Miscellaneous Feature',
    'MiscVal': 'Miscellaneous Feature Value ($)',
    
    # Sale Info
    'MoSold': 'Month Sold',
    'YrSold': 'Year Sold',
    'SaleType': 'Sale Type',
    'SaleCondition': 'Sale Condition',
    'SalePrice': 'Sale Price ($)'
}

# Zoning classifications (matching model expectations)
ZONING_OPTIONS = {
    'C': 'Commercial',
    'FV': 'Floating Village Residential',
    'RH': 'Residential High Density',
    'RL': 'Residential Low Density',
    'RM': 'Residential Medium Density'
}

# MSZoning reverse mapping (code to full name)
ZONING_REVERSE = {
    'A (agr)': 'Agriculture',
    'C (all)': 'Commercial',
    'FV': 'Floating Village Residential', 
    'I (all)': 'Industrial',
    'RH': 'Residential High Density',
    'RL': 'Residential Low Density',
    'RM': 'Residential Medium Density'
}

# Neighborhood full names mapping
NEIGHBORHOOD_OPTIONS = {
    'Blmngtn': 'Bloomington Heights',
    'Blueste': 'Bluestem',
    'BrDale': 'Briardale', 
    'BrkSide': 'Brookside',
    'ClearCr': 'Clear Creek',
    'CollgCr': 'College Creek',
    'Crawfor': 'Crawford',
    'Edwards': 'Edwards',
    'Gilbert': 'Gilbert',
    'Greens': 'Greens',
    'GrnHill': 'Green Hills',
    'IDOTRR': 'Iowa DOT and Rail Road',
    'Landmrk': 'Landmark',
    'MeadowV': 'Meadow Village',
    'Mitchel': 'Mitchell',
    'NAmes': 'North Ames',
    'NoRidge': 'Northridge',
    'NPkVill': 'Northpark Villa',
    'NridgHt': 'Northridge Heights',
    'NWAmes': 'Northwest Ames',
    'OldTown': 'Old Town',
    'SWISU': 'South & West of Iowa State University',
    'Sawyer': 'Sawyer',
    'SawyerW': 'Sawyer West',
    'Somerst': 'Somerset',
    'StoneBr': 'Stone Brook',
    'Timber': 'Timberland',
    'Veenker': 'Veenker'
}

# Quality ratings
QUALITY_OPTIONS = {
    'Ex': 'Excellent',
    'Gd': 'Good', 
    'TA': 'Typical/Average',
    'Fa': 'Fair',
    'Po': 'Poor',
    'NA': 'No Basement/Garage/Fireplace'
}

# Central Air options
CENTRAL_AIR_OPTIONS = {
    'Y': 'Yes',
    'N': 'No'
}

# Paved Drive options  
PAVED_DRIVE_OPTIONS = {
    'Y': 'Paved',
    'P': 'Partial Pavement', 
    'N': 'Dirt/Gravel'
}

# Building Type options
BUILDING_TYPE_OPTIONS = {
    '1Fam': 'Single-family Detached',
    '2FmCon': 'Two-family Conversion',
    'Duplx': 'Duplex',
    'TwnhsE': 'Townhouse End Unit',
    'TwnhsI': 'Townhouse Inside Unit'
}

# House Style options
HOUSE_STYLE_OPTIONS = {
    '1Story': 'One Story',
    '1.5Fin': 'One and Half Story: 2nd level finished',
    '1.5Unf': 'One and Half Story: 2nd level unfinished',
    '2Story': 'Two Story',
    '2.5Fin': 'Two and Half Story: 2nd level finished',
    '2.5Unf': 'Two and Half Story: 2nd level unfinished',
    'SFoyer': 'Split Foyer',
    'SLvl': 'Split Level'
}

# Roof Style options
ROOF_STYLE_OPTIONS = {
    'Flat': 'Flat',
    'Gable': 'Gable',
    'Gambrel': 'Gambrel (Barn)',
    'Hip': 'Hip',
    'Mansard': 'Mansard',
    'Shed': 'Shed'
}

# Foundation options
FOUNDATION_OPTIONS = {
    'BrkTil': 'Brick & Tile',
    'CBlock': 'Cinder Block',
    'PConc': 'Poured Concrete',
    'Slab': 'Slab',
    'Stone': 'Stone',
    'Wood': 'Wood'
}

# Basement Quality options
BASEMENT_QUALITY_OPTIONS = {
    'Ex': 'Excellent (100+ inches)',
    'Gd': 'Good (90-99 inches)',
    'TA': 'Typical (80-89 inches)',
    'Fa': 'Fair (70-79 inches)',
    'Po': 'Poor (<70 inches)',
    'NA': 'No Basement'
}

# Basement Condition options
BASEMENT_CONDITION_OPTIONS = {
    'Ex': 'Excellent',
    'Gd': 'Good',
    'TA': 'Typical - slight dampness allowed',
    'Fa': 'Fair - dampness or some cracking',
    'Po': 'Poor - severe cracking, settlement, wetness',
    'NA': 'No Basement'
}

# Basement Exposure options
BASEMENT_EXPOSURE_OPTIONS = {
    'Gd': 'Good Exposure',
    'Av': 'Average Exposure',
    'Mn': 'Minimum Exposure',
    'No': 'No Exposure',
    'NA': 'No Basement'
}

# Heating Type options
HEATING_OPTIONS = {
    'Floor': 'Floor Furnace',
    'GasA': 'Gas forced warm air furnace',
    'GasW': 'Gas hot water or steam heat',
    'Grav': 'Gravity furnace',
    'OthW': 'Hot water or steam heat other than gas',
    'Wall': 'Wall furnace'
}

# Electrical options
ELECTRICAL_OPTIONS = {
    'SBrkr': 'Standard Circuit Breakers',
    'FuseA': 'Fuse Box over 60 AMP (Good)',
    'FuseF': 'Fuse Box 60 AMP (Fair)',
    'FuseP': 'Fuse Box under 60 AMP (Poor)',
    'Mix': 'Mixed'
}

# Garage Type options (matching model expectations)
GARAGE_TYPE_OPTIONS = {
    'Attchd': 'Attached to home',
    'BuiltIn': 'Built-In (Garage part of house)',
    'CarPort': 'Car Port',
    'Detchd': 'Detached from home',
    'NA': 'No Garage'
}

# Garage Finish options
GARAGE_FINISH_OPTIONS = {
    'Fin': 'Finished',
    'RFn': 'Rough Finished',
    'Unf': 'Unfinished',
    'NA': 'No Garage'
}

# Sale Type options
SALE_TYPE_OPTIONS = {
    'WD': 'Warranty Deed - Conventional',
    'CWD': 'Warranty Deed - Cash',
    'VWD': 'Warranty Deed - VA Loan',
    'New': 'Home just constructed and sold',
    'COD': 'Court Officer Deed/Estate',
    'Con': 'Contract 15% Down payment regular terms',
    'ConLw': 'Contract Low Down payment and low interest',
    'ConLI': 'Contract Low Interest',
    'ConLD': 'Contract Low Down',
    'Oth': 'Other'
}

# Sale Condition options
SALE_CONDITION_OPTIONS = {
    'Normal': 'Normal Sale',
    'Abnorml': 'Abnormal Sale - trade, foreclosure, short sale',
    'AdjLand': 'Adjoining Land Purchase',
    'Alloca': 'Allocation - two linked properties sold separately',
    'Family': 'Sale between family members',
    'Partial': 'Home was not completed when last assessed'
}

# Functional options
FUNCTIONAL_OPTIONS = {
    'Typ': 'Typical Functionality',
    'Min1': 'Minor Deductions 1',
    'Min2': 'Minor Deductions 2',
    'Mod': 'Moderate Deductions',
    'Maj1': 'Major Deductions 1',
    'Maj2': 'Major Deductions 2',
    'Sev': 'Severely Damaged',
    'Sal': 'Salvage only'
}

def get_feature_mapping() -> dict:
    """Return the feature mapping dictionary"""
    return FEATURE_MAPPING

def get_user_friendly_name(technical_name: str) -> str:
    """Convert technical column name to user-friendly name"""
    return FEATURE_MAPPING.get(technical_name, technical_name)

def get_feature_description(feature: str) -> str:
    """Get description for a feature"""
    descriptions = {
        'MSSubClass': 'The building class identifies the type of dwelling involved in the sale',
        'MSZoning': 'General zoning classification of the sale',
        'OverallQual': 'Overall material and finish quality (1-10 scale)',
        'OverallCond': 'Overall condition rating (1-10 scale)',
        'YearBuilt': 'Original construction date',
        'YearRemodAdd': 'Remodel date (same as construction date if no remodeling)',
        'Neighborhood': 'Physical locations within city limits',
        'BldgType': 'Type of dwelling',
        'HouseStyle': 'Style of dwelling',
        'RoofStyle': 'Type of roof',
        'Foundation': 'Type of foundation',
        'BsmtQual': 'Height of the basement',
        'BsmtCond': 'General condition of the basement',
        'BsmtExposure': 'Walkout or garden level basement walls',
        'HeatingQC': 'Heating quality and condition',
        'CentralAir': 'Central air conditioning',
        'Electrical': 'Electrical system',
        '1stFlrSF': 'First Floor square feet',
        'GrLivArea': 'Above grade (ground) living area square feet',
        'BsmtFullBath': 'Basement full bathrooms',
        'KitchenQual': 'Kitchen quality',
        'Fireplaces': 'Number of fireplaces',
        'FireplaceQu': 'Fireplace quality',
        'GarageType': 'Garage location',
        'GarageFinish': 'Interior finish of the garage',
        'GarageCars': 'Size of garage in car capacity',
        'PavedDrive': 'Paved driveway',
        'SaleCondition': 'Condition of sale'
    }
    return descriptions.get(feature, f'Information about {get_user_friendly_name(feature)}')

def get_all_features_info() -> dict:
    """Get comprehensive information about all features"""
    return {
        'mapping': FEATURE_MAPPING,
        'zoning_options': ZONING_OPTIONS,
        'neighborhood_options': NEIGHBORHOOD_OPTIONS,
        'quality_options': QUALITY_OPTIONS,
        'building_type_options': BUILDING_TYPE_OPTIONS,
        'house_style_options': HOUSE_STYLE_OPTIONS,
        'garage_type_options': GARAGE_TYPE_OPTIONS
    }
    return {
        # Basic Property Information
        'MSSubClass': 'Building Class',
        'MSZoning': 'Zoning Classification',
        'LotFrontage': 'Street Frontage (ft)',
        'LotArea': 'Lot Size (sq ft)',
        'Street': 'Road Access Type',
        'Alley': 'Alley Access',
        'LotShape': 'Property Shape',
        'LandContour': 'Land Flatness',
        'Utilities': 'Available Utilities',
        'LotConfig': 'Lot Configuration',
        'LandSlope': 'Land Slope',
        'Neighborhood': 'Neighborhood',
        
        # Location & Conditions
        'Condition1': 'Main Road/Railroad Proximity',
        'Condition2': 'Secondary Road/Railroad Proximity',
        'BldgType': 'Building Type',
        'HouseStyle': 'House Style',
        
        # Quality & Condition
        'OverallQual': 'Overall Quality (1-10)',
        'OverallCond': 'Overall Condition (1-10)',
        'YearBuilt': 'Year Built',
        'YearRemodAdd': 'Year Remodeled',
        
        # Exterior Features
        'RoofStyle': 'Roof Style',
        'RoofMatl': 'Roof Material',
        'Exterior1st': 'Primary Exterior Material',
        'Exterior2nd': 'Secondary Exterior Material',
        'MasVnrType': 'Masonry Veneer Type',
        'MasVnrArea': 'Masonry Veneer Area (sq ft)',
        'ExterQual': 'Exterior Quality',
        'ExterCond': 'Exterior Condition',
        'Foundation': 'Foundation Type',
        
        # Basement Features
        'BsmtQual': 'Basement Height',
        'BsmtCond': 'Basement Condition',
        'BsmtExposure': 'Basement Exposure',
        'BsmtFinType1': 'Basement Finished Area 1 Quality',
        'BsmtFinSF1': 'Basement Finished Area 1 (sq ft)',
        'BsmtFinType2': 'Basement Finished Area 2 Quality',
        'BsmtFinSF2': 'Basement Finished Area 2 (sq ft)',
        'BsmtUnfSF': 'Unfinished Basement Area (sq ft)',
        'TotalBsmtSF': 'Total Basement Area (sq ft)',
        
        # Heating & Electrical
        'Heating': 'Heating Type',
        'HeatingQC': 'Heating Quality',
        'CentralAir': 'Central Air Conditioning',
        'Electrical': 'Electrical System',
        
        # Living Areas
        '1stFlrSF': 'First Floor Area (sq ft)',
        '2ndFlrSF': 'Second Floor Area (sq ft)',
        'LowQualFinSF': 'Low Quality Finished Area (sq ft)',
        'GrLivArea': 'Above Ground Living Area (sq ft)',
        
        # Bathrooms & Bedrooms
        'BsmtFullBath': 'Basement Full Bathrooms',
        'BsmtHalfBath': 'Basement Half Bathrooms',
        'FullBath': 'Full Bathrooms Above Grade',
        'HalfBath': 'Half Bathrooms Above Grade',
        'BedroomAbvGr': 'Bedrooms Above Ground',
        'KitchenAbvGr': 'Kitchens Above Ground',
        'KitchenQual': 'Kitchen Quality',
        'TotRmsAbvGrd': 'Total Rooms Above Ground',
        'Functional': 'Home Functionality',
        
        # Additional Features
        'Fireplaces': 'Number of Fireplaces',
        'FireplaceQu': 'Fireplace Quality',
        'GarageType': 'Garage Type',
        'GarageYrBlt': 'Garage Year Built',
        'GarageFinish': 'Garage Interior Finish',
        'GarageCars': 'Garage Car Capacity',
        'GarageArea': 'Garage Area (sq ft)',
        'GarageQual': 'Garage Quality',
        'GarageCond': 'Garage Condition',
        'PavedDrive': 'Paved Driveway',
        
        # Outdoor Features
        'WoodDeckSF': 'Wood Deck Area (sq ft)',
        'OpenPorchSF': 'Open Porch Area (sq ft)',
        'EnclosedPorch': 'Enclosed Porch Area (sq ft)',
        '3SsnPorch': 'Three Season Porch Area (sq ft)',
        'ScreenPorch': 'Screen Porch Area (sq ft)',
        'PoolArea': 'Pool Area (sq ft)',
        'PoolQC': 'Pool Quality',
        'Fence': 'Fence Quality',
        'MiscFeature': 'Miscellaneous Feature',
        'MiscVal': 'Miscellaneous Feature Value ($)',
        
        # Sale Information
        'MoSold': 'Month Sold',
        'YrSold': 'Year Sold',
        'SaleType': 'Sale Type',
        'SaleCondition': 'Sale Condition',
        'SalePrice': 'Sale Price ($)'
    }


def get_feature_descriptions() -> Dict[str, str]:
    """Get detailed descriptions for each feature"""
    return {
        'MSSubClass': 'Identifies the type of dwelling involved in the sale (20: 1-Story 1946 & newer, 30: 1-Story 1945 & older, 40: 1-Story w/finished attic, 45: 1.5-Story unfinished, 50: 1.5-Story finished, 60: 2-Story 1946 & newer, 70: 2-Story 1945 & older, 75: 2.5-Story all ages, 80: Split or multi-level, 85: Split foyer, 90: Duplex, 120: 1-Story PUD, 150: 1.5-Story PUD, 160: 2-Story PUD, 180: PUD multilevel, 190: 2-Family conversion)',
        
        'MSZoning': 'Identifies the general zoning classification of the sale',
        
        'LotFrontage': 'Linear feet of street connected to property',
        
        'LotArea': 'Lot size in square feet',
        
        'Street': 'Type of road access to property',
        
        'Alley': 'Type of alley access to property',
        
        'LotShape': 'General shape of property',
        
        'LandContour': 'Flatness of the property',
        
        'Utilities': 'Type of utilities available',
        
        'LotConfig': 'Lot configuration',
        
        'LandSlope': 'Slope of property',
        
        'Neighborhood': 'Physical locations within Ames city limits',
        
        'Condition1': 'Proximity to various conditions (arterial street, railroad, park, etc.)',
        
        'Condition2': 'Proximity to various conditions (if more than one is present)',
        
        'BldgType': 'Type of dwelling',
        
        'HouseStyle': 'Style of dwelling',
        
        'OverallQual': 'Rates the overall material and finish of the house (1: Very Poor, 2: Poor, 3: Fair, 4: Below Average, 5: Average, 6: Above Average, 7: Good, 8: Very Good, 9: Excellent, 10: Very Excellent)',
        
        'OverallCond': 'Rates the overall condition of the house (1: Very Poor, 2: Poor, 3: Fair, 4: Below Average, 5: Average, 6: Above Average, 7: Good, 8: Very Good, 9: Excellent, 10: Very Excellent)',
        
        'YearBuilt': 'Original construction date',
        
        'YearRemodAdd': 'Remodel date (same as construction date if no remodeling or additions)',
        
        'RoofStyle': 'Type of roof',
        
        'RoofMatl': 'Roof material',
        
        'Exterior1st': 'Exterior covering on house',
        
        'Exterior2nd': 'Exterior covering on house (if more than one material)',
        
        'MasVnrType': 'Masonry veneer type',
        
        'MasVnrArea': 'Masonry veneer area in square feet',
        
        'ExterQual': 'Evaluates the quality of the material on the exterior',
        
        'ExterCond': 'Evaluates the present condition of the material on the exterior',
        
        'Foundation': 'Type of foundation',
        
        'BsmtQual': 'Evaluates the height of the basement',
        
        'BsmtCond': 'Evaluates the general condition of the basement',
        
        'BsmtExposure': 'Refers to walkout or garden level walls',
        
        'BsmtFinType1': 'Rating of basement finished area',
        
        'BsmtFinSF1': 'Type 1 finished square feet',
        
        'BsmtFinType2': 'Rating of basement finished area (if multiple types)',
        
        'BsmtFinSF2': 'Type 2 finished square feet',
        
        'BsmtUnfSF': 'Unfinished square feet of basement area',
        
        'TotalBsmtSF': 'Total square feet of basement area',
        
        'Heating': 'Type of heating',
        
        'HeatingQC': 'Heating quality and condition',
        
        'CentralAir': 'Central air conditioning',
        
        'Electrical': 'Electrical system',
        
        '1stFlrSF': 'First Floor square feet',
        
        '2ndFlrSF': 'Second floor square feet',
        
        'LowQualFinSF': 'Low quality finished square feet (all floors)',
        
        'GrLivArea': 'Above grade (ground) living area square feet',
        
        'BsmtFullBath': 'Basement full bathrooms',
        
        'BsmtHalfBath': 'Basement half bathrooms',
        
        'FullBath': 'Full bathrooms above grade',
        
        'HalfBath': 'Half baths above grade',
        
        'BedroomAbvGr': 'Bedrooms above grade (does NOT include basement bedrooms)',
        
        'KitchenAbvGr': 'Kitchens above grade',
        
        'KitchenQual': 'Kitchen quality',
        
        'TotRmsAbvGrd': 'Total rooms above grade (does not include bathrooms)',
        
        'Functional': 'Home functionality (Assume typical unless deductions are warranted)',
        
        'Fireplaces': 'Number of fireplaces',
        
        'FireplaceQu': 'Fireplace quality',
        
        'GarageType': 'Garage location',
        
        'GarageYrBlt': 'Year garage was built',
        
        'GarageFinish': 'Interior finish of the garage',
        
        'GarageCars': 'Size of garage in car capacity',
        
        'GarageArea': 'Size of garage in square feet',
        
        'GarageQual': 'Garage quality',
        
        'GarageCond': 'Garage condition',
        
        'PavedDrive': 'Paved driveway',
        
        'WoodDeckSF': 'Wood deck area in square feet',
        
        'OpenPorchSF': 'Open porch area in square feet',
        
        'EnclosedPorch': 'Enclosed porch area in square feet',
        
        '3SsnPorch': 'Three season porch area in square feet',
        
        'ScreenPorch': 'Screen porch area in square feet',
        
        'PoolArea': 'Pool area in square feet',
        
        'PoolQC': 'Pool quality',
        
        'Fence': 'Fence quality',
        
        'MiscFeature': 'Miscellaneous feature not covered in other categories',
        
        'MiscVal': '$Value of miscellaneous feature',
        
        'MoSold': 'Month Sold (MM)',
        
        'YrSold': 'Year Sold (YYYY)',
        
        'SaleType': 'Type of sale',
        
        'SaleCondition': 'Condition of sale',
        
        'SalePrice': 'Sale price in dollars'
    }


def get_categorical_options() -> Dict[str, List[str]]:
    """Get available options for categorical features"""
    return {
        'MSZoning': ['A', 'C', 'FV', 'I', 'RH', 'RL', 'RP', 'RM'],
        'Street': ['Grvl', 'Pave'],
        'Alley': ['Grvl', 'Pave', 'NA'],
        'LotShape': ['Reg', 'IR1', 'IR2', 'IR3'],
        'LandContour': ['Lvl', 'Bnk', 'HLS', 'Low'],
        'Utilities': ['AllPub', 'NoSewr', 'NoSeWa', 'ELO'],
        'LotConfig': ['Inside', 'Corner', 'CulDSac', 'FR2', 'FR3'],
        'LandSlope': ['Gtl', 'Mod', 'Sev'],
        'BldgType': ['1Fam', '2FmCon', 'Duplx', 'TwnhsE', 'TwnhsI'],
        'HouseStyle': ['1Story', '1.5Fin', '1.5Unf', '2Story', '2.5Fin', '2.5Unf', 'SFoyer', 'SLvl'],
        'RoofStyle': ['Flat', 'Gable', 'Gambrel', 'Hip', 'Mansard', 'Shed'],
        'RoofMatl': ['ClyTile', 'CompShg', 'Membran', 'Metal', 'Roll', 'Tar&Grv', 'WdShake', 'WdShngl'],
        'ExterQual': ['Ex', 'Gd', 'TA', 'Fa', 'Po'],
        'ExterCond': ['Ex', 'Gd', 'TA', 'Fa', 'Po'],
        'Foundation': ['BrkTil', 'CBlock', 'PConc', 'Slab', 'Stone', 'Wood'],
        'BsmtQual': ['Ex', 'Gd', 'TA', 'Fa', 'Po', 'NA'],
        'BsmtCond': ['Ex', 'Gd', 'TA', 'Fa', 'Po', 'NA'],
        'BsmtExposure': ['Gd', 'Av', 'Mn', 'No', 'NA'],
        'BsmtFinType1': ['GLQ', 'ALQ', 'BLQ', 'Rec', 'LwQ', 'Unf', 'NA'],
        'BsmtFinType2': ['GLQ', 'ALQ', 'BLQ', 'Rec', 'LwQ', 'Unf', 'NA'],
        'Heating': ['Floor', 'GasA', 'GasW', 'Grav', 'OthW', 'Wall'],
        'HeatingQC': ['Ex', 'Gd', 'TA', 'Fa', 'Po'],
        'CentralAir': ['N', 'Y'],
        'Electrical': ['SBrkr', 'FuseA', 'FuseF', 'FuseP', 'Mix'],
        'KitchenQual': ['Ex', 'Gd', 'TA', 'Fa', 'Po'],
        'Functional': ['Typ', 'Min1', 'Min2', 'Mod', 'Maj1', 'Maj2', 'Sev', 'Sal'],
        'FireplaceQu': ['Ex', 'Gd', 'TA', 'Fa', 'Po', 'NA'],
        'GarageType': ['2Types', 'Attchd', 'Basment', 'BuiltIn', 'CarPort', 'Detchd', 'NA'],
        'GarageFinish': ['Fin', 'RFn', 'Unf', 'NA'],
        'GarageQual': ['Ex', 'Gd', 'TA', 'Fa', 'Po', 'NA'],
        'GarageCond': ['Ex', 'Gd', 'TA', 'Fa', 'Po', 'NA'],
        'PavedDrive': ['Y', 'P', 'N'],
        'PoolQC': ['Ex', 'Gd', 'TA', 'Fa', 'NA'],
        'Fence': ['GdPrv', 'MnPrv', 'GdWo', 'MnWw', 'NA'],
        'SaleType': ['WD', 'CWD', 'VWD', 'New', 'COD', 'Con', 'ConLw', 'ConLI', 'ConLD', 'Oth'],
        'SaleCondition': ['Normal', 'Abnorml', 'AdjLand', 'Alloca', 'Family', 'Partial']
    }


def get_quality_scale_explanation() -> Dict[str, str]:
    """Get explanations for quality scales used in the dataset"""
    return {
        'OverallQual_OverallCond': '10: Very Excellent, 9: Excellent, 8: Very Good, 7: Good, 6: Above Average, 5: Average, 4: Below Average, 3: Fair, 2: Poor, 1: Very Poor',
        'ExterQual_ExterCond_HeatingQC_KitchenQual_FireplaceQu_GarageQual_GarageCond_PoolQC': 'Ex: Excellent, Gd: Good, TA: Typical/Average, Fa: Fair, Po: Poor',
        'BsmtQual': 'Ex: Excellent (100+ inches), Gd: Good (90-99 inches), TA: Typical (80-89 inches), Fa: Fair (70-79 inches), Po: Poor (<70 inches), NA: No Basement',
        'BsmtCond': 'Ex: Excellent, Gd: Good, TA: Typical - slight dampness allowed, Fa: Fair - dampness or some cracking, Po: Poor - Severe cracking, settling, or wetness, NA: No Basement',
        'BsmtExposure': 'Gd: Good Exposure, Av: Average Exposure, Mn: Minimum Exposure, No: No Exposure, NA: No Basement',
        'BsmtFinType1_BsmtFinType2': 'GLQ: Good Living Quarters, ALQ: Average Living Quarters, BLQ: Below Average Living Quarters, Rec: Average Rec Room, LwQ: Low Quality, Unf: Unfinshed, NA: No Basement',
        'Functional': 'Typ: Typical Functionality, Min1: Minor Deductions 1, Min2: Minor Deductions 2, Mod: Moderate Deductions, Maj1: Major Deductions 1, Maj2: Major Deductions 2, Sev: Severely Damaged, Sal: Salvage only'
    }


def get_user_friendly_name(column_name: str) -> str:
    """Get user-friendly name for a column"""
    mapping = get_feature_mapping()
    return mapping.get(column_name, column_name)


def get_feature_explanation(column_name: str) -> str:
    """Get detailed explanation for a feature"""
    descriptions = get_feature_descriptions()
    return descriptions.get(column_name, f"Feature: {column_name}")


def get_important_features() -> List[str]:
    """Get list of most important features for prediction"""
    return [
        'OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea', 'TotalBsmtSF',
        '1stFlrSF', 'FullBath', 'TotRmsAbvGrd', 'YearBuilt', 'YearRemodAdd',
        'GarageYrBlt', 'MasVnrArea', 'Fireplaces', 'BsmtFinSF1', 'LotFrontage',
        'WoodDeckSF', '2ndFlrSF', 'OpenPorchSF', 'HalfBath', 'LotArea',
        'BsmtFullBath', 'BsmtUnfSF', 'BedroomAbvGr', 'ScreenPorch', 'PoolArea'
    ]


def get_feature_categories() -> Dict[str, List[str]]:
    """Group features into logical categories"""
    return {
        'Basic Property Info': [
            'MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'Street', 'Alley',
            'LotShape', 'LandContour', 'Utilities', 'LotConfig', 'LandSlope', 'Neighborhood'
        ],
        'Building Details': [
            'BldgType', 'HouseStyle', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd'
        ],
        'Exterior Features': [
            'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType', 'MasVnrArea',
            'ExterQual', 'ExterCond', 'Foundation'
        ],
        'Basement Features': [
            'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1',
            'BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF'
        ],
        'Heating & Electrical': [
            'Heating', 'HeatingQC', 'CentralAir', 'Electrical'
        ],
        'Living Areas': [
            '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea'
        ],
        'Rooms & Bathrooms': [
            'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr',
            'KitchenAbvGr', 'KitchenQual', 'TotRmsAbvGrd', 'Functional'
        ],
        'Additional Features': [
            'Fireplaces', 'FireplaceQu'
        ],
        'Garage Features': [
            'GarageType', 'GarageYrBlt', 'GarageFinish', 'GarageCars', 'GarageArea',
            'GarageQual', 'GarageCond', 'PavedDrive'
        ],
        'Outdoor Features': [
            'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch',
            'PoolArea', 'PoolQC', 'Fence', 'MiscFeature', 'MiscVal'
        ],
        'Sale Information': [
            'MoSold', 'YrSold', 'SaleType', 'SaleCondition'
        ]
    }
