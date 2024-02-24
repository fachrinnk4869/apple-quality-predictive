# %% [markdown]
# # IMPORT LIBRARY

# %%
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# %% [markdown]
# ## Load Data

# %%
# load the dataset
url = 'apple_quality.csv'
diamonds = pd.read_csv(url)
diamonds

# %%
diamonds.info()

# %% [markdown]
# terdapat 7 column numerical dan 2 column categorical berupa ACidity dan Quality yang merupakan target prediksi kita. Tapi ada yang aneh di kolom Acidity , karena seharusnya acidity berupa numeric dan dapat dilihat kalau pada rows 4000 ada data yang aneh

# %% [markdown]
# drop data ke 4000

# %%
diamonds = diamonds.dropna().copy()

# %% [markdown]
# ubah Acidity ke numerical yaitu float

# %%
diamonds.Acidity = diamonds.Acidity.astype('float64')

# %%
diamonds.info()

# %%
diamonds.describe()

# %%
CATEGORICAL = [
    "Size",
    "Weight",
    "Sweetness",
    "Crunchiness",
    "Juiciness",
    "Ripeness",
    "Acidity",
]

# %% [markdown]
# # EDA

# %% [markdown]
# ## Univariate Analysis

# %%
diamonds.hist(bins=50, figsize=(20, 15))
plt.show()

# %% [markdown]
# ## Multivariate Analysis

# %%
plt.figure(figsize=(10, 8))
correlation_matrix = diamonds.corr().round(2)

# Untuk menge-print nilai di dalam kotak, gunakan parameter anot=True
sns.heatmap(data=correlation_matrix, annot=True,
            cmap='coolwarm', linewidths=0.5, )
plt.title("Correlation Matrix untuk Fitur Numerik ", size=20)

# %% [markdown]
# # Handle Outlier

# %%
sns.boxplot(x=diamonds['Size'])

# %%
sns.boxplot(x=diamonds['Weight'])

# %%
Q1 = diamonds.quantile(0.25)
Q3 = diamonds.quantile(0.75)
IQR = Q3-Q1
diamonds = diamonds[~((diamonds < (Q1-1.5*IQR)) |
                      (diamonds > (Q3+1.5*IQR))).any(axis=1)]

# Cek ukuran dataset setelah kita drop outliers
diamonds.shape

# %% [markdown]
# # Prepare Priction model

# %% [markdown]
# drop A_id karena meupakan data unique tidak penting untuk prediksi

# %%
diamonds.drop(columns=['A_id'], inplace=True)

# %% [markdown]
# merubah target menjadi angka agar mudah dibaca oleh komputer

# %%
diamonds['Quality'] = diamonds['Quality'].map({'good': 1, 'bad': 0})

# %% [markdown]
# Split data ke train dan validasi

# %%

X = diamonds.drop(["Quality"], axis=1)
y = diamonds["Quality"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=123)

# %% [markdown]
# Menstandar data train dan test

# %%

scaler = StandardScaler()
x_train = scaler.fit_transform(X_train)
x_test = scaler.fit_transform(X_test)

# %%
print(f'Total # of sample in whole dataset: {len(X)}')
print(f'Total # of sample in train dataset: {len(X_train)}')
print(f'Total # of sample in test dataset: {len(X_test)}')

# %% [markdown]
# # Melatih Data dengan berbagai model

# %%
# Siapkan dataframe untuk analisis model
models = pd.DataFrame(index=['accuracy'],
                      columns=['KNN', 'RandomForest', 'Boosting'])

# %% [markdown]
# ### KNN

# %%

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
Y_pred = knn.predict(X_test)
acc = accuracy_score(y_test, Y_pred)
print("Akurasi {}".format(acc))
print(confusion_matrix(y_test, Y_pred))
print(classification_report(y_test, Y_pred))
models.loc['accuracy', 'KNN'] = acc

# %% [markdown]
# ### RandomForest

# %%
# Impor library yang dibutuhkan
clf = RandomForestClassifier(n_estimators=200, random_state=123)
clf.fit(X_train, y_train)
Y_pred = clf.predict(X_test)
acc = accuracy_score(y_test, Y_pred)
print("Akurasi {}".format(acc))
print(confusion_matrix(y_test, Y_pred))
print(classification_report(y_test, Y_pred))
models.loc['accuracy', 'RandomForest'] = acc

# %% [markdown]
# ### AdaBoost

# %%

boosting = AdaBoostClassifier(learning_rate=0.001, random_state=55)
boosting.fit(X_train, y_train)
Y_pred = boosting.predict(X_test)
acc = accuracy_score(y_test, Y_pred)
print("Akurasi {}".format(acc))
print(confusion_matrix(y_test, Y_pred))
print(classification_report(y_test, Y_pred))
models.loc['accuracy', 'Boosting'] = acc

# %%
models = models.T

# %%
fig, ax = plt.subplots()
models.sort_values(by='accuracy', ascending=False).plot(
    kind='barh', ax=ax, zorder=3)
ax.grid(zorder=0)
