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

    st.markdown(
        """
        <div style="text-align: justify; font-size: 14px;">
        <p>
        What's Eurovision without some weird trivia? Here are some of our favorite odd, strange, or just funny findings.
        <p>
        First up, what does every Eurovision song have in common? 
        Well, maybe not all of them, but a whole lot certainly use these words.
        Here are the top 20 words used in Eurovision lyrics.
        </p>
        </div>""", unsafe_allow_html=True
    )

#INSERT WORD CLOUD HERE

    st.markdown(
        """
        <div style="text-align: justify; font-size: 14px;">
        <p> We already told you something about how voting in Eurovision is impacted by national politics 
        (don't remember that? Check out Relationships!). But what if we looked at how fair those relationships are? 
        Do countries vote for one another equally? Of course not. Check out the reciprocity in Eurovision voting by country below, 
        as well as the top 10 most uneven relationships since 2016. 
        (Shoutout to the Czech Republic, whose loyalty in voting is never reciprocated).

        </p>
        </div>""", unsafe_allow_html=True
    )

#Reciprocity Dashboard Here

    path_to_html = "./htmls/reciprocity_html.html" 

    with open(path_to_html,'r') as f: 
        html_data = f.read()

    st.components.v1.html(html_data, scrolling=True, height=1000, width = 1600)
    