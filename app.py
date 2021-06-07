import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ['enabled-logging'])
        self.bot = webdriver.Chrome(options=options, executable_path= r'C://Python//bottwitter//chromedriver.exe')
        
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(2)

        username = bot.find_element_by_xpath('//input [@name="session[username_or_email]"]')
        password = bot.find_element_by_xpath('//input [@name="session[password]"]')

        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(2)

    def like_tweets(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+ hashtag +'&src=typed_query&f=live')
        time.sleep(2)

        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)

        tweets = bot.find_elements_by_xpath('//a[@dir="auto" and not(@rel)]')
        tweets_url = [tweet.get_attribute('href') for tweet in tweets]
        print(tweets_url)

        for url in tweets_url:
            bot.get(url)
            time.sleep(2)
            try:
                time.sleep(3)
                likeButton = bot.find_element_by_xpath('//div[@data-testid="like"]')
                likeButton.click()
                time.sleep(15)
            except Exception as ex:
                print(url + " ya te gusta")
                time.sleep(30)

            time.sleep(2)

tb = TwitterBot('zeusdevelopers1', 'zeus16102459')
tb.login()
tb.like_tweets('python')

