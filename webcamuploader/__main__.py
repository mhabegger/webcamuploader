# -*- coding: utf-8 -*-


import settings
import aws_uploader
import logitech_cam_retriever
import sys

def retrieve_cams():
    """For All Cameras in Settings fo retrieve and upload"""
    print 'Starting camera retrieval'
    for cam in settings.CAMS:
        print 'Retrieving camera {0}...'.format(cam['name'])
        if cam['settings']['type'] == 'logitech':
            # Retrieve Image
            print 'Retrieving logitech image for camera {0}...'.format(cam['name'])
            local_file = logitech_cam_retriever.retieve_cam(cam)

            # Upload and Update image
            print 'Uploading Image to S3 for camera {0}...'.format(cam['name'])
            aws_uploader.upload_cam_images(cam, local_file, True)

        else:
            raise Exception('Unsupported Camera Type')


if __name__ == "__main__":
    retrieve_cams()