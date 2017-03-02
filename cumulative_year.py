import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from matplotlib.colors import LogNorm


pd.set_option('display.width', 320)
pd.set_option('display.height', 1000)

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


def makeGroupsBetter(x,Superkingdom,dictio,sorter):
    if(dictio.get(x) == 1):
        sorter.remove(x)
        if(Superkingdom== 'Archaea'):
            return 'Others Archaea';
        else:
            return 'Others Bacteria';
    return x;

data = pd.read_table("pasted_RefSeq_combined")
year = data['seq_rel_date']
data['seq_rel_date_year'] = data['seq_rel_date'].apply(lambda x: seq_rel_to_year(x))
data['Groups'] = data.apply(lambda x: makeGroups(x['Superkingdom'],x['Phylum'],x['Class'],x['Order']), axis=1)

ctab = pd.crosstab(data['seq_rel_date_year'],data['Groups'])
ctab_swap = pd.crosstab(data['Groups'],data['seq_rel_date_year'])




print ctab_swap
ctab = ctab.cumsum(axis=1)
newdf = ctab['Verrucomicrobia']
points = newdf.tolist()
xlabels = ['1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016']

fig, ax = plt.subplots()
plt.plot(xlabels, points)
plt.show()
