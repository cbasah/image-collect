from dotenv import dotenv_values
import imageio
import imageio.v3 as iio
import os
from os import listdir
import pathlib
import requests
from datetime import datetime, timedelta

script_path = pathlib.Path(__file__).parent.resolve()
config = dotenv_values(f"{script_path}/.env")

# part 1: download current image
img_data = requests.get(config["IMAGE_URL"]).content
dtstr = datetime.now().strftime("%y%m%d_%H%M%S")
output_filename = f'{config["IMAGES_FOLDER"]}/{config["OUTPUT_GIF_PREFIX"]}{config["PREFIX_DATESTR_SEPARATOR"]}{dtstr}{config["FILE_EXTENSION"]}'
with open(output_filename, 'wb') as handler:
    handler.write(img_data)
    print(f"Saved {output_filename}")


# part 2: generated a gif from a sequence of past images
images = []
generated_gif_filename = f'{config["OUTPUT_GIF_FOLDER"]}/{config["OUTPUT_GIF_PREFIX"]}{config["FILE_EXTENSION"]}'
for filename in sorted(os.listdir(config["IMAGES_FOLDER"])):
    if (filename.endswith(config["FILE_EXTENSION"])):
        try:
            tokens = filename.replace(".gif", "").split(config["PREFIX_DATESTR_SEPARATOR"])
            datestr = tokens[1] + tokens[2]
            year = int("20" + datestr[0:2])
            month = int(datestr[2:4])
            day = int(datestr[4:6])
            hour = int(datestr[6:8])
            sec = int(datestr[8:10])
            filedt = datetime(year, month, day, hour, sec)
            earliestpossible = datetime.now() - timedelta(hours=int(config["HOURS_AGO"]))
            if filedt > earliestpossible:
                images.append(iio.imread(f'{config["IMAGES_FOLDER"]}/{filename}'))
                print(f"Appending {filename}")
        except Exception as e:
            print(f"Unable to add {filename} into gif. {e}")

imageio.mimsave(generated_gif_filename, images, duration=float(config["OUTPUT_GIF_INTERVAL_SECS"]))
print(f"Updated {generated_gif_filename}")
