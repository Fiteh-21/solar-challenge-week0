import streamlit as st
from utils import (
    load_data, 
    filter_by_countries, 
    plot_ghi_boxplot, 
    plot_ghi_histogram,  # new import
    get_top_locations
)

st.set_page_config(page_title="Solar Resource Dashboard", layout="wide")

st.title("Solar Resource Dashboard")

st.markdown("""
Upload one or more CSV files (Benin, Sierra Leone, Togo) with solar data.  
Select countries to filter and visualize GHI distribution, histogram, and top regions.
""")

# File uploader allowing multiple files
uploaded_files = st.file_uploader(
    "Upload CSV files for countries", 
    type=["csv"], 
    accept_multiple_files=True
)

if uploaded_files:
    # Convert list of UploadedFile objects to dict with filename keys for utils.load_data
    files_dict = {file.name: file for file in uploaded_files}
    
    # Load combined data
    data = load_data(files_dict)
    
    if not data.empty:
        # Country filter multi-select
        countries = st.multiselect(
            "Select countries to visualize",
            options=data['Country'].unique(),
            default=data['Country'].unique()
        )
        
        if countries:
            filtered_data = filter_by_countries(data, countries)
            
            st.subheader("GHI Boxplot")
            plot_ghi_boxplot(filtered_data)

            st.subheader("GHI Histogram")
            plot_ghi_histogram(filtered_data)
            
            # Use get_top_locations instead of get_top_regions (assuming you rename in utils)
            top_locations = get_top_locations(filtered_data)
            if not top_locations.empty:
                if 'Country' in top_locations.columns:
                    st.subheader("Top Countries by Average GHI")
                else:
                    st.subheader("Top Regions by Average GHI")
                st.table(top_locations)
            else:
                st.info("No location data available.")
        else:
            st.info("Please select at least one country to display data.")
    else:
        st.warning("Uploaded files contain no valid data.")
else:
    st.info("Please upload one or more CSV files to begin.")