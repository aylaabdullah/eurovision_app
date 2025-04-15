import streamlit as st
from background import show_background
from home import show_home
from references import show_references
from relationships import show_relationships


# Main application entry point
def main():
    # Sidebar navigation
    st.sidebar.title("Navigation")
    pages = {
        "Home": show_home,
        "Background": show_background,
        "Relationships": show_relationships,
        # "Similarity of Sites": show_cluster_section,
        "References": show_references,
     }
    selected_page = st.sidebar.radio("Go to", list(pages.keys()))

    # Render the selected page
    pages[selected_page]()



# # Maps section handler
# def show_maps_section():
    
#     st.subheader("General Map Showing All Data Points")
#     create_first_map()

#     st.subheader("Filtered Map by Reference")
#     create_second_map()

#     # Add footer to the Maps section
#     add_footer()

# # Analysis section handler (includes multiple analyses)
# def show_analysis_section():

#     show_analysis()
    
#     show_depth_analysis()

#     # Add footer to the Maps section
#     #empty spaces
#     st.markdown("<br><br>", unsafe_allow_html=True)
#     st.write("------")
#     add_footer()

# # clustering
# def show_cluster_section():
#     #show the

#     show_clustermap()



# if __name__ == "__main__":
#     main()