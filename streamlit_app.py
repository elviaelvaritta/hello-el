import streamlit as st

st.markdown("*Hello* aku **elvia** ***keren***.")
st.markdown('''
    :red[Selamat] :orange[datang] :green[di aplikasi] :blue[ini] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)
