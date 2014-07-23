from urllib2 import urlopen
import codecs
import os, sys
import csv
import threading
import time
from datetime import datetime

channels8 = ['45001', 'KGNA', 'DULM5', '45006', 'SXHW3', 'KP59', 'KP53', 'PTIM4']
channels8dict = {}
channels4 = ['45001', '45006', 'KP53', 'KP59']
channelUrls = []
urlStem = 'http://www.ndbc.noaa.gov/data/realtime2/'

def createUrl(channels):
	"""takes in a channel array as an input, cycles through each item and tacks on the necessary text
	to make it a searchable url, returning the items from the input array and its url as k:v in a new dict"""
	for i in channels:
		appended = urlStem + i + '.txt'
		channels8dict.update({i:appended})
	return channels8dict

def getText(url):
	"""takes in a url and returns its html text"""
	page = urlopen(url)
	data = page.read()
	text = data.decode('utf8')
	#print(text)
	return text

def makeCsv(station, text):
	"""takes in a string (station id) and text, saves text as <station>.csv.txt in /data/ subdirectory"""
	reader = csv.reader(text)
	fileStem = '/Users/will/git/timelaps/data/'
	fileName = fileStem + station + '.csv.txt'
	ofile = open(fileName, 'wb')
	writer = csv.writer(ofile, dialect='excel')
	for row in reader:
		writer.writerow(row)
	ofile.close()
	return ofile

def makeFile(station, text):
	fileStem = '/Users/will/git/timelaps/data/'
	fileName = fileStem + station + '.txt'
	ofile = codecs.open(fileName, 'w', 'utf8')
	ofile.write(text)
	ofile.close
	
def run(dict):
	"""runs every function: takes in empty dictionary, passes its url as its value pair;
	pulls the html text from the url into 'data/<dictK/stationID>.csv.txt/;
	prints a timestamp once executed."""
	createUrl(channels4)
	for k,v in dict.items():
		raw = getText(v)
		#makeCsv(k, raw)
		makeFile(k, raw)
	print('run complete at ' + str(datetime.now()))

class TimerClass(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()

    def run(self):
        while not self.event.is_set():
            run(channels8dict)
            self.event.wait(3600)
			

    def stop(self):
        self.event.set()

tmr = TimerClass()
tmr.start()

time.sleep(604800)

tmr.stop()
