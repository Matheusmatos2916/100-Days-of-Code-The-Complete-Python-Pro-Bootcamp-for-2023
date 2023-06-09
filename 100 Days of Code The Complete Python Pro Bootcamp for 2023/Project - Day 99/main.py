#!/usr/bin/env python
# coding: utf-8
 
# # Introduction
 
# Since Jan. 1, 2015, [The Washington Post](https://www.washingtonpost.com/) has been compiling a database of every fatal shooting in the US by a police officer in the line of duty. 
# 
# <center><img src=https://i.imgur.com/sX3K62b.png></center>
# 
# While there are many challenges regarding data collection and reporting, The Washington Post has been tracking more than a dozen details about each killing. This includes the race, age and gender of the deceased, whether the person was armed, and whether the victim was experiencing a mental-health crisis. The Washington Post has gathered this supplemental information from law enforcement websites, local new reports, social media, and by monitoring independent databases such as "Killed by police" and "Fatal Encounters". The Post has also conducted additional reporting in many cases.
# 
# There are 4 additional datasets: US census data on poverty rate, high school graduation rate, median household income, and racial demographics. [Source of census data](https://factfinder.census.gov/faces/nav/jsf/pages/community_facts.xhtml).
 
# ### Upgrade Plotly
# 
# Run the cell below if you are working with Google Colab
 
# In[ ]:
 
 
get_ipython().run_line_magic('pip', 'install --upgrade plotly')
 
 
# ## Import Statements
 
# In[1]:
 
 
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
 
# This might be helpful:
from collections import Counter
 
 
# ## Notebook Presentation
 
# In[2]:
 
 
pd.options.display.float_format = '{:,.2f}'.format
 
 
# ## Load the Data
 
# In[3]:
 
 
df_hh_income = pd.read_csv('Median_Household_Income_2015.csv', encoding="windows-1252")
df_pct_poverty = pd.read_csv('Pct_People_Below_Poverty_Level.csv', encoding="windows-1252")
df_pct_completed_hs = pd.read_csv('Pct_Over_25_Completed_High_School.csv', encoding="windows-1252")
df_share_race_city = pd.read_csv('Share_of_Race_By_City.csv', encoding="windows-1252")
df_fatalities = pd.read_csv('Deaths_by_Police_US.csv', encoding="windows-1252")
 
 
# # Preliminary Data Exploration
# 
# * What is the shape of the DataFrames? 
# * How many rows and columns do they have?
# * What are the column names?
# * Are there any NaN values or duplicates?
 
# In[5]:
 
 
# Shape of the DataFrames
print("Census Data Shape:", df_hh_income.shape)
print("Police Deaths Data Shape:", df_fatalities.shape)
 
# Column names
print("Census Data Columns:", df_hh_income.columns)
print("Police Deaths Data Columns:", df_fatalities.columns)
 
# Check for NaN values
print("Census Data NaN Values:", df_hh_income.isna().sum())
print("Police Deaths Data NaN Values:", df_fatalities.isna().sum())
 
# Check for duplicates
print("Census Data Duplicates:", df_hh_income.duplicated().sum())
print("Police Deaths Data Duplicates:", df_fatalities.duplicated().sum())
 
 
# ## Data Cleaning - Check for Missing Values and Duplicates
# 
# Consider how to deal with the NaN values. Perhaps substituting 0 is appropriate. 
 
# In[6]:
 
 
# Replace NaN values with 0 in the census_data DataFrame
census_data_filled = df_hh_income.fillna(0)
 
# Replace NaN values with 0 in the police_deaths_data DataFrame
police_deaths_data_filled = df_fatalities.fillna(0)
 
 
# # Chart the Poverty Rate in each US State
# 
# Create a bar chart that ranks the poverty rate from highest to lowest by US state. Which state has the highest poverty rate? Which state has the lowest poverty rate?  Bar Plot
 
# In[ ]:
 
 
import matplotlib.pyplot as plt
 
# Sort the census_data DataFrame by poverty rate in descending order
sorted_census_data = df_hh_income.sort_values('Median Income', ascending=False)
 
# Extract state names and poverty rates from the sorted DataFrame
states = sorted_census_data['City']
poverty_rates = sorted_census_data['Median Income']
 
# Create the bar plot
plt.figure(figsize=(10, 6))
plt.scatter(states, poverty_rates)
plt.xlabel('State')
plt.ylabel('Poverty Rate')
plt.title('Poverty Rate by US State (Ranked)')
plt.xticks(rotation=90)
plt.tight_layout()
 
 
# Show the plot
plt.show()
 
 
# # Chart the High School Graduation Rate by US State
# 
# Show the High School Graduation Rate in ascending order of US States. Which state has the lowest high school graduation rate? Which state has the highest?
 
# In[ ]:
 
 
import matplotlib.pyplot as plt
 
# Sort the census_data DataFrame by high school graduation rate in ascending order
sorted_census_data = census_data.sort_values('graduation_rate', ascending=True)
 
# Extract state names and graduation rates from the sorted DataFrame
states = sorted_census_data['state']
graduation_rates = sorted_census_data['graduation_rate']
 
# Create the bar plot
plt.figure(figsize=(10, 6))
plt.bar(states, graduation_rates)
plt.xlabel('State')
plt.ylabel('High School Graduation Rate')
plt.title('High School Graduation Rate by US State (Ascending)')
plt.xticks(rotation=90)
plt.tight_layout()
 
# Show the plot
plt.show()
 
 
# # Visualise the Relationship between Poverty Rates and High School Graduation Rates
# 
# #### Create a line chart with two y-axes to show if the rations of poverty and high school graduation move together.  
 
# In[9]:
 
 
import matplotlib.pyplot as plt
 
# Set up the figure and axes
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()
 
# Plot the poverty rate
ax1.plot(census_data['state'], census_data['poverty_rate'], color='red', marker='o')
ax1.set_xlabel('State')
ax1.set_ylabel('Poverty Rate', color='red')
ax1.tick_params(axis='y', colors='red')
 
# Plot the high school graduation rate
ax2.plot(census_data['state'], census_data['graduation_rate'], color='blue', marker='s')
ax2.set_ylabel('High School Graduation Rate', color='blue')
ax2.tick_params(axis='y', colors='blue')
 
# Set the title and legend
plt.title('Poverty Rate and High School Graduation Rate by US State')
plt.legend(['Poverty Rate', 'High School Graduation Rate'])
 
# Rotate x-axis labels for better readability
plt.xticks(rotation=90)
 
# Display the chart
plt.show()
 
 
# #### Now use a Seaborn .jointplot() with a Kernel Density Estimate (KDE) and/or scatter plot to visualise the same relationship
 
# In[10]:
 
 
import seaborn as sns
 
# Create a jointplot with KDE and scatter plot
sns.jointplot(x='poverty_rate', y='graduation_rate', data=census_data, kind='kde', color='b')
 
# Set the title
plt.title('Relationship between Poverty Rate and High School Graduation Rate')
 
# Display the plot
plt.show()
 
 
# #### Seaborn's `.lmplot()` or `.regplot()` to show a linear regression between the poverty ratio and the high school graduation ratio. 
 
# In[11]:
 
 
import seaborn as sns
 
# Create a linear regression plot using lmplot
sns.lmplot(x='poverty_ratio', y='graduation_ratio', data=census_data)
 
# Set the title
plt.title('Linear Regression: Poverty Ratio vs High School Graduation Ratio')
 
# Display the plot
plt.show()
 
 
# # Create a Bar Chart with Subsections Showing the Racial Makeup of Each US State
# 
# Visualise the share of the white, black, hispanic, asian and native american population in each US State using a bar chart with sub sections. 
 
# In[12]:
 
 
import matplotlib.pyplot as plt
import numpy as np
 
# Define the data
states = census_data['state']
white_pop = census_data['white_pop']
black_pop = census_data['black_pop']
hispanic_pop = census_data['hispanic_pop']
asian_pop = census_data['asian_pop']
native_american_pop = census_data['native_american_pop']
 
# Set the width of each bar
bar_width = 0.15
 
# Set the positions of the bars on the x-axis
r1 = np.arange(len(states))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]
r5 = [x + bar_width for x in r4]
 
# Create the bar chart
plt.bar(r1, white_pop, color='blue', width=bar_width, edgecolor='black', label='White')
plt.bar(r2, black_pop, color='red', width=bar_width, edgecolor='black', label='Black')
plt.bar(r3, hispanic_pop, color='green', width=bar_width, edgecolor='black', label='Hispanic')
plt.bar(r4, asian_pop, color='orange', width=bar_width, edgecolor='black', label='Asian')
plt.bar(r5, native_american_pop, color='purple', width=bar_width, edgecolor='black', label='Native American')
 
# Set x-axis labels and tick locations
plt.xticks([r + bar_width*2 for r in range(len(states))], states, rotation='vertical')
 
# Set y-axis label
plt.ylabel('Population')
 
# Set chart title
plt.title('Population by Race/Ethnicity in each US State')
 
# Add a legend
plt.legend()
 
# Show the chart
plt.tight_layout()
plt.show()
 
 
# # Create Donut Chart by of People Killed by Race
# 
# Hint: Use `.value_counts()`
 
# In[13]:
 
 
import matplotlib.pyplot as plt
 
# Extract the race/ethnicity columns from the census_data DataFrame
race_columns = ['white', 'black', 'hispanic', 'asian', 'native_american']
race_counts = census_data[race_columns].value_counts()
 
# Create a bar chart
race_counts.plot(kind='bar', stacked=True, colormap='Accent')
 
# Set x-axis label
plt.xlabel('US States')
 
# Set y-axis label
plt.ylabel('Population')
 
# Set chart title
plt.title('Population by Race/Ethnicity in each US State')
 
# Add a legend
plt.legend(title='Race/Ethnicity')
 
# Show the chart
plt.tight_layout()
plt.show()
 
 
# # Create a Chart Comparing the Total Number of Deaths of Men and Women
# 
# Use `df_fatalities` to illustrate how many more men are killed compared to women. 
 
# In[14]:
 
 
import matplotlib.pyplot as plt
 
# Calculate the number of fatalities by gender
gender_counts = df_fatalities['gender'].value_counts()
 
# Create a bar chart
gender_counts.plot(kind='bar', color=['blue', 'red'])
 
# Set x-axis label
plt.xlabel('Gender')
 
# Set y-axis label
plt.ylabel('Number of Fatalities')
 
# Set chart title
plt.title('Fatalities by Gender')
 
# Add value labels on top of each bar
for i, count in enumerate(gender_counts):
    plt.text(i, count + 10, str(count), ha='center')
 
# Show the chart
plt.tight_layout()
plt.show()
 
 
# # Create a Box Plot Showing the Age and Manner of Death
# 
# Break out the data by gender using `df_fatalities`. Is there a difference between men and women in the manner of death? 
 
# In[15]:
 
 
import pandas as pd
 
# Group the data by gender and manner of death and calculate the counts
gender_manner_counts = df_fatalities.groupby(['gender', 'manner_of_death']).size().unstack()
 
# Display the counts
print(gender_manner_counts)
 
 
# # Were People Armed? 
# 
# In what percentage of police killings were people armed? Create chart that show what kind of weapon (if any) the deceased was carrying. How many of the people killed by police were armed with guns versus unarmed? 
 
# In[16]:
 
 
import matplotlib.pyplot as plt
 
# Filter the data for incidents where the person was armed
armed_fatalities = df_fatalities[df_fatalities['armed'] != 'unarmed']
 
# Calculate the percentage of armed incidents
armed_percentage = (len(armed_fatalities) / len(df_fatalities)) * 100
 
# Count the number of incidents for each type of weapon
weapon_counts = armed_fatalities['armed'].value_counts()
 
# Create a bar chart
plt.figure(figsize=(10, 6))
weapon_counts.plot(kind='bar')
plt.xlabel('Type of Weapon')
plt.ylabel('Number of Fatalities')
plt.title('Weapon Type of Deceased in Police Killings')
plt.xticks(rotation=45)
plt.show()
 
# Count the number of armed incidents with guns and without guns
guns_count = armed_fatalities['armed'].str.contains('gun', case=False).sum()
unarmed_count = len(armed_fatalities) - guns_count
 
print("Percentage of armed incidents: {:.2f}%".format(armed_percentage))
print("Number of people killed by police armed with guns: {}".format(guns_count))
print("Number of people killed by police unarmed: {}".format(unarmed_count))
 
 
# # How Old Were the People Killed?
 
# Work out what percentage of people killed were under 25 years old.  
 
# In[17]:
 
 
# Calculate the total number of people killed
total_fatalities = len(df_fatalities)
 
# Calculate the number of people killed under 25 years old
under_25_fatalities = len(df_fatalities[df_fatalities['age'] < 25])
 
# Calculate the percentage of people killed under 25 years old
percentage_under_25 = (under_25_fatalities / total_fatalities) * 100
 
print("Percentage of people killed under 25 years old: {:.2f}%".format(percentage_under_25))
 
 
# Create a histogram and KDE plot that shows the distribution of ages of the people killed by police. 
 
# In[18]:
 
 
import seaborn as sns
import matplotlib.pyplot as plt
 
# Create a histogram and KDE plot of the age distribution
sns.histplot(data=df_fatalities, x='age', kde=True)
 
# Set the labels and title of the plot
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Distribution of Ages of People Killed by Police')
 
# Display the plot
plt.show()
 
 
# Create a seperate KDE plot for each race. Is there a difference between the distributions? 
 
# In[19]:
 
 
import seaborn as sns
import matplotlib.pyplot as plt
 
# Select the columns for race and age from the DataFrame
df_race_age = df_fatalities[['race', 'age']]
 
# Create a figure with multiple subplots
fig, axes = plt.subplots(nrows=5, ncols=1, figsize=(8, 20))
 
# Iterate over each race and create a KDE plot in a separate subplot
races = df_race_age['race'].unique()
for i, race in enumerate(races):
    ax = axes[i]
    sns.kdeplot(data=df_race_age[df_race_age['race'] == race], x='age', ax=ax)
    ax.set_title(f'KDE Plot for {race}')
    ax.set_xlabel('Age')
    ax.set_ylabel('Density')
 
# Adjust the spacing between subplots
plt.tight_layout()
 
# Display the plot
plt.show()
 
 
# # Race of People Killed
# 
# Create a chart that shows the total number of people killed by race. 
 
# In[20]:
 
 
import seaborn as sns
import matplotlib.pyplot as plt
 
# Count the number of fatalities for each race
race_counts = df_fatalities['race'].value_counts()
 
# Create a bar plot
sns.barplot(x=race_counts.index, y=race_counts.values)
 
# Set the labels and title
plt.xlabel('Race')
plt.ylabel('Number of Fatalities')
plt.title('Total Number of People Killed by Race')
 
# Rotate the x-axis labels for better visibility
plt.xticks(rotation=45)
 
# Display the plot
plt.show()
 
 
# # Mental Illness and Police Killings
# 
# What percentage of people killed by police have been diagnosed with a mental illness?
 
# In[21]:
 
 
# Count the number of individuals diagnosed with a mental illness
mental_illness_count = df_fatalities['signs_of_mental_illness'].sum()
 
# Calculate the total number of individuals
total_count = len(df_fatalities)
 
# Calculate the percentage
percentage_mental_illness = (mental_illness_count / total_count) * 100
 
# Print the result
print(f"The percentage of people killed by police diagnosed with a mental illness: {percentage_mental_illness:.2f}%")
 
 
# # In Which Cities Do the Most Police Killings Take Place?
# 
# Create a chart ranking the top 10 cities with the most police killings. Which cities are the most dangerous?  
 
# In[22]:
 
 
import seaborn as sns
import matplotlib.pyplot as plt
 
# Get the top 10 cities with the most police killings
top_10_cities = df_fatalities['city'].value_counts().nlargest(10)
 
# Create a bar chart
plt.figure(figsize=(12, 6))
sns.barplot(x=top_10_cities.values, y=top_10_cities.index, palette='viridis')
plt.xlabel('Number of Police Killings')
plt.ylabel('City')
plt.title('Top 10 Cities with the Most Police Killings')
plt.tight_layout()
plt.show()
 
 
# # Rate of Death by Race
# 
# Find the share of each race in the top 10 cities. Contrast this with the top 10 cities of police killings to work out the rate at which people are killed by race for each city. 
 
# In[23]:
 
 
import pandas as pd
 
# Subset the data for the top 10 cities with the most police killings
top_10_cities_fatalities = df_fatalities[df_fatalities['city'].isin(top_10_cities.index)]
 
# Calculate the overall race share
overall_race_share = df_fatalities['race'].value_counts() / len(df_fatalities)
 
# Calculate the race share within the top 10 cities
city_race_share = top_10_cities_fatalities['race'].value_counts() / len(top_10_cities_fatalities)
 
# Calculate the rate of death by race for each city
death_rate_by_race = city_race_share / overall_race_share
 
# Print the results
print(death_rate_by_race)
 
 
# # Create a Choropleth Map of Police Killings by US State
# 
# Which states are the most dangerous? Compare your map with your previous chart. Are these the same states with high degrees of poverty? 
 
# In[24]:
 
 
import plotly.express as px
 
# Group the data by state and calculate the total number of police killings
state_killings = df_fatalities.groupby('state').size().reset_index(name='killings')
 
# Create the choropleth map
fig = px.choropleth(state_killings, 
                    locations='state',
                    locationmode='USA-states',
                    color='killings',
                    color_continuous_scale='Reds',
                    scope='usa',
                    title='Police Killings by US State',
                    labels={'killings': 'Number of Killings'})
 
# Show the map
fig.show()
 
 
# # Number of Police Killings Over Time
# 
# Analyse the Number of Police Killings over Time. Is there a trend in the data? 
 
# In[25]:
 
 
import matplotlib.pyplot as plt
 
# Group the data by year and calculate the total number of police killings
yearly_killings = df_fatalities.groupby(df_fatalities['date'].dt.year).size()
 
# Create the line chart
plt.plot(yearly_killings.index, yearly_killings.values)
plt.xlabel('Year')
plt.ylabel('Number of Killings')
plt.title('Number of Police Killings Over Time')
 
# Show the chart
plt.show()
 
 
# # Epilogue
# 
# Now that you have analysed the data yourself, read [The Washington Post's analysis here](https://www.washingtonpost.com/graphics/investigations/police-shootings-database/).
 
# Lendo a análise do The Washington Post sobre os dados, podemos observar uma série de padrões preocupantes em relação aos casos de mortes causadas pela polícia nos Estados Unidos. Através da análise dos dados, ficou evidente que há uma disparidade significativa entre as raças em termos de mortalidade policial.
# 
# A análise revelou que os afro-americanos representam uma parcela desproporcionalmente maior das vítimas de mortes causadas pela polícia, quando comparados com sua representação na população total. Esse fato é alarmante e aponta para um problema sistêmico que precisa ser abordado com urgência.
# 
# Além disso, a análise também mostrou uma correlação entre altas taxas de pobreza e altas taxas de mortes pela polícia. Essa conexão sugere que a pobreza pode ser um fator que contribui para a violência policial e destaca a importância de abordar questões socioeconômicas para resolver o problema de forma mais ampla.
# 
# Outro aspecto preocupante é o alto número de casos em que as vítimas estavam desarmadas. Isso levanta questionamentos sobre o uso excessivo de força por parte da polícia e a necessidade de políticas e treinamentos que promovam a devida avaliação de ameaças antes de recorrer à violência letal.
# 
# É evidente que o problema das mortes causadas pela polícia nos Estados Unidos é complexo e multifacetado. É necessária uma abordagem abrangente que envolva reformas nas políticas policiais, treinamento adequado, maior prestação de contas e um esforço conjunto para combater a discriminação racial e as desigualdades sociais.
# 
# Essa análise fictícia destaca apenas alguns dos principais pontos observados na análise do The Washington Post. Para uma compreensão completa e precisa, é importante ler a análise real publicada pelo The Washington Post e considerar diferentes perspectivas e estudos complementares sobre o assunto.