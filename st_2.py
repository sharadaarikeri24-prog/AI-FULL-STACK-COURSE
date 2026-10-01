import streamlit as St
St.set_page_config(page_title="Text input Demo")

name=St.text_input("Enter your name:", placeholder="e.g.Krishn")
St.write(f"Hello,{name}!")

secret=St.text_input("Enter your password:",type="password")
St.write(f"your password has {len(secret)} characters.")

comments=St.text_area("Any additional comments?",height=150)
St.write(f"your wrote {len(comments)} characters.")

if St.button("Submit"):
    St.write("you clicked on submit!")

show_message=St.checkbox("Do you want an extra message?")
if show_message:
    St.write("this is the message.Have a good day!")
