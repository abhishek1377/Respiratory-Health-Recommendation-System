import pandas as pd

def calculate_AQI_O3_8hr(o3_8hour_level):
    c = round(o3_8hour_level,3)
    aqi = 0.0
    if pd.isnull(c) or c < 0.0:
#         print("AQI cannot be calculated for negative values. kindly check the input again")
        return 
    elif c <= 0.054:
        aqi = ((50-0)/(.054-0))*(c-0.0) + 0
    elif c <= 0.070:
        aqi = ((100-51)/(.070-0.055))*(c-0.055) + 51
    elif c <= 0.085:
        aqi = ((150-101)/(.085-0.071))*(c-0.71) + 101
    elif c <= 0.105:
        aqi = ((200-151)/(.105-0.086))*(c-0.086) + 151
    elif c <= 0.200:
        aqi = ((300-201)/(.200-0.106))*(c-0.106) + 201
    else:
        aqi = 500
#         print("8-hour O3 values do not define higher AQI values (≥ 301).  AQI values of 301 or higher are calculated with 1-hour O3 concentrations ")
    return int(round(aqi,0))

def calculate_AQI_O3_1hr(o3_1hour_level):
    # print("Areas are generally required to report the AQI based on 8-hour ozone values.  However, there are a small number of areas where an AQI based on 1-hour ozone values would be more precautionary.  In these cases, in addition to calculating the 8-hour ozone index value, the 1-hour ozone value may be calculated, and the maximum of the two values reported.")
    c = round(o3_1hour_level,3)
    aqi = 0.0
    if pd.isnull(c) or c < 0.0:
#         print("AQI cannot be calculated for negative values. kindly check the input again")
        return 
    elif c < 0.125:
#         print("Disregard those numbers and calculate the index using 8-hour ozone value")
        return
    elif c <= 0.164:
        aqi = ((150-101)/(.164-0.125))*(c-0.125) + 101
    elif c <= 0.204:
        aqi = ((200-151)/(.204-0.165))*(c-0.165) + 151
    elif c <= 0.404:
        aqi = ((300-201)/(.404-0.205))*(c-0.205) + 201
    elif c <= 0.504:
        aqi = ((400-301)/(.504-0.405))*(c-0.405) + 301
    elif c <= 0.604:
        aqi = ((500-401)/(.604-0.505))*(c-0.505) + 401
    else:
        aqi = 500
#         print("Note: Values above 500 are considered Beyond the AQI. Follow recommendations for the Hazardous category")

    return int(round(aqi,0))


def calculate_AQI_PM2point5(pm2point5_level):
    
    # print("If a different SHL for PM2.5 is promulgated, these numbers will change accordingly.")
    c = round(pm2point5_level,1)
    aqi = 0.0

    if pd.isnull(c) or c < 0.0:
#         print("AQI cannot be calculated for negative values. kindly check the input again")
        return 
    elif c <= 12.0:
        aqi = ((50-0)/(12.0-0.0))*(c-0.0) + 0
    elif c <= 35.4: 
        aqi = ((100-51)/(35.4-12.1))*(c-12.1) + 51
    elif c <= 55.4:
        aqi = ((150-101)/(55.4-35.5))*(c-35.5) + 101
    elif c <= 150.4:
        aqi = ((200-151)/(150.4-55.5))*(c-55.5) + 151
    elif c <= 250.4:
        aqi = ((300-201)/(250.4-150.5))*(c-150.5) + 201
    elif c <= 350.4:
        aqi = ((400-301)/(350.4-250.5))*(c-250.5) + 301
    elif c <= 500.4:
        aqi = ((500-401)/(500.4-350.5))*(c-350.5) + 401

    else:
        aqi = 500
#         print("Note: Values above 500 are considered Beyond the AQI. Follow recommendations for the Hazardous category")

    return int(round(aqi,0))

# print(calculate_AQI_PM2point5(279)) 

def calculate_AQI_PM10(pm10_level):
    
    # print("If a different SHL for PM2.5 is promulgated, these numbers will change accordingly.")
    c = round(pm10_level,0)
    aqi = 0.0

    if pd.isnull(c) or c < 0.0:
#         print("AQI cannot be calculated for negative values. kindly check the input again")
        return 
    elif c <= 54:
        aqi = ((50-0)/(54-0.0))*(c-0.0) + 0
    elif c <= 154: 
        aqi = ((100-51)/(154-55))*(c-55) + 51
    elif c <= 254:
        aqi = ((150-101)/(254-155))*(c-155) + 101
    elif c <= 354:
        aqi = ((200-151)/(354-255))*(c-255) + 151
    elif c <= 424:
        aqi = ((300-201)/(424-355))*(c-355) + 201
    elif c <= 504:
        aqi = ((400-301)/(504-425))*(c-425) + 301
    elif c <= 604:
        aqi = ((500-401)/(604-505))*(c-505) + 401
    else:
        aqi = 500
#         print("Note: Values above 500 are considered Beyond the AQI. Follow recommendations for the Hazardous category")

    return int(round(aqi,0))

# print(calculate_AQI_PM10(479))


def calculate_AQI_CO(co_level):
    
    c = round(co_level,1)
    aqi = 0.0

    if pd.isnull(c) or c < 0.0:
#         print("AQI cannot be calculated for negative values. kindly check the input again")
        return 
    elif c <= 4.4:
        aqi = ((50-0)/(4.4-0.0))*(c-0.0) + 0
    elif c <= 9.4: 
        aqi = ((100-51)/(9.4-4.5))*(c-4.5) + 51
    elif c <= 12.4:
        aqi = ((150-101)/(12.4-9.5))*(c-9.5) + 101
    elif c <= 15.4:
        aqi = ((200-151)/(15.4-12.5))*(c-12.5) + 151
    elif c <= 30.4:
        aqi = ((300-201)/(30.4-15.5))*(c-15.5) + 201
    elif c <= 40.4:
        aqi = ((400-301)/(40.4-30.5))*(c-30.5) + 301
    elif c <= 50.4:
        aqi = ((500-401)/(50.4-40.5))*(c-40.5) + 401
    else:
        aqi = 500
#         print("Note: Values above 500 are considered Beyond the AQI. Follow recommendations for the Hazardous category")
        

    return int(round(aqi,0))


def calculate_AQI_SO2(so2_level):
    
#     "1-hour SO2 values do not define higher AQI values (≥ 200). AQI values of 200 or greater are calculated with 24-hour SO2 concentrations."

    c = round(so2_level,0)
    aqi = 0.0

    if pd.isnull(c) or c < 0.0:
#         print("AQI cannot be calculated for negative values. kindly check the input again")
        return 
    elif c <= 35:
        aqi = ((50-0)/(35-0.0))*(c-0.0) + 0
    elif c <= 75: 
        aqi = ((100-51)/(75-36))*(c-36) + 51
    elif c <= 185:
        aqi = ((150-101)/(185-76))*(c-76) + 101
    elif c <= 304:
        aqi = ((200-151)/(304-186))*(c-186) + 151
    elif c <= 604:
        aqi = ((300-201)/(804-605))*(c-605) + 201
    elif c <= 804:
        aqi = ((400-301)/(804-605))*(c-605) + 301
    elif c <= 1004:
        aqi = ((500-401)/(1004-805))*(c-805) + 401
    else:
        aqi = 500
#         print("Note: Values above 500 are considered Beyond the AQI. Follow recommendations for the Hazardous category")

    return int(round(aqi,0))

# print(calculate_AQI_SO2(90))

def calculate_AQI_NO2(no2_level):
    
    
    c = round(no2_level,0)
    aqi = 0.0

    if pd.isnull(c) or c < 0.0:
#         print("AQI cannot be calculated for negative values. kindly check the input again")
        return 
    elif c <= 53:
        aqi = ((50-0)/(53-0.0))*(c-0.0) + 0
    elif c <= 100: 
        aqi = ((100-51)/(100-54))*(c-54) + 51
    elif c <= 360:
        aqi = ((150-101)/(360-101))*(c-101) + 101
    elif c <= 649:
        aqi = ((200-151)/(649-361))*(c-361) + 151
    elif c <= 1249:
        aqi = ((300-201)/(1249-650))*(c-650) + 201
    elif c <= 1649:
        aqi = ((400-301)/(1649-1250))*(c-1250) + 301
    elif c <= 2049:
        aqi = ((500-401)/(2049-1650))*(c-1650) + 401
    else:
        aqi = 500
#         print("Note: Values above 500 are considered Beyond the AQI. Follow recommendations for the Hazardous category")

    return int(round(aqi,0))



def calculate_AQI( pollutant = "", concentration_level = 0.0):
    aqi = 0.0
    if pollutant.lower() == "o3 8-hour":
        aqi = calculate_AQI_O3_8hr(concentration_level)

    if pollutant.lower() == "o3 1-hour":
        aqi = calculate_AQI_O3_1hr(concentration_level)

    if pollutant.lower() == "pm2.5":
        aqi = calculate_AQI_PM2point5(concentration_level)

    if pollutant.lower() == "pm10":
        aqi = calculate_AQI_PM10(concentration_level)

    if pollutant.lower() == "so2":
        aqi = calculate_AQI_SO2(concentration_level)

    if pollutant.lower() == "no2":
        aqi = calculate_AQI_NO2(concentration_level)
    
    if pollutant.lower() == "co":
        aqi = calculate_AQI_CO(concentration_level)
    
    return aqi

# print(calculate_AQI("no2",463))
