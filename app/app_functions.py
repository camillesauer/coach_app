import streamlit as st
import requests
import pandas as pd
import json
import asyncio


def set_header():
    # Initialization
    if 'token' not in st.session_state:
        return
    else:
        return {
            'Authorization': 'Bearer ' + st.session_state.token
        }


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
            response = requests.post("https://coachdapi.herokuapp.com/login", data=login, headers={"content-type": "application/x-www-form-urlencoded"})
            if response:
                token_resp = response.json()
                st.session_state.token = token_resp['access_token']
                st.success("Welcome {}".format(username_input))
                status = st.radio("Select Actions: ", ('Create Feeling', 'My Feelings'))
                if (status == 'Create Feeling'):
                    st.info("Evaluate your feelings!")
                    create_feeling()
                else:
                    st.info("Discover all your Feelings")
                    get_feeling()
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
                if response:
                    st.write('hello')



def create_feeling():
    input_feeling = st.text_input('How do you feel?')
    if len(input_feeling) > 0:
        feeling = {'description': input_feeling}
        response = requests.post("https://coachdapi.herokuapp.com/feelings", json=feeling, headers=set_header())
        if response:
            print(response.text)
            feeling = response.json()
            # display original informations about customer
            st.write('score:', feeling['score'])
            st.write('description:', feeling['description'])


def get_feeling():
    response = requests.get("https://coachdapi.herokuapp.com/feelings", headers=set_header())
    if response:
        feelings = response.json()
        # display my feelings
        if feelings:
            st.dataframe(feelings)
            # st.table(feelings.iloc[0:10])
            # st.json(feelings)

