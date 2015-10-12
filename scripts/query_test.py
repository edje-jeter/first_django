#!/usr/bin/env python

import csv
import sys
import os

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

from main.models import State, StateCapital

# #list of all in database
# print State.objects.all()

# #list some in the database
# print State.objects.filter(name__startswith="Ala")

# #list a particular object
# state = State.objects.get(pk=55)
# print state.name
# print state.abbrev

# #order by pop of capital in descending order
# states = State.objects.all().order_by('-pop')

# #order by pop of capital in ascending order
# states = State.objects.all().order_by('pop')
# print states

# for state in states:
#     print state.name

#  # list some objects but exclude some (case-sensitive, 'N' != 'n')
# states = State.objects.all().exclude(name__contains='n')
#  # case-insenstive
# states = State.objects.all().exclude(name__icontains='N')
# # #
# for state in states:
#     print state.name

# # returns the list as a dictionary rather than a list
#states = State.objects.all().values()

# # not whole list, just particular components
# states = State.objects.all().values('name', 'pop')
# for state in states:
#     print state

# # returns list of tuples rather than dictionary
# states = State.objects.all().values_list('name', 'abbrev', 'pk')

# for state in states:
#     print state[2]
#     print state[0]

# states = State.objects.filter(name__startswith="N").values_list('name', 'abbrev', 'pk')

# for state in states:
#     print "State Name: %s, State Abbreviation: %s" % (state[0], state[1])

# # more flexible way of formatting
# states = State.objects.all().values_list('name', 'abbrev', 'pop')

# for name, abbrev, pop in states:
#     print "name:{2}, Abbrev: {0}, Pop:{1}".format(abbrev, pop, name)

# # filtering
# states = State.objects.all().exclude(name__startswith='N').filter(pop__gte='100000').order_by('-pop')

# print states

# for state in states:
#     print "%s %s" % (state.name, state.pop)

# same thing with values/dictionaries
# states = State.objects.all().exclude(name__startswith='N').filter(pop__gte=500000).order_by('-pop').values()

# print states

# for state in states:
#     print "%s %s" % (state['name'], state['pop'])

# # filter list using a sub-list
# states_list = ['Texas', 'California', 'Nevada', 'Alaska']

# states = State.objects.filter(name__in=states_list)

# print states

# after associating State and StateCapital, show the connection... (?)
# state = State.objects.get(name='Alabama')

# print state.statecapital_set.all()

# state = State.objects.get(pk=55)
# state2 = State.objects.get(pk=56)
# state3 = State.objects.get(pk=57)
# state4 = State.objects.get(pk=58)

# cap = StateCapital.objects.get(pk=1)
# cap2 = StateCapital.objects.get(pk=2)
# cap3 = StateCapital.objects.get(pk=3)

# state.statecapital_set.add(cap)
# cap.state.add(state)
# cap.state.add(state2)
# cap.state.add(state3)
# cap.state.add(state4)

# # print state.statecapital_set.all()
# print cap.state.all()
# print "------"
# print state.statecapital_set.all()


# states = State.objects.all()

# for state in states:
#     print "State: %s, Capital: %s" % (state.name, state.statecapital.name)

# # Try / Except for missing data
# states_list = ['Texas', 'Alabama', 'Alaska', 'Mars']

# for state in states_list:
#     try:
#         the_gotten_state = State.objects.get(name=state)
#         print "State found! %s" % the_gotten_state
#     except Exception, e:
#         print "State missing! %s" % e


