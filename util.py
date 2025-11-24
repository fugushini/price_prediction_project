import json
import pickle
import numpy as np
import pandas as pd

__locations = None
__data_columns = None
__model = None

def get_location_names():
    
   return __locations

def get_estimated_price(region, building_type, level, levels, rooms, area, kitchen_area, object_type):
    #x = np.array([region, building_type, level, levels, rooms, area, kitchen_area, object_type]).reshape(-1,1).T
    x = pd.DataFrame({
        "region": [region],
        "building_type": [building_type],
        "level": [level],
        "levels": [levels],
        "rooms": [rooms],
        "area": [area],
        "kitchen_area": [kitchen_area],
        "object_type": [object_type]
    })
    return round(__model.predict(x)[0].item(), 2)
    

def load_saved_artifacts():
    print("loading saved artifacts ... start")
    global __data_columns
    global __locations
    global __model
    with open(r"region_names.json", encoding='utf-8', mode="r") as f:
        __data_columns = json.load(f)["region_names"]
        __locations = __data_columns[:]
        
    with open(r"russian_home_prices_model.pickle", mode="rb") as f:
        __model = pickle.load(f)
    print("loading artifacts are ... done")


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price(3, 0, 2, 5, 2, 45.5, 20.5, 1))
    print(get_estimated_price(4417, 0, 2, 5, 2, 45.5, 20.5, 1))
    