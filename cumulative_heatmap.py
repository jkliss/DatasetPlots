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

#########SORT#########
with open('Organisms.txt') as f:
    sorter = f.read().splitlines()

ylabels = ['1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016']

#####NEW GROUPS#####
group_counts = data['Groups'].value_counts().tolist()
group_counts_index = data['Groups'].value_counts().index.tolist()
group_dict = dict(zip(group_counts_index,group_counts))
data['Groups'] = data.apply(lambda x: makeGroupsBetter(x['Groups'],x['Superkingdom'],group_dict,sorter), axis=1)


data.Groups = data.Groups.astype("category")
data.Groups.cat.set_categories(sorter, inplace=True)
ctab = pd.crosstab(data['seq_rel_date_year'],data['Groups'])
ctab_swap = pd.crosstab(data['Groups'],data['seq_rel_date_year'])

ctab_swap = ctab_swap.cumsum(axis=1)

print ctab_swap

fig, ax = plt.subplots()
#########GRAPH##########
ctab_norm = (ctab - ctab.mean()) / (ctab.max() - ctab.min())
#heatmap = ax.pcolor(ctab, norm=LogNorm(vmin=1, vmax=418), cmap='RdYlBu_r', alpha=0.7, edgecolor='grey')
heatmap_swap = ax.pcolor(ctab_swap, norm=LogNorm(vmin=1, vmax=1565), cmap='RdYlBu_r', alpha=0.8, edgecolor='grey')
cbar = fig.colorbar(heatmap_swap)
cbar.set_alpha(1)
cbar.draw_all()
ax.set_frame_on(False)
ax.set_yticklabels(sorter, minor=False)
ax.set_yticks(np.arange(ctab_norm.shape[1]) + 0.5, minor=False)
ax.set_xticklabels(ylabels, minor=False)
ax.set_xticks(np.arange(19) + 0.5, minor=False)
ax.set_ylim([0,53])
plt.xticks(rotation=90)
plt.gca().invert_yaxis()
#plt.axis('equal')
#plt.yticks(rotation=0)
for (i, j), z in np.ndenumerate(ctab_swap):
    if z != 0 and z != 1:
        ax.text(j, i, z, ha='left', va='top', size='smaller')
    elif z == 1:
        ax.text(j, i, z, ha='left', va='top', size='smaller', color='white')
plt.show()