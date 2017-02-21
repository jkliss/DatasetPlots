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


data = pd.read_table("pasted_RefSeq_combined")

year = data['seq_rel_date']
data['seq_rel_date_year'] = data['seq_rel_date'].apply(lambda x: seq_rel_to_year(x))

data['Groups'] = data.apply(lambda x: makeGroups(x['Superkingdom'],x['Phylum'],x['Class'],x['Order']), axis=1)


xlabels = ['Sulfolobales','Acidilobales' ,'Others Archaea' ,'Archaeoglobales',
'Thermoproteales', 'Methanomassiliicoccales', 'Nitrosopumilales',
'Desulfurococcales','Thermoplasmatales', 'Halobacteriales' ,'Haloferacales',
'Natrialbales', 'Methanobacteriales', 'Methanococcales', 'Methanocellales',
'Methanosarcinales', 'Methanomicrobiales', 'Thermococcales', 'Cyanobacteria',
'Clostridia', 'Alphaproteobacteria', 'Tenericutes', 'Betaproteobacteria',
'Negativicutes', 'Actinobacteria', 'Acidithiobacillia', 'Acidobacteria',
'Gammaproteobacteria', 'Bacteroidetes', 'Bacilli', 'Verrucomicrobia',
'Synergistetes', 'Tissierellia', 'Chloroflexi', 'Deltaproteobacteria',
'Aquificae', 'Epsilonproteobacteria', 'Others Bacteria', 'Spirochaetes',
'Thermodesulfobacteria', 'Caldiserica', 'Deferribacteres',
'Candidatus Cloacimonetes', 'Nitrospirae', 'Chlamydiae', 'Chlorobi',
'Thermotogae', 'Deinococcus-Thermus', 'Chrysiogenetes' ,'Dictyoglomi',
'Elusimicrobia' ,'Erysipelotrichia', 'Fibrobacteres', 'Armatimonadetes',
'Fusobacteria' ,'Gemmatimonadetes', 'Ignavibacteriae' ,'Planctomycetes',
'Limnochordia']
ylabels = ['1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016']
xlabels = sorted(xlabels)
print data['seq_rel_date_year']
pdata = data.copy()
pdata = pdata[pdata['seq_rel_date_year'] != 2017]
ctab = pd.crosstab(pdata['seq_rel_date_year'],pdata['Groups'])
ctab_swap = pd.crosstab(pdata['Groups'],pdata['seq_rel_date_year'])
print ctab_swap
#del ctab_swap['2017']

ctab_norm = (ctab - ctab.mean()) / (ctab.max() - ctab.min())
fig, ax = plt.subplots()
#heatmap = ax.pcolor(ctab, norm=LogNorm(vmin=1, vmax=418), cmap='RdYlBu_r', alpha=0.7, edgecolor='grey')
heatmap_swap = ax.pcolor(ctab_swap, norm=LogNorm(vmin=1, vmax=418), cmap='RdYlBu_r', alpha=0.7, edgecolor='grey',)
cbar = fig.colorbar(heatmap_swap)
cbar.set_alpha(1)
cbar.draw_all()
ax.set_frame_on(False)
ax.set_yticklabels(xlabels, minor=False)
ax.set_yticks(np.arange(ctab_norm.shape[1]) + 0.5, minor=False)
ax.set_xticklabels(ylabels, minor=False)
ax.set_xticks(np.arange(19) + 0.5, minor=False)
plt.xticks(rotation=90)
#plt.axis('equal')
#plt.yticks(rotation=0)

plt.show()