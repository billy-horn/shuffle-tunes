
import os
import vlc
from datetime import datetime
import pandas

def test():
	song_path = ''
	song = vlc.MediaPlayer('./Tribe-Part04.mp3')
	song.play()
	# song.set_time(10000)    # play at 10,000 ms (10 seconds)
	song.set_position(0.5) # 0 to 1

def get_file():
	psss

halloween_path = ''
xmas_path = ''
xmas_range = pd.date_range(start="2020-11-25",end="2020-12-30")
halloween_range = pd.date_range(start="2020-09-25",end="2020-11-02")


seasons = {"christmas": range(), 'halloween': }


now = datetime.now()
this_year = now.year

for season in seasons.keys():
	if seasons[]
if now.month in halloween_range.month \
	and now.day in halloween_range.day:
	print('yes')



