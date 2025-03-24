#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


print(sns.__version__)


# In[3]:


data = pd.read_csv("census_income_dataset.csv")
data.head()


# In[5]:


data.columns


# In[4]:


df = data.copy()


# In[7]:


len(df)


# In[8]:


df["AGE"]


# In[9]:


df[df["AGE"].isnull()]


# In[10]:


df["AGE"].value_counts()[:10]
count = df["AGE"].value_counts()
category = count.index
df["AGE"].value_counts()[:10]


# In[13]:


ret = plt.hist(df["AGE"], bins=5)
plt.show()
ret


# In[6]:


bins = np.arange(10, 100, 5)
plt.figure(figsize=(7,5))
sns.distplot(df["AGE"], kde=True, bins=bins, hist=True)

plt.title('Age Distribution of Respondents', fontsize=14)
plt.xlabel('Age (Years)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
sns.despine(left=True, bottom=True)
plt.tight_layout()
plt.show()


# In[8]:


bins = np.arange(10, 100, 5)
plt.figure(figsize=(7,5))
sns.distplot(df["AGE"], kde = True, bins=bins, hist = True)
plt.title('Age Distribution of Respondents', fontsize=14)
plt.xlabel('Age (Years)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
sns.despine(left=True, bottom=True)
plt.tight_layout()  

mean_age = df["AGE"].mean()
print("Mean:", mean_age)

# median
median_age = df["AGE"].median()
print("Median:", median_age)

# mode
mode_age = df["AGE"].mode().values[0]
print("Mode:", mode_age)


plt.axvline(x=mean_age, ls='--', lw=2, color='tab:orange', label=f'Mean: {mean_age:.0f} years')
plt.axvline(x=median_age, ls='--', lw=2, color='tab:green', label=f'Median: {median_age:.0f} years')
plt.axvline(x=mode_age, ls='--', lw=2, color='tab:red', label=f'Mode: {mode_age:.0f} years')
plt.rcParams['font.size'] = 12 # for now: 12, later: 8


plt.rcParams['svg.fonttype'] = 'none'

plt.legend(frameon=False)
plt.savefig("age_histogram.svg", bbox_inches="tight")
plt.savefig("age_histogram.png", bbox_inches="tight")
plt.show()


# In[9]:


df = data.copy()


# In[10]:


df["RELATIONSHIP"]


# In[11]:


df["RELATIONSHIP"].isnull().sum()


# In[12]:


df["RELATIONSHIP"].value_counts()


# In[14]:


count = df["RELATIONSHIP"].value_counts()
category = count.index
count = count.values
count, category


# In[15]:


plt.figure(figsize=(7,5))
status_counts = df['RELATIONSHIP'].value_counts()

status_counts.plot(kind='pie', autopct='%1.1f%%', startangle=180, colors=sns.color_palette('pastel'))
plt.title('Distribution of Relationship Status', fontsize=14)
plt.ylabel('')  # Hide the y-label
plt.rcParams['font.size'] = 12 # for now: 12, later: 8

# Make the text editable (in the SVG file)
plt.rcParams['svg.fonttype'] = 'none'
plt.savefig("relationship_pie_chart.svg", bbox_inches="tight")
plt.show()


# In[16]:


df = data.copy()


# In[17]:


df["EDUCATION"].value_counts()


# In[18]:


df["SALARY"].value_counts()


# In[19]:


salary_distribution = df.groupby(['EDUCATION', 'SALARY']).size().unstack(fill_value=0)
salary_distribution


# In[20]:


plt.figure()
salary_distribution = df.groupby(['EDUCATION', 'SALARY']).size().unstack(fill_value=0)

# Stacked Bar Chart
salary_distribution.plot(kind='bar', stacked=True, figsize=(10, 6), color=['#2E8B57', '#800080'], alpha=0.8)
plt.title('Salary Distribution by Educational Level', fontsize=14)
plt.ylabel('Number of Respondents', fontsize=12)
plt.legend(title='Salary', labels=['<=50K', '>50K'])

plt.show()


# In[21]:


plt.figure(figsize=(12, 8))
sns.heatmap(salary_distribution, annot=True, fmt='d', cmap='Blues')
plt.title('Salary Distribution by Education Level (Heatmap)', fontsize=20, fontweight='bold', pad=20)
plt.xlabel('Salary Category', fontsize=16, labelpad=10)
plt.ylabel('Education Level', fontsize=16, labelpad=10)
plt.xticks(rotation=0, fontsize=12)
plt.yticks(rotation=0, fontsize=12)
plt.show()


# In[22]:


plt.figure()
salary_distribution = df.groupby(['EDUCATION', 'SALARY']).size().unstack(fill_value=0)

# Stacked Bar Chart
fig, ax = plt.subplots(figsize=(7, 5))
salary_distribution.plot(kind='bar', stacked=True, ax=ax, width=0.85, alpha=0.9)

# Titles and Labels
ax.set_title('Salary Distribution by Educational Level', fontsize=14, pad=20)
ax.set_ylabel('Number of Respondents', fontsize=12, labelpad=10)
ax.set_xlabel('')

# Ticks
ax.set_xticks(range(len(salary_distribution.index)))
ax.set_xticklabels(salary_distribution.index, fontsize=12)
ax.tick_params(axis='y', labelsize=12)
sns.despine(trim=False)
plt.legend(frameon=False)
plt.rcParams['font.size'] = 12 # for now: 12, later: 8

# Make the text editable (in the SVG file)
plt.rcParams['svg.fonttype'] = 'none'
# Legend
ax.legend(title='Salary', labels=['≤50K', '>50K'], fontsize=12, title_fontsize=14, loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.savefig("Salary_dist_by_edu_level.svg", bbox_inches="tight")
plt.show()


# In[ ]:




