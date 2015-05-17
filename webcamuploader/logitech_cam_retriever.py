# -*- coding: utf-8 -*-

import urllib2
import settings
import re
import time
import sys


def print_debug(text):
    """Display debug information on screen tagged as such."""
    if settings.DEBUG:
        print
        u'[DEBUG] {!s}'.format(text)


def print_warning(text):
    """Display information on screen tagged as warning and propose to exit."""
    print
    u'[WARNING] {!s}'.format(text)
    if raw_input("Do you wish to interrupt? ([Y]|N) ") in ['y', 'Y', 'yes', '']:
        print_debug("Exiting...")
        sys.exit(0)
    print


def retieve_cam(cam):
    """Retrieve image for cam"""

    filename = '{0}-{1}.{2}'.format(cam['name'], time.strftime("%Y-%m-%dT%H%M%S"), 'jpg')
    token = get_token(cam)

    # Full Image https://alert.logitech.com/services/camera2.svc/00-12-AB-1D-89-7F/snapshot?_auth=
    # Viewable   https://alert.logitech.com/services/camera2.svc/00-12-AB-1D-89-7F/snapshotviewable?_auth=

    img_url = 'https://alert.logitech.com/services/camera2.svc/{0}/snapshotviewable?_auth={1}'.format(
        cam['settings']['mac'], token)

    f = open(filename, 'wb')
    f.write(urllib2.urlopen(img_url).read())
    f.close()

    return filename


def get_token(cam):
    auth_url = 'https://alert.logitech.com/Services/membership.svc/authenticate'
    post_data = '<AuthInfo><UserName>{0}</UserName><Password>{1}</Password></AuthInfo>'.format(
        cam['settings']['username'], cam['settings']['password'])

    r = urllib2.Request(auth_url, data=post_data,
                        headers={'Content-Type': 'application/xml', 'User-Agent': 'Mozilla/5.0'})
    u = urllib2.urlopen(r)
    u.read()

    token = None
    p = re.compile(ur'X-Authorization-Token: (.*)')

    for header in u.info().headers:
        matchObj = re.match(p, header)
        if matchObj:
            token = matchObj.group(1)
            print_debug("Auth Code is  : " + token)

    if not token:
        print_warning('Response did not return authorization code.')
        raise Exception('Response did not return authorization code.')

    return token

