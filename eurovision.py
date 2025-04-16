import streamlit as st
import streamlit.components.v1 as components
from background import show_background
from home import show_home
from references import show_references
from relationships import show_relationships
from song import show_song
from betting import show_betting
from fun import show_fun


# Main application entry point
def main():
    # Sidebar navigation
    st.sidebar.title("Navigation")
    pages = {
        "Home": show_home,
        "Background": show_background,
        "Song Characteristics": show_song,
        "Relationships": show_relationships,
        "Betting": show_betting,
        "Fun Facts": show_fun,
        "References": show_references
     }
    selected_page = st.sidebar.radio("Go to", list(pages.keys()))

    # Render the selected page
    pages[selected_page]()


if __name__ == "__main__":
    main()