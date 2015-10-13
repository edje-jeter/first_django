#!/usr/bin/env python

import urllib
import urllib2
from lxml import etree
import StringIO
import re
import sys
import os

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from main.models import State

result = urllib.urlopen("http://wwww.50states.com/")
html = result.read()

parser = etree.HTMLParser()
tree = etree.parse(StringIO.StringIO(html), parser)

href_xpath = "//*[@id='ar-full-homepage']/div/ul/li/a/@href"
filtered_html = tree.xpath(href_xpath)

links = [link for link in filtered_html if 'htm' in link]
# print links

for link in links:

    state_page = urllib.urlopen("http://www.50states.com%s" % link)
    state_page_html = state_page.read()

    tree = etree.parse(StringIO.StringIO(state_page_html), parser)

# - Find state abbreviations and correlate them to State model ----------
    state_abbrev_xpath = "//*[@id='content']/div[1]/div[2]/div/div[1]/h1/text()"
    state_abbrev_tree = tree.xpath(state_abbrev_xpath)
    state_abbrev_pattern = "(?<=\().."
    clean_state_abbrev_str = re.search(state_abbrev_pattern,
                                       str(state_abbrev_tree))
    if clean_state_abbrev_str:
        state_abbrev = str(clean_state_abbrev_str.group())

    state_obj = State.objects.filter(abbrev=state_abbrev).first()

# - Find State population and add it to State db ---------------------

    state_pop_xpath = "//*[@id='collapseQuick-Facts']/div/ul/li[6]/div/text()"
    state_pop_tree = tree.xpath(state_pop_xpath)

    if state_pop_tree:
        state_pop_string = str(state_pop_tree[0]).split(";")[0]
        state_pop_string = state_pop_string.replace(",", "")

        state_obj.pop = state_pop_string
        state_obj.save()

# - Find date of admission to union and add it to State db --------------

    state_admit_xpath = '//*[@id="collapseQuick-Facts"]/div/ul/li[1]/div/a/text()'
    state_admit_tree = tree.xpath(state_admit_xpath)

    if state_admit_tree:
        state_admit_string = str(state_admit_tree[0])
        state_obj.admit = state_admit_string
        state_obj.save()

# - Find rank of admission to union and add it to State db --------------

    state_rank_xpath = '//*[@id="collapseQuick-Facts"]/div/ul/li[1]/div/text()'
    state_rank_tree = tree.xpath(state_rank_xpath)

    if state_rank_tree:
        state_rank_string = str(state_rank_tree[0])

        state_rank_pattern = "\d+"
        clean_state_rank_string = re.search(state_rank_pattern,
                                            str(state_rank_string)).group()
        state_obj.rank = clean_state_rank_string
        state_obj.save()

# - Find state flag and add it to State db ------------------------------
    state_page = urllib.urlopen("http://www.50states.com%s" % link)
    state_page_html = state_page.read()

    tree = etree.parse(StringIO.StringIO(state_page_html), parser)

    state_flag_link_xpath = '//*[@id="content"]/div[1]/div[3]/div/a[2]/div/div/div[1]/img/@src'
    state_flag_tree = tree.xpath(state_flag_link_xpath)
    if state_flag_tree:
        flag_url = "http://www.50states.com/%s" % state_flag_tree[0]
        flag_url = flag_url.replace("small", "large")
        flag_img_response = urllib2.urlopen(flag_url).read()
        flag_img_temp = NamedTemporaryFile(delete=True)
        flag_img_temp.write(flag_img_response)
        flag_name = "%s_flag_img.gif" % state_obj.name.lower()
        state_obj.state_flag.save(flag_name, File(flag_img_temp))

# - Find state map and add it to State db -------------------------------

    state_map_link_xpath = "//*[@id='collapseGovernment']/div/ul/li[2]/div/a/@href"
    try:
        state_map_link = tree.xpath(state_map_link_xpath)[0]
    except Exception, e:
        pass

    state_map_page = urllib.urlopen(state_map_link)
    state_map_page_html = state_map_page.read()
    tree = etree.parse(StringIO.StringIO(state_map_page_html), parser)

    image_link_xpath = '//*[@id="innerPage"]/img/@src'
    state_map_image = tree.xpath(image_link_xpath)[0]

    url = 'http://quickfacts.census.gov/%s' % state_map_image
    image_response = urllib2.urlopen(url).read()

    img_temp = NamedTemporaryFile(delete=True)
    img_temp.write(image_response)
    map_name = "%s_map.gif" % state_obj.name.lower()

    try:
        state_obj.state_map.save(map_name, File(img_temp))
    except Exception, e:
        print e

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# First pass scraping state populations
    # try:
    #     state_pop_pattern = "\d+,\d+,\d+"
    #     cleaned_pop_string = re.search(state_pop_pattern,
    #                                    str(state_pop_string))
    #     # print cleaned_pop_string.group()
    #     state_object.pop = cleaned_pop_string.group()
    #     state_object.save()

    # except AttributeError, e:
    #     try:
    #         state_pop_pattern = "\d+,\d+"
    #         cleaned_pop_string = re.search(state_pop_pattern,
    #                                        str(state_pop_string))
    #         # print cleaned_pop_string.group()
    #         state_object.pop = cleaned_pop_string.group()
    #         state_object.save()

    #     except Exception, e:
    #         pass
