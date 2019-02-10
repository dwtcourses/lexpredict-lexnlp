#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import requests
from nose.tools import assert_list_equal

from lexnlp import get_module_path
from lexnlp.nlp.en.segments.titles import get_titles

__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2019, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-lexnlp/blob/master/LICENSE"
__version__ = "0.2.4"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"


def test_title_1():
    """
    Test first example title.
    :return:
    """
    # Setup URL
    url = "https://raw.githubusercontent.com/LexPredict/lexpredict-contraxsuite-samples/master/agreements/" + \
          "construction/1000694_2002-03-15_AGREEMENT%20OF%20LEASE-W.M.RICKMAN%20CONSTRUCTION%20CO..txt"

    # Download file
    file_text = requests.get(url).text

    assert_list_equal(list(get_titles(file_text)),
                      ["LEASE AGREEMENT"])


def test_title_2():
    """
    Test second example title.
    :return:
    """
    # Open file
    test_file_path = os.path.join(get_module_path(), "..", "test_data", "1100644_2016-11-21")
    with open(test_file_path, "rb") as file_handle:
        # Read and parse
        file_text = file_handle.read().decode("utf-8")
        assert_list_equal(list(get_titles(file_text)),
                          ["VALIDIAN SOFTWARE LICENSE AGREEMENT"])


def test_title_3():
    """
    test failure
    """
    text = """
    (1279209, 'en', 'C-106 TRANSPORTATION AND PUBLIC WORKS PERFORMANCE
    MEASURES Actual Forecast FY14 FY15 FY16 FY17 FY18 Traffic Engineering
     # of Miles of Roadway Striping 20 miles 10 miles 70 miles 10 miles
     10 Miles # of Signs Replaced 1,300 1,800 2,100 1,600 1,600 # of
     Traffic Signal Upgrades 2 15 18 25 30 Engineering Average Plan Review
      Time 6.9 days 6.13 days 8.34 days 7 days 7 days % Plan Reviews
      Completed Within 14 / 7 days 94% / 59% 94% / 67% 97% / 74% 100% /
       75% 100%/ 75% # Roadway Miles Receiving Major Roadway Maintenance
       57.8 miles 47 miles 45.0 miles 45.0 miles 45 miles Streets &
       Drainage Average Response Time for Street immediate Work Requests
       1 day 1 day 1 day 1 day 1day Percent of Street immediate work
       requests completed in 3 days 95% 90% 96% 95% 95% Percentage of
       staff hours utilized on recurring work activities 30% 33% 40% 45%
       45% Stormwater Utility Bill Collection Rate 94% 98% 95% 95% 95%
       Average Response Time for...', 1, , ...)"""
    assert_list_equal(list(get_titles(text)), [])
