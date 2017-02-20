import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pnd
import matplotlib as mpl
from matplotlib.colors import Colormap
import colorbrewer

def seq_rel_to_year(x):
     if(int(str(x)[-2:])==99):
         return 1999;
     else:
         return int(str(x)[-2:]) + 2000;

def makeGroups(Superkingdom,Phylum,Class,Order):
    if(Superkingdom=='Archaea'):
        if(Order=='-'):
            return 'Others Archaea'
        else:
            return Order;
    else:
        if(Phylum=='Proteobacteria' or Phylum=='Firmicutes'):
            if(Class=='-'):
                return 'Others Bacteria';
            else:
                return Class;
        else:
            if(Phylum=="-"):
                return 'Others Bacteria'
            else:
                return Phylum;


def makeRelativeData(x,sum):
    return x/sum;

def removeNaN(x):
    if(math.isnan(x)):
        return 0;
    return x;


data = pnd.read_table("pasted_RefSeq_combined")

#print data.head()
year = data['seq_rel_date']
data['seq_rel_date_year'] = data['seq_rel_date'].apply(lambda x: seq_rel_to_year(x))


#print data['seq_rel_date_year'].value_counts()
#print data['seq_rel_date_year'].describe()
#dataf['Year'] = dataf[]



plotFrame = pnd.DataFrame(data.ix[:,['Superkingdom','seq_rel_date_year']])
#print plotFrame


data['Groups'] = data.apply(lambda x: makeGroups(x['Superkingdom'],x['Phylum'],x['Class'],x['Order']), axis=1)

pdata = data.copy()
#print data['Groups'].value_counts()
pdata.set_index('seq_rel_date_year', inplace=True)
plottable = pdata.groupby(level='seq_rel_date_year').Groups.value_counts().unstack('Groups')
relPlot = pnd.DataFrame(plottable.copy())
relPlot = relPlot.applymap(lambda x: removeNaN(x))

for index, row in relPlot.iterrows():
    sum = 0
    for column in relPlot:
        sum += relPlot.loc[index,column]
    for column in relPlot:
        relPlot.set_value(index, column, makeRelativeData(relPlot.loc[index,column],sum)*100)

#for(columnname, column in plottable.iteritems()):



relPlot.plot.bar(stacked=True)
#plt.legend(loc=10,prop={'size':8})
# Shrink current axis by 20%

# Put a legend to the right of the current axis
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), prop={'size':8})
plt.ylim((0,100))
plt.show()

#print data.groupby(level='seq_rel_date_year').Groups

#grps = data['Groups']
#yrs = data['seq_rel_date_year']
#print data['seq_rel_date_year']

#hier alles weg kommentieren und index raus
ctab = pnd.crosstab(data['seq_rel_date_year'],data['Groups'])

#plt.hist(data['seq_rel_date_year'], bins=data['seq_rel_date_year'].nunique(), stacked=True)
#plt.xlim(1999,2017)
#plt.show()



#bact = plotFrame[plotFrame['Superkingdom']=='Bacteria']['seq_rel_date_year']
#arch = plotFrame[plotFrame['Superkingdom']=='Archaea']['seq_rel_date_year']
#print arch
#plt.hist([arch,bact], stacked=True, normed=1)
#plt.show()


##### MOASIC PLOT
#mosaic(ctab.stack(),gap=0)
#plt.show()



#### HEATMAP PLOT
#sns.heatmap(ctab, square=True, cmap='YlGnBu', vmax=100, vmin=0,
#            linewidths=.5, cbar_kws={"shrink": .5})


#plt.xticks(rotation=90)
#plt.yticks(rotation=0)

#lt.show()
