import streamlit as st
from newsgroups_clf import NewsGroupsClf

st.title('News classification demo')

st.markdown('Some instructions')

with st.form('form'):
    text_input = st.text_area('Enter news text here: ', 'news about sport')
    submit_button = st.form_submit_button('Predict group')
    
    if submit_button:
        model = NewsGroupsClf()
        label = model.get_topic(text_input)
        st.write(f'Predicted label: {label}')