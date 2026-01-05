# Medical-LLM Benchmarking Suite (MLBS) 🩺

**The Open-Source Framework for Clinical Safety & Anthropic Claude Alignment.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🔬 Overview
General-purpose benchmarks fail to evaluate **clinical risk**. **MLBS** provides a production-grade testing harness specifically designed for **Anthropic Claude**, implementing a modular architecture for:
- **Clinical Alignment Scoring (CAS):** Identifying medical hallucinations in high-stakes scenarios.
- **Safety Violation Detection:** Automated flagging of "contraindication" mismatches.
- **Reproducible Evaluation:** Zero-temperature settings for scientific consistency.

This framework is based on the methodology established in:
> *Banerjee, S. (2025). Transforming Healthcare with State-of-The-Art Medical-LLMs.*

## 🚀 Why MLBS?
Unlike black-box evaluators, **MLBS** is designed for **Sovereign AI** contexts where transparency and regulatory compliance (NIST AI RMF) are paramount. 

## 🛠️ Getting Started
```bash
# Set your API Key
export ANTHROPIC_API_KEY='your-key-here'

# Run the benchmark
python main.py
