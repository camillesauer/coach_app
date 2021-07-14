
from app_functions import  *
import streamlit as st

# will use this list and next button to increment page, MUST BE in the SAME order
# as the list passed to the radio button
new_choice = ['Home','Coach']


# create your radio button with the index that we loaded
choice = st.sidebar.radio("Menu",('Home','Coach'))


# finally get to whats on each page
if choice == 'Home':
    st.header('Coach Generation')
    st.markdown("***")
    st.video('https://youtu.be/Cpr6pIuptYE')
    st.markdown("***")
    st.info('Please sign in')
    login()
    st.markdown("***")
    st.write('Or')
    if st.button('Create an account'):
        create_user()
    st.markdown("***")
    # create a button in the side bar that will move to the next page/radio button choice
    # next = st.button('Begin experience')

if choice == 'Coach':
    # only if customer exist in db, initialization of choices
    login()
    st.markdown("***")
    selection = st.selectbox("Action",
                             ["Choose action", "Display all users", "Display list of texts", "Display a text",
                              "Delete a user"])

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(240, 255, 255);
}
</style>""", unsafe_allow_html=True)

