import pandas as pd 


def getdb():
    df = pd.read_csv('./data/uszips.csv')
    return df

def valid_zipcode(_zip):
    df=getdb()
    # To do : Create another way to check .isin? 
    # df['zip'].isin(['53186'])) ?? 
    if len(df[df['zip']==_zip]) == 0  :
        return False
    else :
        return True

def haversine_distance(lat1, lng1,lat2, lng2,in_miles=True): 

    from math import radians, cos, sin, asin, sqrt       
    lat1 , lng1  = radians(lat1) ,radians(lng1)
    lat2 , lng2  = radians(lat2) ,radians(lng2)
    dlng,dlat = lng2 - lng1  , lat2 - lat1 
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlng / 2)**2
    c = 2 * asin(sqrt(a))   
    r = 3956 if in_miles else 6371 # Radius of earth in kilometers
    return(c * r) 

def get_lat_lng(zip_):
    df=getdb()
    df_filter = df[df['zip']==zip_]
    if valid_zipcode(zip_) :
        lat,lon = df_filter.iloc[0]['lat'] , df_filter.iloc[0]['lng']
    else :
        return "ZIP code not valid"
    return lat, lon
   
def distance_between(zip1_, zip2_,in_miles=True):
    # vars 
    ERROR = False 
    ERROR_CODE= ""
    
    if valid_zipcode(zip1_) & valid_zipcode(zip2_) :
        valid_ = True
    else:
        valid_  = False
        ERROR_CODE = "Not a valid ZIP code"
        ERROR = True
        
    if valid_ :

        lat1, lng1 = get_lat_lng(zip1_)
        lat2, lng2 = get_lat_lng(zip2_)
        distance_ = round(haversine_distance( lat1, lng1, lat2, lng2,in_miles),2)
            
    if ERROR : 
        return ERROR_CODE
    else :
        return distance_