import streamlit as st
import streamlit.components.v1 as components

def show_betting():
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
        <div style="text-align: justify; font-size: 16px;">
        <p>
        Over time, the competitors in Eurovision have looked very different. 
        Below, you can find visualizations of the first and most recent years that different countries have competed in Eurovision, 
        along with a link to their entry for that year.
        </p>
        </div>""", unsafe_allow_html=True
    )

#first and last year youtube maps

    st.markdown(
        """
        <div style="text-align: justify; font-size: 16px;">
        <p> So, who’s winning though? Well, certain countries are definitely doing much better than others at taking home the prize.
        However, when you look at who’s placed 1st, 2nd, and 3rd each year,
         you can see that although some countries aren’t winning,
         they are certainly consistent top finishers.
        </p>
        </div>""", unsafe_allow_html=True
    )

# INSERT BETTING TABLE WITH ODDS

    path_to_html = "./htmls/betting_table.html" 

    with open(path_to_html,'r') as f: 
        html_data = f.read()

    st.components.v1.html(html_data, scrolling=True, height=1000, width = 1600)

    # give some empty spaces in between
    st.markdown("<br><br>", unsafe_allow_html=True)

# INSERT POWER REGRESSIONS 

    path_to_html = "./htmls/betting_dashboard.html" 

    with open(path_to_html,'r') as f: 
        html_data = f.read()

    st.components.v1.html(html_data, scrolling=True, height=1000, width = 1600)

    # give some empty spaces in between
    st.markdown("<br><br>", unsafe_allow_html=True)
    
