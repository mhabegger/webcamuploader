# WebcamUploader

Set of scripts for Logitech Alert Cam.

These scripts allow the retrieval of the current jpeg image of the camera and
upload the image to an s3 Bucket. 

## Configuration

Create a copy of the settings.dist.py named settings.py. Set the different values.
The name given to the camera will also be used as a prefix when uploading the image
to amazon S3.

Install python and pip

    sudo apt-get install python
    sudo apt-get install python-pip

Install the python requirements

    pip install -U -r pip_requirements.txt

## Usage

    $ python webcamuploader
    
Running the script will download the image locally and upload it twice two the S3 Bucket.  
Once as current.jpg and once as yyyy/mm/dd/hhmm.jpg


### CronJob

Use the following Cronjob line to set a recurrent job that uploads the iamges.

    $ TODO
    
## Contributors

* Mathieu Habegger [@mhabegger](https://github.com/mhabegger)

## License

webcamuploader
Copyright (C) 2015  Matheiu Habegger

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.