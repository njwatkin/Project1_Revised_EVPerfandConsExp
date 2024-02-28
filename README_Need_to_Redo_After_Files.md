

# Electric Vehicle Performance and Consumer Experiences
---

![Presentation_Cover_Image](<Presentation/Images/Cover_and_General/Presentation_Cover.png>)

##Project Purpose
---

We explored data on electric vehicle (EV) attributes, performance, charging, and consumer experiences with a focus on how these are related to:
- Attributes: Real-world fuel economy and carbon dioxide emissions
- Costs:  The financial costs of buying and owning an EV
- Charging:  Charging times and trends
- Barriers:  Consumer barriers to EV adoption

##Project Questions
---
The questions for the projects were those we anticipated from an audience of vehicle manufacturers, EV engineers, and EV sales and marketing teams: 

- *Attributes: Real-world fuel economy and carbon dioxide emissions*:
   - Which EV models and manufacturers have the highest fuel economy and carbon dioxide emissions efficiencies?
   - When can we predict EVs will emit zero carbon dioxide and possibly contribute to carbon negativity?
- *Costs: The financial costs of buying and owning an EV*:
   - What is the greatest cost from owning an EV?
   - How do costs change over time?
- *Charging: Charging time and needs*:
   - What day of the week do most people charge EVs?
   - What is the average charge time and at what kilowatt-hours?
- *Barriers:  Consumer barriers to EV adoption*:  
   - Who is most likely to purchase an EV?
   - Why do people not purchase an EV?


##Secondary Research
---
Our first step was to conduct secondary research on EVs.   The secondary research helped in the following ways:
- Broaden our understanding of the existing research on EVs
- Identify our stakeholders
- Narrow areas for exploration
- Identify data sources

The secondary research exposed us to the variety of EV types on the market.  

![EVTypes](<Presentation/Images/Cover_and_General/EV_Types.png>)

Based on the secondary research, available datasets, and the current focus in popular media on EV cars, we opted to focus on EV cars (passenger cars and sports vehicles) for Project 1.  Accordingly, we preprocessed datasets so pickup truck and heavy utility vehicle data were not included in the analyses. 

Our primary audiences in the EV community would be:
- Vehicle manufacturers
- Engineers  and designers
- Dealerships

Our primary challenge during Project 1 ocurred during the secondary research.  There are several private companies who are growing their datasets on EV efficiency, performancing, and consumer sentiment.  However, these companies charge substantial licensing fees to access their data. Ultimately, we had to rely on publicly accessible data readily available on government websites or made available to us after asking and waiting for permissions.  For more details on these data sources, please see the next section.  


## About the Data
---

Each of the Project 1 teammates focused on one of four topics:

### 1.) Attributes:  Real-world fuel economy and carbon dioxide emissions

####Exploration(s):
- The relationship between EV model and real-world fuel economy
- Differences among manufacturers
- EV CO2 emission trends over time/time series forecast

####Possible variables:
*Independent variables/Features*:   Model, manufacturer, EV type (BEVs, HEVs, PHEVs, FCEVS) horsepower, weight, footprint/vehicle size, battery or engine, seating capacity

*Dependent variables/Labels*:  Fuel economy, CO2, Charging rate and speed
Sources:

####Data Source:
The primary dataset used for the explorations was the US Environmental Protection Agency's (EPA's) *Automotive Trends Data*.  The link to the complete dataset and supporting material follow:
https://www.epa.gov/automotive-trends/explore-automotive-trends-data

The complete dataset can be filtered for specific variables, though this can be challenging and seemed dependent on the browser used with *internet explorer* proving more effective.

These are specific quotes from the EPA that characterize the dataset:
“The Trends database includes all new light-duty vehicles in the United States.”
“The Trends database has been maintained by EPA since 1975 and is updated annually to include the most up to date data available for all model years.”
“All data are based on production volumes delivered for sale in the U.S. by model year, and may vary from publicized data based on calendar year sales.”

#####*Licensure and Credits*:  
This dataset is open access. 
“Suggested data citation: US Environmental Protection Agency. 2023 EPA Automotive Trends Report. Data available at www.epa.gov/automotive-trends/explore-automotive-trends-data. Accessed December, 2023 and January, 2024.”

#####*Limitations of the Automotive Trends Data*:
The EPA's *Automative Trends Data* did not start tracking EVs car models till 2010. Consequently, EV car models are a smaller subset of the the much larger database. When interpeting findings about EVs from this dataset, it is recommended that the reader consider the limitations of a smaller sample size.  

### 2.) Costs:  The financial costs of buying and owning an EV
####Exploration(s):

####Possible variables:
*Independent variables/Features*:   

*Dependent variables/Labels*:  

####Data Source:

#####*Licensure and Credits*:  

#####*Limitations*: 

### 3.) Charging:  Charging times and trends
####Exploration(s):

####Possible variables:
*Independent variables/Features*:   

*Dependent variables/Labels*:  

####Data Source:

#####*Licensure and Credits*:  

#####*Limitations*: 

### 4.) Barriers: Consumer barriers to EV adoption
####Exploration(s):
 - The reasons consumers are hesitant to adopt EVs
 - Demographics of EV buyers
 - Concerns of consumers
 - Exposure of consumers to EVs

####Possible variables:
*Independent variables/Features*:   Types/models available, price, 

*Dependent variables/Labels*:  Charging - locations, rates, speed, number of units available

####Data Source: 2022 BEV and LCF Survey Report_FINAL_2 (consumerreports.org) and More Americans Would Buy an EV | Interest in Low-Carbon Fuels - Consumer Reports

#####*Licensure and Credits*:  This data set is open access.


#####*Limitations*: A large amount of the data regarding consumers was in reports, rather than data sets giving opinions and reasons to adopt and/or not adopt.



## Preprocessing and Analytics
---
### 1.) Attributes: 
#### Exploration:  The relationship between EV model and real-world fuel economy

#####Code (Includes log transformation of 'Real-World MPG'):

```
##Dependencies
import pandas as pd
import sklearn.datasets as dta
import scipy.stats as st
import matplotlib.pyplot as plt
import numpy as np

##Convert excel file to a Pandas dataframe.
df = pd.read_excel('/Users/kim/Desktop/EPA_EV_EnginePackage .xlsx')

## Clean data
# Create a mask where Vehicle Type column does not contain TruckSUV or Pickup
mask = ~df['Vehicle Type'].str.contains('Truck SUV|Pickup', case=False, na=False)

# Apply the mask to the DataFrame
cotwo_by_cfe_df = df[mask]

#Check that Trucks are now excluded from the dataset
cotwo_by_cfe_df['Vehicle Type'].unique() 

##Select columns for analysis
cotwo_by_cfe_df = cotwo_by_cfe_df[['Real-World CO2 (g/mi)', 'Real-World MPG']]

##Convert all columns in DataFrame to strings
cotwo_by_cfe_df.columns = cotwo_by_cfe_df.columns.astype(str)

## Convert column values to numeric.  Error=coerce changes any data to NaN that cannot be converted
cotwo_by_cfe_df['Real-World CO2 (g/mi)'] = pd.to_numeric(cotwo_by_cfe_df['Real-World CO2 (g/mi)'], errors='coerce')
cotwo_by_cfe_df['Real-World MPG'] = pd.to_numeric(cotwo_by_cfe_df['Real-World MPG'], errors='coerce')

## Drop any rows that have NaN values after conversion
cotwo_by_cfe_df = cotwo_by_cfe_df.dropna()

# Checking for missing data
missing_data = cotwo_by_cfe_df['Real-World CO2 (g/mi)'].isnull().sum()
print("Missing data: ", missing_data)

##Create plot(s)/chart(s)

# Transform the y data
ln_y = np.log(cotwo_by_cfe_df['Real-World MPG'])

# Calculate the line of best fit on the transformed data
m, b = np.polyfit(cotwo_by_cfe_df['Real-World CO2 (g/mi)'], ln_y, 1)

# Create a scatterplot of C02 and combined fuel economy/real-world mpg
plt.scatter(cotwo_by_cfe_df['Real-World CO2 (g/mi)'], ln_y)

# Add the line of best fit as a red dotted line
plt.plot(cotwo_by_cfe_df['Real-World CO2 (g/mi)'], m*cotwo_by_cfe_df['Real-World CO2 (g/mi)'] + b, 'g:')

# Label the axes and add a title
plt.xlabel('Real-World CO2 (g/mi)')
plt.ylabel('ln(Real-World MPG)')
plt.title('Scatterplot of CO2 and ln(MPG) with Line of Best Fit')

#Show plot
plt.show()

##Compute the correlation
correlation = cotwo_by_cfe_df['Real-World CO2 (g/mi)'].corr(cotwo_by_cfe_df['Real-World MPG'])

print("Correlation between 'Real-World CO2 (g/mi)' and 'Real-World MPG':", correlation)
```
#####Graph:
![EV_CO2_Rel](<Presentation/Images/EVAttributes/EV_CO2_Rel.png>)

#####Takeaway:
Electric vehicles emit less CO2 emissions than gasoline or diesel-powered vehicles traveling the same distance.  However, some electric car models are much less efficient than their competitors. 

#### Exploration:  The differences among manufacturers
#####Code:  
```
## Dependencies
import pandas as pd
import sklearn.datasets as dta
import scipy.stats as st
import matplotlib.pyplot as plt
import numpy as np

##Convert excel file generated by API to a Pandas dataframe.
df = pd.read_csv('/Users/kim/Desktop/EPA_ManufactureCars_EVFuelEco.csv')

## Clean data
# Create a mask where Regulatory Class column does not contain Truck
mask = ~df['Regulatory Class'].str.contains('Truck', case=False, na=False)

# Apply the mask to the DataFrame
evmanufac_cfe_df = df[mask] 

# Create a mask where Fuel Delivery column does not contain Carb, Port, TBI, GDI, and Diesel
mask2 = ~df['Fuel Delivery'].str.contains('Truck|Carb|Port|GDI|Diesel', case=False, na=False)

# Apply the mask to the DataFrame
evmanufac_cfe_df = df[mask2]

##Select columns for analysis
evmanufac_cfe_df = evmanufac_cfe_df[['Manufacturer','Real-World MPG']]
evmanufac_cfe_df.head()

#Convert all columns in DataFrame to strings
evmanufac_cfe_df.columns = evmanufac_cfe_df.columns.astype(str)

# Convert column to numeric.  Error=coerce changes any data to NaN that cannot be converted
evmanufac_cfe_df['Real-World MPG'] = pd.to_numeric(evmanufac_cfe_df['Real-World MPG'], errors='coerce')

## Drop any rows that have NaN values after conversion
evmanufac_cfe_df = evmanufac_cfe_df.dropna()

# Checking for missing data
missing_data = evmanufac_cfe_df['Real-World MPG'].isnull().sum()
print("Missing data: ", missing_data)

##Create plot(s)/chart(s)

# Group the data by Manufacturer and calculate the mean Real-World MPG for each class
gb_manufac = evmanufac_cfe_df.groupby('Manufacturer')['Real-World MPG'].mean()

# Sort the grouped data in descending order
gb_manufac = gb_manufac.sort_values(ascending=False)

# Create a bar chart
plt.figure(figsize=(28,6))
plt.bar(gb_manufac.index, gb_manufac.values)

# Add labels and title
plt.xlabel('Manufacturer')
plt.ylabel('Average Real-World MPG')
plt.title('Average Real-World MPG for Each Electric Vehicle Manufacturer')

# Show the plot
plt.show()
```

#####Graph:
![EV_Manuf](<Presentation/Images/EVAttributes/EV_Manuf.png>)
#####Takeaway:
Average EV real-world fuel economy/mpg has been considerably lower for Honda, GM, Suzuki, Stellantis, and VW models when compared to Lucid or Hyundai. 

#### Exploration:  Electric vehicle CO2 emission trends over time/time series forecast
#####Code:
```
##Install the required libraries and dependencies.  
!pip install prophet

##Import dependencies
import pandas as pd
from prophet import Prophet
import datetime as dt
import numpy as np

%matplotlib inline

##Store the data in a Pandas DataFrame and set the Model Year column as the Datetime Index.
#Convert excel file generated by API to a Pandas dataframe.
df = pd.read_excel('/Users/kim/Desktop/EPA_EV_EnginePackage .xlsx').dropna()

##Clean data
# Create a mask where Vehicle Type column does not contain TruckSUV or Pickup
mask = ~df['Vehicle Type'].str.contains('Truck SUV|Pickup', case=False, na=False)

# Apply the mask to the DataFrame
df = df[mask]

#Copy dataframe
df2 = df.copy()

# Replace 'Prelim. 2023' with '2023' in 'Model Year' and drop NaN values
df2['Model Year'] = df2['Model Year'].replace('Prelim. 2023', '2023')

df2 = df2.dropna()

# Convert 'Model Year' to integer
df2['Model Year'] = df2['Model Year'].astype(int)

# Convert columns to numeric.  Error=coerce changes any data to NaN that cannot be converted
df2['Real-World CO2 (g/mi)'] = pd.to_numeric(df2['Real-World CO2 (g/mi)'], errors='coerce')

# Sort the DataFrame by the Model Year
df3 = df2.sort_values('Model Year')

grouped_df = df3.groupby('Model Year')

grouped_df2 = grouped_df[['Real-World CO2 (g/mi)']].mean()

grouped_df2 = grouped_df2.dropna(how = 'any')

grouped_df2

##Prophet modeling
# Prepare original dataframe (df) for prophet modeling
prep_prophet = df[['Model Year', 'Real-World CO2 (g/mi)']].copy()  # Create a copy function causes prep_prophet to be a new, separate df that won't reference the original df.  

# Replace 'Prelim. 2023' with '2023' in 'Model Year' and drop NaN values
prep_prophet['Model Year'] = prep_prophet['Model Year'].replace('Prelim. 2023', '2023')

prep_prophet2 = prep_prophet.dropna(how='any')

# Rename the columns to 'ds' and 'y' for Prophet
prophet_df2 = prep_prophet2.rename(columns={'Model Year': 'ds', 'Real-World CO2 (g/mi)': 'y'})

# Exclude rows where 'y' is 0
prophet_df2 = prophet_df2[prophet_df2['y'] != 0]

# Replace non-numeric values with NaN in 'y' column
prophet_df2['y'] = pd.to_numeric(prophet_df2['y'], errors='coerce')

# Remove rows with non-finite 'y' values (NaN or inf)
prophet_df2 = prophet_df2[np.isfinite(prophet_df2['y'])]

# Convert 'y' column to integer
prophet_df2['y'] = prophet_df2['y'].astype(int)

# Convert 'ds' column to string
prophet_df2['ds'] = prophet_df2['ds'].astype(str)

# Add fake month and day, '-01-01', to 'ds' column and convert it to datetime
prophet_df2['ds'] = pd.to_datetime(prophet_df2['ds'] + '-01-01')

# Drop any rows with NaN values
prophet_df2 = prophet_df2.dropna()

# Call the Prophet function, store as an object
prophet_model = Prophet()

# Fit the time-series model.
prophet_model.fit(prophet_df2)

# Create a future dataframe to hold predictions
# Make the prediction go out as far as 5 years
evcotwo_trends = prophet_model.make_future_dataframe(periods = 5, freq='Y')

# Make the predictions for the trend data using the evoctwo DataFrame
forecast_evcotwo_trends = prophet_model.predict(evcotwo_trends)

# Plot the Prophet predictions 
fig1 = prophet_model.plot(forecast_evcotwo_trends, xlabel='Model Year', ylabel='Real-World CO2 (g/mi)')
```

#####Graph:
![FCast](<Presentation/Images/EVAttributes/FCast.png>)

#####Takeaway:
EVs are trending toward zero CO2 emissions by 2027.  However, the small sample size does limite this interpretation.  


### 2.) Costs: The financial costs of buying and owning an EV:
#### Exploration:  What is the greatest cost from owning an EV?
#####Code:
#####Takeaway:
#### Exploration:  How do costs change over time?
#####Code:
#####Takeaway:
### 3.) Charging: Charging time and needs:
#### Exploration:  What day of the week do most people charge EVs?
#####Code:
```
## Dependencies
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
import numpy as np

## Convert excel file generated by API to a Pandas dataframe.
df = pd.read_excel('/Users/kim/Desktop/ev.charge.xlsx')

## Groupby 'weekday' and calculate the mean of 'chargeTimeHrs'
average_charge_time = df.groupby('weekday')['chargeTimeHrs'].mean()

## Sort the average charge time in descending order
average_charge_time2 = average_charge_time.sort_values(ascending=False)

##Plot
average_charge_time2.plot(kind='bar')

# Add labels and title
plt.title('Average Charge Time by Weekday')
plt.xlabel('Weekday')
plt.ylabel('Average Charge Time (Hrs)')

#Show plot
plt.show()

```
#####Graph:
![EVCharge_TBWD](<Presentation/Images/EVCharging/EVCharge_TBWD.png>)

#####Takeaway:
Average overall charge is 2.82 hours, using 5.81kW. Charge times are greatest on Wednesdays with an average of 2.94 hours needed to charge an EV. Sunday is the lowest at 2.1 hours. It is not until the weekend days that we see a substantial drop in the hours needed to charge an electric vehicle. There is only a gradual decline over the days of the work week.

#### What is the average charge time and at what kilowatt-hours?
#####Code:
#####Graph:
#####Takeaway:

### 4.) Barriers:  Consumer barriers to EV adoption:  
#### Exploration:  Who is most likely to purchase an EV?
#####Graph:  ![FCast](<Presentation/Images/ConsumerExperience/BarriersToEVAdoption.png>)
#####Takeaway: The demographics of a typical EV buyer are male, young adult, with a higher education, a higher income level and live in an urban area. 

#### Exploration:  Why do people not purchase an EV?
#####Code:
#####Graph:  ![FCast](<Presentation/Images/ConsumerExperience/ConsumerConcerns.png>)
#####Takeaway: The majority of consumers are not knowledgeable on the subject of Electric Vehicles.  Without this knowledge, they are hesitant to make a purchase.


## Directory Structure
---
- Project1_Work Plan.xlsx/
Initial project workplan
- Code/
contains all code by subtopic
- Data/
contains all datasets by subtopic
- Presentation/
contains the final presentation and its images
- README.md

