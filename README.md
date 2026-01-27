# School Lead Generation Tool

This is a Streamlit application that uses Google X-Ray Search ("Dorks") to find school leads (Principals, Directors) in Tier 3 Indian cities from platforms like LinkedIn, Facebook, and Instagram.

It uses **SerpApi** to perform Google searches reliably.

## Prerequisites

- Python 3.7+
- Internet connection
- A **SerpApi** API Key (Get one at [serpapi.com](https://serpapi.com/))

## Installation

1.  Clone the repository or download the files.
2.  Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

You must configure your SerpApi Key for the application to work.

1.  Create a file named `secrets.toml` inside a `.streamlit` folder in the project root:

    ```
    .streamlit/secrets.toml
    ```

2.  Add your API key to the file:

    ```toml
    SERPAPI_KEY = "your_actual_serpapi_key_here"
    ```

    *Note: Do not commit `secrets.toml` to version control.*

## Usage

1.  Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2.  Open your browser and navigate to the URL shown in the terminal (usually `http://localhost:8501`).
3.  Use the sidebar to configure your search:
    *   **Platform**: Select LinkedIn, Facebook, or Instagram.
    *   **City**: Select a Tier 3 city from the list.
    *   **Keywords**: Enter additional keywords (default: "admissions").
    *   **Number of Results**: Choose how many results to fetch.
4.  Click **Search Leads**.
5.  View the results in the table and download them as a CSV file using the **Download Results as CSV** button.

## Notes

*   **Quota**: Usage depends on your SerpApi plan quota.
*   **Results**: The tool fetches organic results from Google based on the constructed Dork query.
