# 🔐 Password Security Analyzer

> A cybersecurity-focused password analysis tool built with **Python and Streamlit** that evaluates password strength, detects common security weaknesses, estimates entropy, and generates secure passwords.

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#-license)

---

## 🌐 Overview

**Password Security Analyzer** is an educational cybersecurity application designed to demonstrate how password security can be evaluated programmatically.

The application analyzes a password against multiple security criteria instead of relying only on its length. It identifies weak patterns, checks character diversity, estimates password entropy, provides security recommendations, and can generate strong random passwords.

The project was developed using **Python** and **Streamlit** with a focus on defensive cybersecurity and privacy-conscious password analysis.

---

## ✨ Features

### 🔎 Password Strength Analysis

The application evaluates:

* 📏 Password length
* 🔤 Lowercase characters
* 🔠 Uppercase characters
* 🔢 Numbers
* 🔣 Special characters
* 🔁 Repeated characters
* 🔢 Sequential numbers
* 🔤 Sequential letters
* 📖 Common weak passwords

### 📊 Security Score

Passwords receive a score between **0 and 100**.

|  Score | Classification |
| -----: | -------------- |
|   0–29 | 🔴 Very Weak   |
|  30–49 | 🟠 Weak        |
|  50–69 | 🟡 Moderate    |
|  70–84 | 🟢 Strong      |
| 85–100 | 🔵 Very Strong |

---

### 🎲 Entropy Estimation

The application estimates password entropy based on:

* Password length
* Lowercase characters
* Uppercase characters
* Numbers
* Special characters

Entropy is expressed in **bits** and provides an approximate indication of password unpredictability.

> **Note:** Entropy is an estimate and should not be interpreted as an exact real-world password-cracking time.

---

### ⚠️ Weak Pattern Detection

The analyzer detects several predictable patterns, including:

```text
123456
abc123
aaa
password123
qwerty
```

These patterns can reduce the effective security of an otherwise long password.

---

### 💡 Security Recommendations

The application provides personalized recommendations such as:

* Increase password length
* Add uppercase characters
* Add lowercase characters
* Include numbers
* Include special characters
* Avoid repeated characters
* Avoid predictable sequences
* Avoid commonly used passwords

---

### 🎯 Secure Password Generator

The application includes a password generator that uses Python's:

```python
secrets
```

module instead of the standard `random` module.

The generator creates passwords containing a combination of:

* Uppercase letters
* Lowercase letters
* Numbers
* Special characters

Users can select a password length between **12 and 32 characters**.

---

## 🖥️ Application Interface

The Streamlit application provides:

```text
🔐 Password Security Analyzer
│
├── 🔎 Password Analysis
│
├── 📊 Security Score
│
├── 🔎 Character Analysis
│
├── 🎲 Entropy Estimation
│
├── 🛡️ Security Resistance
│
├── ⚠️ Security Warnings
│
├── 💡 Security Suggestions
│
├── 🎲 Password Generator
│
└── 🛡️ Security Tips
```

---

## 🛠️ Technologies Used

| Technology              | Purpose                    |
| ----------------------- | -------------------------- |
| **Python**              | Core application logic     |
| **Streamlit**           | Web application interface  |
| **Regular Expressions** | Pattern detection          |
| **Math**                | Entropy calculations       |
| **Secrets**             | Secure password generation |
| **Git**                 | Version control            |
| **GitHub**              | Source-code hosting        |

---

## 📂 Project Structure

```text
Password-Security-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
    └── app.png
```

---

## ⚙️ Installation

### Prerequisites

Make sure you have:

* Python 3.x
* pip
* Git

### 1. Clone the repository

```bash
git clone https://github.com/vishnupriya-pai/Password-Security-Analyzer.git
```

### 2. Enter the project directory

```bash
cd Password-Security-Analyzer
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will be available locally at:

```text
http://localhost:8501
```

---

## 📦 Requirements

The project currently requires:

```text
streamlit
```

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🔐 Privacy & Security

This project is designed with privacy in mind.

### Password handling

* Passwords are analyzed locally by the application.
* Passwords are not intentionally stored in a database.
* The project does not require sending passwords to an external API.
* Generated passwords are created locally.
* The password generator uses Python's `secrets` module.

### Important

This project is an **educational password analyzer**, not a replacement for a professional password manager or authentication system.

For production applications, passwords should be handled using established authentication practices and secure password-hashing algorithms.

---

## 🧠 Cybersecurity Concepts Demonstrated

This project demonstrates practical concepts including:

* 🔐 Password security
* 🛡️ Defensive cybersecurity
* 📊 Password entropy
* 🔎 Pattern recognition
* 🚫 Common-password detection
* 🎲 Cryptographically secure random generation
* 🔒 Privacy-aware application design
* 🐍 Python security programming
* 🌐 Web-based security tooling

---

## 🎯 Learning Objectives

Through this project, the following concepts can be explored:

1. How password characteristics affect security
2. Why password length matters
3. How character diversity affects entropy
4. Why predictable patterns weaken passwords
5. Difference between `random` and `secrets`
6. Building cybersecurity tools with Python
7. Creating interactive security dashboards with Streamlit
8. Deploying Python applications to the web

---

## 🚀 Deployment

This application can be deployed using **Streamlit Community Cloud**.

Basic deployment flow:

```text
Local Project
     │
     ▼
   Git
     │
     ▼
  GitHub
     │
     ▼
Streamlit Community Cloud
     │
     ▼
 Public Web App
```

### Deployment requirements

Make sure your GitHub repository contains:

```text
passoward_strengthchecker.py
requirements.txt
README.md
```

Then connect the repository to Streamlit Community Cloud and select:

```text
Main file: app.py
Branch: main
```

---

## 🔮 Future Improvements

Possible future versions could include:

* [ ] Larger common-password database
* [ ] Dictionary-word detection
* [ ] Better passphrase analysis
* [ ] Advanced pattern detection
* [ ] Improved entropy estimation
* [ ] Password reuse warnings
* [ ] More detailed security reports
* [ ] Downloadable analysis reports
* [ ] Improved UI/UX
* [ ] Accessibility improvements
* [ ] Unit tests
* [ ] Automated CI/CD
* [ ] Docker support

---

## ⚠️ Disclaimer

This project is created for **educational and defensive cybersecurity purposes**.

Password strength and entropy calculations are estimates. They do not guarantee that a password is secure against every possible attack.

Never use passwords from demonstrations or screenshots for real accounts.

---

## 👨‍💻 Author

**Vishnupriya Pai**

Cybersecurity & Python Project

GitHub:
https://github.com/vishnupriya-pai

---

## ⭐ Support

If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is available under the **MIT License**.

See the `LICENSE` file for details.
