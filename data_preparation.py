import pandas as pd

# Read excel or CSV and display basic info
def load_dataframe ( path, verbose=True ) :

    # Read CSV or Excel file
    if ( path.endswith ( ".csv" ) ) :
        df = pd.read_csv( path, sep=';')
    elif ( path.endswith ( ".xlsx" ) ) :
        df = pd.read_excel ( path )

    # If verbose, display basic info
    if ( verbose ) :
        print("Number of rows:", len(df))
        print("Number of columns:", len(df.columns))
        print("Column names:", df.columns)
        print("Infos of dataframe")
        df.info( verbose=True, show_counts=True)
    return df


# Extract useful columns 
def extract_columns ( df, useful_cols, verbose = True ) :
    # Extract useful columns 
    df = df[useful_cols]
    df.infer_objects()

    # Drop rows with missing values
    #df = df.dropna()
    #df = df.reset_index ( drop = True )
    
    # Display if required
    if ( verbose ) :
        df.info( verbose = True, show_counts = True )
    return df

# Extract the rows of the dataframe that correspond to the filter given by (symbole, value)
def subdataframe ( df, col, symbole, value ) :
    if ( symbole == "==" ) :
        sub = df [ df [ col ] == value ] 
        sub = sub.reset_index ( drop = True )
        return sub
    elif ( symbole == "!=" ) :
        sub = df [ df [ col ] != value ] 
        sub = sub.reset_index ( drop = True )
        return sub
    elif ( symbole == "<" ) :
        sub = df [ df [ col ] < value ] 
        sub = sub.reset_index ( drop = True )
        return sub
    elif ( symbole == "<=" ) :
        sub = df [ df [ col ] <= value ] 
        sub = sub.reset_index ( drop = True )
        return sub
    elif ( symbole == ">" ) :
        sub = df [ df [ col ] > value ] 
        sub = sub.reset_index ( drop = True )
        return sub
    elif ( symbole == ">=" ) :
        sub = df [ df [ col ] >= value ] 
        sub = sub.reset_index ( drop = True )
        return sub
    
    else :
        print ( "Error, unknown symbole :", symbole )
        return None

# Display dataframe full description
def full_description ( df ) :
    for col in df.columns :
        print()
        print ( "*****", col, "*****" )
        print ( df[col].describe() )

# Merge a list of dataframes among a common column
def merge_dataframes ( df_list, suffixes, on ) :

    # Rename the columns of every column that are not the join to avoid duplicates
    for i in range ( len ( df_list ) ) :
        dict = {}
        for col in df_list[i].columns :
            if col != on :
                dict[col] = col + "_" + suffixes[i]
        df_list[i] = df_list[i].rename ( columns = dict )
    
    # Merge the dataframe along the "on" column
    res = df_list[0]
    for i in range ( 1, len(df_list) ) :
        res = pd.merge ( res, df_list[i], on=on, suffixes=( None, "_" + suffixes[i]) ) 
    return res