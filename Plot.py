import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pnd
from statsmodels.graphics.mosaicplot import mosaic

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

data['Groups'] = data.apply(lambda x: makeGroups(x['Superkingdom'],x['Phylum'],x['Class'],x['Order']), axis=1)
#print data['Groups'].value_counts()
#data.set_index('seq_rel_date_year', inplace=True)
#data.groupby(level='seq_rel_date_year').Groups.value_counts().unstack('Groups').plot.bar(stacked=True)
#plt.show()

#print data.groupby(level='seq_rel_date_year').Groups

grps = data['Groups']
#yrs = data['seq_rel_date_year']
#print data['seq_rel_date_year']
print grps.unique()

#hier alles weg kommentieren und index raus
#index = ['Sulfolobales','Acidilobales' ,'Others Archaea' ,'Archaeoglobales',
# 'Thermoproteales', 'Methanomassiliicoccales', 'Nitrosopumilales',
# 'Desulfurococcales','Thermoplasmatales', 'Halobacteriales' ,'Haloferacales',
# 'Natrialbales', 'Methanobacteriales', 'Methanococcales', 'Methanocellales',
# 'Methanosarcinales', 'Methanomicrobiales', 'Thermococcales', 'Cyanobacteria',
# 'Clostridia', 'Alphaproteobacteria', 'Tenericutes', 'Betaproteobacteria',
# 'Negativicutes', 'Actinobacteria', 'Acidithiobacillia', 'Acidobacteria',
# 'Gammaproteobacteria', 'Bacteroidetes', 'Bacilli', 'Verrucomicrobia',
# 'Synergistetes', 'Tissierellia', 'Chloroflexi', 'Deltaproteobacteria',
# 'Aquificae', 'Epsilonproteobacteria', 'Others Bacteria', 'Spirochaetes',
# 'Thermodesulfobacteria', 'Caldiserica', 'Deferribacteres',
# 'Candidatus Cloacimonetes', 'Nitrospirae', 'Chlamydiae', 'Chlorobi',
# 'Thermotogae', 'Deinococcus-Thermus', 'Chrysiogenetes' ,'Dictyoglomi',
# 'Elusimicrobia' ,'Erysipelotrichia', 'Fibrobacteres', 'Armatimonadetes',
# 'Fusobacteria' ,'Gemmatimonadetes', 'Ignavibacteriae' ,'Planctomycetes',
# 'Limnochordia']
ctab = pnd.crosstab(data['seq_rel_date_year'],data['Groups'])
#labelizer = lambda x: {('2016',): "a", ('Gammaproteobacteria',): "a", (,): 'a'}[x]
mosaic(ctab.stack(),gap=0)
plt.show()