import streamlit as st

def show_background():
    # Title of the page
    st.markdown(
        """
        <h1 style="text-align: center; font-size: 24px;">
        Background
        </h1>
        <p style="text-align: center; font-size: 12px; margin-top: -10px;">
        </p>
        """, unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="text-align: justify; font-size: 14px;">
        <p>
        Over time, the competitors in Eurovision have looked very different. 
        Below, you can find visualizations of the first and most recent years that different countries have competed in Eurovision, 
        along with a link to their entry for that year.
        </p>
        </div>""", unsafe_allow_html=True
    )

#INSERT FIRST/LAST YEAR MAPS HERE

    st.markdown(
        """
        <div style="text-align: justify; font-size: 14px;">
        <p> So, who’s winning though? Well, certain countries are definitely doing much better than others at taking home the prize.
        However, when you look at who’s placed 1st, 2nd, and 3rd each year,
         you can see that although some countries aren’t winning,
         they are certainly consistent top finishers.
        </p>
        </div>""", unsafe_allow_html=True
    )

# INSERT WINNERS AND TOP 3