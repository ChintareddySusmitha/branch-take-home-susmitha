# contains data classes
import pydantic
from pydantic.dataclasses import dataclass

class Users(pydantic.BaseModel):
    gender: str
    login_uuid: str
    name_title: str
    name_first: str
    name_last: str
    email: str
    dob_date: str
    dob_age: str
    phone: str
    cell: str
    id_name: str = None
    id_value: str
    picture_large: str
    picture_medium: str
    picture_thumbnail: str
    nat: str

    @pydantic.validator('id_value', pre=True, always=True)
    def default_created(cls, id_value):
        return id_value or ''

class Locations(pydantic.BaseModel):
    login_uuid: str
    location_street_number: str
    location_street_name: str
    location_city: str
    location_state: str
    location_country: str
    location_post_code: str = None
    location_coordinates_latitude: str
    location_coordinates_longitude:str
    location_timezone_offset: str
    location_timezone_description: str

    @pydantic.validator('location_post_code', pre=True, always=True)
    def default_created(cls, value):
        return value or ''


class Registration(pydantic.BaseModel):
    login_uuid: str
    login_username: str
    login_password: str
    login_salt: str
    login_md5: str
    login_sha1: str
    login_sha256: str
    registered_date: str
    registered_age: str

    
'''
sample data:

gender	:	male
name		{3}
    title	:	Mr
    first	:	Ahmet
    last	:	Babaoğlu
location		{7}
	street		{2}
        number	:	5921
        name	:	Abanoz Sk
    city	:	Ankara
    state	:	Balıkesir
    country	:	Turkey
    postcode	:	33219
    coordinates		{2}
        latitude	:	68.8238
        longitude	:	-78.7471
	timezone		{2}
        offset	:	-6:00
    description	:	Central Time (US & Canada), Mexico City
email	:	ahmet.babaoglu@example.com
login		{7}
    uuid	:	02396114-de16-4925-802b-ec1b0ba9013d
    username	:	blackpanda939
    password	:	4242
    salt	:	25eyJktV
    md5	:	9afad83db3213920793f2c5d0da51161
    sha1	:	d43a7038b8fe0dedc4f91aa953a78a26f4c97b93
    sha256	:	933588497c6d45c3b835cbea32038e179787012e39158bb3549596c12d1a30b5
dob		{2}
    date	:	1987-12-13T21:27:58.739Z
    age	:	35
registered		{2}
    date	:	2003-06-03T02:18:01.257Z
    age	:	19
phone	:	(076)-500-2888
cell	:	(677)-569-1803
id		{2}
    name	:	
    value	:	null
picture		{3}
    large	:	https://randomuser.me/api/portraits/men/73.jpg
    medium	:	https://randomuser.me/api/portraits/med/men/73.jpg
    thumbnail	:	https://randomuser.me/api/portraits/thumb/men/73.jpg
nat	:	TR

'''