# YouTube BoundingBox

 ![Alt text](sample/eWyI5lsY0jg_07_0000_00178000_188_50_408_187.jpg?raw=true "Sample image")

This repo contains helpful scripts for using the [YouTube BoundingBoxes](
https://research.google.com/youtube-bb/index.html) 
dataset released by Google Research. The only current hosting method 
provided for the dataset is [annotations in csv
form](https://research.google.com/youtube-bb/download.html). The csv files contain links to the videos on YouTube, but it's up to you to download the video files themselves. For this
reason, these scripts are provided for downloading, cutting, and decoding
the videos into a usable form.

This script only downloads the frames that have been labelled for object detection.
Labels are available for 380,000 video segments of about 19s each.
Bounding box information is only available every second, so that is about 19 JPG images
per segment. However, the videos are encoded
at various framerates (I've found 24fps, 29.99fps, 30fps, ...).
That is why this script uses OpenCV to extract frames from the closest timestamps that have been labelled. 

*You can run `visualise_sample.py` first to check if everything is running okay before running the main script.*

This script was originally written by [Mark Buckler](https://github.com/mbuckler/youtube-bb).
The YouTube BoundingBoxes dataset was created and curated by Esteban Real,
Jonathon Shlens, Stefano Mazzocchi, Xin Pan, and Vincent Vanhoucke.
The dataset web page is [here](https://research.google.com/youtube-bb/index.html) and the
accompanying whitepaper is [here](https://arxiv.org/abs/1702.00824).

This fork was written by [Mehdi Shibahara](https://github.com/mehdi-shiba/youtube-bb-utility) and modified by Yiming Lin.

## Naming format
Different from other forks, this fork encodes the bounding box information directly into the file names, so the naming format of each image is

`[YOUTUBE_ID]_[CLASS_ID]_[OBJECT_ID]_[TIMESTAMP]_[X_TOP_LEFT]_[Y_TOP_LEFT]_[X_BOTTOM_RIGHT]_[Y_BOTTOM_RIGHT].jpg`

Check [here](https://github.com/yl1991/youtube-bb-utility/blob/9c3e4b7a31dd05b9a8883141e46cd7cff160c1fd/visualise_sample.py#L43) for an example of how to easily get the bounding box from the filename.

## Installing the dependencies
This repo was developed on Ubuntu 16.04 using conda 4.6.7 and Python 3.6.

1. Clone this repository.

2. Install majority of dependencies by running 
  + `pip install -r requirements.txt` in this repo's directory.
  + `conda install -c anaconda opencv`. 

Finally `cv2.VideoCapture` is working this way! See [the long-standing problem](https://github.com/ContinuumIO/anaconda-issues/issues/121) with installing OpenCV using Anaconda.

3. Install `wget` through your package manager.

## Running the scripts


### Download and decode

The `download_detection.py` script is provided for users who are interested in
downloading and decoding the videos which accompany the provided annotations. It also
cuts these videos down to the range in which they have been
annotated, then extract only the frames with label.
Parallel video downloads are supported so that you can
saturate your download bandwith even though YouTube throttles per-video.
*The frames with `absent` annotations are not decoded.*

Run `python download_detection.py [VIDEO_DIR] [NUM_THREADS]` to download the dataset into the specified
directory.

## Note
* Some videos may become unavailable as time goes on
* In my test, there are 200,600 valid videos, resulting in 4,771,439 decoded images.
* The size of the decoded dataset is around 340 GB.
