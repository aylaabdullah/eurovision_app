import streamlit as st
import streamlit.components.v1 as components



def show_references():
    # Title for the references section
    st.title("References")

    # give some empty spaces in between
    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("Key References:")

    # Header for supplementary material
    st.markdown(
        "<h2 style='font-size: 18px;'>2023 John Ashley Burgoyne and Janne Spijkervet and David John Baker,<p> \
       'Measuring the {Eurovision Song Contest}: A Living Dataset for Real-World {MIR}.' "
        "Proceedings of the 24th International Society for Music Information Retrieval Conference, Milan, Italy. </h2>",
        unsafe_allow_html=True
    )
    st.link_button(url='https://archives.ismir.net/ismir2023/paper/000097.pdf', label = 'Paper Link')
    st.link_button(url='https://github.com/Spijkervet/eurovision-dataset', label = 'Repository Link')

    st.markdown(
        "<h2 style='font-size: 18px;'>2023 diamondsnake, <p> 'Eurovision Song Contest Data.' </h2>",
        unsafe_allow_html=True)
    st.link_button(url='https://www.kaggle.com/datasets/diamondsnake/eurovision-song-contest-data', label = 'Repository Link')

    st.markdown(
        "<h2 style='font-size: 18px;'>2025 Wikipedia, <p>"
        "'List of countries in the Eurovision Song Contest.' </h2>",
        unsafe_allow_html=True
    )
    st.link_button(url='https://en.wikipedia.org/wiki/List_of_countries_in_the_Eurovision_Song_Contest', label = 'Page Link')

    st.markdown(
        "<h2 style='font-size: 18px;'>2025 Wikipedia, <p>"
        "'List of LGBTQ participants in the Eurovision Song Contest.' </h2>",
        unsafe_allow_html=True
    )
    st.link_button(url='https://en.wikipedia.org/wiki/List_of_LGBTQ_participants_in_the_Eurovision_Song_Contest', label = 'Page Link')
#empty spaces
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.write("------")