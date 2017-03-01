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



pnd.set_option('display.width', 320)

taxonomy = pd .read_table("pasted_RefSeq_combined")
taxonomy['Groups'] = taxonomy.apply(lambda x: makeGroups(x['Superkingdom'],x['Phylum'],x['Class'],x['Order']), axis=1)
conversion = dict(zip(taxonomy['# assembly_accession'], taxonomy['Groups']))

data = pd.read_table("amount_plasmid_per_org")
data['Groups'] = data['org'].apply(lambda x: conversion.get(x))


print data
