# Industrial Data Quality & Anomaly Detection Engine

## Overview

This project is a **production-oriented data quality and anomaly detection engine** designed for high-throughput industrial data pipelines.  
It targets environments where **data reliability, explainability, and operational stability** are critical, such as advanced manufacturing, automotive production, and industrial analytics.

The engine is optimized for **streaming and large-scale batch data**, with a strong focus on transparency and deterministic behavior rather than opaque black-box models.

---

## Core Capabilities

### 1. Streaming Processing at Scale
- Chunk-based ingestion for large files
- Stable memory footprint
- High throughput (rows/sec metric included)
- Suitable for ETL, ingestion, and offline/near-real-time pipelines

---

### 2. Hybrid Anomaly Detection

#### Rule-Based Validation
- Column-level rules (`>`, `<`, `between`, `regex`, `null`, etc.)
- Expression rules (`expr: "a > b * 1.2"`)
- Severity levels (`error`, `warning`)
- Fully explainable rule hits per row

#### Statistical Detection
- Robust Median Absolute Deviation (MAD)
- Automatic fallback to standard deviation when needed
- Resistant to outliers and skewed distributions
- Column-level anomaly attribution

---

### 3. Data Profiling & Health Monitoring
- Null rate tracking
- Approximate distinct cardinality (HyperLogLog-style)
- Top frequent values
- Streaming min / max / mean / standard deviation
- Designed for schema drift and data contract monitoring

---

### 4. Production-Grade Engineering
- Deterministic results
- SHA-256 input hashing for auditability
- Chunk-level timing metrics
- Sample anomaly extraction
- Clean separation of valid vs anomalous data
- JSON summary report for downstream systems

---

### 5. Format & Pipeline Flexibility
- Supports CSV, TXT, GZ, JSONL
- Optional external schema definition
- Optional external rule configuration
- Output formats: CSV, JSONL, Parquet
- Easily embeddable into existing data platforms

---

## Typical Use Cases

- Sensor data quality validation
- Manufacturing data ingestion control
- Early anomaly filtering before ML pipelines
- Feature health monitoring
- Schema drift detection
- ETL validation layer
- Offline analysis and audit reporting

---

## Design Philosophy

- **Explainability first**: every anomaly has a reason
- **Engineering-driven**, not experimental AI
- **Composable foundation** for ML, predictive maintenance, or advanced analytics
- Built for environments where **trust in data is as important as accuracy**

---

## Why This Matters

In advanced manufacturing contexts, unreliable data leads to:
- False alerts
- Missed degradation signals
- Reduced trust in analytics and AI systems

This engine acts as a **data integrity and anomaly control layer**, ensuring that downstream analytics and decision systems operate on validated, explainable, and monitored data.

---

## Technology Stack

- Python
- Pandas / NumPy
- Streamlit (for demonstration and presentation)
- Stateless, dependency-light core engine

---

## Status

- Production-ready core
- Demonstration UI included
- Designed for integration into industrial data platforms

---

## Contact / Demo

The Streamlit application included in this repository provides a live, interactive demonstration of the engine’s capabilities for evaluation and discussion.
