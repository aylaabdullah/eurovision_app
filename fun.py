import streamlit as st
import streamlit.components.v1 as components

def show_fun():
    # Title of the page
    st.markdown(
        """
        <h1 style="text-align: center; font-size: 24px;">
        Fun Facts
        </h1>
        <p style="text-align: center; font-size: 12px; margin-top: -10px;">
        </p>
        """, unsafe_allow_html=True
    )

# text about word cloud
    st.markdown(
        """
        <div style="text-align: justify; font-size: 16px;">
        <p>
        What's Eurovision without some weird trivia? Here are some of our favorite odd, strange, or just funny findings.
        <p>
        First up, what does every Eurovision song have in common? 
        Well, maybe not all of them, but a whole lot certainly use these words.
        Here are the top 20 words used in Eurovision lyrics.
        </div>""", unsafe_allow_html=True
    )

#INSERT WORD CLOUD HERE

# text about reciprocity
    st.markdown(
        """
        <div style="text-align: justify; font-size: 16px;">
       We already told you something about how voting in Eurovision is impacted by national politics 
        (don't remember that? Check out Relationships!). But what if we looked at how fair those relationships are? 
        Do countries vote for one another equally? Of course not. Check out the reciprocity in Eurovision voting by country below, 
        as well as the top 10 most uneven relationships since 2016. 
        (Shoutout to the Czech Republic, whose loyalty in voting is never reciprocated).
        </div>""", unsafe_allow_html=True
    )

#Reciprocity Dashboard Here

    path_to_html = "./htmls/reciprocity_html.html" 

    with open(path_to_html,'r') as f: 
        html_data = f.read()

    st.components.v1.html(html_data, scrolling=True, height=1000, width = 1600)
    
# text about key and country
    st.markdown(
        """
        <div style="text-align: justify; font-size: 16px;">
        Ever wondered what a country songs like? 
        Well, it turns out Slovakia loves the key of A Major, 
        because every entry they've sent since 2009 has been in that key. 
        Azerbaijan and Norway, in the meanwhile, really like to mix it up, 
        changing the key of their song almost every year.
        </div>""", unsafe_allow_html=True
    )

#Key_country Here

    path_to_html = "./htmls/key_country_html.html" 

    with open(path_to_html,'r') as f: 
        html_data = f.read()

    st.components.v1.html(html_data, scrolling=True, height=500, width = 800)

    # text about first place by year
    st.markdown(
        """
        <div style="text-align: justify; font-size: 16px;">
        We've already told you about which countries have won the most, but what about which years? 
        1969 blew the competition out of the water, 
        as France, the Netherlands, Spain, and the United Kingdom all took first that year. 
        Sometimes even a competition can be collaborative. 
        </div>""", unsafe_allow_html=True
    )

#first_year Here

    path_to_html = "./htmls/first_year_html.html" 

    with open(path_to_html,'r') as f: 
        html_data = f.read()

    st.components.v1.html(html_data, scrolling=True, height=1000, width = 1600)

 # text about gender and lgbtqia+ status
    st.markdown(
        """
        <div style="text-align: justify; font-size: 16px;">
        How does gender and LGBTQIA+ identity impact song choices? See what percentages of all-men, 
        all-women, 
        and mix-gender groups, 
        as well as LGBTQIA+ performers and cisgender, heterosexual performers chose specific musical genres and keys from 2009-2023.
        </div>""", unsafe_allow_html=True
    )

#first_year Here

    path_to_html = "./htmls/gender_dash_html.html" 

    with open(path_to_html,'r') as f: 
        html_data = f.read()

    st.components.v1.html(html_data, scrolling=True, height=1000, width = 1600)