import pandas as pd
url = 'football.csv'
col_names = ['name', 'weight','height','calf','thigh','kickforce']
kickdata = pd.read_csv(url, header=None, names=col_names)

numofrows = kickdata.shape[0]
#plotting the kickforces in a scatter plot
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (6, 4)
plt.rcParams['font.size'] = 14
from matplotlib.colors import ListedColormap
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

plots = kickdata.plot(kind='scatter', x='calf', y='thigh', c='kickforce', colormap=cmap_bold)
fig = plots.get_figure()
fig.savefig('kickforcescatter.pdf')


kickdata['Clusters'] = pd.qcut(kickdata['kickforce'], 4)
#print kickdata
kickdata.to_csv('kickforce2.csv')

plots = kickdata.groupby('Clusters').count().plot(kind='bar')
fig = plots.get_figure()
fig.savefig('kickforcebar.pdf')

plots = ''
fig = ''

plots1 = kickdata.Clusters.value_counts().plot(kind='bar', legend=False)
print plots1
fig1 = plots1.get_figure()
fig1.savefig('kickforcebar1.pdf')

X = kickdata.iloc[:, 1:5]
print X.head(2)

Y = kickdata.iloc[:, 6:7]
print Y.head(2)

import sklearn
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
print type(knn)

knn.fit(X,Y)
X_new =  ([[67,85,18,20],[90,165,18,20]])

print knn.predict(X_new)
