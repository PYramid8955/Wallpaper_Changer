from datetime import datetime
from Packages.getUnsplImg import *
import os

WARNING_MSG = """###########################################################
# Be careful! Editing this can lead to unexpected errors! #
# Syntax:  (Suggest - run client.py, it'll edit it for u) #
# option=1|2|3                                            #
# search=STRING       - Only if the option is 2           #
# time=1|2|3|4                                            #
#                                                         #
# Values for option: Get wallpaper based on...            #
# 1 - The season.                                         #
# 2 - Your search query.                                  #
# 3 - Unsplash trending.                                  #
#                                                         #
# Values for time: How often do you want your wallpapers  #
# to change?                                              #
# 1 - On every log in                                     #
# 2 - Daily                                               #
# 3 - Weekly                                              #
# 4 - When season changes                                 #
###########################################################"""

with open("db.txt", "r") as f:
	db = f.read().split('\n')
db = {i.split("=")[0]: eval(i.split("=")[1]) for i in db[:db.index('###########################################################')]} # make a pretty dictionary from all the raw data obtained from the database by getting the data before comment, and then getting the keys and values using split and an inline for.

if db['time'] == 1:
	if db['option'] == 1:
		seasons = {(12, 1, 2): 'winter', (3, 4, 5): 'spring', (6, 7, 8): 'summer', (9, 10, 11): 'autumn'}
		now = int(datetime.now().strftime("%m"))
		for i in seasons.keys():
			if now in i:
				now = seasons[i]
		os.system('wget -O wallpaper ' + getLinks(now))
	elif db['option'] == 2:
		os.system('wget -O wallpaper ' + getLinks(db['search']))
	else:
		os.system('wget -O wallpaper ' + getLinks('trending'))
elif db['time'] in (2, 3):
	timeNow = datetime.now()
	ADD_TO_DATE = [datetime.timedelta(days=1), datetime.timedelta(weeks=1)]
	change = False
	if db['lastRun']:
		lastRun = db['lastRun'].split(' ')
		timeDB = datetime(lastRun[0], lastRun[1], lastRun[2]) + ADD_TO_DATE[db['time']-2]
		if timeDB <= timeNow: change = True
	if change or not db['lastRun']:
		if db['option'] == 1:
			seasons = {(12, 1, 2): 'winter', (3, 4, 5): 'spring', (6, 7, 8): 'summer', (9, 10, 11): 'autumn'}
			now = int(datetime.now().strftime("%m"))
			for i in seasons.keys():
				if now in i:
					now = seasons[i]
			os.system('wget -O wallpaper ' + getLinks(now))
		elif db['option'] == 2:
			os.system('wget -O wallpaper ' + getLinks(db['search']))
		else:
			os.system('wget -O wallpaper ' + getLinks('trending'))
		db['lastRun'] = timeNow.strftime('"%Y %m %d"')
		dbText = ''
		for i in range(len(db.keys())):
			dbText += db.keys()[i] + '=' + db.values()[i] + '\n'
		dbText += WARNING_MSG
		with open("db.txt", "w") as f:
			f.write(dbText)
		
	
else:
	seasons = {(12, 1, 2): 'winter', (3, 4, 5): 'spring', (6, 7, 8): 'summer', (9, 10, 11): 'autumn'}
	now = int(datetime.now().strftime("%m"))
	for i in seasons.keys():
		if db['lastRun'] in i:
			then = seasons[i]
		if now in i:
			now = seasons[i]
	if now != then:
		if db['option'] == 1:
			os.system('wget -O wallpaper ' + getLinks(now))
		elif db['option'] == 2:
			os.system('wget -O wallpaper ' + getLinks(db['search']))
		else:
			os.system('wget -O wallpaper ' + getLinks('trending'))
		
	
