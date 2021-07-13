import streamlit as st
import numpy as np
import pandas as pd
import requests
from datetime import datetime
from streamlit import *

def login():
    """
    Log user before using app
    :return:
    """
    username_input = st.text_input('Username:')
    if len(username_input) > 0:
        input_pass = st.text_input('Password:')
        if len(input_pass) > 0:
                login = {'username': username_input, 'password': input_pass }
                response = requests.post("https://coachdapi.herokuapp.com/login", json=login)
                st.success("Welcome {}".format(username_input))
                status = st.radio("Select Actions: ", ('Create Feeling', 'My Feelings'))
                if (status == 'Create Feeling'):
                    st.info("Evaluate your feelings!")

                else:
                    st.info("Discover all your Feelings")
        else:
            st.error("user not registered!")


def create_user():
    """
    dsplay the inputs to create a user and request api to create in db
    :return: none
    """
    input_name = st.text_input('Name:')
    if len(input_name) > 0:
        input_password = st.text_input('Pass:')
        if len(input_password) > 0:
                user = {'username': input_name, 'password': input_password}
                response = requests.post("https://coachdapi.herokuapp.com/users/", json=user)


def create_feeling():
    input_feeling = st.text_input('How do you feel?')
    if len(input_feeling) > 0:
        feeling = {'description': input_feeling}
        response = requests.post("https://coachdapi.herokuapp.com/feelings/", json=feeling)
        print(response.text)
        feeling = response.json()
        # display original informatiosn about customer
        st.write('score:', feeling['score'])
        st.write('description:', feeling['description'])

def display_feeling_by_cust(user_id: int):
    """
    display the list of all the texts writen by one customer
    :param id_customer: int, id of the customer choosen
    :return: none
    """
    # request to api to get the list of the texts written by one customer
    response = requests.get("https://coachdapi.herokuapp.com/feelings/{}".format(user_id))
    if response:
        feelings = response.json()
        if len(feelings) > 0:
            for feeling in feelings:
                # call to api to get the customer writer of thoses texts
                result = requests.get("https://coachdapi.herokuapp.com/feelings/{}".format(feeling['user_id']))
                if result:
                    user = result.json()
                    st.write('Feeling Id: ', feeling['id'])
                    st.write('User: {} {} '.format(user['username'], user['user_id']))
                    st.write('Score: ', feeling['score'])
                    st.write('------------------------------------------------')
        else:
            st.write("this customer has not yet writen texts")



# def get_feeling():
#     url = f"https://coachdapi.herokuapp.com/feelings/{'user_id'}"
#     res = requests.get(url)
#     if res:
#         st.info(res)


def display_user_by_id(user_id):
    """
    request api to get one customer by its id, and display
    :param id: int (id of the customer we want to display)
    :return: none
    """
    response = requests.get(" http://127.0.0.1:8000/users/{}".format(user_id))
    if not response:
        st.write('No Data!')
    else:
        user = response.json()
        st.write('Name: ', user['name'])

def display_all_user():
    """
    request api for the list of all customers, and display it
    :return:none
    """
    response = requests.get("https://coachdapi.herokuapp.com/users/")
    print(response.text)
    users = response.json()
    for user in users:
        st.write(user)
        st.write('---------------------------------------')