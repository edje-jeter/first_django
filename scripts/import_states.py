#!/usr/bin/env python

import csv
import sys
import os

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import State, StateCapital

# print os.path.abspath(__file__)

dir_name = os.path.dirname(os.path.abspath(__file__))
file_name = "states.csv"

# print "%s/%s" % (dir_name, file_name)
# print "{0}/{1}".format(dir_name, file_name)

states_csv = os.path.join(dir_name, file_name)

csv_file = open(states_csv, 'r')

reader = csv.DictReader(csv_file)

for row in reader:
    new_state, created = State.objects.get_or_create(name=row['state'])
    new_state.abbrev = row['abbrev']
    new_state.save()

    new_capital, created = StateCapital.objects.get_or_create(name=row['capital'])
    new_capital.lat = row['latitude']
    new_capital.lon = row['longitude']
    new_capital.pop = row['population']

    new_capital.state = new_state

    new_capital.save()


