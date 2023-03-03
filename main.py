import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

dict_default=dict(data=None,x=None, y=None,bins=50,title=None,xlabel=None,ylabel=None,color=None,sns_color='RdBu',legend_bool=True,
                  autopct='%1.1f%%',xlim=None,ylim=None,hue=None,palette=None,xticks=None,yticks=None,color_count='b'
                  ,clim=(-1,1),rotate_x=0,save='fig.png')

data=None ; library=None ; Kind=None; x=None; y=None; bins=None ;title=None;xlabel=None;ylabel=None;color=None;sns_color='RdBu'
legend_bool=True;color_count=None;xlim=None;ylim=None;hue=None;palette=None;xticks=None;yticks=None;rotate_x=0;save='fig.png'

def additional_argument(dict):
  plt.title(dict_default['title'])  
  plt.xlabel(dict_default['xlabel'])
  plt.ylabel(dict_default['ylabel'])
  plt.xticks(dict_default['xticks'],rotation=dict_default['rotate_x'])
  plt.yticks(dict_default['yticks'])   
  plt.xlim(dict_default['xlim'])
  plt.ylim(dict_default['ylim'])
  plt.tight_layout()
  plt.savefig(dict_default['save'])
  try:
    print('Your Graph has been successfully generated.')
  except:
    print('An exception occurred')



for i in range(10):
    data_location=input('Enter the location of DataFrame:')
    try:
      data=pd.read_csv(data_location)
      break
    except:
      print('Invalid file location',data_location,'entered')
      continue
for i in  range(10):
  library=input('Enter the library used for plot [matplotlib or seaborn]:')
  if library =='matplotlib' or library =='seaborn':
    break
    
  else: 
     print('Wrong input,Please enter correct library ,Options: [matplotlib or seaborn]')
     continue
print('Plots available : [line,scatter,hist,bar,heatmap,pie,count]')
for i in  range(10):
  kind=input('Enter the type of plot:')
  if kind =='line'or kind =='scatter'or kind =='hist'or kind =='bar'or kind =='heatmap'or kind =='pie'or kind =='count':
    break
    
  else: 
    print('Wrong input,Please enter correct Graph type ,Options: [line,scatter,hist,bar,heatmap,pie,count]')
    continue
if (kind=='bar' and library=='matplotlib') or (kind=='pie' and library=='matplotlib')or (kind=='count' and library=='matplotlib') or (kind=='line' and library=='matplotlib') or(kind=='scatter' and library=='matplotlib') or (kind=='hist' and library=='matplotlib') or (kind=='bar' and library=='seaborn') or (kind=='line' and library=='seaborn') or (kind=='pie' and library=='seaborn') or  (kind=='hist' and library=='seaborn') or (kind=='count' and library=='seaborn') or (kind=='scatter' and library=='seaborn'):
   if (kind=='bar' and library=='matplotlib') or (kind=='pie' and library=='matplotlib') or (kind=='line' and library=='matplotlib') or(kind=='scatter' and library=='matplotlib') or (kind=='hist' and library=='matplotlib') or (kind=='bar' and library=='seaborn') or (kind=='line' and library=='seaborn') or (kind=='pie' and library=='seaborn') or  (kind=='hist' and library=='seaborn') or (kind=='count' and library=='seaborn') or (kind=='scatter' and library=='seaborn'):
      x=input('Enter the X column:')
      if ((kind=='bar' and library=='matplotlib') or (kind=='line' and library=='matplotlib') or(kind=='scatter' and library=='matplotlib') or (kind=='count' and library=='matplotlib') or (kind=='bar' and library=='seaborn') or (kind=='line' and library=='seaborn') or (kind=='pie' and library=='seaborn') or (kind=='scatter' and library=='seaborn')):
        y=input('Enter the Y column:')
      if kind=='hist':
        try:
          bins=int(input('Enter the number of bins :'))
        except:
          print('bins only carry integer value')
      if (library=='seaborn') and (kind!='pie'):
        try:
          hue=eval(input('Enter the hue column(must be in invertedcoma or None):'))
        except:
          print('Put the correct value with given instruction in hue')
      title_labels=input('Wants to add titles and graph[y/n]?:')
      if title_labels=='y':
          title=input('Enter the title in Graph :')
          xlabel=input('Enter the xlabel in Graph :')
          ylabel=input('Enter the ylabel in Graph :')
      else : xlabel=x;ylabel=y
      if (kind == 'pie' and library=='seaborn'):
        print("color options:[deep,muted,pastel,bright,dark,colorblind]")
        sns_color=input('Enter the seaborn_color for graph:')
      if (kind != 'pie' and library=='seaborn') or (kind != 'pie' and library=='matplotlib' or hue==None):
        print("color options: [blue,green,red,cyan,magenta,yellow,black,white]")
        color=input('Enter the color in Graph:')
      if ((kind=='line' and library=='seaborn') or (kind=='pie' and library=='seaborn') or  (kind=='hist' and library=='seaborn') or (kind=='scatter' and library=='seaborn')):
        legend_bool=eval(input('Enter the legend(True or False):'))
      if (library=='seaborn'and kind!='pie') and hue !=None:
        print ('Palette options: [deep , muted , pastel , bright , dark , and colorblind]')
        palette=eval(input('Enter the palette:'))
      if kind!='pie':
        additional_arguments=input('Wants to add more arguments like xticks and xlim[y/n]: ')
        while additional_arguments=='y':
          print('arguments to add : [xlim,ylim,xticks,yticks]')
          argument=input('Enter the argument to add :')
          try:
            if argument=='xlim': xlim=eval(input('Enter the xlim:'))
            if argument=='ylim': ylim=eval(input('Enter the ylim:'))
            if argument=='xticks': xticks=eval(input('Enter the xticks:'))
            if argument=='yticks': yticks=eval(input('Enter the yticks:'))
            additional_arguments=input('Wants to add more arguments : ')
          except:
            print('Wrong Input')
  

if (kind=='count' and library=='matplotlib'):
  color_count=input('Enter the color for Countplot:')
if (kind=='bar' and library=='matplotlib') or (kind=='count' and library=='matplotlib') or (kind=='line' and library=='matplotlib') or(kind=='scatter' and library=='matplotlib') or (kind=='heatmap' and library=='matplotlib') or (kind=='bar' and library=='seaborn') or (kind=='line' and library=='seaborn') or (kind=='heatmap' and library=='seaborn')  or (kind=='count' and library=='seaborn') or (kind=='scatter' and library=='seaborn'):
  rotate_true=input('wants to rotate x axis values[y/n]?:')
  if rotate_true=='y':
    rotate_x=int(input('Enter the rotate x axis values:'))
save=input('Enter the figure save file name in .png file:')

dict_sorted=dict(data=data,x=x, y=y,hue=hue,title=title,xlabel=xlabel,ylabel=ylabel,color=color,legend_bool=legend_bool,palette=palette,bins=bins,
                 sns_color=sns_color,color_count=color_count,xlim=xlim,ylim=ylim,xticks=xticks,yticks=yticks,rotate_x=rotate_x,save=save)
dict_default.update(dict_sorted)

def lineplot_seaborn(dict):
  try:
    fig=sns.lineplot(data=dict_default['data'], x=dict_default['x'], y=dict_default['y'], hue=dict_default['hue'],color=dict_default['color'],
                              legend=dict_default['legend_bool'],palette=dict_default['palette'])
    additional_argument(dict_default)
  except:
    print('Invalid Input Variables')

def histogram_seaborn(dict):
  try:
    fig=sns.histplot(data=dict_default['data'], x=dict_default['x'], y=dict_default['y'], hue=dict_default['hue'], bins=dict_default['bins'],color=dict_default['color'],
                            legend=dict_default['legend_bool'],palette=dict_default['palette'])
    additional_argument(dict_default)
  except:
    print('Invalid Input Variables')

def barplot_seaborn(dict):
  try:
    fig=sns.barplot(data=dict_default['data'], x=dict_default['x'], y=dict_default['y'], hue=dict_default['hue'],color=dict_default['color'],palette=dict_default['palette'])
    additional_argument(dict_default)
  except:
    print('Invalid Input Variables')

def scatterplot_seaborn(dict):
  try:
    fig=sns.scatterplot(data=dict_default['data'], x=dict_default['x'], y=dict_default['y'], hue=dict_default['hue'],color=dict_default['color'],
                        legend=dict_default['legend_bool'],palette=dict_default['palette'])
    additional_argument(dict_default)
  except:
    print('Invalid Input Variables')

def piechart_seaborn(dict):
  try:
    fig=dict_default['data'].plot(x=dict_default['x'], y=dict_default['y'],autopct=dict_default['autopct'],kind='pie',legend=dict_default['legend_bool'],
                 colors=sns.color_palette(dict_default['sns_color']),explode=dict_default['explode'])
    additional_argument(dict_default)
  except:
    print('Invalid Input Variables')

def heatmap_seaborn(dict):
  try:
    fig=sns.heatmap(data=dict_default['data'].corr(),annot=True)
    additional_argument(dict_default)
  except:
    print('Invalid Input Variables')

def countplot_seaborn(dict):
  try:
    fig=sns.countplot(data=dict_default['data'],x=dict_default['x'], hue=dict_default['hue'],color=dict_default['color'],
                     palette=dict_default['palette'])
    additional_argument(dict_default)
  except:
    print('Invalid Input Variables')

def lineplot_matplotlib(dict):
  try:
    fig=plt.plot(dict_default['data'][dict_default['x']],dict_default['data'][dict_default['y']],color=dict_default['color']) 
    additional_argument(dict_default)
  except:
    print('Invalid Input Variables')

def histogram_matplotlib(dict):
  try:
    fig=plt.hist(dict_default['data'][dict_default['x']],bins=dict_default['bins'],color=dict_default['color'])
    additional_argument(dict_default)
  except:
    print('Invalid Input Variables')

def piechart_matplotlib(dict):
  try:
    count=dict_default['data'][dict_default['x']].value_counts().reset_index()
    fig= plt.pie(x=count[dict_default['x']],labels=count['index'],autopct="%1.1f%%")
    additional_argument(dict_default)
  except:
    print('Invalid Input Variables')

def barplot_matplotlib(dict):
  try:
    fig=plt.bar(dict_default['data'][dict_default['x']],dict_default['data'][dict_default['y']],color=dict_default['color'])
    additional_argument(dict_default)
  except:
    print('Invalid Input Variables')

def scatterplot_matplotlib(dict):
  try:
    fig=plt.scatter(dict_default['data'][dict_default['x']],dict_default['data'][dict_default['y']],color=dict_default['color'])
    additional_argument(dict_default)
  except:
    print('Invalid Input Variables')

def countplot_matplotlib(dict):
  try:
    fig=dict_default['data'].count().plot(kind='bar',color=dict_default['color_count']) 
    additional_argument(dict_default)
  except:
    print('Invalid Input Variables')

def heatmap_matplotlib(dict):
  try:
    print('Heatmap is not available in matplotlib,using seaborn instread to plot heatmap')
    heatmap_seaborn(dict_default)
  except:
    print('Invalid Input Variables')


def custom_plot(dict_default):
  print("Your plot is processing...........")
  if library == 'seaborn': 
    if kind == 'hist':
      histogram_seaborn(dict_default)
    elif kind == 'pie':
      piechart_seaborn(dict_default)
    elif kind == 'heatmap':
      heatmap_seaborn(dict_default)
    elif kind == 'line':
      lineplot_seaborn(dict_default)
    elif kind == 'bar':
      barplot_seaborn(dict_default)
    elif kind == 'scatter':
      scatterplot_seaborn(dict_default)
    elif kind == 'count':
      countplot_seaborn(dict_default)
  elif library == 'matplotlib': 
    if kind == 'hist':
      histogram_matplotlib(dict_default)
    elif kind == 'pie':
      piechart_matplotlib(dict_default)
    elif kind == 'heatmap':
      heatmap_matplotlib(dict_default)
    elif kind == 'count':
      countplot_matplotlib(dict_default)
    elif kind == 'line':
      lineplot_matplotlib(dict_default)
    elif kind == 'bar':
      barplot_matplotlib(dict_default)
    elif kind == 'scatter':
      scatterplot_matplotlib(dict_default)

custom_plot(dict_default)