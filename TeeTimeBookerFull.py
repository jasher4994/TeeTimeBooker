"""outline"""

"""
This File aims to automatically book tee times at Nairn golf club.
First of all the file will navigate to the correct page to sign in as a member and enter username and password.
It will then find the correct data that has been specified that a time is required and then book that time.
The main issues here are the timing, as the process takes around 30 seconds to run and the tee times go live at exactly 6pm
the file has to be quicker than the average human as well as being timed correctly. Therefore i am trying to build is such 
that it will navigate to the correct page in advance of the tee times opening and then constantly refresh and attempt to
book the time until it is succesful. I would like to further build this such that if it is too slow to book the tee time then
it will automatically book the next one.

The file should then print out the succesful time it has booked.
"""


"""Package import"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


"""Data Input - insert correct data here """

#player name
name_of_player = "James Asher"
#players identifier
identifier = "3046"
#players password
password = "0409"
#date the person wants to play - must be in this format and correct
date_of_play = "Sunday 05 July 2020"
#ideal time the player wants to play - in 24 time
time_of_play = "1420"
#number of total players to play at this time
number_of_players ="3"




"""initialising web driver - launching chrome"""
#This chunks opens the chromedriver, naviagates to the desired webpage, enters username and password then hits enter.


driver = webdriver.Chrome("/Users/jamesasher/Desktop/Code portfolio/TeeTime/drivers/chromedriver")

driver.get("https://nairn.freetime-online.co.uk/")

title = driver.title

assert "Nairn Golf Club - Member Login" in title

driver.find_element_by_id("MainPlaceHolder_UserName").send_keys(identifier)
driver.find_element_by_id("MainPlaceHolder_Password").send_keys(password)
driver.find_element_by_id("MainPlaceHolder_LoginButton").send_keys(Keys.RETURN)



"""Navigating to booking page"""
#This chunk navigates to the correct page to book tee times.

booking = driver.find_element_by_link_text("BOOKING")
booking.click()

"""navigating to data of play page"""

#This is the current date (or todays date) and we need to itterate such that we hit the next button until this date
#matches the date we want to book at. There is probably an easier (more efficient) way to do this by using xpath but its
#not really worth my time at the present moment

current_date = driver.find_element_by_id("MainPlaceHolder_DateText").get_attribute("value")

while current_date != date_of_play:
    driver.find_element_by_id("MainPlaceHolder_NextDate").send_keys(Keys.RETURN)
    current_date = driver.find_element_by_id("MainPlaceHolder_DateText").get_attribute("value")

#It has now navigated to the correct page that was specified




"""Booking the tee time"""
#We now need to make sure we are first to book the tee time therefore we will continuously refresh and attempt to book

#refresh button
driver.find_element_by_id("MainPlaceHolder_RefreshButton").send_keys(Keys.RETURN)
#the element that is used to book a tee time is below. The last five numbers correspond to the time with the time being precded by a 1
#driver.find_element_by_id("MainPlaceHolder_bookChoiceButton-1{}".format(time_of_play)).send_keys(Keys.RETURN)

#number of particpants entry box
#driver.find_element_by_id("MainPlaceHolder_BookingParticipants").clear()
#driver.find_element_by_id("MainPlaceHolder_BookingParticipants").send_keys(number_of_players)
#driver.find_element_by_id("MainPlaceHolder_OkButton").send_keys(Keys.RETURN)

#The above code works if threre is no competition for times but thats not much use as you would have to go on the website
#to check the times anyway. We therefore want to book it such that it will try book times in a set period and return an
#error if it cant and return the time if it did.

time = driver.find_element_by_id("MainPlaceHolder_ClubTime").get_attribute("text")
print(time)

time2 = driver.find_element_by_class_name("timetext").get_attribute("value")
print(time2)

time2 = driver.find_element_by_class_name("timetext").get_attribute("timetext")
print(time2)







"""confirmation"""

#print(driver.find_element_by_id("MainPlaceHolder_DateText").get_attribute("value"))






