import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def load_data(uploaded_files):
    """
    Accepts a dict of uploaded files with keys as filenames and values as UploadedFile objects.
    Returns a combined DataFrame with a 'Country' column inferred from the filename.
    """
    df_list = []
    for filename, file in uploaded_files.items():
        try:
            df = pd.read_csv(file)
            # Extract country name from filename, e.g. "benin.csv" -> "Benin"
            country = filename.split('.')[0].replace('_', ' ').title()
            df['Country'] = country
            df_list.append(df)
        except Exception as e:
            st.error(f"Error loading {filename}: {e}")
    if df_list:
        combined_df = pd.concat(df_list, ignore_index=True)
        return combined_df
    else:
        return pd.DataFrame()  # empty

def filter_by_countries(df, countries):
    return df[df['Country'].isin(countries)]

def plot_ghi_boxplot(df):
    """
    Create a boxplot of GHI grouped by country
    Assumes df has columns: 'GHI' and 'Country'
    """
    if df.empty:
        st.warning("No data to plot.")
        return
    fig, ax = plt.subplots(figsize=(8,5))
    sns.boxplot(data=df, x='Country', y='GHI', ax=ax)
    ax.set_title("GHI Distribution by Country")
    st.pyplot(fig)

def plot_ghi_histogram(df):
    """
    Plot a histogram of GHI values
    """
    if df.empty:
        st.warning("No data to plot.")
        return
    fig, ax = plt.subplots(figsize=(8,5))
    sns.histplot(df['GHI'], bins=30, kde=True, color='skyblue', ax=ax)
    ax.set_title("GHI Distribution Histogram")
    st.pyplot(fig)

def get_top_locations(df, top_n=10):
    """
    Returns top N locations (regions or countries) by average GHI.
    """
    if df.empty:
        return pd.DataFrame()

    # Try region columns first, then fall back to country
    possible_cols = ['Region', 'region', 'Location', 'location', 'Area', 'area', 'Country', 'country']
    
    location_col = None
    for col in possible_cols:
        if col in df.columns:
            location_col = col
            break

    if location_col is None:
        st.warning(f"No region or country column found. Available columns: {list(df.columns)}")
        return pd.DataFrame()

    if 'GHI' not in df.columns:
        st.warning("No GHI column found in data")
        return pd.DataFrame()

    top_locations = (
        df.groupby(location_col)['GHI']
        .mean()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )
    
    # Use appropriate column name based on what we found
    if location_col.lower() == 'country':
        top_locations = top_locations.rename(columns={location_col: 'Country', 'GHI': 'Average GHI'})
    else:
        top_locations = top_locations.rename(columns={location_col: 'Region', 'GHI': 'Average GHI'})

    return top_locations