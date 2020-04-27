## story_01
* greet{"name": "Ali"}
  - slot{"name": "Ali"}
  - utter_greet

## story_unhappy
* greet
  - utter_greet
* mood_unhappy
    - utter_cheer_up
    - utter_help_find

## story_default
* out_of_scope
    - utter_default

## story_hello
* hello
    - utter_welcome_message


## happy_path1
* greet
    - utter_greet
* inform{"keyword": "italy"}
    - slot{"keyword": "italy"}
    - utter_will_help
    - action_get_info
* thanks
    - utter_noworries
    - utter_question
* goodbye
    - utter_goodbye

## story_affirmqq
* affirm_qq
    - utter_happy
    - utter_goodbye


## story_denyqq
* deny_qq
    - utter_sorry
    - utter_help_find

## story_news
* news
    - utter_news

## story_case
* cases
    - utter_cases

## story_fines
* fines
    - utter_fines

## chitchat
* chitchat
   - respond_chitchat

## That's great
* mood_great
   - utter_happy
   - utter_help_find

## happy_path2
* greet
    - utter_greet
* inform{"keyword": "italy"}
    - slot{"keyword": "italy"}
    - utter_will_help
    - action_get_info
* affirm
    - utter_happy
    - utter_question
* inform{"keyword": "india"}
    - slot{"keyword": "india"}
    - utter_will_help
    - action_get_info
* affirm
    - utter_happy
    - utter_question
* goodbye
    - utter_goodbye

## happy_path3
* greet
    - utter_greet
* inform{"keyword": "money"}
    - slot{"keyword": "money"}
    - utter_will_help
    - action_get_info
* affirm
    - utter_happy
    - utter_question
* goodbye
    - utter_goodbye

## unhappy_path1
* greet
    - utter_greet
* inform{"keyword": "mexico"}
    - slot{"keyword": "mexico"}
    - utter_will_help
    - action_get_info
* deny
    - action_default_ask_rephrase
    - utter_sorry
* inform{"keyword": "mexico"}
    - slot{"keyword": "mexico"}
    - utter_will_help
    - action_get_info
* thanks
    - utter_noworries
    - utter_question
* goodbye
    - utter_goodbye

## unhappy path2
* greet
    - utter_greet
* inform{"keyword": "london"}
    - slot{"keyword": "london"}
    - utter_will_help
    - action_get_info
* deny
    - action_default_ask_rephrase
    - utter_sorry
* inform{"keyword": "china"}
    - slot{"keyword": "china"}
    - utter_will_help
    - action_get_info
* thanks
    - utter_noworries
    - utter_question
* goodbye
    - utter_goodbye

## story_goodbye
* goodbye
    - utter_goodbye

## story_thankyou
* thanks
    - utter_noworries

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## interactive_story_1
* greet
    - utter_greet
* chitchat
    - respond_chitchat
* chitchat
    - respond_chitchat
* greet
    - utter_greet
* greet
    - utter_greet
* mood_great
    - utter_happy
    - utter_help_find
* inform{"category": "news", "keyword": "India"}
    - slot{"category": "news"}
    - slot{"keyword": ["money laundering", "India"]}
    - utter_will_help
    - action_get_info
* affirm
    - utter_happy
    - utter_question
* goodbye
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* inform{"category": "case", "keyword": "Mexico"}
    - slot{"category": "case"}
    - slot{"keyword": "Mexico"}
    - utter_will_help
    - action_get_info
* affirm
    - utter_happy
    - utter_question
* goodbye
    - utter_goodbye

## interactive_story_3
* greet
    - utter_greet
* inform{"category": "report", "keyword": "Zimbabwe"}
    - slot{"category": "report"}
    - slot{"keyword": "Zimbabwe"}
    - utter_will_help
    - action_get_info
* affirm
    - utter_happy
    - utter_question
* goodbye
    - utter_goodbye

## interactive_story_4
* greet
    - utter_greet
* inform{"category": "report", "keyword": "HSBC"}
    - slot{"category": "report"}
    - slot{"keyword": "HSBC"}
    - utter_will_help
    - action_get_info
* affirm
    - utter_happy
    - utter_question
* goodbye
    - utter_goodbye

## interactive_story_5
* greet
    - utter_greet
* inform{"category": "report", "keyword": "hsbc"}
    - slot{"category": "report"}
    - slot{"keyword": "hsbc"}
    - utter_will_help
    - action_get_info
* affirm
    - utter_happy
    - utter_question
* goodbye
    - utter_goodbye

## interactive_story_6
* greet
    - utter_greet
* inform{"category": "cases", "keyword": "india"}
    - slot{"category": "cases"}
    - slot{"keyword": "india"}
    - utter_will_help
    - action_get_info
* affirm
    - utter_happy
    - utter_question
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* inform{"keyword": "aml"}
    - slot{"keyword": ["aml"]}
    - utter_will_help
    - action_get_info
* inform{"category": "cases", "keyword": "aml"}
    - slot{"category": "cases"}
    - slot{"keyword": ["aml"]}
    - utter_will_help
    - action_get_info
* inform{"category": "reports", "keyword": "aml"}
    - slot{"category": "reports"}
    - slot{"keyword": ["aml"]}
    - utter_will_help
    - action_get_info

## interactive_story_1
* greet
    - utter_greet
* mood_great
    - utter_happy
    - utter_help_find
* inform{"keyword": "aml"}
    - slot{"keyword": ["aml"]}
    - utter_will_help
    - action_get_info
* previous{"category": "data", "keyword": "previous"}
    - slot{"category": "data"}
    - slot{"keyword": ["previous"]}
    - utter_will_help
    - action_get_info

## interactive_story_1
* greet
    - utter_greet
* mood_great
    - utter_happy
    - utter_help_find
* inform{"keyword": "aml"}
    - slot{"keyword": ["aml"]}
    - utter_will_help
    - action_get_info
* previous{"previous": "previous"}
    - slot{"previous": ["more", "previous"]}
    - utter_will_help
    - action_get_info

## interactive_story_1
* greet
    - utter_greet
* inform{"keyword": "aml"}
    - slot{"keyword": ["aml"]}
    - utter_will_help
    - action_get_info
* previous{"previous": "previous"}
    - slot{"previous": ["more", "previous"]}
    - utter_will_help
    - action_get_info
* inform{"category": "details", "keyword": "distribution"}
    - action_slot_reset
    - slot{"category": "details"}
    - slot{"keyword": ["distribution"]}
    - utter_will_help
    - action_get_info
* previous{"previous": "previous"}
    - slot{"previous": ["previous"]}
    - utter_will_help
    - action_get_info

## New Story

* greet
    - utter_greet
* inform{"keyword":"aml"}
    - slot{"keyword":["aml"]}
    - slot{"keyword":["aml"]}
    - utter_will_help
    - action_get_info
    - slot{"prev_count":"0"}
* previous{"previous":"previous"}
    - slot{"previous":["previous"]}
    - slot{"previous":["previous"]}
    - utter_will_help
    - action_get_info
    - slot{"prev_count":"1"}
* previous{"previous":"previous"}
    - slot{"previous":["previous"]}
    - slot{"previous":["previous"]}
    - utter_will_help
    - action_get_info
    - slot{"prev_count":2}
* previous{"previous":"previous"}
    - slot{"previous":["previous"]}
    - slot{"previous":["previous"]}
    - utter_will_help
    - action_get_info
    - slot{"prev_count":3}
* inform{"keyword":"distribution"}
    - slot{"keyword":["distribution"]}
    - slot{"keyword":["aml"]}
    - slot{"previous":["previous"]}
    - slot{"previous":["previous"]}
    - slot{"previous":["previous"]}
    - slot{"keyword":["distribution"]}
    - action_slot_reset
    - slot{"previous":null}
    - slot{"prev_count":"0"}
    - utter_will_help
    - action_get_info
    - slot{"prev_count":"0"}
* previous{"previous":"previous"}
    - slot{"previous":["previous"]}
    - slot{"previous":["previous"]}
    - utter_will_help
    - action_get_info
    - slot{"prev_count":"1"}
* previous{"previous":"previous"}
    - slot{"previous":["previous"]}
    - slot{"previous":["previous"]}
    - utter_will_help
    - action_get_info
    - slot{"prev_count":2}
* inform{"keyword":"million"}
    - slot{"keyword":["million"]}
    - action_slot_reset
    - slot{"previous":null}
    - slot{"prev_count":"0"}
    - utter_will_help
    - action_get_info
    - slot{"prev_count":"0"}
* previous{"previous":"previous"}
    - slot{"previous":["previous"]}
    - utter_will_help
    - action_get_info
    - slot{"prev_count":"1"}
* previous{"previous":"previous"}
    - slot{"previous":["previous"]}
    - utter_will_help
    - action_get_info
    - slot{"prev_count":2}
* previous{"previous":"previous"}
    - slot{"previous":["previous"]}
    - utter_will_help
    - action_get_info
    - slot{"prev_count":3}
* affirm
    - utter_happy
    - utter_question
* thanks
    - utter_noworries

## interactive_story_1
* greet
    - utter_greet
* inform{"keyword": "South Korea"}
    - slot{"keyword": ["South Korea"]}
    - utter_will_help
    - action_get_info
    - slot{"prev_count": "0"}
* inform{"previous": "more", "keyword": "South Korea"}
    - slot{"keyword": ["South Korea"]}
    - slot{"previous": ["more"]}
    - utter_will_help
    - action_get_info
    - slot{"prev_count": "1"}
