import streamlit as st
import numpy as np
import pandas as pd
import requests
from datetime import datetime



def login():
    """
    Log user before using app
    :return:
    """
    username_input = st.text_input('Username:')
    if len(username_input) > 0:
        input_pass = st.text_input('Password:')
        if len(input_pass) > 0:
                if st.button('Login'):
                    login = {'username': username_input, 'password': input_pass }

                    response = requests.post("https://coachdapi.herokuapp.com/login", json=login)
                    if not response:
                        st.write("no user exists")
                        if st.button('Créer un compte'):
                            next(create_user())
                    else:
                        st.write("Welcome {}".format(username_input))
                        PAGES = {
                            "App1": app1,
                            "App2": app2
                        }
                        st.sidebar.title('Navigation')
                        selection = st.sidebar.radio("Go to", list(PAGES.keys()))
                        page = PAGES[selection]
                        page

# app1.py
def app1():
    st.title('APP1')
    st.write('Welcome to app1')

# app2.py
def app2():
    st.title('APP2')
    st.write('Welcome to app2')

def create_user():
    """
    dsplay the inputs to create a user and request api to create in db
    :return: none
    """
    input_name = st.text_input('Name:')
    if len(input_name) > 0:
        input_role = st.text_input('Rôle:')
        if len(input_role) > 0:
            st.write("choose between user or admin!")
        if input_role != 'user' or 'admin':
            input_password = st.text_input('Pass:')
            if len(input_password) > 0:
                # if st.button('create user'):
                    user = {'username': input_name, 'role': input_role, 'password': input_password}
                    response = requests.post("https://coachdapi.herokuapp.com/users/", json=user)
                    print(response.text)
                    # if not response:
                    #     st.write("request failed")
                    # else:
                    #     st.write("compte crée avec succès!")
                    st.write("Welcome {} to your board".format(input_name))