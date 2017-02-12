"""Script that monitors a dropbox file to start and drop different crytocoin miners"""
#!/usr/bin/python
import os
import datetime

def read_instructions_file():
	"""Reads instuctions file"""
	dropbox_folder_location = "[INSERT DROPBOX LOCATION]"
	instructions_file = open(dropbox_folder_location, "r")
	instuction = instructions_file.read(10)
	instructions_file.close()
	return instuction

def orchestrate_mining():
	"""Orchestration function"""
	instuction = read_instructions_file()
	time_to_stop = 2 # Stop mining if its 2 am

	time = datetime.datetime.now().hour
	print time

	if "stop" in instuction:
		kill_mining()
	elif "shutdown" in instuction:
		shutdown()
	elif "lite" in instuction:
		start_loincoin_mining()
	elif "doge" in instuction:
		start_doge_coin_mining()
	elif time == time_to_stop:
		shutdown()
	else:
		print "Nothing to do..."

def start_loincoin_mining():
	"""Starts litecoin mining"""
	lite_coin_url = "[URL]"
	lite_coin_username = "[USERNAME]"
	os.system("	C:\\cudaminer-2013-12-18\\x64\\cudaminer.exe -l auto -H 1 -i 0 -C 1 -D -o stratum+tcp://%s -O %s.1:1" % (lite_coin_url, lite_coin_username))

def start_doge_coin_mining():
	"""Starts dogecoin mining"""
	doge_coin_url = "[URL]"
	doge_coin_username = "[USERNAME]"
	os.system("C:\\cudaminer-2013-12-18\\x64\\cudaminer.exe -l auto -H 1 -i 0 -C 1 -D -o stratum+tcp://%s -O %s.1:1" % (doge_coin_url, doge_coin_username))

def shutdown():
	"""Shutdown mining PC"""
	os.system("shutdown -s")

def kill_mining():
	"""Kill the cudaminer"""
	os.system("TASKKILL /F /IM cudaminer.exe")

orchestrate_mining()
