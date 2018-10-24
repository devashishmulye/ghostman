from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import os





driver_path = os.getcwd() + "/chromedriver5"
driver = webdriver.Chrome(driver_path)
driver.get("https://www.goodreads.com/")
time.sleep(10)
# elem = driver.find_element_by_id('//*[@id="sign_in"]')
elem = driver.find_element_by_id('userSignInFormEmail')
elem.send_keys('devashish.mulye@gmail.com')
elem2 = driver.find_element_by_xpath('//*[@id="user_password"]')
elem2.send_keys("placeholderpw")

sign_in_elem = driver.find_element_by_xpath('//*[@id="sign_in"]/div[3]/input[1]')
sign_in_elem.click()


time.sleep(10)
driver.get('https://www.goodreads.com/friend')



do_not_delete_list = ['Murtaza Phalasiya','Subhomoy Bakshi']

friend_number = 4
for i in range(0,0):
    select = Select(driver.find_element_by_id('sort'))
    select.select_by_visible_text('first name')
    print 'friend number', friend_number
    edit_friends_elem = driver.find_element_by_id('edit_friends_button')
    edit_friends_elem.click()

    try:
        del_friend = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[1]/div[3]/div[{}]/div[4]/div'.format(str(friend_number)))
    except NoSuchElementException:
        'No Such Element Bruf'
        break

    elem_with_name = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[1]/div[3]/div[{}]/div[1]/a[1]'.format(str(friend_number)))
    name_of_person = elem_with_name.text
    print name_of_person, 'Name of Person'
    if name_of_person in do_not_delete_list:
        friend_number +=1
        print 'Did Not Unfriend ', name_of_person
        continue
    time.sleep(9)
    del_friend.click()
    alert_obj = driver.switch_to.alert
    alert_obj.accept()

# try:
#     null_elem = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[1]/div[3]/div[4]/div[4]/div/div/div/div/div')
# except NoSuchElementException:
#     print 'No Such Element Bruff'







'''



'/html/body/div[2]/div[3]/div[1]/div[1]/div[3]/div[4]/div[4]/div'
'orig'
'/html/body/div[3]/div[3]/div[1]/div[1]/div[3]/div[5]/div[4]/div'
'/html/body/div[2]/div[3]/div[1]/div[1]/div[3]/div[4]/div[4]/div/a'
'/html/body/div[2]/div[3]/div[1]/div[1]/div[3]/div[4]/div[4]/div/a'
'/html/body/div[2]/div[3]/div[1]/div[1]/div[3]/div[4]/div[4]/div'


# profile_elem = '/html/body/div[2]/div[1]/div/header/div[1]/div/div[4]/span/a'

'''

el_1_xpath = '/html/body/div[2]/div[3]/div[1]/div[1]/div[3]/div[4]/div[4]/div'
el_2_xpath = '/html/body/div[2]/div[3]/div[1]/div[1]/div[3]/div[5]/div[4]/div'
el_3_xpath = '/html/body/div[2]/div[3]/div[1]/div[1]/div[3]/div[6]/div[4]/div'



