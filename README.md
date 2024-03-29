# RLHF & DPO Preference Data Quality Toolkit

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A specialized toolkit for **Reinforcement Learning from Human Feedback (RLHF)** and **Direct Preference Optimization (DPO)** data quality assurance. Computes inter-annotator agreement metrics (Fleiss' & Cohen's Kappa), detects length bias heuristics, flags toxicity/leakage, and formats datasets for HuggingFace TRL.

---

## 🚀 Key Features

- **Inter-Annotator Agreement**: Calculate Cohen's Kappa and Fleiss' Kappa for multi-annotator preference ranking tasks.
- **Length Bias Auditor**: Flags superficial length preference artifacts (where models reward longer outputs regardless of quality).
- **Arabic Script Quality Assurance**: Checks dialect consistency, Tashkeel validity, and linguistic fluency.
- **DPO Dataset Export**: Validates and serializes paired data directly to JSONL / Parquet format compatible with HuggingFace TRL `DPOTrainer`.

---

## 📊 Minimum Quality Threshold Findings

Our empirical studies indicate downstream alignment gains plateau when:
- **Inter-annotator Kappa $\ge 0.78$**
- **Length Ratio Bias $0.85 \le \frac{\text{len}(y_w)}{\text{len}(y_l)} \le 1.25$**

---

## ⚡ Quick Start

```bash
git clone https://github.com/yousefkhaled2005/rlhf-annotation-tools.git
cd rlhf-annotation-tools
pip install -r requirements.txt

# Run QA audit on sample dataset
python -m src.audit --input data/sample_preferences.jsonl
```

---

## 📜 License

MIT License (c) 2024 Yousef Khaled
