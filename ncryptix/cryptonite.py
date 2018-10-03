#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

# Import python libraries
import os
import sys
import requests
import validators
import dropbox
from pyrainbowterm import *

# Import local library
import _alert as alert


# Source code meta data
__author__ = 'Dalwar Hossain'
__email__ = 'dalwar.hossain@protonmail.com'


# Check internet connection
def __is_online():
    """
    This function checks Internet connectivity

    :return: (boolean) True, if online. False, otherwise
    """
    # Google will always be online, so if the device can reach google, it's online
    host = "http://www.google.com"
    time_out = 5

    # Check connectivity
    try:
        response = requests.get(url=host, timeout=time_out)
        alert.online()
        return True
    except requests.ConnectionError:
        alert.offline()


# Check if the remote host is alive
def __is_alive(remote_host_url=None, time_out=None):
    """
    This function checks if the host is alive/reachable/has HTTP access

    :param remote_host_url: (str) complete URL of the remote host
    :param time_out: (int) time out amount while checking the connection
    :return: (boolean) True, if alive. False, otherwise
    """
    # Validate that remote host argument is provided
    if remote_host_url is not None:
        # Remote host URL provided
        # Validate the URL
        url_is_valid = validators.url(remote_host_url)
        if url_is_valid:
            # Provided URL is valid
            # Set time out value
            if time_out is None:
                time_out = 5
            else:
                time_out = time_out
            # Check for a response
            try:
                response = requests.get(url=remote_host_url, timeout=time_out)
                response.raise_for_status()  # HTTP errors are not raised by default, this function raised HTTP errors
                return True
            except requests.ConnectionError:
                alert.offline()
            except requests.HTTPError as e:
                print('ERROR: {}'.format(e), log_type='info')
                alert.http_error()
        else:
            alert.invalid_url()
    else:
        alert.no_url()


# Check if the remote host has data or not
def __has_data(directory=None):
    """
    This function checks if the remote host has data or not

    :param directory: (str) name of the directory to look for data
    :return: (boolean) True, if the directory has data. False, otherwise
    """
    # dropbox_directory = '/' + directory
    dropbox_access_token = 'WzVm1LOMZnMAAAAAAAAI0QG_VlAFEgdfvG8A9ExqVOcZMBrXD5bKY0tqu3NOQRHE'
    dbx = dropbox.Dropbox(oauth2_access_token=dropbox_access_token)
    response = dbx.files_list_folder('')
    print(response.entries)
    pass
