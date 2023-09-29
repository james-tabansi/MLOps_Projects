import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


# Defining the function for creating boxplot and hisogram 
def histogram_boxplot(data, feature, figsize=(9, 5), kde=False, bins=None):
    """
    Boxplot and histogram combined

    data: dataframe
    feature: dataframe column
    figsize: size of figure (default (12,7))
    kde: whether to show the density curve (default False)
    bins: number of bins for histogram (default None)
    """
    f2, (ax_box2, ax_hist2) = plt.subplots(
        nrows=2,  # Number of rows of the subplot grid= 2
        sharex=True,  # x-axis will be shared among all subplots
        gridspec_kw={"height_ratios": (0.25, 0.75)},
        figsize=figsize)  # creating the 2 subplots
    
    sns.boxplot(data=data, x=feature, ax=ax_box2, showmeans=True, color="mediumturquoise")  # boxplot will be created and a star will indicate the mean value of the column
    
    if bins:
      sns.histplot(data=data, x=feature, kde=kde, ax=ax_hist2, bins=bins, color="mediumpurple")
    else: 
      sns.histplot(data=data, x=feature, kde=kde, ax=ax_hist2, color="mediumpurple")  # For histogram
    
    ax_hist2.axvline(data[feature].mean(), color="green", linestyle="--")  # Add mean to the histogram
    
    ax_hist2.axvline(data[feature].median(), color="black", linestyle="-")  # Add median to the histogram
    


# function to create labeled barplots

def labeled_barplot(data, feature, perc=False, n=None):
    """
    Barplot with percentage at the top

    data: dataframe
    feature: dataframe column
    perc: whether to display percentages instead of count (default is False)
    n: displays the top n category levels (default is None, i.e., display all levels)
    """

    total = len(data[feature])  # length of the column
    count = data[feature].nunique()
    if n is None:
        plt.figure(figsize=(count + 1, 5))
    else:
        plt.figure(figsize=(n + 1, 5))

    plt.xticks(rotation=90, fontsize=15)
    ax = sns.countplot(
        data=data,
        x=feature,
        palette="Paired",
        order=data[feature].value_counts().index[:n].sort_values(),
    )

    for p in ax.patches:
        if perc == True:
            label = "{:.1f}%".format(
                100 * p.get_height() / total
            )  # percentage of each class of the category
        else:
            label = p.get_height()  # count of each level of the category

        x = p.get_x() + p.get_width() / 2  # width of the plot
        y = p.get_height()  # height of the plot

        ax.annotate(
            label,
            (x, y),
            ha="center",
            va="center",
            size=12,
            xytext=(0, 5),
            textcoords="offset points",
        )  # annotate the percentage

    plt.show()  # show the plot
    
    
    
def labeled_barplot_hue(data, feature, hue, perc=False,n=None):
  """ this function will plot a labelled count plot for the feature
  data:dataframe
  feature: column
  perc: boolean, percentage value to be displayed
  n: int, display top n category
  hue: hue
  """

  total = len(data[feature])
  count= data[feature].nunique()

  if n is None:
    plt.figure(figsize=(count+2, 6))
  else:
    plt.figure(figsize=(n+3, 6))

    plt.title(feature + " countplot")

    plt.xticks(rotation=90, fontsize=15)
    plt.yticks(fontsize=15)
    
  ax = sns.countplot(
                data=data,
                x=feature,
                order = data[feature].value_counts().index[:n].sort_values(), hue=hue,
            palette="Paired")
  
  for a,i in enumerate(ax.patches):
    if perc == True: #if percentage is true
      label = "{:.1f}%".format(#display the format as 2 digits after the dot
       (i.get_height()/ total) * 100) #convert the height value to percentage
    else:
      label = i.get_height() #if perc is false display on height value

    x = i.get_x() + i.get_width() / 2  # width of the plot
    y = i.get_height()  # height of the plot 

    ax.annotate(text=label, xy=(x, y), #display label on cordinates x_ax, y
                            va="center", ha="center", #align it to the center of both vertical and horizontal axis
                            xytext = (0,5), #gap between the text relative to the bars
                            textcoords="offset points")
    plt.show()
