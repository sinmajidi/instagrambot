from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd


def getRandomTime():
        randTime = randint(3, 5)
        return randTime

username = "***"
password = "****"
driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.instagram.com/")
print(driver.title)
driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
driver.find_element_by_xpath("//button[contains(.,'Log In')]").click()
sleep(3)
notnow = driver.find_element_by_xpath('//html//body//div[1]//section//main//div//div//div//div//button')
notnow.click()  # Comment these last 2 lines out, if you don't get a pop up asking about notifications
sleep(3)
notnow2 = driver.find_element_by_xpath('//html//body//div[5]//div//div//div//div[3]//button[2]').click()

hashtag_list = ['python', 'html', 'css']  # Change this to your own tags

prev_user_list = []  # If it's the first time you run it, use this line and comment the two below
# prev_user_list = pd.read_csv('20190604-224633_users_followed_list.csv', delimiter=',').iloc[:,1:2] # useful to build a user log
# prev_user_list = list(prev_user_list['0'])

new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0

for hashtag in hashtag_list:
	tag += 1
	driver.get('https://www.instagram.com/explore/tags/' + hashtag_list[tag] + '/')
	sleep(5)
	first_thumbnail = driver.find_element_by_xpath(
		'//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')

	first_thumbnail.click()
	sleep(3)

	# for x in range(1,200):

	# username = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div/div[1]/div/header/div[2]/div[1]/div[1]').text
	# if username not in prev_user_list:

	# If we already follow, do not unfollow
	if driver.find_element_by_xpath(
		'//html//body//div[5]//div[2]//div//article//div//div[1]//div//header//div[2]//div[1]//div[2]//button').text == 'Follow':
		driver.find_element_by_xpath(
			'//html//body//div[5]//div[2]//div//article//div//div[1]//div//header//div[2]//div[1]//div[2]//button').click()
		new_followed.append(username)
		followed += 1
		# sleep(3)
		# # Liking the picture
		# driver.find_element_by_xpath('//html//body//div[5]//div[2]//div//article//div//div[3]//div//div//section[1]//span[1]//button').click()
		# likes += 1
		# sleep(randint(18,25))

for n in range(0, len(new_followed)):
	prev_user_list.append(new_followed[n])

updated_user_df = pd.DataFrame(prev_user_list)
updated_user_df.to_csv('{}_users_followed_list.csv'.format(strftime("%Y%m%d-%H%M%S")))
print('Liked {} photos.'.format(likes))
print('Commented {} photos.'.format(comments))
print('Followed {} new people.'.format(followed))