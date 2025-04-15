import streamlit as st

def show_relationships():
    # Title of the page
    st.markdown(
        """
        <h1 style="text-align: center; font-size: 24px;">
        Relationships
        </h1>
        <p style="text-align: center; font-size: 12px; margin-top: -10px;">
        </p>
        """, unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="text-align: justify; font-size: 14px;">
        <p>
        But what about just good, old fashioned politics? 
        It turns out, in Eurovision, some competitors start with an advantage just because of where they’re from. <p>
        Using each year’s votes, we wanted to see if we could find a pattern between which countries vote for which other countries. 
        After all, if some countries are just more likely to give their votes to others, 
        then that could be an important factor in who wins. 
        <p>
        To find out, we wanted to know how many points any given country (e.g., Germany) gave to another given country (e.g., France) each year in years that both competed. 
        This amount was then divided by the total maximum number of points* that a country could have awarded that year. 
        So, for example, if Germany gave France 6 points in 2005, when the maximum number of points was 12, then its relationship for that year would be 0.5. 
        <p>
        Then, we calculated the mean of that voting point ratio across a given amount of years to show the relative likelihood that one country would cast their votes for another during that time span. 
        To use our same example, if Germany’s mean voting ratio with France from 1956-2015 was 0.23, 
        then that indicates that, regardless of France’s entry in a given year, 
        Germany would award France roughly 3 points in an average year (using the old scoring system).
        <p>
        Using these mean voting scores, 
        it is then possible to calculate a country’s popularity across all countries by taking a mean of all mean voting ratios for a given country. 
        So, for example, using France again, between the years 1956 and 2015, 
        it has a mean voting ratio of 0.20 across all countries, meaning that between those years, 
        countries, on average, gave France 2 points in an average year. That might sound good, 
        until you see that Russia, during that same time period (though Russia joined Eurovision much later) was receiving nearly 4 points on average from each country in an average year (score of 0.32)! 
        In other words, some countries, statistically, are just more likely to get points from their peers.
        <p>
        You can also invert an individual country’s mean voting ratios to see which countries are more (or less) popular with other countries, 
        or what we call a popularity ratio. 
        France during this same time period, for example, has its highest popularity ratios from Monaco, Andorra, and Armenia.
        </div>""", unsafe_allow_html=True
    )

#INSERT Relationship Dashboard Here