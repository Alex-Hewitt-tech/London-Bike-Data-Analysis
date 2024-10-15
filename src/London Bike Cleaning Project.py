#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Required Packages
import numpy as np
import pandas as pd


# In[58]:


#Reads in the London Bike data into a pandas dataframe
bike_df = pd.read_csv('C:/Users/Alex Hewitt/Downloads/london_merged.csv')


# In[59]:


#Exploring Data
bike_df.info()


# In[60]:


#To see the first 5 rows to see how the data is formatted
bike_df.head()


# In[61]:


#To see all unique seasonal values and their counts
bike_df.season.value_counts()


# In[62]:


#To see all unique weather 
bike_df.weather_code.value_counts()


# In[63]:


#Convernts these columns to integers
bike_df['season'] = bike_df['season'].astype(int)
bike_df['weather_code'] = bike_df['weather_code'].astype(int)

#Creates a new dictionary with the new column names
new_columns = {
    'timestamp' : 'time',
    'cnt' : 'count',
    't1' : 'temp_c',
    't2' : 'feel_like_temp_c',
    'hum' : 'humidity',
    'wind_speed' : 'wind_speed_kph',
    'weather_code' : 'weather',
    'is_holiday' : 'is_holiday',
    'is_weekend' : 'is_weekend',
    'season' : 'season'
}

#Renames the columns and then updates the csv to fit the new columns
bike_df = bike_df.rename(columns = new_columns)
bike_df.to_csv("london_merged.csv")

# Convert humidity values to percentage
bike_df['humidity'] = bike_df['humidity'].apply(lambda x: x / 100)


# In[64]:


#Makes the numerical season values into string values for better understanding of the variables
season_dict = {
    '0' : 'Spring',
    '1' : 'Summer',
    '2' : 'Fall', 
    '3' : 'Winter'
}

bike_df.season = bike_df.season.astype('str')
bike_df.season = bike_df.season.map(season_dict)

#Makes the numerical weather values into string values for better understanding of the variables
weather_dict = {
    '1' : 'Clear',
    '2' : 'Scattered Clouds',
    '3' : 'Broken Clouds',
    '4' : 'Cloudy',
    '7' : 'Rain',
    '10' : 'ThunderStorm',
    '26' : 'Snowfall'
}


bike_df.weather = bike_df.weather.astype('str')
bike_df.weather = bike_df.weather.map(weather_dict)


# In[65]:


bike_df.head()


# In[66]:


#Downloads my cleaned dataframe into a new csv
bike_df.to_csv("C:/Users/Alex Hewitt/Downloads/london_bike.csv", index = False)

