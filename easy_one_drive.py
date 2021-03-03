from datetime import date
import re
import os
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from win32com.client import Dispatch #Solo para windows

correo = '' #write your hotmail/outlook email
contra = '' #write your password
path = '' #write your chromedriver.exe path

class easy_one_drive:
    
    def __init__(self,correo,contra,driver_path):
        self.correo = correo
        self.contra = contra
        self.driver_path = driver_path
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(self.driver_path, chrome_options=options)
    
    def logging_in(self):
        # Login your account
        print('Login into account ',self.correo)
        self.driver.get("https://onedrive.live.com/about/es-es/signin/")
        time.sleep(15)
        self.driver.switch_to.frame(1)
        time.sleep(15)
        self.driver.find_element_by_class_name('form-control').send_keys(self.correo)
        self.driver.find_element_by_class_name('form-control').send_keys(Keys.ENTER)
        time.sleep(15)
        self.driver.find_element(By.ID, "i0118").send_keys(self.contra)
        time.sleep(10)
        self.driver.find_element(By.ID, "idSIButton9").click()
        time.sleep(5)
        print('Logged in!')
        print('Tip: you can change the uploading or downloagind waiting time. Default time: 300 seconds')

    def download_file(self,url,pat,espera=300):    
        # This works with pattern or vector of names
        self.driver.get(url)       
        time.sleep(20)

        if isinstance(pat,type(list)):
            print('Downloading ', len(pat), 'files of the list, remember to be specific :D')
            cajas = []
            
            for i in range(0,len(pat)):
                caja = self.driver.find_element(By.XPATH,'//div[contains(@data-automationid,"' + str(pat[i]) + '")]/span[contains(@role,"checkbox")]')
                cajas.append(caja)
            
            for i in range(0,len(cajas)):
                cajas[i].click()
            
        else:
            print('Downloading files that match pattern, it could fail if there are more than 25 files in folder')
            cajas = self.driver.find_elements(By.XPATH,'//div[contains(@data-automationid,"' + str(pat) + '")]/span[contains(@role,"checkbox")]')
            for i in range(0,len(cajas)):
                cajas[i].click()
            
            time.sleep(3)
            
        # Final click to download    
        self.driver.find_element(By.XPATH, "//i[contains(@data-icon-name,'Download')]").click()
        time.sleep(espera)
        print("Download completed")

    def download_folder(self,url,nombre,espera=300):    
        # Download a complete folder
        self.driver.get(url)
        time.sleep(10)
        print("Downloading folder")
        self.driver.find_element(By.XPATH,'//div[contains(@data-automationid,"'+ nombre + '")]/span[contains(@role,"checkbox")]').click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//i[contains(@data-icon-name,'Download')]").click()
        time.sleep(espera)
        print("Descarga Completa")


    def upload_file(self,url,archivo,espera=90):
        # Path of file to upload
        print("Uploading file: ",archivo)
        self.driver.get(url)
        time.sleep(10)
        
        # Subir archivos
        self.driver.find_element(By.XPATH, "//i[contains(@data-icon-name,'Upload')]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(archivo)
        time.sleep(3)
        try:
            self.driver.find_element_by_xpath("//button[contains(@class,'od-Button OperationMonitor-itemButtonAction')]").click()
        except:
            pass
        time.sleep(espera)
        print("File uploaded")
        
    def logging_out(self):
        print("Logging out")
        self.driver.find_element(By.CSS_SELECTOR, ".\\_2KqWkae0FcyhdNhWQ-Cp-M > img").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "mectrl_body_signOut").click()
        time.sleep(5)
        self.driver.quit()
        print("Logged out. Thanks for using this API")
        
# Set the class to object "s"
s = easy_one_drive(correo, contra, path)

# First you must logging in
s.logging_in()

# Some examples here:
## First for downloading files with patterns, you only must set URL where files are located, then the pattern (string, not list), and optionally the waiting time
s.download_file('','_d') # Here all files that contains string '_d' in their names will be downloaded with default waiting time
s.download_file('','informe',30) # Here all files that contains string 'informe' in their names will be downloaded with only 30 seconds of waiting to download
s.download_file('','.xlsx') # Here all files with extension '.xlsx' will be downloaded with default waiting time

### NOTE: CAN'T use REGEX, so a suggestion is first create a list with files you want to download like in the next lines:

## Now let's download only 2 files, you only must set URL where files are located, then the files to download (in list, with their extensions), and optionally the waiting time
s.download_file('',['informe limpio del 2021-02-02.xlsx','informe limpio del 2021-02-03.xlsx']) # Like before, optionally you can change waiting time after set the list

## For download an entire folder (more robust if you want all files)
s.download_folder('',"Quantico-informes_diarios") # Here given the url, will download the folder with the name specified, and you can change waiting time

## In case of uploading you must specify the complete route of the file to upload like this:
archivo = r"C:\Users\IDEAPAD530S\data_todo.dta"
s.upload_file('',archivo,50) # Finally, specify the url where file will be upload, as before optionally you can change waiting time

## When you finish everything, log out! (security reasons only)
s.logging_out()

### NOTE: you can make any actions as you want between loggin_in and logging_out!
