# Telco Customer Churn Story

An interactive Streamlit + Plotly dashboard that turns the public IBM Telco Customer Churn sample into a guided retention narrative.

## Run it

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

The app downloads the CSV from IBM's public GitHub repository on first run, caches it, and prepares numeric charges plus tenure bands automatically.

## Narrative flow

1. Establish churn exposure with headline metrics.
2. Locate risk across tenure and contract commitment.
3. Test payment-method friction and service adoption.
4. Translate the selected segment into practical retention actions.

Every chart responds to the sidebar filters; the data table can be exported as a CSV.
