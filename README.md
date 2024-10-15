# London-Bike-Data-Analysis
## Project Summary
The analysis of London bike rides reveals distinct patterns in ridership based on time of day, reflecting commuting habits and the impact of weather and seasonal variations on bike usage. Peak hours for bike rides coincide with typical commuting times, suggesting the strong influence of work and school schedules on cycling behavior. This analysis offers valuable insights for urban planning and enhancing bike-sharing programs. Utilizing tools like Tableau for further visualization can provide stakeholders with actionable insights into trends in urban mobility, supporting data-driven decisions to promote cycling as a sustainable transport option.

![image](https://github.com/user-attachments/assets/c33b944e-931f-4bcd-a50b-6796f7716c32)
## Code Setup
You can simply download the London Bike Data in the data folder on this repository named 'london_merged.csv' and also download the code named London_Bike_Cleaning_Project.py in the src folder. To use this dataset ensure you have the necessary packages installed, and then read the data into a DataFrame using the command:

bike_df = pd.read_csv('C:/Users/Alex Hewitt/Downloads/london_merged.csv')

There is also a cleaned dataset in CSV format named 'london_bike.csv' available for use in Tableau.

Then to access the Tableau Project online the link is here: https://public.tableau.com/app/profile/alex.hewitt/viz/LondonBikeAnalysis_17289590936850/Dashboard2?publish=yes

## Code Overview
### 1.Loading Packages,Loading Dataset, and Data Exploration
Importing Necessary Packages The code begins by importing essential libraries: NumPy for numerical operations, Pandas for data manipulation and analysis.

![image](https://github.com/user-attachments/assets/53d5e950-b866-4685-91f9-4f42932bb216)

The code reads a dataset of London bike rides into a pandas DataFrame, which is a format designed for data analysis in Python. It uses the pd.read_csv() function to load the data from a file named london_merged.csv into the variable bike_df. This dataset includes information about bike rides in London, with details such as timestamps, weather conditions, temperatures, wind speed, and the number of rides recorded at specific times. By importing the dataset into bike_df, it becomes ready for analysis, manipulation, and visualization using pandas' data-processing features. This step is crucial for setting up the data to explore trends, analyze patterns, and create visualizations that show how bike ride activity is linked to weather and other factors.

![image](https://github.com/user-attachments/assets/3e871da8-e028-4b69-a3b3-574647978138)

The code starts by using the pd.read_csv() function from the pandas library to load the dataset named london_merged.csv into a DataFrame called bike_df. This step takes the data and puts it into a format that's easy to work with for analysis and manipulation using Python.

The dataset contains 17,414 rows, where each row represents a record of bike rides in London. It has 10 columns that include different pieces of information related to the rides, such as the timestamp, which tells the date and time of each ride, and the cnt column, which shows the number of bike rides that happened at that specific time.

The data also includes details like temperatures (t1 for the actual temperature and t2 for the "feels-like" temperature), humidity (hum), and wind speed (wind_speed). It uses a weather_code to classify the weather conditions and has flags to indicate whether a ride took place on a holiday (is_holiday) or a weekend (is_weekend). The season column shows the season when each ride happened.

The dataset takes up about 1.3 MB of memory, which is quite manageable for data analysis. The information in this dataset can help identify patterns in bike ride behavior based on things like weather, time of year, and specific conditions. This analysis can be useful for urban planning, improving bike-sharing services, or for businesses looking to understand bike traffic trends.

![image](https://github.com/user-attachments/assets/5858791a-f5d3-44a5-b8cd-a4f05f1075c4)

The code uses the bike_df.head() function to look at the first five rows of the dataset to see how the data is organized. This quick check helps confirm that the data was imported properly and gives an overview of the structure.

The output shows that each row represents an hour of bike ride data in London. The columns include details like timestamp, which tells the date and time of each ride, and cnt, which indicates how many bike rides happened in that specific hour. Other columns, such as t1 (temperature), t2 (feels-like temperature), hum (humidity), and wind_speed, provide information about the weather during those rides.

The weather_code column shows the weather type at that time, and the is_holiday and is_weekend columns indicate whether the ride occurred on a holiday or a weekend. The season column tells which season each ride took place in, using numbers to represent the seasons. This quick look at the data helps understand its structure and the kind of information available, setting up a good starting point for further analysis.

![image](https://github.com/user-attachments/assets/b963a75f-fc63-4245-a62e-9f17b69a0714)

### 2.Cleaning Data on Python


The code uses the value_counts() function on the season column to display all unique seasonal values and their counts. The result shows four unique numeric values representing seasons: 0.0, 1.0, 2.0, and 3.0, with counts of 4394, 4387, 4330, and 4303, respectively. This output indicates that the dataset has a relatively even distribution of data points across these four seasonal categories.

The purpose of checking these unique seasonal values and their counts is to understand the data's structure before converting these numeric codes into more descriptive string labels, such as "Winter," "Spring," "Summer," and "Fall." Replacing numeric values with string labels helps make the dataset more readable and easier to interpret when performing further analysis or visualizing the data.
![image](https://github.com/user-attachments/assets/6de312e7-b6dc-4ed2-a8fb-1b559f68a96e)


The code snippet retrieves the unique weather codes from the dataset and counts how many times each code appears using the value_counts() function. The output shows the distribution of different weather conditions represented by their corresponding numeric codes. For instance, code 1.0 indicates clear weather with 6,150 occurrences, while code 2.0 represents scattered clouds with 4,034 instances. Other codes represent various conditions, such as broken clouds (3.0), cloudy (4.0), rain (7.0), thunderstorms (10.0), and snowfall (26.0).

This analysis is essential for preparing the dataset for further processing. Since the weather codes are currently numeric, I plan to clean this data by converting these codes into descriptive strings that clearly indicate the weather condition they represent. This conversion will make the dataset more intuitive and easier to interpret, enhancing the overall analysis of bike ride patterns in relation to different weather conditions.

![image](https://github.com/user-attachments/assets/e89448fb-a2b1-45ff-bdc7-1578fdea5afc)


This code snippet performs several important data cleaning and transformation tasks on the London bike rides dataset. First, it converts the data types of the season and weather_code columns to integers using the astype(int) method. This conversion ensures that these columns are represented in the correct format for subsequent analysis, as they should contain whole number values rather than floating-point numbers.

Next, the code creates a new dictionary called new_columns that maps the original column names to more descriptive names. For instance, timestamp is renamed to time, cnt to count, and t1 to temp_c, among others. This renaming process enhances the clarity of the dataset by providing more intuitive and meaningful names for each column, making it easier for users to understand the data at a glance.

After renaming the columns, the updated DataFrame is saved back to the original CSV file using to_csv("london_merged.csv"). This step ensures that the changes made to the DataFrame are reflected in the dataset, allowing for future analyses to utilize the cleaned and updated column names.

Finally, the code converts the humidity values from a decimal format to a percentage by applying a lambda function that divides each humidity value by 100. This transformation is beneficial because it makes the humidity data more interpretable and relatable, as percentages are a more commonly understood way to represent humidity levels. Overall, these steps are crucial for preparing the dataset for effective analysis and visualization, enabling more accurate insights into bike usage patterns in relation to weather conditions.

![image](https://github.com/user-attachments/assets/30496837-c7d5-444d-88ea-42c41c13a43e)

This code snippet focuses on enhancing the readability of the season and weather columns in the London bike rides dataset by converting numerical values into descriptive string labels. First, a dictionary called season_dict is defined, mapping numerical season values to their corresponding string representations: '0' for Spring, '1' for Summer, '2' for Fall, and '3' for Winter. The code then converts the season column to a string type using astype('str') and applies the mapping with the map(season_dict) function. This transformation makes it easier for users to interpret the data since descriptive labels are generally more comprehensible than numerical codes.

Similarly, the code creates a dictionary named weather_dict, which maps numerical weather codes to meaningful string descriptions, such as '1' for Clear and '7' for Rain. Like the season column, the weather column is also converted to a string type and then mapped to the new descriptive values.

These changes are essential because they significantly improve the interpretability of the dataset. By using string labels instead of numbers, the dataset becomes more user-friendly, allowing anyone analyzing the data to quickly understand the context of each observation. This is particularly valuable for data visualization and reporting, where clear communication of results is crucial for stakeholders and decision-makers. Overall, these steps are part of the data preprocessing phase, aimed at preparing the dataset for effective analysis and ensuring that the information it contains is accessible and actionable.

![image](https://github.com/user-attachments/assets/6a3c1e55-1dca-4d85-89d3-ffa4a9ddafe9)

This segment of the analysis involves two important actions concerning the London bike rides dataset: displaying the first five rows of the cleaned DataFrame and saving the processed data into a new CSV file. The function bike_df.head() provides a preview of the top entries in the DataFrame, which allows for a quick inspection of the cleaned data structure and its contents. This step is essential for confirming that the data has undergone the necessary transformations, such as converting numerical values into descriptive strings for the weather and season columns.

The output from this function shows several columns, including time, count, temp_c, feel_like_temp_c, humidity, wind_speed_kph, weather, is_holiday, is_weekend, and season. Each row corresponds to a specific hour of bike ride data, detailing metrics like the number of rides, weather conditions, and temperature readings. This preview serves as a visual confirmation that the data is now in a more interpretable format, which is crucial for effective analysis and visualization.

After the inspection, the command bike_df.to_csv("C:/Users/Alex Hewitt/Downloads/london_bike.csv", index = False) is executed to save the cleaned DataFrame into a new CSV file named "london_bike.csv" at the specified file path. The index = False parameter ensures that the DataFrame's index is not included in the saved file, resulting in a cleaner and more straightforward CSV format for future use.

Creating this new CSV file is an important part of the data preprocessing workflow. It allows you to preserve all modifications made to the dataset, ensuring that the cleaned version is easily accessible for future analyses without the need to repeat the cleaning steps. Additionally, saving the cleaned data facilitates collaboration, enabling others to access the refined dataset for their own analyses. Overall, these actions not only validate the cleaning process but also set the stage for deeper data exploration and analysis.

![image](https://github.com/user-attachments/assets/cb53366c-6953-4f9b-81d9-6438e90a0fa8)

### 3.Data Summary and Hourly Analysis
As I embark on my Tableau project utilizing the cleaned dataset from london_bike.csv, my primary focus will be to analyze the total number of bike rides recorded in London between January 4, 2015, and December 31, 2016. This dataset, refined through extensive preprocessing in Python, provides a solid foundation for insightful analysis and visualization.

The total number of bike rides during this period amounts to 19,868,202. This figure highlights the extensive usage of the bike-sharing program in London and serves as a key metric for understanding biking trends and patterns over the specified timeframe. By visualizing this data in Tableau, I aim to explore various factors influencing bike usage, such as seasonal variations, weather conditions, and the impact of holidays and weekends on ridership.

Through this project, I will create interactive dashboards that not only showcase the total ride count but also provide deeper insights into how external factors correlate with bike usage. This analysis can inform city planners, bike-sharing services, and other stakeholders interested in promoting cycling as a sustainable mode of transportation in London. Overall, this project represents a significant step toward leveraging data analytics to foster a better understanding of urban mobility trends in the city.

![image](https://github.com/user-attachments/assets/0b5718f3-9f28-4ff5-a4a0-4287cd398203)

In summarizing the results of my hourly analysis of bike rides in London, several key observations emerge regarding ridership patterns throughout the day.

The highest ridership hours occur between 7 AM and 8 AM, with a peak at 8 AM, where bike rides reach a staggering 2,083,968. This indicates that morning commuters significantly contribute to the usage of the bike-sharing program, likely as people travel to work or school. Another peak is observed at 5 PM to 6 PM, with 2,056,327 rides logged during the 5 PM hour, suggesting that evening commute times also see substantial bike traffic.

Conversely, the lowest ridership hours are recorded during the early morning hours, particularly 4 AM with only 52,626 rides and 3 AM with 67,736 rides. This pattern indicates minimal bike usage during the night, likely due to reduced demand for transportation during these hours.

Overall, the analysis reveals a general trend where bike usage significantly increases during the morning and evening commute hours, reflecting the influence of work and school schedules on ridership. Notably, there is a noticeable dip in ridership during the late evening hours, particularly after 8 PM, highlighting a decrease in demand as the day winds down. This hourly analysis provides valuable insights into how bike-sharing services align with urban commuting patterns, which can inform strategies for optimizing bike availability and resources during peak times.

![image](https://github.com/user-attachments/assets/5a1426c6-5fd7-4fe5-909f-29d8c567875c)


### 4.Weather Impact Analysis
The analysis highlights that clear weather conditions result in the highest ridership, with over 7 million rides, followed by scattered clouds at approximately 6 million rides. This trend suggests that favorable weather significantly encourages bike usage, likely due to the more pleasant riding conditions.

Conversely, ridership declines sharply in adverse weather. For instance, the number of rides drops to around 1.5 million during rainy conditions and even lower during cloudy weather with about 925,613 rides. The impact is even more pronounced during snowfall, which accounts for only 14,941 rides, and thunderstorms, with a mere 8,168 rides.

Overall, these results indicate a clear trend: people are much more likely to utilize bike-sharing services in pleasant weather, while adverse conditions deter riders significantly. Understanding these weather-related patterns can help in planning and resource allocation for bike-sharing services, ensuring availability during favorable conditions and perhaps implementing strategies to encourage usage during less favorable weather.

![image](https://github.com/user-attachments/assets/412cbfa1-470f-4046-b0fa-23faf8b9268c)

The line graph analysis reveals significant insights into the relationship between bike ride counts, actual temperature (Temp C), and perceived temperature (Feel Like Temp C). In examining the temperature data, it becomes evident that lower bike counts correspond with colder temperatures. As the temperature decreases, there is a noticeable decline in ridership, indicating that cyclists are less inclined to ride in colder weather. Additionally, higher humidity levels are observed during these lower temperatures, which further diminishes cycling activity. An interesting anomaly occurs at a temperature of 10.33°C, where an unexpected drop in bike counts coincides with extremely high humidity (0.98), suggesting that very humid conditions can deter riders.

The most favorable conditions for cycling appear to be within a moderate temperature range of 7-20°C, where humidity levels are typically between 0.61 and 0.76. During this range, bike counts peak, with the highest number of rides recorded at 10.33°C and a humidity level of 0.7559. As temperatures rise beyond this optimal range, bike counts begin to decline, particularly when humidity drops to levels between 0.33 and 0.48. This trend suggests that extreme heat can also negatively impact cycling behavior.

Similarly, the analysis of the Feel Like Temp C data aligns closely with the findings related to actual temperature. Lower ride counts are consistently observed at both colder and hotter perceived temperatures. There is a notable drop in bike counts at 8.5°C and 10.33°C, which corresponds with periods of high humidity (0.77-0.98), indicating discomfort in such conditions. The peak for bike counts in this dataset occurs at a perceived temperature of 13°C and a humidity of 0.7559, reinforcing the idea that comfortable weather promotes cycling.

Interestingly, at a temperature of 21°C, bike counts exhibit a decline, with counts dropping to 492,937 for actual temperature, while the Feel Like Temp C shows a higher count of 722,712. This discrepancy indicates that perceived temperature can influence rider behavior in different ways compared to actual temperature. Overall, the trends highlighted in this analysis underscore the crucial role that both actual and perceived weather conditions play in shaping cycling patterns in London. Understanding these trends can aid urban planners and bike-sharing services in optimizing bike availability and encouraging cycling during favorable weather.

![image](https://github.com/user-attachments/assets/1612ae09-93d4-4d48-9b29-c0865cc122fb)


### 5.Seasonal and Temporal Analysis
The seasonal analysis of bike ride totals provides a clear understanding of cycling patterns throughout the year. The data indicates that Summer has the highest number of rides, totaling 6,424,609. This peak in ridership is likely attributed to warmer weather, longer daylight hours, and generally more favorable conditions for outdoor activities, making it the most popular season for cyclists.

Following Summer, Fall shows a significant count of 5,073,040 rides, which can be attributed to the moderate temperatures and picturesque scenery typical of this season, encouraging people to bike. In contrast, Spring reports a total of 4,850,237 rides, reflecting a gradual increase in cycling as the weather begins to warm up, although not as high as in Fall.

Winter records the lowest count with 3,520,407 rides, consistent with the colder temperatures and harsher weather conditions that discourage cycling. Overall, the analysis highlights a clear seasonal trend where ridership increases with warmer temperatures, peaking in the summer months and declining during the winter, underscoring the significant influence of seasonal weather on biking behavior in London.

![image](https://github.com/user-attachments/assets/3c8f90cb-d6de-42b9-ac62-51e9cf97721a)


The area chart provides a comprehensive visualization of bike rides in London, differentiating between the years 2015 and 2016 while organizing the data into quartile ranges (Q1 to Q4). Each quartile represents a specific season, with Q1 corresponding to Winter, Q2 to Spring, Q3 to Summer, and Q4 to Fall. The chart presents counts for three months in each quartile, segmented further by weather conditions—Broken Clouds, Clear, Cloudy, Rain, and Scattered Clouds. This structure allows for a detailed analysis of bike ride patterns across different seasons and weather conditions. Additionally, the chart features filters that enable users to explore data by weather type, season, and day type, distinguishing between weekends, holidays, all days, and weekdays.

Highlighting the key findings, the Summer season in both years had the highest bike ride counts, with Clear weather contributing significantly—recording 404,557 rides in 2015 and 577,541 in 2016. Conversely, Cloudy weather during the Summer saw the lowest counts, with only 19,854 rides in 2015 and 22,514 in 2016. Winter exhibited the lowest seasonal bike counts overall, with Scattered Clouds yielding the highest figures for this season, totaling 174,265 in 2015 and 227,409 in 2016.

The general trend reveals that bike ride counts are at their lowest in Winter, increase during Spring to become the second highest, peak in Summer, and then decline in Fall, where the counts are lower than in Spring, making Fall the third highest season for bike rides. Typically, lower bike ride counts are associated with Cloudy and Rainy weather conditions. In contrast, Clear weather dominates in both Spring and Summer, while Scattered Clouds lead in Winter and Fall, indicating a seasonal reversal in preferences.

The analysis of the filters indicates that Weekdays generally lead to a slight decrease in bike ride counts across all seasons, reinforcing the notion that weekday commuting may be less favorable for cycling. When applying the Holidays filter, a notable trend emerges, particularly in Spring (Q2) for 2015, where bike rides peak above 50,000 between April and May, showcasing increased cycling activity during holiday periods. However, 2016 shows a decline, with May only surpassing 40,000 rides. In Summer (Q3), bike rides reach nearly 10,000 in August for 2015, reflecting a consistent interest in cycling during warmer months. The data also highlights the Winter season's limited activity, with peaks in January and March reaching above 35,000 in 2016. Interestingly, no bike rides were recorded for Fall under the Holidays filter, indicating that holidays may not significantly influence cycling behavior during this season. Overall, the trends suggest that seasonal variations and specific days, such as weekends and holidays, significantly affect bike ride counts, aligning with the broader patterns observed throughout the dataset.

![image](https://github.com/user-attachments/assets/f6224577-5c0d-43c5-a409-90e259c03a16)

### 6.Wind Speed and Tempature Impact

The highlight table presents the relationship between wind speed (KPH) and temperature (°C) in relation to bike ride counts, illustrating how these two factors influence cycling activity. The table's design highlights values based on the frequency of bike rides, providing clear insights into the conditions that most encourage or deter biking. The analysis shows that the most bike rides tend to occur when the temperature ranges between 4.98°C and 22.41°C, with wind speeds between 3.52 KPH and 24.64 KPH. These ranges suggest that moderate temperatures and wind conditions are the most favorable for cyclists.

The specific data points indicate that the highest bike ride count was recorded at a temperature of 14.94°C and a wind speed of 10.56 KPH, reaching a peak of 631,940 rides. The second-highest count occurred at the same temperature of 14.94°C but with a higher wind speed of 17.60 KPH, resulting in 588,037 rides. This pattern highlights that while temperature has a consistent impact on cycling activity, variations in wind speed also play a significant role in influencing the number of rides, with moderate wind speeds being optimal.

Overall, the general trend in the model suggests that bike riding activity peaks during conditions of mild to warm temperatures combined with light to moderate wind speeds. Extremely low or high temperatures and strong winds seem to discourage cycling, as indicated by lower ride counts outside the identified ranges. These findings emphasize the importance of weather conditions in determining the level of cycling activity, with cyclists generally preferring days that are neither too hot nor too cold, and with manageable wind conditions that do not create too much resistance.

![image](https://github.com/user-attachments/assets/0ac6a5e5-6821-4c9d-bffe-45cc1339c97f)


