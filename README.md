# Industrial Degradation Engine

A production-oriented data quality and anomaly detection engine designed to
demonstrate analytical rigor, systems thinking, and a structured engineering
approach to complex datasets.

This project was developed as a focused proof of concept in an industrial and
business process context.

---

## Overview

The engine processes structured datasets in a streaming manner, validates data
quality, detects statistical and rule-based anomalies, and produces explainable,
actionable outputs.

It is intentionally conservative and deterministic, prioritizing trust and
robustness over noisy or exaggerated results.

---

## Core Capabilities

- Streaming ingestion of large datasets
- Rule-based data validation
- Robust statistical anomaly detection (MAD / z-score)
- Explainable anomaly reasons
- Column-level data profiling
- Approximate distinct cardinality estimation
- Performance and throughput metrics
- CLI and interactive Streamlit interface

---

## Project Context and Relevance

This project demonstrates an approach aligned with roles involving:

- Process analysis and optimization
- Data-driven decision support
- Digital systems and analytics
- Cross-functional collaboration between business and technical teams
- Reliability and explainability in operational environments

Rather than forcing anomaly detection, the engine correctly identifies when
datasets are statistically stable.  
**Zero detected anomalies is a valid and correct outcome** for healthy data.

---

## Intended Usage Scenarios

The engine can be applied to:

- Industrial and operational datasets
- Procurement or supply chain data
- Data quality gates before analytics or reporting
- Process monitoring and early deviation detection
- Support for continuous improvement initiatives

The architecture is modular and adaptable to different business domains.

---

## Demo

An interactive demo is available via Streamlit.

Users can upload datasets and immediately inspect results, statistics, and
detected anomalies.

### Supported input formats
- CSV
- TXT
- GZ (compressed text)
- JSON / JSONL

Depending on the dataset characteristics:
- Stable industrial data may produce **no anomalies**
- Heterogeneous or business data may reveal statistical deviations

Both outcomes are expected and indicate correct system behavior.

For a detailed explanation of demo results, see:
`demo/DEMO_INTERPRETATION.md`

---

## Running the Project

### Install dependencies
```bash
pip install -r requirements.txt
