import os
import sys
import time
import pathlib
from sys import platform
from time import sleep
import urllib
from constants import xPathSource
from chrome import ChromeOptions
from firefox import FirefoxOptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
try:
    import httplib
except:
    import http.client as httplib

constant = xPathSource()
dic=constant.get_xpath_dic()
invalid_number_text="Invalid number! Try again..."
file_not_found_text="File not found!"
def title():
    if platform == 'win32':
        os.system('mode con: cols=85 lines=25')
        os.system('cls')
    else:
        os.system('clear')
    print(r"""                                              
                         _      
  __ _  ___   ___   __ _| | ___ 
 / _` |/ _ \ / _ \ / _` | |/ _ \
| (_| | (_) | (_) | (_| | |  __/
 \__, |\___/ \___/ \__, |_|\___|
 |___/             |___/        
 _                       _       _       
| |_ _ __ __ _ _ __  ___| | __ _| |_ ___ 
| __| '__/ _` | '_ \/ __| |/ _` | __/ _ \
| |_| | | (_| | | | \__ \ | (_| | ||  __/
 \__|_|  \__,_|_| |_|___/_|\__,_|\__\___|
            """,end="\r\n\n\n")
def is_internet_on(host='www.google.com'):
    conn = httplib.HTTPConnection(host, timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False

def load_animation(): 
    load_str = "starting google translate..."
    ls_len = len(load_str) 
    animation = "|/-\\"
    anicount = 0
    counttime = 0        
    i = 0                     
    while (counttime != 100): 
        sleep(0.030)
        load_str_list = list(load_str)  
        x = ord(load_str_list[i]) 
        y = 0                             
        if x != 32 and x != 46:              
            if x>90: 
                y = x-32
            else: 
                y = x + 32
            load_str_list[i]= chr(y) 
        res =''              
        for j in range(ls_len): 
            res = res + load_str_list[j] 
        sys.stdout.write("\r"+res + animation[anicount]) 
        sys.stdout.flush() 
        load_str = res 
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len 
        counttime = counttime + 1
    if platform =="win32": 
        os.system("cls") 
    else: 
        os.system("clear")  
def get_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time
def cursor_animation():
    print('\n')
    animation = "|/-\\"
    for i in range(100):
        sleep(0.025)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
def test_dic():
    constant=xPathSource()
    selection = 0
    global is_setup
    is_setup=False
    while True:
        title()
        print("Which web driver will you use?\n")
        if is_previously_setup() :
            data = get_data_from_previously_setup()
            is_setup=True
            print("0) Previously Run -> "+data[0]+' '+"Path "+data[1])
        print("1) Chrome",end='\n')
        print("2) Firefox",end='\n\n')
        try:
            selection = int(input("WebDriver : "))
        except ValueError:
            print(invalid_number_text)
            sleep(2)
            continue
        if is_setup:
            if selection >=0 and selection <=2:
                break
            else:
                print(invalid_number_text)
                sleep(2)
                continue
        else:
            if selection == 1 or selection == 2:
                break
            else:
                print(invalid_number_text)
                sleep(2)
                continue
    if is_setup:
        if selection==0:
            selected_previous()
    if selection==1:
        selected_chrome()
    if selection==2:
        selected_firefox()

def test_all_languages(driver):
    start_time=get_time()
    error_counter=0
    test_counter=0
    title()
    print("Testing............\n\n")
    print("English -> car\n")
    print("*******************\n")
    total_dic_len=len(dic)
    for country in dic.keys():
        if country == "English":
            continue
        sleep(0.2)
        translate_url = "https://translate.google.com/#view=home&op=translate&sl=en&tl=%s&text=car"%(dic[country]['code'])
        driver.get(translate_url)
        while True:
            try:
                translate_word_element=driver.find_element_by_xpath(dic[country]['xpath'])
                translate_word=translate_word_element.text
                if translate_word=='car' :
                    break
                output=country + ' -> ' +translate_word
                sys.stdout.write('\x1b[K\t%s\r' % output)
                sys.stdout.flush()
                test_counter+=1
                progressBar(test_counter,total_dic_len)
                sleep(0.2)
                break
            except NoSuchElementException:
                error_counter+=1
                if error_counter>10:
                    driver.refresh()
                    error_counter=0
                continue
    end_time=get_time()
    print("\n")
    print("All languages tested successfully!\n")
    print("Start Time : "+start_time,end='\n')
    print("End Time : "+end_time,end='\n')
    remaining_for_seconds(10)
    mode_select_func(driver)
def selected_chrome():
    global driver
    global path
    title()
    current_path=str(pathlib.Path().absolute())
    if platform == 'win32':
        current_path=current_path+"\\chromedriver.exe" ### CHECK FOR \\
    else:
        current_path=current_path+"/chromedriver"
    try:
        driver=webdriver.Chrome(executable_path=current_path, options=ChromeOptions().get())
        print("Chrome driver..........OK!\n")
        sleep(0.5)
        save_setup("Chrome",current_path)
        mode_select_func(driver)
    except WebDriverException as e:
        print(str(e))
        sleep(5)
        selected_chrome()
def selected_firefox():
    global driver
    global path
    title()
    current_path=str(pathlib.Path().absolute())
    if platform == 'win32':
        current_path=current_path+"\\geckodriver.exe"
    else:
        current_path=current_path+"/geckodriver"
    try:
        driver=webdriver.Firefox(executable_path=current_path,options=FirefoxOptions().get())
        print("Firefox driver ..........OK!\n")
        sleep(0.5)
        save_setup("Firefox",current_path)
        mode_select_func(driver)
    except WebDriverException as e:
        print(str(e))
        sleep(5)
        selected_firefox()

def selected_previous():

    data=get_data_from_previously_setup()
    browser_selection=str(data[0])
    path=str(data[1])
    if browser_selection == "Chrome":
        driver=webdriver.Chrome(executable_path=path,options=ChromeOptions().get())
        mode_select_func(driver)
    elif browser_selection == "Firefox":
        driver=webdriver.Firefox(executable_path=path,options=FirefoxOptions().get())
        mode_select_func(driver)

def mode_select_func(driver):
    global mode_selection
    while True:
        title()
        print("**********************")
        print("*                    *")
        print("*   Mode Selection   *")
        print("*                    *")
        print("**********************\n")
        print("0) Test All Languages")
        print("1) Multiple Word Translate")
        print("2) Single Word Translate\n")
        try:
            mode_selection=int(input("Selection : "))
            if mode_selection < 0 or mode_selection > 2:
                print(invalid_number_text)
                sleep(2)
                continue
            else:
                break
        except ValueError:
            print(invalid_number_text)
            sleep(2)
            continue
        
    if mode_selection == 0:
        test_all_languages(driver)
        mode_select_func(driver)
    elif mode_selection == 1:
        multiple_input_or_file(driver)
    elif mode_selection == 2:
        single_word_translation(driver)

def multiple_input_or_file(driver):
    selectionsArr=pick_from_and_to_language()
    from_selection=selectionsArr[0]
    to_selection=selectionsArr[1]
    while True:
        title()
        print("*************")
        print("Mode : Multiple")
        print("From : "+from_selection)
        print("To   : "+to_selection)
        print("*************")
        print("-1) Back\n")
        char = input("Is word file in the same directory of the program?(y/n) : ")
        if char=="y" or char=="Y":
            multiple_provide_filename(True,driver,from_selection,to_selection)
            break
        elif char =="n" or char=="N":
            multiple_provide_filename(False,driver,from_selection,to_selection)
            break
        elif char=="-1":
            mode_select_func(driver)
        else:
            print("Invalid input! Try again...")
            sleep(2)
            continue
def multiple_provide_filename(is_same_directory,driver,from_selection,to_selection):
    if is_same_directory:
        while True:
            title()
            print("*************")
            print("Mode : Multiple")
            print("From : "+from_selection)
            print("To   : "+to_selection)
            print("*************")
            print("-1) Back\n")
            filename=input("Input file name : ")
            if filename=="-1":
                mode_select_func(driver)
            else:
                if platform == 'win32':
                    file_path=str(pathlib.Path().absolute())+"\\"+filename 
                    if os.path.isfile(file_path)==False:
                        print(file_not_found_text)
                        sleep(2)
                        continue
                    else:
                        multiple_file_translate(file_path,driver,from_selection,to_selection)
                else:
                    file_path=str(pathlib.Path().absolute())+"/"+filename 
                    if os.path.isfile(file_path)==False:
                        print(file_not_found_text)
                        sleep(2)
                        continue
                    else:
                        multiple_file_translate(file_path,driver,from_selection,to_selection)
    else:
        while True:
            title()
            print("*************")
            print("Mode : Multiple")
            print("From : "+from_selection)
            print("To   : "+to_selection)
            print("*************")
            print("-1) Back\n")
            file_path=input("Full path of input file : ")
            if file_path=="-1":
                mode_select_func(driver)
            else:
                if os.path.isfile(file_path)==False:
                    print(file_not_found_text)
                    sleep(2)
                    continue
                else:
                    multiple_file_translate(file_path,driver,from_selection,to_selection)

def multiple_file_translate(input_file_path,driver,from_selection,to_selection):
        title()
        print("*************")
        print("Mode : Multiple")
        print("From : "+from_selection)
        print("To   : "+to_selection)
        print("Input File Path : "+input_file_path)
        print("*************")
        print("-1) Back\n")
        input_file_seperator=input("Input file word seperator(default endline) : ")
        if input_file_seperator=="-1":
            multiple_input_or_file(driver)
        if len(input_file_seperator)==0:
            # Seperated with \n
            data=[]
            f = open(input_file_path,"r")
            data = [x.strip() for x in f.readlines()]
            f.close()

        else:
            data=[]
            f = open(input_file_path,"r")
            data = [x.strip() for x in f.read().split(input_file_seperator)]
            f.close()
            
        title()
        print("*************")
        print("Mode : Multiple")
        print("From : "+from_selection)
        print("To   : "+to_selection)
        print("Input File Path : "+input_file_path)
        if len(input_file_seperator)==0:
            print("Input File Seperator : endline")
        else:
            print("Input File Seperator : "+input_file_seperator)
        print("*************")
        print("-1) Back\n")
        output_file_name=input("Output file name(default \"result.txt\") : ")
        if output_file_name=="-1":
            multiple_file_translate(input_file_path,driver,from_selection,to_selection)
        if len(output_file_name)==0:
            output_file_name="result.txt"
        title()
        print("*************")
        print("Mode : Multiple")
        print("From : "+from_selection)
        print("To   : "+to_selection)
        print("Input File Path : "+input_file_path)
        if len(input_file_seperator)==0:
            print("Input File Seperator : endline")
        else:
            print("Input File Seperator : "+input_file_seperator)
        print("Output File Name : "+output_file_name)
        print("*************")
        print("-1) Back\n")
        output_file_seperator=input("Output file seperator(default endline) : ")
        if output_file_seperator=="-1":
            multiple_file_translate(input_file_path,driver,from_selection,to_selection)
        if len(output_file_seperator)==0:
            output_file_seperator='\n'
        f = open(output_file_name,"w")
        title()
        count=0
        word_counter=1
        counter=1
        start_time=get_time()
        total_word_count=len(data)
        print("\n***************************")
        print("Mode : Multiple")
        print("From : "+from_selection)
        print("To : "+to_selection)
        print("Word Count : "+str(total_word_count))
        print("Input File Path : "+input_file_path)
        if len(input_file_seperator)==0:
            print("Input File Seperator : endline")
        else:
            print("Input File Seperator : "+input_file_seperator)
        print("Output File Name : "+output_file_name)
        if output_file_seperator=='\n':
            print("Output File Seperator : endline")
        else:
            print("Output File Seperator : "+output_file_seperator)
        print("Start Time : " + start_time)
        print("***************************\n")
        for word in data:
            translated=translate(driver,word,from_selection,to_selection)
            f.write(translated+output_file_seperator)
            count+=1
            word_counter+=1
            counter+=1
            if count == 200:
                f.flush()
                count=0
            progressBar(word_counter,total_word_count)
        f.close()
        print("\n"+str(word_counter) + " words translated and saved to "+output_file_name+" file!\n")
        print("Start Time : " + start_time)
        print("End Time : " + get_time()+"\n")
        remaining_for_seconds(10)
        mode_select_func(driver)

def single_word_translation(driver):
    selectionsArr=pick_from_and_to_language("Single")
    from_selection=selectionsArr[0]
    to_selection=selectionsArr[1]
    save_from_to(from_selection,to_selection)
    title()
    print("*************")
    print("Mode : Single")
    print("From : "+from_selection)
    print("To   : "+to_selection)
    print("*************")
    print("-1) Back\n")
    word=input("Word for translate : ")
    if word == "-1":
        mode_select_func(driver)
    sys.stdout.write("\rTranslating...")
    result=translate(driver,word,from_selection,to_selection)
    sys.stdout.flush()
    sys.stdout.write("\rTranslated ! -> "+result+"\n")
    remaining_for_seconds(10)
    mode_select_func(driver)

def progressBar(value, endvalue, bar_length=20):

    percent = float(value) / endvalue
    arrow = '-' * int(round(percent * bar_length)-1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write("\rPercent: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
    sys.stdout.flush()

def translate(driver,word,from_language,to_language):
    errorCounter=0
    from_code=dic[from_language]['code']
    to_code=dic[to_language]['code']
    url = "https://translate.google.com/#view=home&op=translate&sl="+from_code+"&tl="+to_code+"&text=%s"%(word)
    driver.get(url)
    sleep(0.2)
    while True:
        try:
            translate_word_element=driver.find_element_by_xpath(dic[to_language]['xpath'])
            translate_word=translate_word_element.text
            if translate_word == word:
                return translate_word
                break
            return translate_word
        except NoSuchElementException:
            errorCounter += 1
            if errorCounter > 10:
                driver.refresh()
                errorCounter=0
            continue

def pick_from_and_to_language(mode="Multiple"):
    constant=xPathSource()
    dic=constant.get_xpath_dic()
    global selected_from_language
    global selected_to_language
    selectionFrom = -1
    languages = []
    for key in dic.keys():
        languages.append(key)
    while True:
        title()
        print(mode + " word translation")
        print("**************************")
        print("-1) Back")
        print("**************************\n")
        print("From\n")
        dic_range=len(languages)
        i=0
        while i<dic_range:
            if i+25 < len(languages):
                print(str(i+1)+") "+languages[i],end='')
                if i>8:
                    space_count=34-len(str(languages[i]))
                else:
                    space_count=35-len(str(languages[i]))
                for j in range(space_count):
                    print(' ',end='')
                print(str(i+1+25)+") "+languages[i+25])
            
            if i+25==50:
                print("\n")
                i+=25
            i+=1
            
        try:
            print("\n")
            print("******************************************************\n")
            selectionFrom=int(input("From : "))
            if selectionFrom == -1:
                mode_select_func(driver)
            if selectionFrom < 1 or selectionFrom > i:
                print(invalid_number_text)
                sleep(2)
                continue
            else:
                break
        except ValueError:
            print(invalid_number_text)
            sleep(2)
            continue
    j=1
    
    for key in dic.keys():
        if j == selectionFrom:
            selected_from_language=key
            break
        j += 1
    languages.remove(selected_from_language)
    selectionTo = -1
    while True:
        title()
        print(mode + " word translation")
        print("**************************")
        print("-1) Back")
        print("**************************\n")
        print("From : "+selected_from_language+"\n")
        print("To\n")
        dic_range=len(languages)
        i=0
        while i<dic_range:
            if i+25 < len(languages):
                print(str(i+1)+") "+languages[i],end='')
                if i>8:
                    space_count=34-len(str(languages[i]))
                else:
                    space_count=35-len(str(languages[i]))
                for j in range(space_count):
                    print(' ',end='')
                print(str(i+1+25)+") "+languages[i+25])
            
            if i+25==50:
                print("\n")
                i+=25
            i+=1
        
        try:
            print("\n")
            print("******************************************************\n")
            print("From : "+selected_from_language+"\n")
            selectionTo=(int(input("To : ")))
            if selectionTo == -1:
                mode_select_func(driver)
            if selectionTo < 1 or selectionTo > i:
                print(invalid_number_text)
                sleep(2)
                continue
            else:
                break
        except ValueError:
            print(invalid_number_text)
            sleep(2)
            continue
    j=1
    if selectionFrom < selectionTo:
        selectionTo+=1
    for key in dic.keys():
        if j == selectionTo:
            selected_to_language=key
            break
        j += 1
    selections=[selected_from_language,selected_to_language]
    return selections

def is_previously_setup():
    if platform == 'win32':
        saved=str(pathlib.Path().absolute())+"\\save.txt"
    else:
        saved=str(pathlib.Path().absolute())+"/save.txt"
    if os.path.isfile(saved):
        return True
    return False
def get_data_from_previously_setup():
    data=[]
    f =open('save.txt','r')
    data = [x.strip() for x in f.readlines()]
    f.close()
    return data

def save_setup(driver_name,driver_path):
    f = open("save.txt",'w')
    f.write(driver_name+'\n')
    f.write(driver_path+'\n')
    f.close()

def save_from_to(select_from,select_to):
    f = open("save.txt","a")
    f.write(select_from+'\n')
    f.write(select_to+'\n')
    f.close()

def get_from_to():
    data=[]
    f = open("save.txt","r")
    data = [x.strip() for x in f.readlines()]
    f.close()
    return data
def remaining_for_seconds(countdown):
    for remaining in range(countdown, 0, -1):
        sys.stdout.write("{:2d} seconds remaining for redirect to Mode Selection.\r".format(remaining))
        sys.stdout.flush()
        sleep(1)
if __name__ == '__main__': 
    title() 
    load_animation()
    title()
    if not is_internet_on() :
        sys.exit("There is no internet connection, program will close...\n")
    cursor_animation()
    test_dic()
    