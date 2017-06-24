
# coding: utf-8

# In[1]:

# Import the Titanic dataset
import pandas as pd
Location = "titanic3.xls"
df = pd.read_excel(Location)


# In[2]:

# Observe the data
df.head()


# In[3]:

# Remove passengers who didn't survive and create a dataframe for survivors and non-survivors
df_survived= df[df["survived"] == 1]
df_died= df[df["survived"] == 0]


# In[4]:

# Compare the average age of survivors to non-survivors
# Average age of survivors
df_survived['age'].mean()
# Average age of non-survivors
df_died['age'].mean()


# In[5]:

# Compare the averae ticket price that survivors paid to non-survivors
# Average ticket price that survivors paid
df_survived['fare'].mean()


# In[6]:

# Average ticket price that non-survivors paid
df_died['fare'].mean()


# In[7]:

# Max fare of non-survivor
df_died['fare'].max()


# In[8]:

#Min fare of survivor
df_survived['fare'].min()


# In[9]:

# Correlation of df (both survivals and deceased)
df.corr()


# In[10]:

# correlation of deceased
df_died.corr()


# In[11]:

df.corr()


# In[12]:

# Regression
import statsmodels.formula.api as sm
result = sm.ols(formula = 'survived ~ pclass + age + fare + parch', data = df).fit()
result.summary()


# In[13]:

# Regression without intercept
import statsmodels.formula.api as sm
result = sm.ols(formula = 'survived ~ pclass + age + fare + parch-1', data = df).fit()
result.summary()


# In[14]:

# Regression without intercept
import statsmodels.formula.api as sm
result = sm.ols(formula = 'survived ~  pclass + age +  fare  - 1', data = df).fit()
result.summary()


# In[15]:

# Some Maps of the distribution of fare and age of s
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
df_survived.hist
df_survived.hist('fare', bins = 4)
plt.xlabel('Fare')
plt.ylabel('Number of Passengers')
plt.title('Distribution of Fare for Survivers')
plt.yticks([0, 150, 300, 450, 525, 600, 675, 750])
plt.xticks([0, 75, 150, 225, 300, 375, 450, 500])
df_died.hist('fare', bins = 4)
plt.xlabel('Fare')
plt.ylabel('Number of Passengers')
plt.title('Distribution of Fare for Deceased')
plt.yticks([0, 150, 300, 450, 525, 600, 675, 750])
plt.xticks([0, 75, 150, 225, 300, 375, 450, 500])


# In[16]:

# Maps of dist for age
df_survived.hist('age')
plt.xlabel('Age')
plt.ylabel('Number of Passengers')
plt.title('Distribution of Age for Survivers')
df_died.hist('age')
plt.xlabel('Age')
plt.ylabel('Number of Passengers')
plt.title('Distribution of Age for Deceased')

