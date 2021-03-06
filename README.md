# WebcamUploader

Set of scripts for Logitech Alert Cam.

These scripts allow the retrieval of the current jpeg image of the camera and
upload the image to an s3 Bucket. 

## Configuration

Create a copy of the settings.dist.py named settings.py. Set the different values.
The name given to the camera will also be used as a prefix when uploading the image
to amazon S3.

Install python, pip and other dependencies

    sudo apt-get install python
    sudo apt-get install python-pip
    sudo apt-get install python-dev
    sudo apt-get install libjpeg-dev
    sudo apt-get install zlib1g-dev
    sudo apt-get install libpng12-dev
    sudo apt-get install libfreetype6-dev

Install the python requirements

    pip install -U -r pip_requirements.txt
    
Update Timezone

    echo "Europe/Zurich" | sudo tee /etc/timezone
    sudo dpkg-reconfigure --frontend noninteractive tzdata
    sudo apt-get install ntp    

## Usage

    $ python webcamuploader
    
Running the script will download the image locally and upload it twice two the S3 Bucket.  
Once as current.jpg and once as yyyy/mm/dd/hhmm.jpg


### CronJob

Use the following Cronjob line to set a recurrent job that uploads the images.
If you cloned the repo into ubuntu's home directory, the default command to run the script would be
`python /home/ubuntu/webcamuploader/webcamuploader`

    */5  * * * * python /home/ubuntu/webcamuploader/webcamuploader > /dev/null
    
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