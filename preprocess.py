import numpy as np
import torch
from datetime import datetime
class DataProcess:
    
    def __init__(self):
        pass

    def process(self, date_obj, plat, plong, dlat, dlong, fare_class,passenger_count ):
        date_obj = datetime.strptime(date_obj[:-4], '%Y-%m-%d %H:%M:%S')
        pickup_hour = date_obj.hour
        am_or_pm = [1 if pickup_hour < 12 else 0][0]
        weekday = date_obj.weekday()	
        def haversine_distance(lat1, long1, lat2, long2):
            r = 6371
            phi1 = np.radians(lat1)
            phi2 = np.radians(lat2)
            
            delta_phi = np.radians(lat2 - lat1)
            delta_lambda = np.radians(long2 -long1)
            
            a = np.sin(delta_phi/2)**2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda/2)**2
            c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
            d = (r * c)
            return d
        distance_km = haversine_distance(plat,plong, dlat, dlong)
        
        cat_array  = torch.LongTensor(np.array([pickup_hour,am_or_pm, weekday])).reshape(-1,3)
        cont_number_arry = torch.FloatTensor(np.array([fare_class, passenger_count,distance_km])).reshape(-1,3)
        return cat_array, cont_number_arry
        
# date = '2010-04-19 08:17:56 UTC'
# fare_class = 0
# passenger_count = 1
# plong = -73.992365
# plat = 40.730521
# dlong = -73.975499
# dlat = 40.744746
# a = DataProcess()
# print(a.process(date, plat, plong, dlat, dlong, fare_class, passenger_count))


