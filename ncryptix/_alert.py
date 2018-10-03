#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

# Import python libraries
import sys
from pyrainbowterm import *


# Source code meta data
__author__ = 'Dalwar Hossain'
__email__ = 'dalwar.hossain@protonmail.com'


# Online
def online():
    """
    This function show online message

    :return: <>
    """
    print("Device is ", log_type='info', end='')
    print("ONLINE", color='green', text_format='bold')


# Offline
def offline():
    """
    This function shows offline message
    If the device is offline, program exits

    :return: <>
    """
    print("Device is ", log_type='info', end='')
    print("OFFLINE", color='red', text_format='bold')
    print("Please check Internet connection and try again!", log_type='info')
    sys.exit(1)


# HTTP error
def http_error():
    """
    This function shows http error message
    Python 'requests' doesn't raise http error by default
    :return: <>
    """
    print('HTTP error occurred!', log_type='info')


# Invalid URL
def invalid_url():
    """
    This function shows invalid URL message

    :return: <>
    """
    print('Provided URL is invalid! Please use a full URL (including http://)', log_type='info')


# No URL
def no_url():
    """
    This function shows no URL provided message

    :return: <>
    """
    print('No URL provided! Please provide a full valid URL', log_type='info')