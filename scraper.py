"""
Scrapes lists from Forbes.

Forbes API is undocumented so code could break if url structure is changed.
"""

import requests
import numpy as np
from pandas import DataFrame
from pathlib import Path

# Forbes lists
lists = [
  { 'type': 'person', 'year': 2017, 'uri': 'billionaires' },                  # World richest
    { 'type': 'person', 'year': 2017, 'uri': 'forbes-400' },                  # American richest 400
    { 'type': 'person', 'year': 2017, 'uri': 'hong-kong-billionaires' },      # Hong Kong richest 50
    { 'type': 'person', 'year': 2017, 'uri': 'australia-billionaires' },      # Australia richest 50
    { 'type': 'person', 'year': 2017, 'uri': 'china-billionaires' },          # China richest 400
    { 'type': 'person', 'year': 2017, 'uri': 'taiwan-billionaires' },         # Taiwan richest 50
    { 'type': 'person', 'year': 2017, 'uri': 'india-billionaires' },          # India richest 100
    { 'type': 'person', 'year': 2017, 'uri': 'japan-billionaires' },          # Japan richest 50
    { 'type': 'person', 'year': 2017, 'uri': 'africa-billionaires' },         # Africa richest 50
    { 'type': 'person', 'year': 2017, 'uri': 'korea-billionaires' },          # Korea richest 50
    { 'type': 'person', 'year': 2017, 'uri': 'malaysia-billionaires' },       # Malaysia richest 50
    { 'type': 'person', 'year': 2017, 'uri': 'philippines-billionaires' },    # Philippines richest 50
    { 'type': 'person', 'year': 2017, 'uri': 'singapore-billionaires' },      # Singapore richest 50
    { 'type': 'person', 'year': 2017, 'uri': 'indonesia-billionaires' },      # Indonesia richest 50
    { 'type': 'person', 'year': 2017, 'uri': 'thailand-billionaires' },       # Thailand richest 50
    { 'type': 'person', 'year': 2017, 'uri': 'self-made-women' },             # American richest self-made women
    { 'type': 'person', 'year': 2017, 'uri': 'richest-in-tech' },             # tech richest
    { 'type': 'person', 'year': 2017, 'uri': 'hedge-fund-managers' },         # hedge fund highest-earning
    { 'type': 'person', 'year': 2016, 'uri': 'powerful-people' },             # world powerful
    { 'type': 'person', 'year': 2017, 'uri': 'power-women' },                 # world powerful women
    { 'type': 'person', 'year': 0, 'uri': 'rtb' },                            # real-time world billionaires
    { 'type': 'person', 'year': 0, 'uri': 'rtrl' },                           # real-time American richest 400
]

url = 'http://www.forbes.com/ajax/list/data'
SOURCES_DIR = Path('./sources')

for forbes_list in lists:
    response = requests.get(url, params=forbes_list)

    if not SOURCES_DIR.exists():
        SOURCES_DIR.mkdir(exist_ok=True, parents=True)

    DataFrame(response.json()).to_csv('sources/forbes-{}.csv'.format(forbes_list['uri']))


