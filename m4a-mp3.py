#!/usr/local/bin/python3
"""
M4A to MP3 convert script
require ffmpeg
usage:
$ python m4a-mp4.py source.m4a

above is as following ffmpeg command line
$ ffmpeg -i input.m4a -b:a 192k output.mp3

option:
BITS:  ffmpeg -ba option, it is mp3 bitrate. if you change another rate then you change BITS variable
"""
import argparse
import os
import subprocess

    
FFMPEG = 'ffmpeg -i '
BITS = ' -b:a 192k '

def call_ffmpeg(m4a_file):
    basename = split_basename(m4a_file)

    cmd = FFMPEG + m4a_file + BITS + basename + '.mp3'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    p.wait()
    return 

def split_basename(m4a_filename):
    return os.path.splitext(m4a_filename)[0]

def setup_args():
    p = argparse.ArgumentParser()
    p.add_argument('input_m4a', help='souce file (M4A format)')
    return p.parse_args()

if __name__ == "__main__":
    args = setup_args()
    print(args.input_m4a)

    basename = split_basename(args.input_m4a)
    print('base:', basename)
    call_ffmpeg(args.input_m4a)