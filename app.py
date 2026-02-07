import streamlit as st
import tempfile
import json
import pandas as pd
import os

# импорт твоего движка
from engine import Engine

st.set_page_config(
    page_title="Industrial Data Quality Engine",
    layout="wide"
)

st.title("Industrial Data Quality & Anomaly Detection")
st.caption("Streaming • Rules • Statistics • Production-ready")

# ===============================
# Upload
# ===============================
uploaded_file = st.file_uploader(
    "Upload data file",
    type=["csv", "txt", "gz", "json", "jsonl"]
)

schema_file = st.file_uploader(
    "Optional schema (JSON)",
    type=["json"]
)

rules_file = st.file_uploader(
    "Optional rules (JSON)",
    type=["json"]
)

run = st.button("Run engine")

# ===============================
# Run engine
# ===============================
if uploaded_file and run:
    with st.spinner("Processing data..."):

        # save input
        tmp_data = tempfile.NamedTemporaryFile(delete=False)
        tmp_data.write(uploaded_file.read())
        tmp_data.close()

        tmp_schema = None
        tmp_rules = None

        if schema_file:
            tmp_schema = tempfile.NamedTemporaryFile(delete=False)
            tmp_schema.write(schema_file.read())
            tmp_schema.close()

        if rules_file:
            tmp_rules = tempfile.NamedTemporaryFile(delete=False)
            tmp_rules.write(rules_file.read())
            tmp_rules.close()

        engine = Engine(
            schema=tmp_schema.name if tmp_schema else None,
            rules=tmp_rules.name if tmp_rules else None
        )

        report = engine.run(tmp_data.name)

    st.success("Analysis completed")

    # ===============================
    # Metrics
    # ===============================
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total rows", report["rows_total"])
    c2.metric("Clean rows", report["rows_clean"])
    c3.metric("Anomalies", report["rows_anomalies"])
    c4.metric("Rows / sec", report["rows_per_sec"])

    # ===============================
    # Sample anomalies
    # ===============================
    st.subheader("Sample anomalies")

    if report["sample_anomalies"]:
        st.dataframe(pd.DataFrame(report["sample_anomalies"]))
    else:
        st.info("No anomalies detected")

    # ===============================
    # Profile
    # ===============================
    st.subheader("Data profile")

    profile_df = (
        pd.DataFrame(report["profile"])
        .T
        .reset_index()
        .rename(columns={"index": "column"})
    )

    st.dataframe(profile_df)

    # ===============================
    # Charts
    # ===============================
    st.subheader("Numeric distributions")

    numeric_cols = [
        c for c in profile_df["column"]
        if "mean" in profile_df.columns
    ]

    for col in numeric_cols[:5]:
        if col in profile_df["column"].values:
            st.bar_chart(
                profile_df.set_index("column")[["mean", "std"]],
                height=200
            )

    # ===============================
    # Download summary
    # ===============================
    st.subheader("Download report")

    st.download_button(
        "Download summary JSON",
        json.dumps(report, indent=2),
        file_name="summary.json",
        mime="application/json"
    )

else:
    st.info("Upload a file and press **Run engine**")
