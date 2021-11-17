import numpy as np

import pandas as pd

import re 

import seaborn as sns

import matplotlib.pyplot as plt

Re_xl= pd.read_excel('Insurance_data.xls', sheet_name= None)

print(Re_xl.keys())
Re_xl['claims'].head()

#print(Re_xl)


print(Re_xl['claims'].columns)

Select_data= Re_xl['claims'] [['KIDSDRIV', 'PLCYDATE', 'TRAVTIME', 'CAR_USE', 'POLICYNO',
       'BLUEBOOK', 'INITDATE', 'RETAINED', 'NPOLICY', 'CAR_TYPE', 'RED_CAR',
       'OLDCLAIM', 'CLM_FREQ', 'REVOKED', 'MVR_PTS', 'CLM_AMT', 'CLM_DATE',
       'CLM_FLAG', 'BIRTH', 'AGE', 'HOMEKIDS', 'YOJ', 'INCOME', 'GENDER',
       'MARRIED', 'PARENT1', 'JOBCLASS', 'MAX_EDUC', 'HOME_VAL', 'SAMEHOME','DENSITY','YEARQTR']]
	   
	   
Select_data.head()

Select_data.info() 

Select_data = Select_data.dropna()

Select_data['CAR_USE'] = Select_data['CAR_USE'].astype('category')

Select_data['CAR_TYPE'] = Select_data['CAR_TYPE'].astype('category')

Select_data['AGE'] = Select_data['AGE'].astype('category')

Select_data['GENDER'] = Select_data['GENDER'].astype('category')

Select_data['MARRIED'] = Select_data['MARRIED'].astype('category')

Select_data['MAX_EDUC'] = Select_data['MAX_EDUC'].astype('category')

Select_data['DENSITY'] = Select_data['DENSITY'].astype('category')

#Transform object data type to category 

#remove  sign 

Select_data['BLUEBOOK'] = Select_data['BLUEBOOK'].apply(lambda x: re.findall('\d+',x)[0])

Select_data['INCOME'] = Select_data['INCOME'].apply(lambda x: re.findall('\d+',x)[0])

Select_data['BLUEBOOK'] = Select_data['BLUEBOOK'].astype(int)

Select_data['INCOME'] = Select_data['INCOME'].astype(int)

#Change datatype to intger 

print(Select_data['CLM_FREQ'].value_counts())



sns.countplot(x='CLM_FREQ', data= Select_data, palette='hls') # data should be assigned for the Select_data

#plt.hist(Select_data['CLM_FREQ'].value_counts())
plt.grid()
#plt.show()
print("mean =" +str(Select_data['CLM_FREQ'].mean()))
print ("variance= " +str(Select_data['CLM_FREQ'].var()))

Select_data['CLM_YesNo'] = Select_data.loc[:,'CLM_FREQ']> 0
Select_data['CLM_YesNo'] = Select_data.loc[:,'CLM_YesNo'].astype(int)

Select_data.drop('CLM_FREQ', axis = 1, inplace= True)

pd.crosstab(Select_data['MAX_EDUC'], Select_data['CLM_YesNo']).plot(kind='bar', stacked= False)

plt.title('Claim Frequency for Educational Degree')
plt.xlabel('Education')

plt.ylabel('Claim Yes/No')
plt.grid()

#plt.show()

pd.crosstab(Select_data['MARRIED'], Select_data['CLM_YesNo']).plot(kind='bar', stacked=False)

plt.title('Claim Frequency for Married')

plt.xlabel('Married')
plt.ylabel('Claim Yes/No')
plt.grid()
#plt.show()

pd.crosstab(Select_data['CAR_USE'], Select_data['CLM_YesNo']).plot(kind='bar', stacked=False)
plt.title("Claim Frequency for Car Use")

plt.xlabel("Car Use")

plt.ylabel("Claim Yes/No")

plt.grid()

#plt.show()


pd.crosstab(Select_data['CAR_TYPE'], Select_data['CLM_YesNo']).plot(kind='bar', stacked=False)

plt.title("Claim Frequency for Car Type")

plt.xlabel('Car Type')

plt.ylabel('Claim Yes/No')

plt.grid()

#plt.show()


pd.crosstab(Select_data['DENSITY'], Select_data['CLM_YesNo']).plot(kind='bar', stacked=False)

plt.title('Claim Frequency for Density')

plt.xlabel('Density')

plt.ylabel("Claim Yes/No")

plt.grid()

#plt.show()


colormap =plt.cm.viridis

cor = Select_data.corr()

plt.figure(figsize=(12,12))

sns.heatmap(cor, vmax=0.8, cmap=colormap, annot=True, fmt='.2f', square=True, annot_kws={'size':10},linecolor='white', linewidth=0.1)

plt.show()

plt.close()

data_final = pd.get_dummies(Select_data, drop_first = True)

data_final.columns.values 

y_all = data_final['CLM_YesNo']

X_all = data_final.drop('CLM_YesNo', axis=1)


from sklearn import datasets

from sklearn.feature_selection import RFE

from sklearn.linear_model import RandomizedLasso

from sklearn.linear_model import LogisticRegression 


logreg = LogisticRegression()

#rfe = RFE(logreg, 13)

#rfe = rfe.fit(X_all, y_all)

#print (rfe.support_)
#print (rfe.ranking_)


#X_rfe = X_all[X_all.columns[rfe.support_]]

rlasso = RandomizedLasso(scaling=0.025)

rlasso.fit(X_all, y_all)

print(rlasso.scores_)



































































