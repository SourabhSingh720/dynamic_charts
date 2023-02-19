import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

x1=[1,2,3,4,5,7]
y1=[10,20,30,40,50,60]
y2=[1,2,3,454,54]
df=pd.DataFrame([x1,y1,y2])
#Wind Speed_km/h	
df_weather=pd.read_csv('Weather Data.csv')

df_weather_int=df_weather.drop(['Date/Time','Weather'],axis=1)

legend_str=None

dict_default=dict(data=None,x=None, y=None,bins=50,title=None,xlabel=None,ylabel=None,color=None,sns_color='RdBu',legend_bool=True,
                explode=None,autopct='%1.1f%%',xlim=None,ylim=None,hue=None,palette=None,xticks=None,yticks=None,color_count='b'
                ,clim=(-1,1),rotate_x=0,save='fig.png')

def lineplot_seaborn(dict):
  fig=sns.lineplot(data=dict_default['data'], x=dict_default['x'], y=dict_default['y'], hue=dict_default['hue'],color=dict_default['color'],
                              legend=dict_default['legend_bool'],palette=dict_default['palette'])
  fig.set_title(dict_default['title'])  
  fig.set_xlabel(dict_default['xlabel'])
  fig.set_ylabel(dict_default['ylabel'])
  plt.xticks(dict_default['xticks'],rotation=dict_default['rotate_x'])
  plt.yticks(dict_default['yticks'])   
  fig.set_xlim(dict_default['xlim'])
  fig.set_ylim(dict_default['ylim'])
  plt.savefig(dict_default['save'])

def barplot_seaborn(dict):
  fig=sns.barplot(data=dict_default['data'], x=dict_default['x'], y=dict_default['y'], hue=dict_default['hue'],color=dict_default['color'],palette=dict_default['palette'])
  fig.set_title(dict_default['title'])  
  fig.set_xlabel(dict_default['xlabel'])
  fig.set_ylabel(dict_default['ylabel'])
  plt.xticks(dict_default['xticks'],rotation=dict_default['rotate_x'])
  plt.yticks(dict_default['yticks'])   
  fig.set_xlim(dict_default['xlim'])
  fig.set_ylim(dict_default['ylim'])
  plt.savefig(dict_default['save'])

def histogram_seaborn(dict):
  fig=sns.histplot(data=dict_default['data'], x=dict_default['x'], y=dict_default['y'], hue=dict_default['hue'], bins=dict_default['bins'],color=dict_default['color'],
                            legend=dict_default['legend_bool'],palette=dict_default['palette'])
  fig.set_title(dict_default['title'])  
  fig.set_xlabel(dict_default['xlabel'])
  fig.set_ylabel(dict_default['ylabel'])
  plt.xticks(dict_default['xticks'],rotation=dict_default['rotate_x'])
  plt.yticks(dict_default['yticks'])   
  fig.set_xlim(dict_default['xlim'])
  fig.set_ylim(dict_default['ylim'])
  plt.savefig(dict_default['save'])

def scatterplot_seaborn(dict):
  fig=sns.scatterplot(data=dict_default['data'], x=dict_default['x'], y=dict_default['y'], hue=dict_default['hue'],color=dict_default['color'],
                        legend=dict_default['legend_bool'],palette=dict_default['palette'])
  fig.set_title(dict_default['title'])  
  fig.set_xlabel(dict_default['xlabel'])
  fig.set_ylabel(dict_default['ylabel'])
  plt.xticks(dict_default['xticks'],rotation=dict_default['rotate_x'])
  plt.yticks(dict_default['yticks'])   
  fig.set_xlim(dict_default['xlim'])
  fig.set_ylim(dict_default['ylim'])
  plt.savefig(dict_default['save'])

def piechart_seaborn(dict):
  fig=dict_default['data'].plot(x=dict_default['x'], y=dict_default['y'],autopct=dict_default['autopct'],kind='pie',legend=dict_default['legend_bool'],
                 colors=sns.color_palette(dict_default['sns_color']))
  fig.set_title(dict_default['title'])  
  fig.set_xlabel(dict_default['xlabel'])
  fig.set_ylabel(dict_default['ylabel'])
  plt.xticks(dict_default['xticks'],rotation=dict_default['rotate_x'])
  plt.yticks(dict_default['yticks'])   
  fig.set_xlim(dict_default['xlim'])
  fig.set_ylim(dict_default['ylim'])
  plt.savefig(dict_default['save'])

def heatmap_seaborn(dict):
  fig=sns.heatmap(data=dict_default['data'].corr(),annot=True)
  plt.xticks(dict_default['xticks'],rotation=dict_default['rotate_x'])
  plt.yticks(dict_default['yticks'])   
  fig.set_xlim(dict_default['xlim'])
  fig.set_ylim(dict_default['ylim'])
  plt.savefig(dict_default['save'])

def countplot_seaborn(dict):
  fig=sns.countplot(data=dict_default['data'],x=dict_default['x'], hue=dict_default['hue'],color=dict_default['color'],
                     palette=dict_default['palette'])
  fig.set_title(dict_default['title'])  
  fig.set_xlabel(dict_default['xlabel'])
  fig.set_ylabel(dict_default['ylabel'])
  plt.xticks(dict_default['xticks'],rotation=dict_default['rotate_x'])
  plt.yticks(dict_default['yticks'])   
  fig.set_xlim(dict_default['xlim'])
  fig.set_ylim(dict_default['ylim'])
  plt.savefig(dict_default['save'])

def lineplot_matplotlib(dict):
  fig=plt.plot(dict_default['data'][dict_default['x']],dict_default['data'][dict_default['y']],color=dict_default['color']) 
  plt.title(dict_default['title'])
  plt.xlabel(dict_default['xlabel'])
  plt.ylabel(dict_default['ylabel'])
  plt.xlim(dict_default['xlim'])
  plt.ylim(dict_default['ylim'])
  plt.xticks(dict_default['xticks'],rotation=dict_default['rotate_x'])
  plt.yticks(dict_default['yticks'])          
  plt.savefig(dict_default['save'])

def histogram_matplotlib(dict):
  fig=plt.hist(dict_default['data'][dict_default['x']],bins=dict_default['bins'],color=dict_default['color'])
  plt.title(dict_default['title'])
  plt.xlabel(dict_default['xlabel'])
  plt.ylabel(dict_default['ylabel'])
  plt.xlim(dict_default['xlim'])
  plt.ylim(dict_default['ylim'])
  plt.xticks(dict_default['xticks'],rotation=dict_default['rotate_x'])
  plt.yticks(dict_default['yticks'])          
  plt.savefig(dict_default['save'])

def piechart_matplotlib(dict,data,x):
  fig=plt.pie(data[x],colors=dict_default['color'],autopct=dict_default['autopct'])
  plt.title(dict_default['title'])
  plt.xlabel(dict_default['xlabel'])
  plt.ylabel(dict_default['ylabel'])
  plt.xlim(dict_default['xlim'])
  plt.ylim(dict_default['ylim'])
  plt.xticks(dict_default['xticks'],rotation=dict_default['rotate_x'])
  plt.yticks(dict_default['yticks'])          
  plt.savefig(dict_default['save'])

def barplot_matplotlib(dict):
  fig=plt.bar(dict_default['data'][dict_default['x']],dict_default['data'][dict_default['y']],color=dict_default['color'])
  plt.title(dict_default['title'])
  plt.xlabel(dict_default['xlabel'])
  plt.ylabel(dict_default['ylabel'])
  plt.xlim(dict_default['xlim'])
  plt.ylim(dict_default['ylim'])
  plt.xticks(dict_default['xticks'],rotation=dict_default['rotate_x'])
  plt.yticks(dict_default['yticks'])          
  plt.savefig(dict_default['save'])

def countplot_matplotlib(dict):
  fig=dict_default['data'].count().plot(kind='bar',color=dict_default['color_count']) 
  plt.title(dict_default['title'])
  plt.xlabel(dict_default['xlabel'])
  plt.ylabel(dict_default['ylabel'])
  plt.xlim(dict_default['xlim'])
  plt.ylim(dict_default['ylim'])
  plt.xticks(dict_default['xticks'],rotation=dict_default['rotate_x'])
  plt.yticks(dict_default['yticks'])          
  plt.savefig(dict_default['save'])

def heatmap_matplotlib(dict):
  fig=plt.imshow( dict_default['data'] , cmap = dict_default['sns_color'] , interpolation = 'nearest' )
  plt.colorbar()
  plt.clim(dict_default['clim']) 
  plt.title(dict_default['title'])
  plt.xlabel(dict_default['xlabel'])
  plt.ylabel(dict_default['ylabel'])
  plt.xlim(dict_default['xlim'])
  plt.ylim(dict_default['ylim'])
  plt.xticks(dict_default['xticks'],rotation=dict_default['rotate_x'])
  plt.yticks(dict_default['yticks'])          
  plt.savefig(dict_default['save'])

def scatterplot_matplotlib(dict,data,x,y):
  fig=plt.scatter(data[x],data[y],color=dict_default['color'])
  plt.title(dict_default['title'])
  plt.xlabel(dict_default['xlabel'])
  plt.ylabel(dict_default['ylabel'])
  plt.xlim(dict_default['xlim'])
  plt.ylim(dict_default['ylim'])
  plt.xticks(dict_default['xticks'],rotation=dict_default['rotate_x'])
  plt.yticks(dict_default['yticks'])          
  plt.savefig(dict_default['save'])

"""Plots to be created by function :   line, scatter,heatmap, bar,histogram,pie,count

input parameters to function:
dataset

1.   dataset
2.   type of plot
3. type of library(seaborn,matplotlib) USING SWITCH-CASE
4. x-axis,y-axis
5. xlim,ylim
6. col,row,
7. hue,legend
8. pallete,
9. xticklables, yticklabels
10. xlabel,ylabel
11. title
12. rotating the names of x_axis label(plt.xtick)
13. bins in histplot
14. Return: saving the plot as .png file
"""


def custom_plot():
        data=eval(input('Enter the DataFrame:'))
        library=input('Enter the library used for plot:')
        kind=input('Enter the type of plot:')
        if (kind=='bar' and library=='matplotlib') or (kind=='pie' and library=='matplotlib')or (kind=='count' and library=='matplotlib') or (kind=='line' and library=='matplotlib') or(kind=='scatter' and library=='matplotlib') or (kind=='hist' and library=='matplotlib') or (kind=='bar' and library=='seaborn') or (kind=='line' and library=='seaborn') or (kind=='pie' and library=='seaborn') or  (kind=='hist' and library=='seaborn') or (kind=='count' and library=='seaborn') or (kind=='scatter' and library=='seaborn'):
            if (kind=='bar' and library=='matplotlib') or (kind=='pie' and library=='matplotlib') or (kind=='line' and library=='matplotlib') or(kind=='scatter' and library=='matplotlib') or (kind=='hist' and library=='matplotlib') or (kind=='bar' and library=='seaborn') or (kind=='line' and library=='seaborn') or (kind=='pie' and library=='seaborn') or  (kind=='hist' and library=='seaborn') or (kind=='count' and library=='seaborn') or (kind=='scatter' and library=='seaborn'):
               x=input('Enter the X column:')
               if ((kind=='bar' and library=='matplotlib') or (kind=='line' and library=='matplotlib') or(kind=='scatter' and library=='matplotlib') or (kind=='count' and library=='matplotlib') or (kind=='bar' and library=='seaborn') or (kind=='line' and library=='seaborn') or (kind=='pie' and library=='seaborn') or  (kind=='hist' and library=='seaborn') or (kind=='scatter' and library=='seaborn')):
                  y=input('Enter the Y column:')
               if kind=='hist':
                   bins=int(input('Enter the number of bins :'))
               if (library=='seaborn') and (kind!='pie'):
                   hue=eval(input('Enter the hue column:'))
            title=input('Enter the title in Graph :')
            xlabel=input('Enter the xlabel in Graph:')
            ylabel=input('Enter the ylabel in Graph:')
            if (kind == 'pie' and library=='seaborn')or (kind == 'heatmap' and library=='matplotlib'):
                    sns_color=input('Enter the seaborn_color for graph:')
            elif (kind != 'pie' and library=='seaborn')or (kind != 'heatmap' and library=='matplotlib'):
                    color=eval(input('Enter the color in Graph:'))
            elif kind =='count' and library=='matplotlib':
                    color_count=input('Enter the color for countplot: ')
            if ((kind=='bar' and library=='matplotlib') or (kind=='pie' and library=='matplotlib') or (kind=='line' and library=='matplotlib')or (kind=='hist' and library=='matplotlib') or(kind=='scatter' and library=='matplotlib') or (kind=='count' and library=='matplotlib') or (kind=='bar' and library=='seaborn') or (kind=='line' and library=='seaborn') or (kind=='pie' and library=='seaborn') or  (kind=='hist' and library=='seaborn') or (kind=='scatter' and library=='seaborn')):
                  legend_bool=eval(input('Enter the legend(True or False):'))
            if kind=='pie':
                autopct=input('Enter the autopct in piechart:')
            if library=='seaborn'and kind!='pie':
                palette=input('Enter the palette:')
        additional_arguments=input('Wants to add more arguments like xticks and xlim: ')
        if additional_arguments=='yes':
                  xlim=eval(input('Enter the xlim:'))
                  ylim=eval(input('Enter the ylim:'))
                  xticks=eval(input('Enter the xticks:'))
                  yticks=eval(input('Enter the yticks:'))
                  rotate_x=int(input('Enter the rotate x axis values:'))
        save=input('Enter the figure save file name in .png file:')
        if library == 'seaborn': 
           if kind == 'hist':
              if additional_arguments=='yes':
                 dict_sorted=dict(data=data,x=x, y=y,bins=bins,hue=hue,title=title,xlabel=xlabel,ylabel=ylabel,color=color,legend_bool=legend_bool
                               ,xlim=xlim,ylim=ylim,xticks=xticks,yticks=yticks,rotate_x=rotate_x,pallete=palette,save=save)
              else:
                 dict_sorted=dict(data=data,x=x, y=y,bins=bins,hue=hue,title=title,xlabel=xlabel,ylabel=ylabel,color=color,legend_bool=legend_bool
                               ,palette=palette,save=save)
              dict_default.update(dict_sorted)
              histogram_seaborn(dict_default)
           elif kind == 'pie':
              if additional_arguments=='yes':
                 dict_sorted=dict(data=data,x=x, y=y,title=title,xlabel=xlabel,ylabel=ylabel,sns_color=sns_color
                               ,xlim=xlim,ylim=ylim,xticks=xticks,yticks=yticks,rotate_x=rotate_x,autopct=autopct,save=save)
              else:
                 dict_sorted=dict(data=data,x=x, y=y,title=title,xlabel=xlabel,ylabel=ylabel,sns_color=sns_color,autopct=autopct,
                                  save=save)
              dict_default.update(dict_sorted)
              piechart_seaborn(dict_default)
           elif kind == 'heatmap':
              if additional_arguments=='yes':
                 dict_sorted=dict(data=data,xlim=xlim,ylim=ylim,xticks=xticks,yticks=yticks,rotate_x=rotate_x,palette=palette,save=save)
              else:
                 dict_sorted=dict(data=data,save=save)
              dict_default.update(dict_sorted)
              heatmap_seaborn(dict_default)
           elif kind == 'line':
              if additional_arguments=='yes':
                 dict_sorted=dict(data=data,x=x, y=y,hue=hue,title=title,xlabel=xlabel,ylabel=ylabel,color=color,legend_bool=legend_bool
                               ,xlim=xlim,ylim=ylim,xticks=xticks,yticks=yticks,rotate_x=rotate_x,palette=palette,save=save)
              else:
                 dict_sorted=dict(data=data,x=x, y=y,hue=hue,title=title,xlabel=xlabel,ylabel=ylabel,color=color,legend_bool=legend_bool
                               ,palette=palette,save=save)
              dict_default.update(dict_sorted)
              lineplot_seaborn(dict_default)
           elif kind == 'bar':
              if additional_arguments=='yes':
                 dict_sorted=dict(data=data,x=x, y=y,hue=hue,title=title,xlabel=xlabel,ylabel=ylabel,color=color,legend_bool=legend_bool
                               ,xlim=xlim,ylim=ylim,xticks=xticks,yticks=yticks,rotate_x=rotate_x,palette=palette,save=save)
              else:
                 dict_sorted=dict(data=data,x=x, y=y,hue=hue,title=title,xlabel=xlabel,ylabel=ylabel,color=color,legend_bool=legend_bool
                               ,palete=palette,save=save)
              dict_default.update(dict_sorted)
              barplot_seaborn(dict_default)
           elif kind == 'scatter':
              if additional_arguments=='yes':
                 dict_sorted=dict(data=data,x=x, y=y,hue=hue,title=title,xlabel=xlabel,ylabel=ylabel,color=color,legend_bool=legend_bool
                               ,xlim=xlim,ylim=ylim,xticks=xticks,yticks=yticks,rotate_x=rotate_x,palette=palette,save=save)
              else:
                 dict_sorted=dict(data=data,x=x, y=y,hue=hue,title=title,xlabel=xlabel,ylabel=ylabel,color=color,legend_bool=legend_bool
                               ,palete=palette,save=save)
              dict_default.update(dict_sorted)
              scatterplot_seaborn(dict_default)
           elif kind == 'count':
              if additional_arguments=='yes':
                 dict_sorted=dict(data=data,x=x,hue=hue,title=title,xlabel=xlabel,ylabel=ylabel,color=color,legend_bool=legend_bool
                               ,xlim=xlim,ylim=ylim,xticks=xticks,yticks=yticks,rotate_x=rotate_x,palette=palette,save=save)
              else:
                 dict_sorted=dict(data=data,x=x,hue=hue,title=title,xlabel=xlabel,ylabel=ylabel,color=color,legend_bool=legend_bool
                               ,palete=palette,save=save)
              dict_default.update(dict_sorted)
              countplot_seaborn(dict_default)
        elif library == 'matplotlib': 
           if kind == 'hist':
              if additional_arguments=='yes':
                 dict_sorted=dict(data=data,x=x,title=title,xlabel=xlabel,ylabel=ylabel,color=color,legend_bool=legend_bool
                               ,xlim=xlim,ylim=ylim,xticks=xticks,yticks=yticks,rotate_x=rotate_x,save=save)
              else:
                 dict_sorted=dict(data=data,x=x,title=title,xlabel=xlabel,ylabel=ylabel,color=color,legend_bool=legend_bool
                               ,save=save)
              dict_default.update(dict_sorted)
              histogram_matplotlib(dict_default)
           elif kind == 'pie':
              if additional_arguments=='yes':
                 dict_sorted=dict(data=data,x=x,title=title,xlabel=xlabel,ylabel=ylabel,color=color,legend_bool=legend_bool
                               ,autopct=autopct,xlim=xlim,ylim=ylim,xticks=xticks,yticks=yticks,rotate_x=rotate_x,save=save)
              else:
                 dict_sorted=dict(data=data,x=x,title=title,xlabel=xlabel,ylabel=ylabel,color=color,legend_bool=legend_bool
                               ,autopct=autopct,save=save)
              dict_default.update(dict_sorted)
              piechart_matplotlib(dict_default,data,x)
           elif kind == 'heatmap':
              if additional_arguments=='yes':
                 dict_sorted=dict(data=data,xlim=xlim,ylim=ylim,xticks=xticks,yticks=yticks,rotate_x=rotate_x,palette=palette,save=save)
              else:
                 dict_sorted=dict(data=data,save=save)
              dict_default.update(dict_sorted)
              heatmap_matplotlib(dict_default)
           elif kind == 'count':
              if additional_arguments=='yes':
                 dict_sorted=dict(data=data,title=title,xlabel=xlabel,ylabel=ylabel,color=color,legend_bool=legend_bool
                               ,xlim=xlim,ylim=ylim,xticks=xticks,yticks=yticks,rotate_x=rotate_x,save=save)
              else:
                 dict_sorted=dict(data=data,title=title,xlabel=xlabel,ylabel=ylabel,color=color,legend_bool=legend_bool
                               ,save=save)
              dict_default.update(dict_sorted)
              countplot_matplotlib(dict_default)
           elif kind == 'line':
              if additional_arguments=='yes':
                 dict_sorted=dict(data=data,x=x, y=y,title=title,xlabel=xlabel,ylabel=ylabel,color=color,legend_bool=legend_bool
                               ,xlim=xlim,ylim=ylim,xticks=xticks,yticks=yticks,rotate_x=rotate_x,save=save)
              else:
                 dict_sorted=dict(data=data,x=x, y=y,title=title,xlabel=xlabel,ylabel=ylabel,color=color,legend_bool=legend_bool
                               ,save=save)
              dict_default.update(dict_sorted)
              lineplot_matplotlib(dict_default)
           elif kind == 'bar':
              if additional_arguments=='yes':
                 dict_sorted=dict(data=data,x=x, y=y,title=title,xlabel=xlabel,ylabel=ylabel,color=color,legend_bool=legend_bool
                               ,xlim=xlim,ylim=ylim,xticks=xticks,yticks=yticks,rotate_x=rotate_x,save=save)
              else:
                 dict_sorted=dict(data=data,x=x, y=y,title=title,xlabel=xlabel,ylabel=ylabel,color=color,legend_bool=legend_bool
                               ,save=save)
              dict_default.update(dict_sorted)
              barplot_matplotlib(dict_default)
           elif kind == 'scatter':
              if additional_arguments=='yes':
                 dict_sorted=dict(data=data,x=x, y=y,title=title,xlabel=xlabel,ylabel=ylabel,color=color,legend_bool=legend_bool
                               ,xlim=xlim,ylim=ylim,xticks=xticks,yticks=yticks,rotate_x=rotate_x,save=save)
              else:
                 dict_sorted=dict(data=data,x=x, y=y,title=title,xlabel=xlabel,ylabel=ylabel,color=color,legend_bool=legend_bool
                               ,save=save)
              dict_default.update(dict_sorted)
              scatterplot_matplotlib(dict_default,data,x,y)
          
custom_plot()

