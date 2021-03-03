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
# NOTE: if you are using using Google Colab or other virtual environment that use webdriver.Chrome, ignore driver_path

class easy_one_drive:
    
    def __init__(self,correo,contra,driver_path='',chromedriver=''):
        self.correo = correo
        self.contra = contra
        if driver_path!='':
            self.driver_path = driver_path
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(self.driver_path, chrome_options=options)
            self.chromedriver = chromedriver
        else:
            self.driver_path = driver_path
            self.driver = chromedriver
    
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
