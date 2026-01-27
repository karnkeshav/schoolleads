import streamlit as st
from googlesearch import search
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
    Fetches results using googlesearch-python.
    Returns a list of dictionaries.
    """
    results_data = []
    try:
        # sleep_interval might be supported, but we will also add manual sleep if needed.
        # We try to use advanced=True to get Title and Description.
        # Note: num_results in some versions is 'stop'.

        # We use a generator to fetch results
        # To be safe with potential API variations, we'll try-except the advanced param?
        # No, let's assume standard googlesearch-python.

        # "Pro-Tips": Increase Delay to 5 seconds to avoid blocks.
        search_gen = search(query, num_results=num_results, advanced=True, sleep_interval=5)

        for result in search_gen:
            results_data.append({
                "Title": result.title,
                "URL": result.url,
                "Description": result.description
            })
            # Adding a small delay to be safe, though sleep_interval should handle it.
            time.sleep(random.uniform(1.0, 2.0))

    except Exception as e:
        # Check if it's a 429 or related to rate limiting
        error_msg = str(e)
        if "429" in error_msg or "Too Many Requests" in error_msg:
            st.error("⚠️ HTTP 429 Error: Too many requests. Google has rate-limited the search. Please wait a few minutes before trying again.")
        else:
            st.error(f"An error occurred: {error_msg}")

    return results_data

if __name__ == "__main__":
    st.set_page_config(page_title="School Lead Gen - X-Ray Search", page_icon="🏫", layout="wide")

    st.title("🏫 School Lead Generation Tool")
    st.markdown("""
    Use **Google X-Ray Search** to find school leads in Tier 3 Indian cities.
    This tool targets platforms like **LinkedIn**, **Facebook**, and **Instagram** to find Principals and Directors.
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
                st.warning("No results found. Try adjusting keywords or check if Google is blocking requests.")
