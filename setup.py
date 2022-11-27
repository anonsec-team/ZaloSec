#!/usr/bin/python
#coding=utf-8

__AUTOR__	= "Fnkoc"
__DATA__	= "10/07/15"
__GITHUB__	= "https://github.com/fnk0c"

'''Agradecimento especial ao Maximoz e BernardoGO'''

"""
    Copyright (C) 2015  Franco Colombino

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
"""

from sys import platform, argv
from os import system, path
from zipfile import ZipFile
from urllib import urlretrieve
import tarfile
 
try:
	if argv[1] == "install":
 
		linux = False
		windows = False
 
		if platform == "linux" or platform == "linux2":
			linux = True
		elif platform == "win32":
			windows = True
		else:
			print(" [-] This installer does not support your current system (%s)" % platform)
			exit()

		"""===L.I.N.U.X======================================================"""

		if linux == True:
			#Check which package manager is going to be use

			if path.isfile("/etc/apt/sources.list"):
				system("sudo apt-get install python-mechanize python-socksipy \
python-bs4 -y")

			elif path.isfile("/etc/pacman.conf"):
				#Socksipy can only be found on AUR. That's why we need to build
				system("sudo pacman -S python2-mechanize python2-beautifulsoup4\
 --needed")
				urlretrieve("https://aur.archlinux.org/packages/py/python-socks/PKGBUILD", "PKGBUILD")
				system("makepkg PKGBUILD")
				system("sudo pacman -U python-socks-1.5.0-1-any.pkg.tar.xz")
				system("rm -rf PKGBUILD python-socks-1.5.0-1-any.pkg.tar.xz pkg")

			elif path.isfile("/etc/yum.conf"):
				print(" [+] Downloading Modules ...\n")
				urlretrieve("https://pypi.python.org/packages/source/m/mechanize/mechanize-0.2.5.zip#md5=a497ad4e875f7506ffcf8ad3ada4c2fc", "mechanize.zip")
				with ZipFile("mechanize.zip", "r") as ZIP:
					ZIP.extractall(".")

				urlretrieve("https://pypi.python.org/packages/source/b/beautifulsoup4/beautifulsoup4-4.4.0.tar.gz#md5=63d1f33e6524f408cb6efbc5da1ae8a5", "bs4.tar.gz")
				with tarfile.open("bs4.tar.gz", "r:gz") as TAR:
	
	import os
	
	def is_within_directory(directory, target):
		
		abs_directory = os.path.abspath(directory)
		abs_target = os.path.abspath(target)
	
		prefix = os.path.commonprefix([abs_directory, abs_target])
		
		return prefix == abs_directory
	
	def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
	
		for member in tar.getmembers():
			member_path = os.path.join(path, member.name)
			if not is_within_directory(path, member_path):
				raise Exception("Attempted Path Traversal in Tar File")
	
		tar.extractall(path, members, numeric_owner=numeric_owner) 
		
	
	safe_extract(TAR, ".")

				urlretrieve("https://github.com/Anorov/PySocks/archive/1.5.0.zip", "socks.zip")
				with ZipFile("socks.zip", "r") as ZIP:
					ZIP.extractall(".")

				for i in ("mechanize-0.2.5", "beautifulsoup4-4.4.0", "PySocks-1.5.0"):
					system("cd %s && sudo python setup.py install" % i)
				
				system("rm -rf socks* bs4.tar.gz beautiful* mechanize* PySocks*")

			else:
				print(" [-] This installer does not support your distribution. \
Please install manually")
				exit()

			#Remove if already installed
			if path.isfile("/usr/bin/anonsec"):
				system("sudo rm -rf /usr/bin/anonsec")
				system("sudo rm -rf /usr/share/anonsec")

			#Creates Symlink
			with open("anonsec", "w") as symlink:
				symlink.write("#!/bin/bash\n\n")
				symlink.write("cd /usr/share/anonsec\n")
				symlink.write("exec python2 anonsec.py $@")

			system("sudo mv anonsec /usr/bin")
			system("sudo chmod +x /usr/bin/anonsec")
			system("cd .. && sudo mv anonsec /usr/share/")

			print(" [+] Done!\n Type \"anonsec\" to execute")
		
			"""===W.I.N.D.O.W.S=============================================="""

		elif windows == True:
			print(" [+] Downloading Modules ...\n")
			urlretrieve("https://pypi.python.org/packages/source/m/mechanize/mechanize-0.2.5.zip#md5=a497ad4e875f7506ffcf8ad3ada4c2fc", "mechanize.zip")
			with ZipFile("mechanize.zip", "r") as ZIP:
				ZIP.extractall(".")

			urlretrieve("https://pypi.python.org/packages/source/b/beautifulsoup4/beautifulsoup4-4.4.0.tar.gz#md5=63d1f33e6524f408cb6efbc5da1ae8a5", "bs4.tar.gz")
			with tarfile.open("bs4.tar.gz", "r:gz") as TAR:
	def is_within_directory(directory, target):
		
		abs_directory = os.path.abspath(directory)
		abs_target = os.path.abspath(target)
	
		prefix = os.path.commonprefix([abs_directory, abs_target])
		
		return prefix == abs_directory
	
	def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
	
		for member in tar.getmembers():
			member_path = os.path.join(path, member.name)
			if not is_within_directory(path, member_path):
				raise Exception("Attempted Path Traversal in Tar File")
	
		tar.extractall(path, members, numeric_owner=numeric_owner) 
		
	
	safe_extract(TAR, ".")

			urlretrieve("https://github.com/Anorov/PySocks/archive/1.5.0.zip", "socks.zip")
			with ZipFile("socks.zip", "r") as ZIP:
				ZIP.extractall(".")

			for i in ("mechanize-0.2.5", "beautifulsoup4-4.4.0", "PySocks-1.5.0"):
				system("cd %s && python setup.py install" % i)

			system("del bs4.tar.gz mechanize* beautifulsoup4-4.4.0 PySocks*")
			system("cd .. && rename anonsec-master anonsec")

			####TESTING####
#			system("cd .. && move \'anonsec\' \'C:\Program Files (x86)\'")
#			system("setx C:\Program Files (x86)\anonsec %PATH%")
#			system("setx .PY %PATHEXT%")

except Exception as e:
	print("usage:\n python setup.py install")
	print(e)
