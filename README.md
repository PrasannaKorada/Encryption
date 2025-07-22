
##  **Substitution Cipher Tool** – `README.md`
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

```markdown
# 🔐 Substitution Cipher Encryption-Decryption in Python

This is a simple Python-based **substitution cipher** tool that lets users encrypt and decrypt messages using a randomly shuffled character set.

---

## 🧠 How It Works

- Uses a character set that includes:
  - Letters (A–Z, a–z)
  - Digits (0–9)
  - Punctuation
  - Space
- Randomly shuffles that character set to generate a cipher key
- Maps input text using the shuffled key for encryption
- Decryption reverses the mapping using the same key

---

## 📦 Features

- ✅ Encrypts and decrypts based on a randomized key
- ✅ Handles letters, digits, punctuation, and spaces
- ✅ Clean CLI interaction

---

## 🛠️ Tech Stack

- **Python 3**
- `random` and `string` libraries

---

## ▶️ How to Run

```bash
python cipher.py
