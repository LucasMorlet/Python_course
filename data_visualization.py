import pandas as pd
import matplotlib.pyplot as plt

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
def display_correlation_matrix ( df ) :
    corr = df.corr()
    plt.matshow ( corr, cmap="bwr", vmin = -1, vmax = 1 )
    plt.xticks ( range ( len(df.columns) ), df.columns, rotation = 90, ha = "left" )
    plt.yticks ( range ( len(df.columns) ), df.columns )
    plt.colorbar()
    plt.show()
