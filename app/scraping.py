from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from time import sleep
from app.model import Post




class FBPublicPageScraper:

   

    def __init__(self, page_name):
        self.page_name = page_name
        self.page_url = "https://m.facebook.com/" + self.page_name

        # self.driver = webdriver.Chrome(executable_path="./drivers/chromedriver") Local_test

        
        sleep(4)

        options = webdriver.ChromeOptions()
        URL = 'http://selenium:4444/wd/hub'
        options.add_argument('--headless')
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--remote-debugin-port=9222")
        options.add_argument("--screen-size=1200x800")
        options.add_argument('--disable-dev-shm-usage')        

        self.driver = webdriver.Remote(command_executor=URL,
                          desired_capabilities=options.to_capabilities())





    def get_page_info(self):
        self.driver.get(self.page_url)
        for j in range(0,2):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(5)
        
        
        about=self.driver.find_elements_by_css_selector('div[class*=_9_7]>div[class*=_59k]') 
        posts=self.driver.find_elements_by_css_selector('div[class*=_5rgt]>div>span>p')       
        
        
        list_posts=[]
        for i in range(0,len(posts)):
            list_posts.append(Post(post_id=i,post_text=posts[i].text))
        
        return (about ,list_posts)
        
      




    