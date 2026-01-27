# School Lead Generation Tool

This is a Flask application that uses Google X-Ray Search ("Dorks") to find school leads (Principals, Directors) in Tier 3 Indian cities from platforms like LinkedIn, Facebook, and Instagram.

It is designed to be deployed on **Vercel**.

## Prerequisites

- Python 3.9+
- A **SerpApi** API Key (Get one at [serpapi.com](https://serpapi.com/))

## Installation

1.  Clone the repository.
2.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3.  Set up your environment variable:

    ```bash
    export SERPAPI_KEY="your_api_key"
    ```

## Usage (Local)

1.  Run the Flask app:

    ```bash
    flask run
    ```

2.  Open `http://localhost:5000` in your browser.

## Deployment (Vercel)

1.  Install Vercel CLI: `npm i -g vercel`
2.  Run `vercel` in the project root.
3.  Add your `SERPAPI_KEY` in the Vercel Project Settings > Environment Variables.

## Notes

*   **Quota**: Usage depends on your SerpApi plan quota.
*   **Results**: The tool fetches organic results from Google based on the constructed Dork query.
