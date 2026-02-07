# Demo Result Interpretation

This document explains expected behaviors observed during the demo runs
and helps interpret results correctly.

---

## Why some datasets show zero anomalies

During the demo, certain datasets (e.g. industrial telemetry or engine
sensor data) may produce:

**0 anomalies detected**

This is an expected and correct outcome.

These datasets are:
- Statistically stable
- Operating within normal physical ranges
- Free of extreme outliers
- Consistent over time

The engine is designed to avoid false positives.
Detecting no anomalies indicates healthy and reliable data.

---

## Why other datasets show anomalies

Heterogeneous datasets (e.g. real estate or mixed business data) typically
contain:
- Extreme values
- Skewed distributions
- Rare combinations
- Natural outliers

In these cases, the engine correctly flags anomalies and provides
column-level explanations and profiles.

---

## Detection philosophy

The demo uses a **production-safe configuration**:

- Robust statistics (MAD-based)
- Conservative thresholds
- Deterministic behavior
- Fully explainable results

This is intentional and suitable for industrial environments.

---

## Sensitivity and adaptability

The engine can be tuned conceptually for different goals:

- Conservative mode (production)
- Exploratory mode (analysis)
- Strict mode (audit)

The demo demonstrates the conservative, production-oriented behavior.

---

## What this demonstrates

The demo shows that the engine:
- Distinguishes normal from abnormal data
- Does not generate noise
- Produces trustworthy results
- Is suitable as a data quality and anomaly gate

Zero anomalies is a valid and often desirable result.

---

## Summary

Different datasets lead to different outcomes by design.
This behavior demonstrates robustness and readiness for real-world use.
