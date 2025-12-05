# 🤖 Virtual Assistant QA Tests

This project simulates QA work for a virtual assistant, focusing on test design and automation using Python, Pytest and a Jenkins CI pipeline.

The goal is to validate that a simple virtual assistant responds correctly to different user intents (greeting, time, help, unknown queries), similar to real-world testing of AI-based assistants and smart devices.

## 🔧 Tech stack

- Python 3
- Pytest for automated tests
- Jenkins (via Jenkinsfile) for CI
- GitHub Codespaces as development environment

## 🧩 What is tested?

- Correct response for known intents:
  - Greeting
  - Time request
  - Help / fallback
- Handling of unknown inputs
- Basic validation of response structure

## ▶️ How to run tests (locally or in Codespaces)

```bash
pip install -r requirements.txt
pytest -v
