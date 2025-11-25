import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# Display a list of curves from the same dataframe
def display_curves ( df, x_name, Y_names, labels, colors, xlabel, ylabel, title ) :
    # Check coherency of passed lists
    if ( len(Y_names) != len(labels) or len(Y_names) != len(colors) ) :
        print ( "Lengths are not compatible :", len(Y_names), len(labels), len(colors) )
        return
    
    for i in range ( len (Y_names) ) :
        plt.plot( df[x_name], df[Y_names[i]], label=labels[i], color=colors[i] )

    plt.xlabel(xlabel)  
    plt.ylabel(ylabel)
    plt.title(title)  
    plt.legend()
    plt.show()

# Display the point cloud of two series from the same dataframe
def display_points_cloud ( df, x_name, y_name, xlabel, ylabel, title, fit = None ) :
    plt.plot ( df[x_name], df[y_name], marker = '.', markersize = 2.0, linestyle = "", color = "tab:blue" )
    if not fit is None :
        x_sort = df[x_name].to_list()
        x_sort.sort()
        plt.plot ( x_sort, fit(x_sort), linestyle = "-", color = "tab:orange" )
    plt.xlabel(xlabel)  
    plt.ylabel(ylabel)
    plt.title(title)  
    plt.show()

# Display the correlation matrix of a dataframe
def display_correlation_matrix ( df, title = "Correlation matrix" ) :

    heatmap = sns.heatmap( df.corr(), vmin=-1, vmax=1, annot=True, cmap="bwr", fmt=".2f" )
    plt.title ( title )
    plt.show()

    '''
            #corr.style.background_gradient(cmap='coolwarm').set_precision(2)
    plt.matshow ( corr, cmap="bwr", vmin = -1, vmax = 1 )
    plt.xticks ( range ( len(df.columns) ), df.columns, rotation = 90, ha = "left" )
    plt.yticks ( range ( len(df.columns) ), df.columns )
    plt.colorbar()
    plt.show()'''

def display_clustering ( df, x_name, y_name, cluster_col, nb, centers = None ) :

    # Display the clusters
    colors = plt.cm.get_cmap('tab10', nb)
    for i in range ( nb ) :
        subdf = df[ df[cluster_col] == i ]
        plt.plot ( subdf[x_name], subdf[y_name], marker = '.', markersize = 2.0, linestyle = "", color = colors(i), label = "Cluster " + str(i) )

    # Display the centers (if any)
    if not centers is None :
        for i in range ( nb ) :
            plt.plot ( centers[x_name][i], centers[y_name][i], marker = 's', markersize = 5.0, linestyle = "", color = colors(i) )
            plt.plot ( centers[x_name][i], centers[y_name][i], marker = mpl.markers.MarkerStyle('s', fillstyle="none"), markersize = 5.0, linestyle = "", color = "black" )
        #plt.scatter ( centers[x_name], centers[y_name], color = "black", marker = "triangle", size = 10, label = "Centers" )

    plt.xlabel(x_name)  
    plt.ylabel(y_name)
    plt.title("Clustering by " + cluster_col )  
    plt.legend()
    plt.show()
