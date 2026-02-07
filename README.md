# Industrial Streaming Degradation Analysis Engine

This repository contains a lightweight industrial data analysis engine designed to detect **early-stage system degradation** in complex engineering and sensor datasets.

The tool focuses on **progressive degradation patterns across system lifecycles**, rather than isolated point anomalies or static threshold violations.

---

## Key Concepts

- Lifecycle-aware analysis (baseline vs late-stage behavior)
- Early degradation detection
- Streaming-friendly and scalable approach
- Interpretable results oriented toward engineering use
- No reliance on external services or cloud processing
- No storage or caching of uploaded data (privacy-by-design)

---

## Typical Use Cases

- System and electronics validation  
- Reliability and degradation analysis  
- Sensor and test data exploration  
- Failure analysis support  
- Engineering data quality checks  

---

## Security & Data Handling

- Data is processed locally in memory
- No external APIs or services are used
- Uploaded files are not stored or cached
- Suitable for sensitive engineering datasets

---

## Live Demo

A live Streamlit demo is available, allowing users to upload their own datasets and immediately explore degradation patterns.

*(Insert Streamlit link here)*

---

## Local Execution

```bash
pip install -r requirements.txt
streamlit run app.py
Philosophy

This project was developed as a practical engineering tool, demonstrating an approach to data analysis that prioritizes:

system behavior over time,

early signal detection,

transparency and interpretability,

and responsible data handling.
Author

Nicolae Pascal
Systems & Data Analysis Engineer
Based in Renazzo, Italy
