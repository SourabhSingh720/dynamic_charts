

def custom_plot(data,kind,library,x=None, y=None,bin=None,title=None,xlabel=None,ylabel=None,color=None,sns_color='RdBu',
                explode=None,autopct='%1.1f%%',xlim=None,ylim=None,legend=True,hue=None,palette=None,xtick=None,ytick=None,
                rotate_x=0,save='fig.png'):
       if library == 'seaborn': 
           if kind == 'hist':
              fig=sns.histplot(data=data, x=x, y=y, hue=hue, bins=bin,color=color,legend=legend,palette=palette)
           elif kind == 'pie':
              fig=data.plot(x=x, y=y,autopct=autopct,kind='pie',legend=legend,colors=sns.color_palette(sns_color))
           elif kind == 'heatmap':
              fig=sns.heatmap(data=data.corr(),annot=True)
           elif kind == 'line':
              fig=sns.lineplot(data=data, x=x, y=y, hue=hue,color=color,legend=legend,palette=palette)
           elif kind == 'bar':
              fig=sns.barplot(data=data, x=x, y=y, hue=hue,color=color,palette=palette)
           elif kind == 'scatter':
              fig=sns.scatterplot(data=data, x=x, y=y, hue=hue,color=color,legend=legend,palette=palette)
           elif kind == 'count':
              fig=sns.countplot(data=data, x=x, y=y,hue=hue,color=color,palette=palette)
           fig.set_title(title)  
           fig.set_xlabel(xlabel)
           fig.set_ylabel(ylabel)
           plt.xticks(xtick,rotation=rotate_x)
           plt.yticks(ytick)   
           fig.set_xlim(xlim)
           fig.set_ylim(ylim)
           plt.savefig(save)
       if library == 'matplotlib': 
           if kind == 'hist':
              fig=plt.hist(data[x],bins=bin,color=color)
           elif kind == 'pie':
              fig=plt.pie(data[x],colors=color)
           elif kind == 'heatmap':
              fig=plt.imshow( data , cmap = sns_color , interpolation = 'nearest' )
           elif kind == 'count':
              fig=df.count().plot(kind='bar',color=color)
           elif kind == 'line':
              fig=plt.plot(data[x],data[y],color=color)
           elif kind == 'bar':
              fig=plt.bar(data[x],data[y],color=color)
           elif kind == 'scatter':
              fig=plt.scatter(data[x],data[y],color=color)
           plt.legend(legend)
           plt.title(title)
           plt.xlabel(xlabel)
           plt.ylabel(ylabel)
           plt.xlim(xlim)
           plt.ylim(ylim)
           plt.xticks(xtick,rotation=rotate_x)
           plt.yticks(ytick)          
           plt.savefig(save)
          