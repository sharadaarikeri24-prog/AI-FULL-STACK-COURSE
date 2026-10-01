import streamlit as St 

St.set_page_config(page_title="streamlit Demo",page_icon=".")
St.title("streamlit Demo")

St.write("This is plain text.")
St.markdown("This is **bold**,this is *italic*,this is :blue[colored.]")
St.write("you can also include a divider.")
St.divider()