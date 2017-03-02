import math
import matplotlib.pyplot as plt
import pandas as pnd
import seaborn as sns
import pandas as pd



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


def seq_rel_to_year(x):
    if (int(str(x)[-2:]) == 99):
        return 1999;
    else:
        return int(str(x)[-2:]) + 2000;

pnd.set_option('display.width', 320)

taxonomy = pd .read_table("pasted_RefSeq_combined")
taxonomy['Groups'] = taxonomy.apply(lambda x: makeGroups(x['Superkingdom'],x['Phylum'],x['Class'],x['Order']), axis=1)
conversion = dict(zip(taxonomy['# assembly_accession'], taxonomy['Groups']))
timepoint = dict(zip(taxonomy['# assembly_accession'], taxonomy['seq_rel_date']))

data = pd.read_table("amount_plasmid_per_org")
data['Groups'] = data['org'].apply(lambda x: conversion.get(x))
data['seq_rel_date'] = data['org'].apply(lambda x: seq_rel_to_year(timepoint.get(x)))


#Normalisieren
print data

plasmidSet = pnd.DataFrame()

plasmidSet['Groups'] = data['Groups'].unique().tolist()
plasmidSet['Amount'] = data.groupby(by='Groups').sum()['amt'].tolist()
plasmidSet['GroupCount'] = data['Groups'].value_counts().tolist()
grp2cnt = dict(zip(plasmidSet['Groups'],plasmidSet['GroupCount']))

plasmidSet['Normalized'] = plasmidSet['Amount']/plasmidSet['GroupCount']
#
# plt.subplots()
# ax = sns.barplot(data=plasmidSet, x='Groups', y='Normalized')
#
# labels = plasmidSet['GroupCount'].tolist()
# height = plasmidSet['Normalized'].tolist()
# i = 0
# for p in ax.patches:
#     ax.text(p.get_x()+p.get_width()/2.,
#             height[i] + 30,
#             '{:1}'.format(labels[i]),
#             ha="center")
#     i+=1
#
#
# plt.show()


ax = sns.boxplot(data=data, x='Groups', y='amt')
ax = sns.swarmplot(x="Groups", y="amt", data=data, color='0.6', size=8, alpha=1, edgecolor='black', linewidth=0.5)
ax.set_ylim([0,max(data['amt'])*1.05])
ax.set_ylabel("Amount ")
ax.set_title("Plasmid coded genes in Groups")
plt.show()