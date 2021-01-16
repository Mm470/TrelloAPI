from __future__ import print_function, unicode_literals

from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint
import requests
import json



## API key and token generated fron trello
key = '36e9b1a3007d0822bc43f669db6aebfa'
token = '557d40830599c1e5f010d7112fa9e619c2844f1b91acff78f6b3f9d709a9f408'

## Getting all the lists fron the board

url_list = "https://api.trello.com/1/boards/1Ln9wmuY/lists"

query = {
   'key': key,
   'token': token
}

getlists = requests.request(
   "GET",
   url_list,
   params=query
)

# Getting the list names 

lists = getlists.json()
l = len(lists)
x = int(0)
C = []
while x < l: 
    C.append(lists[x]['name'])
    x += 1

def get_list_choices(lchoice):
    lchoice = json.dumps(C)
    data  = json.loads(lchoice)
    return data


# Style the CLI

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


# Questions  

questions = [
    {
    ##Question 1 : Ask for the Card name as input
        'type': 'input',
        'message': 'Please enter the name of your new card:',
        'name': 'name_info',
        'validate': lambda answer: 'You must choose a list.' \
            if len(answer) == 0 else True
    },
    {
    ## Question 2 : Choose the list where the new card will be as a list
        'type': 'list',
        'message': 'Choose the list where you want to create the new card:',
        'name': 'list_info',
        'choices': get_list_choices,
        'validate': lambda answer: 'You must choose a list.' \
            if len(answer) == 0 else True
    },
    {
    ## Question 3 : Choose the labels as a checkbox:
        'type': 'checkbox',
        'message': 'Choose Labels for your new card:',
        'name': 'color_info',
        'choices': [
            {
                'name': 'Red'
            },
            {
                'name': 'Green'
            },
            {
                'name': 'Yellow'
            },
            {
                'name': 'Orange'
            },
             {
                'name': 'Bleu'
            },
             {
                'name': 'Purple'
            },
         
        ],
        'validate': lambda answer: 'You must choose a list.' \
            if len(answer) == 0 else True
    },

]

## Get the answers
answers = prompt(questions, style=style)
#pprint(answers)

## Get the answer for the list where the card will be
list_info = answers['list_info']
for i in lists:
     if i['name'] == list_info:
        list_id = i['id']
        
        break

## Get the answer for the name of the new card
name_info = answers['name_info']
c_info = json.dumps(answers['color_info'])
color_info  = json.loads(c_info)


## These are the IDs of all the labels created on the board
id_green = "60036bd46542d49419c39d92"
id_yellow = "60036bd46542d49419c39d94"
id_orange = "60036bd46542d49419c39d96"
id_red = "60036bd46542d49419c39d99"
id_purple = "60036bd46542d49419c39d9b"
id_bleu = "60036bd46542d49419c39d9c"

## Number of selected labels
num_colors = len(answers['color_info'])

## Get the label IDs according to the selected labels
a = int(0)
labels_id = []
while a < num_colors: 
    if color_info[a] == "Green":
      labels_id.append(id_green)
      a += 1
    elif color_info[a] == "Red":
      labels_id.append(id_red)
      a += 1
    elif color_info[a] == "Yellow":
      labels_id.append(id_yellow)
      a += 1
    elif color_info[a] == "Orange":
      labels_id.append(id_orange)
      a += 1
    elif color_info[a] == "Bleu":
      labels_id.append(id_bleu)
      a += 1
    elif color_info[a] == "Purple":
      labels_id.append(id_purple)
      a += 1
    else:
      print("Invalid Input") 


## ADD the new card
url_card = "https://api.trello.com/1/cards"

query_card = {
   'key': key,
   'token': token,
   'idList': list_id,
   'name': name_info,
   'idLabels': labels_id
   #'idLabels': ["5e1f08bbaf988c41f2e90eba", "5e1f08bbaf988c41f2e90ebb", "5e1f08bbaf988c41f2e90ebc", "5e1f08bbaf988c41f2e90ebf", "5e1f08bbaf988c41f2e90ec0"]

}

response = requests.request(
   "POST",
   url_card,
   params=query_card
)

print("Your card was added! Thank you!")
 
 