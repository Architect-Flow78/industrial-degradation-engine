import streamlit as st
import tempfile
import json
import pandas as pd
import os

from engine import Engine

st.set_page_config(
    page_title="Industrial Data Quality Engine",
    layout="wide"
)

st.title("Industrial Data Quality & Anomaly Detection")

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

if uploaded_file and run:
    with st.spinner("Processing..."):
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

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total rows", report["rows_total"])
    c2.metric("Clean rows", report["rows_clean"])
    c3.metric("Anomalies", report["rows_anomalies"])
    c4.metric("Rows/sec", report["rows_per_sec"])

    st.subheader("Sample anomalies")
    if report["sample_anomalies"]:
        st.dataframe(pd.DataFrame(report["sample_anomalies"]))
    else:
        st.write("No anomalies")

    st.subheader("Data profile")
    profile_df = (
        pd.DataFrame(report["profile"])
        .T
        .reset_index()
        .rename(columns={"index": "column"})
    )
    st.dataframe(profile_df)

    st.subheader("Numeric statistics")
    numeric_cols = [
        c for c in profile_df.columns
        if c in ["min", "max", "mean", "std"]
    ]
    if numeric_cols:
        st.dataframe(profile_df[["column"] + numeric_cols])

    st.subheader("Download summary")
    st.download_button(
        "Download summary JSON",
        json.dumps(report, indent=2),
        file_name="summary.json",
        mime="application/json"
    )
