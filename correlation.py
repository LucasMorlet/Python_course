import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def correlation_coefficient ( df, col1, col2 ) :
    # Extract the two columns and drop rows with missing values
    subdf = df [ [ col1, col2 ] ].dropna()

    # Check if correlation can be computed
    n = len ( subdf )
    if ( n == 0 ) :
        print ( "No data to compute correlation between", col1, "and", col2 )
        return 0.0
    
    if ( max(subdf [ col1 ]) - min(subdf [ col1 ]) < 0.001 ) :
        print ( "Column", col1, "is constant, cannot compute correlation" )
        return 0.0
    
    if ( max(subdf [ col2 ]) - min(subdf [ col2 ]) < 0.001 ) :
        print ( "Column", col2, "is constant, cannot compute correlation" )
        return 0.0
    
    if ( subdf[col1].dtype not in [ np.float64, np.int64 ] ) :
        print ( "Column", col1, "is not numeric, cannot compute correlation" )
        return 0.0
    
    if ( subdf[col2].dtype not in [ np.float64, np.int64 ] ) :
        print ( "Column", col2, "is not numeric, cannot compute correlation" )
        return 0.0
    
    return np.corrcoef ( subdf[col1], subdf[col2] ) [0,1]

def correlated_subdataframe ( df, threshold = 0.0 ) :
    # Remove non-numeric columns
    df = df.select_dtypes(include=['int64', 'float64'])

    # Remove empty or constant columns
    useful_column = []
    for col in df.columns :
        if ( df[col].count() > 0 and (max(df[col]) - min(df[col])) > 0.001 ) :
            useful_column.append ( col )
    df = df[useful_column]

    # Create correlation matrix and keep only the series with at least one correlation above the threshold (in absolute value)
    corr = df.corr()
    useful_column = []
    for col in corr.columns :
        corr[col][col] = 0
        if ( max(corr[col]) >= threshold or min(corr[col]) <= -threshold ) :
            useful_column.append ( col )
    df = df[useful_column]
    return df

def fitting ( df, x_name, y_name, degree, verbose = True ) :
    df = df[ [x_name, y_name] ]
    df = df.dropna()
    coeffs, residual, rank, singular_values, rcond = np.polyfit ( df[x_name], df[y_name], degree, full=True )
    poly = np.poly1d(coeffs)
    if ( verbose ) :
        print ( poly, "/ MAE =", residual[0] / len(df) )
    return poly
