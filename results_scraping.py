from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()


for i in range(0,10):
    rollnumber = 180021039642 + i
    browser.get('https://college.mgu.ac.in/index.php/public/ResultView_ctrl/')

    dropdown_element = browser.find_element_by_xpath('//*[@id="exam_id"]')
    dropdown_object = Select(dropdown_element)

    dropdown_object.select_by_value('17')
    searchbox = browser.find_element_by_xpath('//*[@id="prn"]')
    searchbutton = browser.find_element_by_xpath('//*[@id="btnresult"]')
    if i != 29:
        searchbox.send_keys(rollnumber)
        searchbutton.click()
        time.sleep(1)
        print('  ')
        student_name = browser.find_element_by_xpath('//*[@id="mgu_btech_contentholder"]/table/tbody/tr[4]/td/fieldset/table[1]/tbody/tr/td/table/tbody/tr[2]/td[3]')
        print(student_name.text)
        total_percentage = 0
        for x in range(3,11):
            subject_name = browser.find_element_by_xpath(f'//*[@id="mgu_btech_contentholder"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[{x}]/td[2]').text
            external_mark = browser.find_element_by_xpath(f'//*[@id="mgu_btech_contentholder"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[{x}]/td[4]').text
            internal_mark = browser.find_element_by_xpath(f'//*[@id="mgu_btech_contentholder"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[{x}]/td[6]').text
            max_mark = browser.find_element_by_xpath(f'//*[@id="mgu_btech_contentholder"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[{x}]/td[9]').text
            int_external_mark = 0
            int_internal_mark = 0
            try:
                int_external_mark = int(external_mark)
            except :
                print('Student was absent')
            try:
                int_internal_mark = int(internal_mark)
            except :
                print('Student was absent')   
                    
            percentage_mark = ((int_external_mark  + int_internal_mark)/ int(max_mark)) * 100
            total_percentage += (percentage_mark // 8)
            print(f'    >>{subject_name} : {percentage_mark} %')
        print(f'    >>>> Total Percentage {total_percentage} %')
        print('  ')
        time.sleep(1)


    else:
        pass    


browser.close()
        