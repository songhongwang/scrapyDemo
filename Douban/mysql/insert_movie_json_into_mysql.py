#!/usr/bin/python
from sqlutils import SqlUtils
import json, sys, os

file_path = os.path.split(os.path.realpath(__file__))[0]  + "/../spiders/list_json.txt"

with open(file_path, "r") as file:
    str_movies_dict = file.read()
    #print(str_movies_dict)
    dict_movies = json.loads(str_movies_dict)
    print(len(dict_movies)) 

    mysql = SqlUtils()

    mysql.insert(dict_movies)
