# 🔐 Substitution Cipher Encryption-Decryption in Python

This is a simple **text encryption and decryption tool** built in Python using a basic **substitution cipher**.  
The program randomly shuffles characters to create a cipher key and then maps each character of the plain text to a new encrypted form.

---

## 🧠 How It Works

- The script defines a character set that includes:
  - All punctuation
  - Digits (0–9)
  - Letters (A–Z, a–z)
  - Space (`" "`)
- It then creates a shuffled copy of this list to use as the **cipher key**
- The program:
  - Takes **plain text** input from the user
  - Encrypts it using the key
  - Then asks for **cipher text** input and decrypts it back using the same key

---

## 📦 Features

- ✅ Randomly generated substitution keys
- ✅ Bidirectional conversion (encrypt/decrypt)
- ✅ Supports symbols, digits, punctuation, and letters
- ✅ Clean CLI interaction

---

## 🛠️ Tech Stack

- Language: **Python 3**
- Libraries used:
  - `random`
  - `string`

---

## ▶️ How to Run

1. Make sure Python 3 is installed on your system
2. Download or clone this repository:
   ```bash
   git clone https://github.com/yourusername/python-substitution-cipher-tool.git
