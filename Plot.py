import math
import matplotlib.pyplot as plt
import pandas as pnd
import seaborn as sns

pnd.set_option('display.width', 320)

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

def DFmakeRelativeData(x):
    for index, row in x.iterrows():
        sum = 0
        for column in x:
            sum += x.loc[index, column]
        for column in x:
            x.set_value(index, column, makeRelativeData(x.loc[index, column], sum))
    return x

def removeNaN(x):
    if(math.isnan(x)):
        return 0;
    return x;

########################## READ DATA
data = pnd.read_table("pasted_RefSeq_combined")

year = data['seq_rel_date']
data['seq_rel_date_year'] = data['seq_rel_date'].apply(lambda x: seq_rel_to_year(x))


data['Groups'] = data.apply(lambda x: makeGroups(x['Superkingdom'],x['Phylum'],x['Class'],x['Order']), axis=1)



########################### BAR AND HISTOGRAM
pdata = data.copy()
## REMOVE 2017 DATASET

print pdata[pdata['seq_rel_date_year'] == 2017]
pdata = pdata[pdata['seq_rel_date_year'] != 2017]
pdata.set_index('seq_rel_date_year', inplace=True)

subset = pnd.DataFrame()
subset['Year'] = data['seq_rel_date_year'].copy()
subset['Groups'] = data['Groups'].copy()
ct_subset = pnd.crosstab(subset['Groups'],subset['Year'], normalize='columns')

#print ct_subset
sns.heatmap(ct_subset, annot=True, annot_kws={"size": 8})

plt.yticks(rotation=0)
plt.show()
#sns.countplot(y = 'seq_rel_date_year', hue='Groups', data=data, stack)

#### Wie dropt man Daten?
#pdata = pdata.drop(pdata['2017'])

plottable = pdata.groupby(level='seq_rel_date_year').Groups.value_counts().unstack('Groups')
relPlot = pnd.DataFrame(plottable.copy())
relPlot = relPlot.applymap(lambda x: removeNaN(x))
b
for index, row in relPlot.iterrows():
    sum = 0
    for column in relPlot:
        sum += relPlot.loc[index,column]
    for column in relPlot:
        relPlot.set_value(index, column, makeRelativeData(relPlot.loc[index,column],sum))


array = [data['seq_rel_date_year'],data['Groups']]
Tuple = list(zip(*array))
#print Tuple
index = pnd.MultiIndex.from_tuples(Tuple, names=['rel','grp'])

relPlot.plot.bar(stacked=True)
relPlot.reset_index(index)
#print relPlot

# Put a legend to the right of the current axis und size auf 8
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), prop={'size':8})
plt.ylim((0,1))
#plt.show()

#grps = data['Groups']
#yrs = data['seq_rel_date_year']

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

#plt.show()

