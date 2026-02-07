import streamlit as st
import pandas as pd
import numpy as np
import gzip
import tempfile

# ------------------------------------------------------------
# Streamlit configuration
# ------------------------------------------------------------

st.set_page_config(
    page_title="Industrial Degradation Analysis",
    layout="wide"
)

st.title("Industrial Degradation Analysis Dashboard")

# ------------------------------------------------------------
# Utilities
# ------------------------------------------------------------

def open_file(path):
    if path.endswith(".gz"):
        return gzip.open(path, "rt", encoding="utf-8", errors="replace")
    return open(path, "r", encoding="utf-8", errors="replace")

# ------------------------------------------------------------
# Degradation detector
# ------------------------------------------------------------

class DegradationDetector:
    def __init__(self, late_frac=0.3, mean_sigma=1.5):
        self.late_frac = late_frac
        self.mean_sigma = mean_sigma

    def detect(self, df):
        mask = pd.Series(False, index=df.index)

        sensor_cols = [c for c in df.columns if c.startswith("sensor_")]

        for engine_id, group in df.groupby("engine_id"):
            group = group.sort_values("cycle")
            n = len(group)

            if n < 50:
                continue

            split_idx = int(n * (1 - self.late_frac))
            baseline = group.iloc[:split_idx]
            late_stage = group.iloc[split_idx:]

            degraded = False

            for col in sensor_cols:
                b = baseline[col].dropna()
                l = late_stage[col].dropna()

                if len(b) < 10 or len(l) < 10:
                    continue

                if b.std() > 0 and abs(l.mean() - b.mean()) > self.mean_sigma * b.std():
                    degraded = True
                    break

            if degraded:
                mask.loc[late_stage.index] = True

        return mask

# ------------------------------------------------------------
# Engine
# ------------------------------------------------------------

def run_engine(path):
    columns = (
        ["engine_id", "cycle"]
        + [f"op_{i}" for i in range(1, 4)]
        + [f"sensor_{i}" for i in range(1, 22)]
    )

    df = pd.read_csv(open_file(path), sep=r"\s+", names=columns)
    df = df.apply(pd.to_numeric, errors="coerce")

    detector = DegradationDetector()
    df["is_degraded"] = detector.detect(df)

    return df

# ------------------------------------------------------------
# Streamlit UI
# ------------------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload dataset",
    type=["txt", "gz"]
)

if uploaded_file and st.button("Run analysis"):

    with st.spinner("Processing data"):
        tmp = tempfile.NamedTemporaryFile(delete=False)
        tmp.write(uploaded_file.read())
        tmp.close()

        df = run_engine(tmp.name)

    st.success("Analysis completed")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total rows", len(df))
    col2.metric("Clean rows", int((~df["is_degraded"]).sum()))
    col3.metric("Degraded rows", int(df["is_degraded"].sum()))

    st.subheader("Download results")

    st.download_button(
        "Download clean rows (CSV)",
        df[~df["is_degraded"]].to_csv(index=False),
        "clean_rows.csv"
    )

    st.download_button(
        "Download degraded rows (CSV)",
        df[df["is_degraded"]].to_csv(index=False),
        "degraded_rows.csv"
    )

    st.subheader("Degradation visualization")

    engine_id = st.selectbox(
        "Engine ID",
        sorted(df["engine_id"].unique())
    )

    sensor = st.selectbox(
        "Sensor",
        [c for c in df.columns if c.startswith("sensor_")]
    )

    view = df[df["engine_id"] == engine_id][["cycle", sensor, "is_degraded"]]

    st.line_chart(
        view.set_index("cycle")[sensor],
        height=250
    )

    st.scatter_chart(
        view[view["is_degraded"]].set_index("cycle")[sensor],
        height=250
    )

else:
    st.info("Upload a dataset and run the analysis")
