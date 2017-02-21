import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from statsmodels.graphics.mosaicplot import mosaic
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

#print data.head()
year = data['seq_rel_date']
data['seq_rel_date_year'] = data['seq_rel_date'].apply(lambda x: seq_rel_to_year(x))


#print data['seq_rel_date_year'].value_counts()
#print data['seq_rel_date_year'].describe()
#dataf['Year'] = dataf[]

#plt.hist(data['seq_rel_date_year'], bins=data['seq_rel_date_year'].nunique(), stacked=True)
#plt.xlim(1999,2017)
#plt.show()


plotFrame = pd.DataFrame(data.ix[:,['Superkingdom','seq_rel_date_year']])
#print plotFrame

bact = plotFrame[plotFrame['Superkingdom']=='Bacteria']['seq_rel_date_year']
arch = plotFrame[plotFrame['Superkingdom']=='Archaea']['seq_rel_date_year']
#print arch
#plt.hist([arch,bact], stacked=True)
#plt.show()

data['Groups'] = data.apply(lambda x: makeGroups(x['Superkingdom'],x['Phylum'],x['Class'],x['Order']), axis=1)
#print data['Groups'].value_counts()
#data.set_index('seq_rel_date_year', inplace=True)
#data.groupby(level='seq_rel_date_year').Groups.value_counts().unstack('Groups').plot.bar(stacked=True)
#plt.show()

#print data.groupby(level='seq_rel_date_year').Groups

grps = data['Groups']
#yrs = data['seq_rel_date_year']
#print data['seq_rel_date_year']
#print grps.unique()

# #hier alles weg kommentieren und index raus
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
ylabels = ['1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']
xlabels = sorted(xlabels)
ctab = pd.crosstab(data['seq_rel_date_year'],data['Groups'])
ctab_norm = (ctab - ctab.mean()) / (ctab.max() - ctab.min())
#print ctab
#print ctab.max()
fig, ax = plt.subplots()
heatmap = ax.pcolor(ctab, norm=LogNorm(vmin=1, vmax=418), cmap='RdYlBu_r', alpha=0.7, edgecolor='grey')
ax.set_frame_on(False)
ax.set_xticklabels(xlabels, minor=False)
ax.set_xticks(np.arange(ctab_norm.shape[1]) + 0.5, minor=False)
ax.set_yticklabels(ylabels, minor=False)
ax.set_yticks(np.arange(19) + 0.5, minor=False)
#plt.grid(True, which='minor', axis='both', linestyle='-', color='k')
#labelizer = lambda x: {('2016',): "a", ('Gammaproteobacteria',): "a", (,): 'a'}[x]
#mosaic(data.sort_values('seq_rel_date_year'),['seq_rel_date_year','Groups'],gap=0,labelizer= lambda x: blub(x))
#plt.pcolor()
#sns.heatmap(ctab,square=True)
plt.xticks(rotation=90)
#plt.yticks(rotation=0)
plt.show()