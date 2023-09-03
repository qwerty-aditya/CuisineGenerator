import numpy as np
import pandas as pd
import streamlit as st
import langchain_helper
st.title('Restaurant Name Generator')

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "British", "Italian", "Chinese", "Mexican", "German", "American"))


if cuisine:
    response = langchain_helper.restaurant_name_and_item(cuisine)
    st.header(response['restauraunt_name'].strip())
    menu_items = response['menu_items'].split("\n")
    st.write("**Menu items**")
    for item in menu_items:
        if len(item) > 2:
            st.write(item.strip())