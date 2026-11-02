"""Interactive narrative dashboard for the IBM Telco Customer Churn dataset."""

from __future__ import annotations

from io import BytesIO

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


st.set_page_config(page_title="Telco Churn Story", page_icon="📡", layout="wide")

DATA_URL = (
    "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/"
    "master/data/Telco-Customer-Churn.csv"
)
CHURN_COLORS = {"No": "#4C78A8", "Yes": "#E45756"}


@st.cache_data(show_spinner="Collecting the public IBM Telco dataset…")
def load_data() -> pd.DataFrame:
    """Download and prepare the public IBM sample, cached by Streamlit."""
    try:
        raw = pd.read_csv(DATA_URL)
    except Exception as exc:
        raise RuntimeError(
            "The public dataset could not be reached. Check your internet connection "
            "and refresh the app."
        ) from exc

    raw["TotalCharges"] = pd.to_numeric(raw["TotalCharges"], errors="coerce")
    raw["TotalCharges"] = raw["TotalCharges"].fillna(0)
    raw["MonthlyCharges"] = pd.to_numeric(raw["MonthlyCharges"], errors="coerce")
    raw["tenure_band"] = pd.cut(
        raw["tenure"],
        bins=[-1, 6, 12, 24, 48, 72],
        labels=["0–6 mo", "7–12 mo", "13–24 mo", "25–48 mo", "49–72 mo"],
    )
    return raw


def rate_table(frame: pd.DataFrame, group: str, sort: bool = True) -> pd.DataFrame:
    result = (
        frame.groupby(group, observed=True)["Churn"]
        .agg(customers="size", churn_rate=lambda s: (s == "Yes").mean())
        .reset_index()
    )
    return result.sort_values("churn_rate", ascending=False) if sort else result


def percent(value: float) -> str:
    return f"{value:.1%}"


df = load_data()

st.title("📡 The customer churn story")
st.caption(
    "An interactive exploration of the public IBM Telco Customer Churn dataset. "
    "Use the filters to test whether the story holds for each customer segment."
)

with st.sidebar:
    st.header("Focus the story")
    contract = st.multiselect("Contract", sorted(df["Contract"].unique()), default=sorted(df["Contract"].unique()))
    internet = st.multiselect("Internet service", sorted(df["InternetService"].unique()), default=sorted(df["InternetService"].unique()))
    payment = st.multiselect("Payment method", sorted(df["PaymentMethod"].unique()), default=sorted(df["PaymentMethod"].unique()))
    tenure_range = st.slider("Tenure (months)", 0, int(df.tenure.max()), (0, int(df.tenure.max())))
    st.divider()
    st.caption("Data source: IBM sample dataset, downloaded when the app first runs.")

filtered = df[
    df["Contract"].isin(contract)
    & df["InternetService"].isin(internet)
    & df["PaymentMethod"].isin(payment)
    & df["tenure"].between(*tenure_range)
].copy()

if filtered.empty:
    st.warning("No customers match those filters. Widen a selection to continue.")
    st.stop()

churned = filtered[filtered.Churn.eq("Yes")]
churn_rate = churned.shape[0] / filtered.shape[0]

st.subheader("1. Start with the size of the problem")
k1, k2, k3, k4 = st.columns(4)
k1.metric("Customers in view", f"{len(filtered):,}")
k2.metric("Churn rate", percent(churn_rate))
k3.metric("Customers lost", f"{len(churned):,}")
k4.metric("Avg. monthly charge", f"${filtered.MonthlyCharges.mean():.2f}")

st.markdown(
    f"**{percent(churn_rate)}** of the selected customer base has churned. "
    "The next views identify which parts of the customer journey concentrate that risk."
)

left, right = st.columns((1.25, 1))
with left:
    st.subheader("2. Risk is front-loaded in the relationship")
    tenure = rate_table(filtered, "tenure_band", sort=False).dropna()
    fig = px.line(
        tenure, x="tenure_band", y="churn_rate", markers=True,
        labels={"tenure_band": "Customer tenure", "churn_rate": "Churn rate"},
        color_discrete_sequence=[CHURN_COLORS["Yes"]],
    )
    fig.update_yaxes(tickformat=".0%", rangemode="tozero")
    fig.update_layout(height=340, margin=dict(l=10, r=10, t=25, b=10), showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.subheader("Contract is the clearest retention lever")
    contracts = rate_table(filtered, "Contract")
    fig = px.bar(
        contracts, x="churn_rate", y="Contract", orientation="h", text="customers",
        labels={"churn_rate": "Churn rate", "Contract": "Contract"},
        color="churn_rate", color_continuous_scale=["#9ecae1", "#e45756"],
    )
    fig.update_xaxes(tickformat=".0%", rangemode="tozero")
    fig.update_layout(height=340, margin=dict(l=10, r=10, t=25, b=10), coloraxis_showscale=False)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("Monthly customers deserve special attention: in the full dataset their churn rate is substantially above longer-term contracts.")

left, right = st.columns(2)
with left:
    st.subheader("3. Payment friction shows up in the data")
    payments = rate_table(filtered, "PaymentMethod")
    fig = px.bar(
        payments, x="PaymentMethod", y="churn_rate", color="PaymentMethod", text="customers",
        labels={"churn_rate": "Churn rate", "PaymentMethod": "Payment method"},
    )
    fig.update_yaxes(tickformat=".0%", rangemode="tozero")
    fig.update_layout(height=360, margin=dict(l=10, r=10, t=25, b=80), showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.subheader("4. Services reveal who needs intervention")
    service_cols = ["OnlineSecurity", "TechSupport", "DeviceProtection", "StreamingTV"]
    service_rows = []
    for service in service_cols:
        for response, group in filtered.groupby(service, observed=True):
            service_rows.append({"Service": service, "Response": response, "Churn rate": (group.Churn == "Yes").mean(), "Customers": len(group)})
    services = pd.DataFrame(service_rows)
    fig = px.bar(
        services, x="Service", y="Churn rate", color="Response", barmode="group",
        hover_data={"Customers": True, "Churn rate": ":.1%"},
        color_discrete_map={"Yes": "#4C78A8", "No": "#E45756", "No internet service": "#A0AEC0"},
    )
    fig.update_yaxes(tickformat=".0%", rangemode="tozero")
    fig.update_layout(height=360, margin=dict(l=10, r=10, t=25, b=50), legend_title_text="Service status")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("5. Turn the evidence into a retention playbook")
insights = rate_table(filtered, "Contract").iloc[0]
pay_risk = rate_table(filtered, "PaymentMethod").iloc[0]
support = rate_table(filtered[filtered.TechSupport.isin(["Yes", "No"])], "TechSupport").iloc[0]

col1, col2, col3 = st.columns(3)
col1.info(f"**Stabilize early tenure**\n\nPrioritize onboarding in the first 6–12 months, when churn is most concentrated.")
col2.warning(f"**Convert {insights['Contract']} plans**\n\nThis contract type currently has the highest risk in the selected view ({percent(insights['churn_rate'])}).")
col3.success(f"**Reduce payment or support friction**\n\nWatch {pay_risk['PaymentMethod']} customers ({percent(pay_risk['churn_rate'])} churn); test service outreach where support is absent.")

with st.expander("See the filtered customer data"):
    st.dataframe(filtered, use_container_width=True, hide_index=True)
    st.download_button(
        "Download filtered data as CSV",
        filtered.to_csv(index=False).encode("utf-8"),
        file_name="telco_churn_filtered.csv",
        mime="text/csv",
    )
