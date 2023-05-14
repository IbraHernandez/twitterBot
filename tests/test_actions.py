from page_objects.page_objects import TwitterObjects
from page_objects.page_objects import MotivationalPhrasesObjects
from page_objects.page_objects import TrendingTopicsObjects
import random


class MotivationalPhrases(MotivationalPhrasesObjects):
    def test_phrases(self):
        self.open(self.phrases_URL)
        self.maximize_window()
        self.click(self.accept_cookies_btn)
        phrases = self.find_elements(self.phrases)
        random_number = random.randint(0, 88)
        random_phrase = phrases[random_number].text
        print(random_phrase)
        return random_phrase


class TrendingTopics(TrendingTopicsObjects):
    def test_trends(self):
        self.open_url(self.trend_url)
        self.click(self.cookies_btn)
        self.click(self.trend1)
        trendtopic1 = self.get_text("h1[class='insight-modal--title']")
        self.click(self.trend1_exit_btn)
        self.click(self.trend2)
        trendtopic2 = self.get_text("h1[class='insight-modal--title']")
        twitter_trends = ' ' + '#' + trendtopic1 + ' ' + '#' + trendtopic2
        print(twitter_trends)
        return twitter_trends


class MyTestClass(TwitterObjects, MotivationalPhrases, TrendingTopics):
    def test_twitter(self):
        phrase = MotivationalPhrases.test_phrases(self)
        trends = TrendingTopics.test_trends(self)
        self.open("https://twitter.com")
        self.maximize_window()
        self.click(self.accept_cookies)
        self.click(self.iniciar_sesion_btn)
        self.wait_for_element_visible(self.username_input)
        self.send_keys(self.username_input, self.username)
        self.click(self.siguiente_btn)
        self.wait_for_element_visible(self.pass_input)
        self.send_keys(self.pass_input, self.password)
        self.click(self.iniciar_sesion_btn2)
        post = str(phrase) + str(trends)
        print(post)
        self.send_keys(self.post_input, post)
        self.click(self.tweet_btn)


