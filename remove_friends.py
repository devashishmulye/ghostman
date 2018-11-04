from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import os
import argparse




do_not_delete_list = ['Murtaza Phalasiya','Subhomoy Bakshi','Aaditya Rajawat']


def check_if_friend_in_dnd(friend_name,dnd_list):

    if friend_name in dnd_list:
        return True
    else:
        return False


def sort_by_first_name(driver):
    select = Select(driver.find_element_by_id('sort'))
    select.select_by_visible_text('first name')
    return driver




def execute_deletion(driver,friend_element,is_dry_run):
    print 'Deleted', friend_element.text
    deletion_element = friend_element.find_element_by_xpath("../../div[4]/div/a")
    if is_dry_run is False:
        deletion_element.click()
        time.sleep(5)
        alert_obj = driver.switch_to.alert
        alert_obj.accept()
        is_break = True
    else:
        is_break = False
    return is_break


def delete_friends_flow(driver, do_not_delete_list,is_dry_run):

    next_page_enabled=True

    while next_page_enabled is True:
        time.sleep(5)
        driver = sort_by_first_name(driver)
        driver = activate_edit_friends(driver)
        all_friends = driver.find_elements_by_class_name('userLink')

        for friend in all_friends:
            if check_if_friend_in_dnd(friend.text,do_not_delete_list) is False:
                is_break = execute_deletion(driver,friend,is_dry_run)
                if is_break is True:
                    break
            else:
                is_break = False
                print 'Did Not Delete', friend.text
        if is_break is True:
            continue


        next_page_element = driver.find_element_by_class_name('next_page')
        next_page_enabled = next_page_element.get_attribute('href')

        if next_page_enabled is not None:
            next_page_enabled = True
            next_page_element.click()
        else:
            next_page_enabled = False



def activate_edit_friends(driver):
    edit_friends_elem = driver.find_element_by_id('edit_friends_button')
    edit_friends_elem.click()
    return driver


def initialize_driver():
    driver_path = os.getcwd() + "/chromedriver5"
    driver = webdriver.Chrome(driver_path)
    return driver


def get_goodreads_homepage(driver):
    driver.get("https://www.goodreads.com/")
    return driver

def log_in_to_goodreads(driver, email_id, password):
    sing_in_elem = driver.find_element_by_id('userSignInFormEmail')
    sing_in_elem.send_keys(email_id)
    password_elem = driver.find_element_by_xpath('//*[@id="user_password"]')
    password_elem.send_keys(password)

    sign_in_elem = driver.find_element_by_xpath('//*[@id="sign_in"]/div[3]/input[1]')
    sign_in_elem.click()
    return driver


def get_goodreads_friends_page(driver):
    driver.get('https://www.goodreads.com/friend')
    return driver


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run")
    parser.add_argument("--email",type=str)
    parser.add_argument("--password",type=str)
    parser.add_argument("--retain",type=str)
    args = parser.parse_args()

    if args.dry_run:
        print 'This is a Dry Run'
        is_dry_run = True
    else:
        is_dry_run = False

    email = args.email
    password = args.password
    do_not_delete_list = args.retain.split(',')
    print 'These Friends Will Not Be Deleted',do_not_delete_list

    driver = initialize_driver()
    driver = get_goodreads_homepage(driver)
    time.sleep(10)
    driver = log_in_to_goodreads(driver,email,password)
    driver = get_goodreads_friends_page(driver)
    time.sleep(10)
    driver = delete_friends_flow(driver, do_not_delete_list,is_dry_run)



#python remove_friends.py --email devashish.mulye@gmail.com --password pwpw --retain "Murtaza Phalasiya,Subhomoy Bakshi,Aaditya Rajawat" --dry-run 1
