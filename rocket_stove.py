#! /bin/python3
'''`rocket_stove` module contains `rocket_stove()` method which renders \
a template of YouTube links.'''
from csv import reader
from flask import Flask
from flask import render_template


APP = Flask(__name__)  # initialize Flask instance
VIDEO_TITLE = []  # list of video titles
URL = {}  # dict values: URL, profile name, stove material


@APP.route('/')  # decorator modifies rocket_stove(); sets root route
def rocket_stove():
    '''`rocket_stove()` method renders list of YouTube links to a template.'''
    with open('csv/rocket_stove.csv') as _file:
        _reader = reader(_file)  # initialize csv.reader()
        next(_reader)  # skip column title row
        for record in _reader:
            VIDEO_TITLE.append(record[0])  # append video titles to list
            URL[record[0]] = [record[1]]  # append key/value to dict
    return render_template('template.htm', video_title=VIDEO_TITLE, url=URL)


if __name__ == '__main__':
    rocket_stove()  # if standalone
