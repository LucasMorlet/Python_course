# My Python files
import data_preparation as prep
import data_visualization as viz
import correlation as corr

# Standard libraries
import pandas as pd
import matplotlib as mpl

df = prep.load_dataframe ( "data/burgundy_2023.csv", True )
df = prep.extract_columns ( df, [ "NUM_POSTE", "NOM_USUEL", "LAT", "LON", "ALTI", "AAAAMMJJHH", "T", "RR1", "U", "DG" ], True )

cities = df["NOM_USUEL"].unique()
print ( cities )
subdataframes = {}
for city in cities :
    subdataframes[city] = prep.subdataframe ( df, "NOM_USUEL", "==", city )
    subdataframes[city]["AAAAMMJJHH"] = pd.to_datetime(subdataframes[city]["AAAAMMJJHH"], format="%Y%m%d%H")

#prep.full_description ( subdataframes["DIJON"] )
df_extended = prep.merge_dataframes ( list(subdataframes.values()), list(subdataframes.keys()), "AAAAMMJJHH")
prep.full_description ( df_extended )
viz.display_curves ( df_extended[df_extended["AAAAMMJJHH"] <= pd.to_datetime("2023-02-01") ], "AAAAMMJJHH", ["T_DIJON", "T_NEVERS-MARZY", "T_MACON", "T_AUXERRE-PERRIGNY"], ["Dijon", "Nevers", "Macon", "Auxerre"], mpl.colormaps['tab10'].colors[:4], "Date", "Temperature", "Temperature in January 2023" )
viz.display_curves ( df_extended, "AAAAMMJJHH", ["T_DIJON", "T_NEVERS-MARZY", "T_MACON", "T_AUXERRE-PERRIGNY"], ["Dijon", "Nevers", "Macon", "Auxerre"], mpl.colormaps['tab10'].colors[:4], "Date", "Temperature", "Temperature in 2023" )


correlation_matrix = corr.correlation_matrix ( df_extended, 0.8 )
#viz.display_correlation_matrix ( correlation_matrix )

'''for i in range ( len ( correlation_matrix.columns ) ) :
    for j in range ( i+1, len ( correlation_matrix.columns ) ) :
        fit = corr.fitting ( df_extended, correlation_matrix.columns[i], correlation_matrix.columns[j], 1 ) 
        viz.display_points_cloud ( df_extended, correlation_matrix.columns[i], correlation_matrix.columns[j], correlation_matrix.columns[i], correlation_matrix.columns[j], "Title", fit )
'''

print(df.info())
print(df_extended.info())