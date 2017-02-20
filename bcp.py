import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pnd

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


data = pnd.read_table("pasted_RefSeq_combined")

#print data.head()
year = data['seq_rel_date']
data['seq_rel_date_year'] = data['seq_rel_date'].apply(lambda x: seq_rel_to_year(x))


#print data['seq_rel_date_year'].value_counts()
#print data['seq_rel_date_year'].describe()
#dataf['Year'] = dataf[]

#plt.hist(data['seq_rel_date_year'], bins=data['seq_rel_date_year'].nunique(), stacked=True)
#plt.xlim(1999,2017)
#plt.show()


plotFrame = pnd.DataFrame(data.ix[:,['Superkingdom','seq_rel_date_year']])
#print plotFrame

bact = plotFrame[plotFrame['Superkingdom']=='Bacteria']['seq_rel_date_year']
arch = plotFrame[plotFrame['Superkingdom']=='Archaea']['seq_rel_date_year']
#print arch
#plt.hist([arch,bact], stacked=True)
#plt.show()

data['groups'] = data.apply(lambda x: makeGroups(x['Superkingdom'],x['Phylum'],x['Class'],x['Order']), axis=1)
print data['groups']=="-"
data.set_index('seq_rel_date_year', inplace=True)
data.groupby(levels='seq_rel_date_year').groups.value_counts().unstack('groups').plot.bar(stacked=True)
plt.show()