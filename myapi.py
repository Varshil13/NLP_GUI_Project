import json
import requests
class API:

  def __init__(self):

      self.headers = {
        "apikey": "your api key here!"
      }

  def sentiment_analysis(self,text):
    url = "https://api.apilayer.com/sentiment/analysis"

    payload = text.encode("utf-8")
    response = requests.request("POST", url, headers=self.headers, data = payload)
    status_code = response.status_code
    result = response.text
    return result

  def language_detector(self,text):


      url = "https://api.apilayer.com/nlp/lang_detect"
      payload = text.encode("utf-8")

      response = requests.request("POST", url, headers=self.headers, data=payload)

      status_code = response.status_code
      result = response.text
      return result

  def badwords_analysis(self,text):

      url = "https://api.apilayer.com/bad_words?censor_character=censor_character"
      payload = text.encode("utf-8")
      response = requests.request("POST", url, headers=self.headers, data=payload)
      status_code = response.status_code
      result = response.text
      return result



