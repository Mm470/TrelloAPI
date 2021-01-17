# TrelloAPI
## A simple python code to create a new card on trello board 
This CLI programme will ask to enter the card name, choose a list, and add labels to a new card.

## Installation
1- This code needs python3.6.5, if you dont have this python version, you can create a virtual environments using pyenv:


    pyenv install 3.6.5
    pyenv local 3.6.5 # Activate Python 3.6.5 for the current project


2- Simply use pip to install the PyInquirer package, pprint, and make sure you have json package and requests.


    pip3 install PyInquirer


    pip3 install pprint

3- This code was tested on the following board: https://trello.com/b/1Ln9wmuY/trello-api 
This is a public board for the purpose of testing this code so feel free to edit.

4- Run the code:


    python3 newcard.py

## Use on a different board
Log in to Trello and visit [trello.com/app-key](https://trello.com/app-key) to get a `token` and `app key`. These need to be supplied when you create the Trello object (see below).

Replace the token and key in the code.

Get the board ID and replace it in the code.

Create new labels, get the labels ID and replace it in the code.

After running the code you will see the lists from your new board.
