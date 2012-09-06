#!/usr/bin/python

APPDIR="/usr/share/applications"
from sys import argv,exit
from subprocess import Popen
import os
def usage():
	print "usage: mimeset appname"
	print "       mimeset --listapps"
	print "       mimeset --mimes appname"

def get_mimes(appname):
	try:
		with open(os.path.join(APPDIR, appname + ".desktop"), "r") as f:
			mimes = filter(lambda x: x.startswith("MimeType="), f.readlines())[0].split("MimeType=")\
					[1].rstrip().split(';')
	except:
		return
	mimes = filter(None, mimes)
	if mimes != []:
		return mimes
	
if __name__ == '__main__':
	if len(argv) == 1:
		usage()
		exit(0)
	if argv[1] == "--listapps":
		for a in map(lambda x: x.split(".desktop")[0], os.listdir(APPDIR)):
			if get_mimes(a):
				print a
		exit(0)
	if argv[1] == '--mimes':
		if len(argv) == 2:
			print "Error: option --mimes requires the argument"
			exit(1)
		mimes= get_mimes(argv[2])
		if not mimes:
			print argv[2], "don't contain mime types."
			exit(1)
		print "%s:" % argv[2], mimes
		exit(0)
	mimes= get_mimes(argv[1])
	if not mimes:
		print argv[1], "don't contain mime types."
		exit(1)

	for mime in mimes:
		cmd = ["xdg-mime", "default", argv[1]+".desktop", mime]
		print "xdg-mime default %s.desktop %s" % (argv[1], mime)
		Popen(cmd).wait()

