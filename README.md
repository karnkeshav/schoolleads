# School Lead Generation Tool

This is a Streamlit application that uses Google X-Ray Search ("Dorks") to find school leads (Principals, Directors) in Tier 3 Indian cities from platforms like LinkedIn, Facebook, and Instagram.

## Prerequisites

- Python 3.7+
- Internet connection (access to Google)

## Installation

1.  Clone the repository or download the files.
2.  Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

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
    *   **Number of Results**: Choose how many results to fetch (be careful with high numbers to avoid Google blocks).
4.  Click **Search Leads**.
5.  View the results in the table and download them as a CSV file using the **Download Results as CSV** button.

## Notes

*   **Rate Limiting**: Google may block your IP if you make too many requests in a short period (HTTP 429). If this happens, wait a few minutes or switch your internet connection/IP.
*   **Results**: The quality of results depends on the data indexed by Google.
