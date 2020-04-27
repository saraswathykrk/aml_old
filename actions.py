# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

#from rasa_core.domain import Domain
#from rasa_core.trackers import EventVerbosity
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action, Tracker
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import Restarted
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher


from typing import Any, Text, Dict, List
from operator import itemgetter

import json
import logging
import nltk
import urllib3
import requests

logger = logging.getLogger(__name__)
nltk.download('punkt')


class ActionSlotReset(Action): 	
    def name(self): 		
        return 'action_slot_reset' 	
    def run(self, dispatcher, tracker, domain): 		
        return[SlotSet("previous", None), SlotSet("prev_count", "0")]


		
from bs4 import BeautifulSoup
import re


def topicnews(topic):
    """api call for getting news based on specific topic"""
    response=requests.get("https://amlabc.com/aml-updates/posts-list-sra/")
    print("resp:",response)
    quote_page = "https://amlabc.com/aml-updates/posts-list-sra/"
    http = urllib3.PoolManager()
    page=http.request('GET',quote_page)
    data=page.data
    print(data)
    return data


'''from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.agent import Agent

fallback = FallbackPolicy(fallback_action_name="utter_default",
                          core_threshold=0.3,
                          nlu_threshold=0.3)

agent = Agent("domain.yml",
               policies=[KerasPolicy(), fallback])
'''




def check(sentence, words): 
	#print("sent:",sentence)
	res = [all([k in s for k in words]) for s in sentence]
	return [sentence[i] for i in range(0, len(res)) if res[i]]


class ActionGetInfo1(Action):
	def name(self) -> Text:
		return 'action_get_info1'


	def run(self, 
			dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		keyword_dets=tracker.get_slot('keyword')
		category_dets=tracker.get_slot('category')
		previous_dets=tracker.get_slot('previous')
		prev_count_dets=tracker.get_slot('prev_count')
		date_dets=tracker.get_slot('dated')
		print("latest:",tracker.latest_message)
		print("events:",tracker.events)

		print(category_dets)
		if category_dets is None:
			category_dets = 'aml-news'
		elif category_dets.lower() in ('news','information','links','details','detail','data'):
			category_dets = 'aml-news'
		elif category_dets.lower() in ('cases','case','report', 'reports'):
			category_dets = 'aml-case-studies'
		elif category_dets.lower() in ('fine','fines'):
			category_dets = 'aml-sanction-fines'
		else:
			category_dets = 'aml-news'

		pop_flag=False

		print("prev_count_dets:",prev_count_dets)

		if previous_dets is None:
			pop_flag=False
			prev_count_dets1 = "0"
		else:
			if prev_count_dets is None:
				prev_count_dets1 = "1"
			elif prev_count_dets == "0":
				prev_count_dets1 = "1"
			else:
				prev_count_dets1 = int(prev_count_dets) + 1

			for i in previous_dets:	
				if i in ('previous','previously','earlier','first','help','more','few'):
					pop_flag=True
				else:
					print("all ok")
		data=topicnews(keyword_dets)
		leng=len(data)
		for i in range(leng): 
			gt = {
					"attachment": {
					  "type": "template",
					  "payload": {
					      "template_type": "generic",
					      "elements": [
					                                  {
					              "title": data['post_content'][i],
					              "image_url":data['post_url'][i]['urlToImage'],
					              "subtitle": data['post_content'][i]['title'],
					              "buttons": [
					                  {
					                      "type": "web_url",
					                      "url": data['articles'][i]['url'],
					                      "title": "Read More"
					                  },
					              ]
					          },
					      ]
					  }
					}
	        	}
		dispatcher.utter_custom_json(gt)
		return []      


class ActionGetInfo(Action):
	def name(self) -> Text:
		return 'action_get_info'


	def run(self, 
			dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		keyword_dets=tracker.get_slot('keyword')
		category_dets=tracker.get_slot('category')
		previous_dets=tracker.get_slot('previous')
		prev_count_dets=tracker.get_slot('prev_count')
		date_dets=tracker.get_slot('dated')
		#print("latest:",tracker.latest_message)
		#print("events:",tracker.events)

		print(category_dets)
		if category_dets is None:
			category_dets = 'aml-news'
		elif category_dets.lower() in ('news','information','links','details','detail','data'):
			category_dets = 'aml-news'
		elif category_dets.lower() in ('cases','case','report', 'reports'):
			category_dets = 'aml-case-studies'
		elif category_dets.lower() in ('fine','fines'):
			category_dets = 'aml-sanction-fines'
		else:
			category_dets = 'aml-news'

		pop_flag=False

		print("prev_count_dets:",prev_count_dets)

		if previous_dets is None:
			pop_flag=False
			prev_count_dets1 = "0"
		else:
			if prev_count_dets is None:
				prev_count_dets1 = "1"
			elif prev_count_dets == "0":
				prev_count_dets1 = "1"
			else:
				prev_count_dets1 = int(prev_count_dets) + 1

			for i in previous_dets:	
				if i in ('previous','previously','earlier','first','help','more','few'):
					pop_flag=True
				else:
					print("all ok")

		quote_page = "https://amlabc.com/aml-updates/posts-list-sra/"
		http = urllib3.PoolManager()
		print('keyword:', keyword_dets)
		print('category:', category_dets)
		
		page=http.request('GET',quote_page) #.format(orig,dest,dat))
		soup = BeautifulSoup(page.data, 'html.parser')

		list1=[]
		list2=[]
		list3=[]
		list4=[]
		list5=[]
		list6=[]

		#print("soup:",soup)
		tweetArr = []
		for tweet in soup.findAll('tr',attrs={"id": re.compile("TR_")}):
			tweetObject = {"post_id": tweet.find('td', attrs={"id": "post_id"}).text,#.encode('utf-8'),
				"post_title": tweet.find('td', attrs={"id": "post_title"}).text,#.encode('utf-8'),
				"post_date": tweet.find('td', attrs={"id": "post_date"}).text,#.encode('utf-8'),
				"post_url": tweet.find('td', attrs={"id": "post_url"}).text,#.encode('utf-8'),
				"post_source": tweet.find('td', attrs={"id": "post_source"}).text,#.encode('utf-8'),
				"post_via": tweet.find('td', attrs={"id": "post_via"}).text,#.encode('utf-8'),
				"post_content": tweet.find('td', attrs={"id": "post_content"}).text.replace("\n","")#.encode('utf-8')
		    }
			tweetArr.append(tweetObject)
		
		tweetArr1 = sorted(tweetArr, key=itemgetter('post_date'), reverse = True)
		#print("tweetArr1:",tweetArr1)
		


		for i in tweetArr1:
			list_tmp=[]
			j = i['post_content']
			sentence1 = nltk.tokenize.sent_tokenize(j)
			list_tmp.extend(sentence1)
			output = check(list_tmp,keyword_dets)
			if output:
				if category_dets == i['post_url'].split('/')[4]:
					list1.extend(output)
					list2.append(i['post_url'])
					list5.append(i['post_title'])
					list6.append(i['post_date'])
					l = i['post_title']
					j = i['post_content']
					m = i['post_url']
					n = i['post_via']
					o = i['post_source']
					p = i['post_date']

		print("List1:",list1)
		print("List2:",list2)


		if len(list1) > 0:
			if pop_flag:
				if len(list2) > 1 and int(prev_count_dets1) < len(list2) :
					Link=list2.pop(int(prev_count_dets1))
					Title=list5.pop(int(prev_count_dets1))
					dispatcher.utter_message(template="utter_info",title=Title,link=Link)
					dispatcher.utter_message(template="utter_help")
					print("list2:",list2)
					print("list2:",list2)
					
				else:
					dispatcher.utter_message(template="utter_diff_ques")
			else:
				Content=list1[0]
				dispatcher.utter_message(template="utter_relevant_info",content=Content)

				if len(list2) > 0:
					Link=list2[0]
					Title=list5[0]
					logger.debug("tracker slots:",tracker.slots)
					print("tracker slots:",tracker.slots)
					dispatcher.utter_message(template="utter_info",title=Title,link=Link)
					dispatcher.utter_message(template="utter_help")
		else:
			dispatcher.utter_message(template="utter_rephrase")

		#data=topicnews(keyword_dets)
		'''data=tweetArr1
		leng=len(data)
		print(leng, data[0:2])
		for i in range(leng):
			list_tmp=[]
			list_tmp.extend(nltk.tokenize.sent_tokenize(data[i]['post_content']))
			output = check(list_tmp,keyword_dets)
			if output:
				if category_dets == data[i]['post_url'].split('/')[4]:
					if pop_flag and i==int(prev_count_dets1):
						gt = {
								"attachment":
									{
									  "type": "template",
									  "payload": {
									      "template_type": "generic",
									      "elements": [{
											              "title": data[i]['post_title'],
											              "image_url": data[i]['post_source'],
											              "subtitle": output,
											              "buttons": [
											                  {
											                      "type": "web_url",
											                      "url": data[i]['post_url'],
											                      "title": "Read More"
											                  },
											              ]
									          },
									      ]
									  }
									}
							}
					else:
						gt = {
								"attachment":
									{
									  "type": "template",
									  "payload": {
									      "template_type": "generic",
									      "elements": [{
											              "title": data[i]['post_title'],
											              "image_url": data[i]['post_source'],
											              "subtitle": output,
											              "buttons": [
											                  {
											                      "type": "web_url",
											                      "url": data[i]['post_url'],
											                      "title": "Read More"
											                  },
											              ]
									          },
									      ]
									  }
									}
							}'''
		'''gt = {
					"attachment": {
					  "type": "template",
					  "payload": {
					      "template_type": "generic",
					      "elements": [
					                                  {
					              "title": data[i]['post_title'],
					              "image_url":data[i]['post_source'],
					              "subtitle": data[i]['post_content'],
					              "buttons": [
					                  {
					                      "type": "web_url",
					                      "url": data[i]['post_url'],
					                      "title": "Read More"
					                  },
					              ]
					          },
					      ]
					  }
					}
	        	}
		dispatcher.utter_message(json_message=gt)'''
		
		return [SlotSet('prev_count',prev_count_dets1)]