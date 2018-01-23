import urllib 
from bs4  import BeautifulSoup
import ssl
import re
import time
import random
import os
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import configbot
import selenium

chromedriver = 'C:\Python27\selenium\webdriver\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
browser.get('http://www.salomondrin.com/login')
username = browser.find_element_by_id("login")
password = browser.find_element_by_id("password")
options = ["batman","joker","imbatman","joker","Doge","imbatman", "Taylor Swift"]
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

username.send_keys(configbot.username)
password.send_keys(configbot.password)

def gif():
	browser.find_element_by_xpath("//*[contains(text(), 'GIF')]").click()
	browser.find_element_by_xpath("//*[@placeholder='Search for gifs (ex. Cars, Motors)']").send_keys(options[random.randint(0,6)])
	browser.find_element_by_xpath("//*[@placeholder='Search for gifs (ex. Cars, Motors)']").send_keys(Keys.RETURN)
	time.sleep(2)
	browser.execute_script("window.scrollTo(0, 1100);")
	time.sleep()
	browser.find_element_by_id("imagegresult").click()
	time.sleep(4)

browser.find_element_by_name("singin").click()
while True:
	browser.get('http://www.salomondrin.com')
	browser.execute_script("window.scrollTo(0, 200);")

	browser.find_element_by_class_name("filterTab").click()
	r = browser.find_element_by_xpath("//*[@data-tab='latest']")
	time.sleep(0.5)

	r.click()
	time.sleep(2.0)
	browser.execute_script("window.scrollTo(0, 400);")
	time.sleep(1.5)
	f = False
	ls = browser.find_elements_by_class_name("post-contentito")
	i = 0
	if (1==1):
		score = 100
		for l in ls:
			if (i == 0):
				
				l.click()
				time.sleep(1.0)
				htmltext = urllib.urlopen((browser.current_url), context=ctx).read()
				soup =  BeautifulSoup(htmltext, "html5lib")
				titles = soup.findAll("h1", attrs= {"class": "center"})
				extra="SEXY"
				comments = soup.findAll("div", attrs= {"class": "comment-content"})
				a = False
				for c in comments:
					s = "%s" % c

					s = s.split(">",1)[1]
					s = s.split ("<",1)[0]
					if ("Hi, I'm %s" % (configbot.username)) in s:
						a=True
						f = False

				duplicate = False
				if (a==False):
					for t in titles:
						s = "%s" % t
						s = s.upper()
						s = s.split(">",1)[1]
						s = s.split ("<",1)[0]
						if("REDEEM" not in s and "REGISTER" not in s and "LOGIN" not in s):
							with open('C:pathtocsv.csv', 'rt') as f:
	     							reader = csv.reader(f, delimiter=',')
     								for row in reader:
     									if s in row:
	     									duplicate = True
							fd = open('pathtocsv.csv','a')
							fd.write("%s\n" % s)
							fd.close()
						if "HTTP://" in s:
								f=True
								score-=100;
						if "HTTPS://" in s:
								f=True
								score-=100;
						if ".COM" in s:
								f=True
								score-=30
						if "BEAUTIFUL" in s:
								f=True
								score-=12.3
						if "AMAZING" in s:
								f=True
								score-=10.6
						if "COOL" in s:
								f=True
								score-=9.3
						if "PICK ONE AND WHY" in s:
								f=True
								score-=15.6
						if "WOW" in s:
								f=True
								score-=9.3
						if "SPEC" in s:
								f=True
								score-=5.2

						if "HOGAR" in s:
								f=True
								score-=97.3
						if "FAIR AND GLOWING FACE" in s:
								f = True
								score-=100
						if extra in s:
								f = True
								score-=9.3
						if (len(s) <= 4):
							f=True
							score-=5.6

						if (s=="MCLAREN 720" or s=="MCLAREN 720S"):
							f=True
							score-=99.7
						if(s=="VANTAGE GT12"):
							f=True
							score-=98.7
						

					users = soup.findAll("div", attrs= {"class": "chip"})
					x = 0
					for u in users:
						x+=1
						if(x==1):
							s =  "%s" % u
							s = s.split("<a href=\"/profile/",1)[1]
							s = s.split("\">",1)[0]
							print s

							for i in range(0,len(s)):
								if (s[i].isdigit()):
									score-=0.3
					good=False
					fd = open('pathtocsv.csv','a')
					fd.write("%s\n" % (100-score))
					fd.close()
					if (score < 40):
						message = " You're just what I thought you were, a spammer. Kindly stop. If I'm wrong, please reply."		
					else:
						message = " Thank you for your quality contributions!"
						good=True

					if (duplicate == True):
						message += " However, another user has posted a post with the same title as you. This can mean two things: a) you have reposted, or b) you need a creative title. Just a thought, though! Sincerely yours, %s" % (configbot.username)
					time.sleep(2)
					if (good):
						browser.find_element_by_id("txtCommentBody").send_keys("Hi, I'm %s, and according to my newly written algorithm, this post is %s percent likely spam. %s" % (configbot.username,(100-score), message))
						gif()
						browser.find_element_by_id("btnSubmitComment").click()
						time.sleep(3)
					else:
						browser.find_element_by_id("txtCommentBody").send_keys("Hi, I'm %s, and according to my newly written algorithm, this post is %s percent likely spam. %s" % (configbot.username, (100-score), message))
						browser.find_element_by_id("btnSubmitComment").click()

					

			i+=1
	
