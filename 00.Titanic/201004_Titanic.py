#!/usr/bin/env python
# coding: utf-8

# In[70]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv('train_t.csv')
test = pd.read_csv('test_t.csv')


# In[71]:


print(type(train))


# In[72]:


print(train.head())


# In[73]:


print(test.head())


# In[74]:


print(train.shape)
print(test.shape)


# In[75]:


print(train.isnull()) #Check if there is any NULL value: True-no ; False-yes


# In[76]:


print(train.info()) #Check if there is any NULL value


# In[77]:


#Visyalization 
def bar_chart(feature):
    survived = train[train['Survived']==1][feature].value_counts()
    dead = train[train['Survived']==0][feature].value_counts()
    df = pd.DataFrame([survived, dead])
      
    df.index= ['Sur', 'Die'] 
    print(df)
    df.plot(kind='bar', stacked=True, figsize=(10,5))
    plt.show()
    


# In[78]:


bar_chart('Embarked')


# In[79]:


bar_chart('Sex')


# In[80]:


bar_chart('Pclass')


# In[81]:


train_test_data = [train, test]
print(train_test_data)


# In[89]:


for dataset in train_test_data:
    dataset['Title']= dataset['Name'].str.extract('([A-Za-z]+)\.', expand=False)
print(train)


# In[90]:


title_mapping = {"Mr":0, "Miss":1, "Mrs":3, "Mr":0, "Miss":1, "Mrs":2, "Master":3, "Dr":3, "Rev":3, "Col":3, "Major":3, "Mile":3, "Countess":3, "Ms":3, "Lady":3, "Jonkheer":3, "Don":3, "Dona":3, "Mme":3, "Capt":3, "Sir":3}
for dataset in train_test_data:
    dataset['Title'] = dataset['Title'].map(title_mapping)


# In[91]:


print(train_test_data)


# In[92]:


#train.drop('Name',axis=1, inplace=True)
#test.drop('Name', axis=1, inplace=True)


# In[93]:


bar_chart('Title')


# In[87]:


sex_mapping = {"male":0, "female":1}
for dataset in train_test_data:
    dataset['Sex'] = dataset['Sex'].map(sex_mapping)


# In[88]:


print(test.head())


# In[94]:


bar_chart('Sex')


# In[96]:


#Age: exchange Nullvaluee with the average value
print(train.isnull().sum())


# In[98]:


train['Age'].fillna(train.groupby('Title')['Age'].transform('median'), inplace=True)


# In[99]:


print(train)


# In[100]:


print(train.isnull().sum())


# In[101]:


test['Age'].fillna(test.groupby('Title')['Age'].transform('median'), inplace=True)


# In[104]:


print(test.isnull().sum())


# In[ ]:




