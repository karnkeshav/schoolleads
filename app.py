import streamlit as st
from serpapi import GoogleSearch
import pandas as pd
import time
import random

TIER_3_CITIES = [
    "Udaipur", "Jhansi", "Madurai", "Aligarh", "Guntur",
    "Warangal", "Tirunelveli", "Nellore", "Rajahmundry", "Kurnool",
    "Bikaner", "Amravati"
]

def construct_query(platform, city, keywords="admissions"):
    """
    Constructs a Google Dork query based on the platform and city.
    """
    # Base query part: ("Principal" OR "Director") "{City}" "{keywords}"
    base_query = '("Principal" OR "Director") "{}" "{}"'.format(city, keywords)

    if platform == "LinkedIn":
        # site:linkedin.com/in ("Principal" OR "Director") "Udaipur" "admissions"
        return f'site:linkedin.com/in {base_query}'
    elif platform == "Facebook":
        return f'site:facebook.com {base_query}'
    elif platform == "Instagram":
        return f'site:instagram.com {base_query}'
    else:
        return f'{base_query}'

def fetch_results(query, num_results=10):
    """
    Fetches results using SerpApi.
    Returns a list of dictionaries.
    """
    results_data = []

    # Retrieve API Key from secrets or input
    api_key = None
    if "SERPAPI_KEY" in st.secrets:
        api_key = st.secrets["SERPAPI_KEY"]
    else:
        # Fallback for development/first run without secrets
        # In a real app, we might ask the user to input it
        # For now, we will warn if missing
        pass

    if not api_key:
        st.error("⚠️ SERPAPI_KEY not found in secrets. Please configure it in .streamlit/secrets.toml.")
        return []

    params = {
        "q": query,
        "engine": "google",
        "api_key": api_key,
        "num": num_results
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()

        # Check for error in response
        if "error" in results:
             st.error(f"SerpApi Error: {results['error']}")
             return []

        for result in results.get("organic_results", []):
            results_data.append({
                "Title": result.get("title"),
                "URL": result.get("link"),
                "Description": result.get("snippet")
            })

    except Exception as e:
        st.error(f"Error occurred during search: {e}")

    return results_data

if __name__ == "__main__":
    st.set_page_config(page_title="School Lead Gen - X-Ray Search", page_icon="🏫", layout="wide")

    st.title("🏫 School Lead Generation Tool")
    st.markdown("""
    Use **Google X-Ray Search** to find school leads in Tier 3 Indian cities.
    This tool targets platforms like **LinkedIn**, **Facebook**, and **Instagram** to find Principals and Directors.

    **Note:** This tool requires a valid SerpApi Key.
    """)

    st.sidebar.header("Search Configuration")

    platform = st.sidebar.selectbox("Select Platform", ["LinkedIn", "Facebook", "Instagram"])
    city = st.sidebar.selectbox("Select City", TIER_3_CITIES)
    keywords = st.sidebar.text_input("Keywords", value="admissions")
    num_results = st.sidebar.slider("Number of Results", min_value=5, max_value=20, value=10, step=1)

    if st.sidebar.button("Search Leads"):
        with st.spinner(f"Searching for {platform} profiles in {city}..."):
            # Construct Query
            dork_query = construct_query(platform, city, keywords)
            st.info(f"**Executing Query:** `{dork_query}`")

            # Fetch Results
            results = fetch_results(dork_query, num_results=num_results)

            if results:
                df = pd.DataFrame(results)
                st.success(f"Found {len(df)} results!")
                st.dataframe(df, use_container_width=True)

                # CSV Download
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download Results as CSV",
                    data=csv,
                    file_name="leads_ready4exam.csv",
                    mime="text/csv",
                )
            else:
                st.warning("No results found or search failed.")
