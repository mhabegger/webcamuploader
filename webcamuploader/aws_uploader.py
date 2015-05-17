# -*- coding: utf-8 -*-

import settings
import image_label
import boto
from boto.s3.key import Key
import time
import os

def upload_cam_images(cam, img_path, del_after_upload = True):
    """Upload camera image and update current picture"""
    path, name = os.path.split(img_path)
    name, ext = os.path.splitext(name)
    current_cam_path = '{0}/{1}{2}'.format(cam['name'], 'current', ext)
    dated_cam_path = '{0}/{1}{2}'.format(cam['name'], time.strftime("%Y/%m/%d/%H%M"), ext)

    upload_public_file(settings.AWS_BUCKET, dated_cam_path, img_path)
    # Label and upload current
    current_path = 'current.jpg'
    image_label.label_image(cam, img_path, current_path)
    upload_public_file(settings.AWS_BUCKET, current_cam_path, current_path)
    os.unlink(current_path)

    if del_after_upload:
        os.unlink(img_path)

def get_or_create_bucket(bucketName):
    """Returns the bucket or creates a new one"""
    s3 = boto.connect_s3(settings.AWS_ACCESS_KEY, settings.AWS_SECRET_KEY,  host='s3-eu-west-1.amazonaws.com')

    try:
        bucket = s3.get_bucket(bucketName)
        return bucket
    except boto.exception.S3ResponseError:
        bucket = s3.create_bucket(bucketName, location='eu-west-1')
        set_right_bucket(bucket)
        return bucket


def get_website_endpoint(bucket):
    """Bypasses the us-east vs. eu-west issue on website endpoint"""
    endpoint = bucket.get_website_endpoint()
    return endpoint #.replace("us-east-1", "eu-west-1") works with spec connection


def set_right_bucket(bucket):
    """Sets the rights and website access on the bucket"""
    bucket.set_acl('public-read')
    bucket.configure_website("index.html")
    bucket.make_public(True, None)


def upload_public_file(bucketName, filename, filepath):
    """upload image to a bucket"""

    bucket = get_or_create_bucket(bucketName)
    newFile = Key(bucket)
    newFile.key = filename
    newFile.set_contents_from_filename(filepath)
    newFile.set_acl('public-read')

    return filename

def delete_public_file(bucketName, filename):
    """Delete file from a bucket"""

    bucket = get_or_create_bucket(bucketName)
    bucket.delete_key(filename)

    return filename

def get_public_urlprefix(bucketName):
    """Public Url to filename"""
    # TODO Handle https depending on AWS
    return "http://%s/" % bucketName

def get_public_image_url(bucketName, filename):
    """Public Url to filename"""
    return "%s%s" % (get_public_urlprefix(bucketName), filename)
