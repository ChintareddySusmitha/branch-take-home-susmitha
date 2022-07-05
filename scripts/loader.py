import models as models
from collections import namedtuple
import requests
from pandas import json_normalize
import configparser
import pandas as pd

model = namedtuple("modelname", "name model fields")
models = [
    model(
        "Users",
        models.Users,
        ["gender", "email", "phone", "cell", "nat", "name_title", "name_first", "name_last", "login_uuid", "dob_date", "dob_age", "id_name", "id_value", "picture_large", "picture_medium", "picture_thumbnail"]
    ),
    model("Registration", models.Registration, ["login_uuid", "login_username", "login_password", "login_salt", "login_md5", "login_sha1", "login_sha256", "registered_date", "registered_age"]),
    model("Locations", models.Locations, ["login_uuid", "location_street_number", "location_street_name", "location_city", "location_state", "location_country", "location_postcode", "location_coordinates_latitude", "location_coordinates_longitude", "location_timezone_offset", "location_timezone_description"]),
]


def create_csv(name, model, fields, data):
    flattened_data = json_normalize(data, sep='_')
    flattened_data = flattened_data[fields]
    flattened_data = flattened_data.to_dict(orient='records')
    transformed_data = [model(**x).dict() for x in flattened_data]
    transformed_data = pd.DataFrame(transformed_data)
    transformed_data.to_csv(name + ".csv", encoding='utf-8-sig', index=False)

    print(f"{name}.csv is created...")


def iterate_models(data):
    for table in models:
        create_csv(table.name, table.model, table.fields, data)

if __name__ == "__main__":
    try:
        config = configparser.ConfigParser()
        config.read('config.ini')
        url = config['RANDOMUSER']['url']

        response = requests.get(url).json()
        data = response["results"]
        iterate_models(data)
    except:
        print("ERROR: Failed to retrieve data")