# image-collect

This simple python script is to poll an image from a URL and combine them into a gif sequence.

Create a `.env` file in the project's root directory with following environment variables:

```
HOURS_AGO=6 # integer. generate gif from images created X hours ago
IMAGE_URL="https://www.met.gov.my/data/radar_east.gif"
IMAGES_FOLDER="/home/cbasah/radar/images"
OUTPUT_GIF_FOLDER="/home/cbasah//radar"
OUTPUT_GIF_PREFIX="radar"
OUTPUT_GIF_INTERVAL_SECS=0.2 # seconds between frame images
PREFIX_DATESTR_SEPARATOR="_"
FILE_EXTENSION=".gif" # must begin with '.' e.g. '.gif', '.png'
```

## Use Case ##
For me, I use this script to collect the Malaysian Meteorological Department's radar image and to determine whether there is rain overnight.
