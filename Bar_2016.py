import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import math
import matplotlib.ticker as ticker
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


pdata = data.copy()
pdata = pdata[pdata['seq_rel_date_year'] != 2017]



with open('Organisms.txt') as f:
    sorter = f.read().splitlines()
print sorter

data.Groups = pdata.Groups.astype("category")
data.Groups.cat.set_categories(sorter, inplace=True)

val_counts = data['Groups'].value_counts(sort=False)
count_index = data.Groups.value_counts().index
count_index = count_index.tolist()

print count_index
#print val_counts
#val_counts=val_counts.apply(lambda x: math.log(x,10)).copy()
val_counts= val_counts
print val_counts
#val_counts=val_counts.apply(lambda x: x).copy()
myset =  set(data['Groups'].tolist())
print myset



fig, ax = plt.subplots()
#sns.countplot(x='Groups', data=pdata , ax=ax )
plt.xticks(rotation=90)
#sns.barplot(count_index, val_counts, order = sorter, palette='Blues_d')
#plt.bar(count_index, val_counts)


w = 3
nitems = len(val_counts)
x_axis = np.arange(0, nitems*w, w)    # set up a array of x-coordinates

ax.bar(x_axis, val_counts, width=w, align='center', log='True',)
ax.set_xticks(x_axis);
ax.set_xticklabels(sorter, rotation=90)






# ncount= len(pdata)
# print ncount
#
#
#
# ax2=ax.twinx()
#
# # Switch so count axis is on right, frequency on left
# ax2.yaxis.tick_left()
# ax.yaxis.tick_right()
#
# # Also switch the labels over
# ax.yaxis.set_label_position('right')
# ax2.yaxis.set_label_position('left')
#
#
# ax2.set_ylabel('Frequency [%]')
#
# for p in ax.patches:
#     x=p.get_bbox().get_points()[:,0]
#     y=p.get_bbox().get_points()[1,1]
#     ax.annotate('{:.1f}%'.format(100.*y/ncount), (x.mean(), y),
#             ha='center', va='bottom', size='smaller') # set the alignment of the text
#
#
# # Use a LinearLocator to ensure the correct number of ticks
# ax.yaxis.set_major_locator(ticker.LinearLocator(11))
#
# # Fix the frequency range to 0-100
# ax2.set_ylim(0,100)
# ax.set_ylim(0,ncount)
# # And use a MultipleLocator to ensure a tick spacing of 10
# ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
#
# # Need to turn the grid on ax2 off, otherwise the gridlines end up on top of the bars
#ax2.grid(None)




plt.show()