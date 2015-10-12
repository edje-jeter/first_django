#!/usr/bin/env python

import csv
import sys
import os

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import State, StateCapital, City

# print os.path.abspath(__file__)

dir_name = os.path.dirname(os.path.abspath(__file__))
file_name = "zip_codes_states.csv"

# print "%s/%s" % (dir_name, file_name)
# print "{0}/{1}".format(dir_name, file_name)

cities_csv = os.path.join(dir_name, file_name)

csv_file = open(cities_csv, 'r')

reader = csv.DictReader(csv_file)

for row in reader:
    new_city, created = City.objects.get_or_create(zipc=row['zip_code'])
    new_city.abbrev = row['state']
    new_city.lat = row['latitude']
    new_city.lon = row['longitude']
    new_city.name = row['city']
    new_city.county = row['county']

    try:
        new_state = State.objects.get(abbrev=new_city.abbrev)
        new_city.state = new_state
    except Exception, e:
        new_city.state = None

    new_city.save()
