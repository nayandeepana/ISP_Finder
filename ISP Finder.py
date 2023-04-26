from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep
# Give here the path of chrome driver
IP=input('Enter IP address : ')
path="G:/Python/Practice/chrome driver/chromedriver.exe"  
s=Service(path)
driver=webdriver.Chrome(service = s)


driver.get("https://whatismyipaddress.com/ip-lookup")
ipurl=driver.find_element_by_xpath('//*[@id="fl-post-162"]/div[1]/div[1]/div[1]/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/form/label/input')
ipurl.send_keys(IP)
clickbtn=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/article/div[1]/div[1]/div[1]/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/form/button').click()
sleep(3)
isp=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/article/div/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[1]/p[4]/span[2]')
print(isp.text)
with open ("isp.txt","w") as f:
    f.write(isp.text)

'''
NOTE - Use only IPv4 address
'''