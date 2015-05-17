# -*- coding: utf-8 -*-

"""
Create your own settings.py file containing all the parameters entered here.
Add the values on your side and avoid exchange through the git repository.
"""
import os


DEBUG = True  # False


AWS_ACCESS_KEY = ''
AWS_SECRET_KEY = ''
AWS_BUCKET = 'bucket.name'

CAMS = [{'name': 'nameofcamera', 'title': 'Title for Image Name',
         'settings': {
             'type': 'logitech',
             'username': 'logitech_portal_username',
             'password': 'logitech_portal_password',
             'mac': 'mac_address_of_cam_see_portal'
         }
        }]