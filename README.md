# 🚀 Ollama for Google Colab

<p align="center">

![Platform](https://img.shields.io/badge/Platform-Google%20Colab-F9AB00?style=for-the-badge\&logo=googlecolab)
![Ollama](https://img.shields.io/badge/Ollama-Latest-000000?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge\&logo=python)
![Models](https://img.shields.io/badge/Models-Multiple-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

</p>

<p align="center">
  <b>One-click Ollama setup for Google Colab</b><br>
  Automatically installs Ollama, starts the server, and downloads your preferred LLM.
</p>

---

## ✨ Features

✅ Installs the latest Ollama release automatically

✅ Starts the Ollama service in the background

✅ Downloads and prepares LLMs for immediate use

✅ Supports multiple popular models

✅ Optimized for Google Colab

✅ Perfect for:

* 📊 Dataset Processing
* 🏷️ Data Labeling
* 🤖 AI Agents
* 🔍 RAG Pipelines
* 📄 JSON Extraction
* 🧠 LLM Experimentation

---

# 📦 What This Script Does

The setup script performs the following steps automatically:

```text
1️⃣ Install Python Dependencies
      ↓
2️⃣ Download Latest Ollama Release
      ↓
3️⃣ Install Ollama
      ↓
4️⃣ Start Ollama Server
      ↓
5️⃣ Download Selected Model
      ↓
6️⃣ Ready For Inference
```

---

# 🚀 Quick Start

Run:

```python
%run ollama_setup.py
```

After installation completes, Ollama will be running locally inside your Colab environment.

---

# 🧠 Default Model

The script currently downloads:

```text
zephyr:7b
```

### Why Zephyr?

✅ Excellent instruction following

✅ Very good JSON generation

✅ Fast on Colab

✅ Reliable structured outputs

---

# 🔄 Changing Models

Locate:

```python
"/usr/local/bin/ollama pull zephyr:7b"
```

Replace with:

```python
"/usr/local/bin/ollama pull MODEL_NAME"
```

Example:

```python
"/usr/local/bin/ollama pull mistral:7b"
```

---

# 📚 Available Models

| Model                  | Parameters | Speed | Quality | Recommended For    |
| ---------------------- | ---------- | ----- | ------- | ------------------ |
| 🏆 **zephyr:7b**       | 7B         | ⚡⚡⚡   | ⭐⭐⭐⭐⭐   | JSON, Instructions |
| 🎯 **mistral:7b**      | 7B         | ⚡⚡⚡   | ⭐⭐⭐⭐    | General Purpose    |
| 💬 **neural-chat:7b**  | 7B         | ⚡⚡⚡   | ⭐⭐⭐⭐    | Chat Applications  |
| 🦙 **llama2:7b**       | 7B         | ⚡⚡    | ⭐⭐⭐⭐    | Stable Baseline    |
| 🧩 **orca-mini:7b**    | 7B         | ⚡⚡⚡   | ⭐⭐⭐⭐    | Reasoning          |
| 👑 **dolphin-mixtral** | 8x7B       | ⚡     | ⭐⭐⭐⭐⭐   | Highest Quality    |
| 🚄 **phi:2.7b**        | 2.7B       | ⚡⚡⚡⚡  | ⭐⭐⭐     | Lightweight & Fast |

---

# 🏅 Model Recommendations

## 📄 JSON Extraction

```text
zephyr:7b
```

### Strengths

* Structured outputs
* Instruction following
* Low hallucination rate

---

## 🎯 General Purpose

```text
mistral:7b
```

### Strengths

* Balanced performance
* Fast responses
* Good reasoning

---

## 🚄 Speed Priority

```text
phi:2.7b
```

### Strengths

* Very lightweight
* Low memory usage
* Fast inference

---

## 👑 Maximum Quality

```text
dolphin-mixtral
```

### Strengths

* Superior reasoning
* Better context understanding
* High-quality outputs

---

# 💻 Example Usage

```python
import ollama

response = ollama.chat(
    model="zephyr:7b",
    messages=[
        {
            "role": "user",
            "content": "Return a JSON object containing name and age."
        }
    ]
)

print(response["message"]["content"])
```

---

# 📊 Resource Guide

| Model Size     | Recommended Runtime     |
| -------------- | ----------------------- |
| 2B - 3B        | ✅ Colab Free            |
| 7B             | ✅ Colab Free / Pro      |
| 13B+           | ⚠️ Colab Pro            |
| Mixtral Models | ⚠️ High RAM Recommended |

---

# ⚠️ Notes

* First-time downloads may take several minutes.
* Larger models consume more RAM.
* Colab sessions are temporary.
* Re-running the notebook may require downloading models again.
* If a model pull fails, simply execute the script again.

---

# 🛠️ Troubleshooting

### Ollama Not Starting

```bash
ollama serve
```

### Verify Installation

```bash
ollama --version
```

### List Installed Models

```bash
ollama list
```

### Check Running Models

```bash
ollama ps
```

---

# 📜 License

MIT License

---

<p align="center">
  Built for AI Engineers • Data Scientists • Hackathons • RAG Systems • LLM Experiments 🚀
</p>
