#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from subprocess import check_call
import os
import glob
import shutil
import cv2
import pandas as pd
import numpy as np
from download_detection import dl_and_cut

d_set = 'yt_bb_detection_validation'
# Column names for detection CSV files
col_names = ['youtube_id', 'timestamp_ms','class_id','class_name', 'object_id','object_presence','xmin','xmax','ymin','ymax']

# Download & extract the annotation list
if not os.path.isfile(d_set+'.csv'):
    print (d_set+': Downloading annotations...')
    check_call(['wget', web_host+d_set+'.csv.gz'])
    print (d_set+': Unzipping annotations...')
    check_call(['gzip', '-d', '-f', d_set+'.csv.gz'])


dl_dir = 'sample'
d_set_dir = dl_dir+'/'+d_set+'/'
check_call(['mkdir', '-p', d_set_dir])

df = pd.DataFrame.from_csv(d_set+'.csv', header=None, index_col=False)
df.columns = col_names

# Get list of unique video files
vids = df['youtube_id'].unique()
idx = np.random.randint(len(vids))
vid =vids[idx]

print (vid+': Downloading and visulising ... ')
dl_and_cut(vid, df[df['youtube_id']==vid], d_set_dir)
imgs = sorted(glob.glob(d_set_dir+'/*/*.jpg'))
for im in imgs:
    image = cv2.imread(im)
    x1,y1,x2,y2 = np.array(im[:-4].split('_')[-4:],int)
    cv2.rectangle(image, (x1, y1), (x2, y2), (0,0,255), 2)
    out_fn = os.path.join(dl_dir, os.path.basename(im))
    print (vid+': writing '+out_fn)
    cv2.imwrite(out_fn,image)
shutil.rmtree(d_set_dir)
print (vid+': Visualisation done!')
