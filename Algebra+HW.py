
# coding: utf-8

# In[1]:

# Import the Zip file
path_to_zip_file = "datasets-1.zip"
directory_to_extract_to = ""

import zipfile
zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
zip_ref.extractall(directory_to_extract_to)
zip_ref.close()


# In[2]:

# Load the csv data
import pandas as pd
Location = "datasets/algebradata.csv"
df = pd.read_csv(Location)


# In[3]:

# Observe the data
df.head()
df.tail()


# In[4]:

# Drop any missing values
df = df.dropna()


# In[5]:

# The percentage of the students with a passing grade
# total number of students
total_count = len(df)
# number of students with A, B, C

pass_grade = len(df[(df['Grade'] == 'A') | (df['Grade'] == 'B') | (df['Grade'] == 'C')])

# percentage of passing grade
float(pass_grade) / total_count


# In[6]:

# Percentage of Women with a passing grade
women_total = len(df[df['Gender'] == 'F'])
pass_grade_female = len(df[(df['Gender'] == 'F') & ((df['Grade'] == 'A') | (df['Grade'] == 'B') | (df['Grade'] == 'C'))])
float(pass_grade_female) / women_total


# In[7]:

# Average hours of study for all students
df['Hours of Study'].mean()


# In[8]:

# average hours of study for students with passing grade
# pass_grade will be a dataframe of all students with passing grades
pass_grade = df[(df['Grade'] == 'A') | (df['Grade'] == 'B') | (df['Grade'] == 'C')]
pass_grade['Hours of Study'].mean()


# In[9]:

# Correlation between Hours of Study and Grade
# First convert Grades into Numeric data

def grade_convert(x):
    if x == "A":
        return 90
    if x == "B":
        return 80
    if x == "C":
        return 70
    if x == "D":
        return 60
    if x == "F":
        return 50


# In[10]:

# Change the 'Grade' Columns
df['Grade'] = df['Grade'].apply(grade_convert)
df.tail()


# In[11]:

# Correlation between Grade and Hours of Study
df.corr()


# In[12]:

# Change header name
headers = list(df.columns.values)
headers[4] = 'hours'
df.columns = headers
# Regression without intercept
import statsmodels.formula.api as sm
result = sm.ols(formula = 'Grade ~ hours -1', data = df).fit()
result.summary()

