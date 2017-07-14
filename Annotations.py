import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import seaborn as sns
import pandas as pd
from collections import Counter

def numElem(x):
    x = x.replace("[", "")
    x = x.replace("]", "")
    x = x.replace(",", "")
    x = x.replace("(", "")
    x = x.replace(")", "")
    counter = Counter(x)
    return counter.items()

def singleormixed(x):
    if(len(x) == 1):
        return x[0][0]
    else:
        return "mixed"

def singlename(x):
    if("," in x or ";" in x):
        return "mixed"
    else:
        return x

data = pd.read_table("mapped_cog_fusions.txt.ps.uniq" , header = None)

data['cnts'] = data[2].apply(lambda x: numElem(x))
data['Annotation'] = data['cnts'].apply(lambda x: singleormixed(x))

#print data

#plt.hist(c)
charc_list =  pd.DataFrame(data['Annotation'].value_counts()).sort_index()
charc_list.plot(kind = "bar", title = "Annotation by character")

data['Name'] = data[5].apply(lambda x: singlename(x))
name_list = pd.DataFrame(data['Name'].value_counts().sort_index())
name_list.plot(kind = "bar", title = "Annotation by function")
#sns.barplot(name_list.index, name_list.Name, palette="Blues_d")
#plt.show()
#sns.barplot(charc_list.index, charc_list.Annotation, palette="Blues_d")
plt.show()
