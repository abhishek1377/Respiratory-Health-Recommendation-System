# Respiratory-Health-Recommendation-System
Respiratory Health Recommendation System based on Air Quality Index Forecasts:

This project aims to provide predictions and visualization of Air Quality Index across 100 counties in United States.  Air quality index or AQI forecasts are important as it’s one of the most useful measure of air quality calculated from different pollutant concentrations in the air.  Currently there are websites providing AQI forecasts but do not provide customized health recommendations. Using this product, Individuals can take appropriate preventive measures based on our recommendations and public authorities can use AQI forecasts to make decisions for policy making, urban planning and well-being of public health. The project is an  end to end product that creates forecasts, provides visualizations, and delivers personalized health recommendations.

BigQuery database with an API was used to download EPA data as well as OpenWeatherMap API to compile the last 11 years of data for 6 key atmospheric pollutants which are CO, NO2, PM2.5, PM10, SO2, and O3. 

Data was cleaned for missing values. First rolled up data to county level from site level through max aggregation and used time series interpolation to fill in the possible missing values. Afterwards, we were finally able to select 100 counties across US which ensured enough data to effectively allow for model building. The individual pollutants time series data was merged with temperature, pressure, relative humidity, and windspeed to take climate conditions into account as well. As the final data consists of 11 years of data for 100 counties, there are around half a million observation points with 20 columns.

VAR(vector autoregression) has been used which being a multivariate approach, should capture the complexities in the models. Through VAR, novel geospatial effects have also been incorporated in our models, for which we added 5 neighbor counties data for each county for every day. 

Thus were created 100 models one for each county using VAR. Best models have been selected using optimum lag(number of past days  data to be used into a model) based on AIC and BIC values which were then used to forecast respective pollutant concentration Data and ultimately AQI.

Results were evaluated using Root Mean Square Error values and found out that forecasts are within acceptable error range for most of the counties. VAR is definitely an improvement over ARIMA and further hyper parameter tuning in conjunction with the availability of more recent data will even further improve the quality of forecasts.

Based on our merged and forecast datasets, we have created interactive visualisations, to see the past 11 years trends, and forecasts. Users can choose from 1 to 6 pollutants, data range and counties as per requirement.


![image](https://user-images.githubusercontent.com/15328642/151678210-3cff94d0-d508-4247-baa6-dab5478bb66f.png)

![image](https://user-images.githubusercontent.com/15328642/151678260-2a5dafb0-bdf5-470e-af1f-f85249243456.png)



