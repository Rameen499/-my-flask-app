# 🔐 Post-Quantum Cryptography Demo App

A simple web app built with **Flask** and **PyCryptodome** that demonstrates encryption and decryption using AES (Advanced Encryption Standard), simulating the behavior of post-quantum cryptographic systems.

---

## 👥 Group Members

- Rameen  
- Isma
- 



## 💡 Project Description

This project is a basic demo that focuses on secure encryption and decryption using **AES *. While AES is not a post-quantum asymmetric algorithm, it remains **resistant to quantum attacks** when implemented with 256-bit keys. The aim was to simulate how encryption workflows may look under PQC settings, and pave the way for integrating more advanced algorithms like Kyber in the future.

The application was built in a virtual environment and is fully contained, requiring only Flask and PyCryptodome to run.

---

## 🔐 PQC Algorithm Used

We used **AES (Advanced Encryption Standard)** with:
- 128-bit key (for demo simplicity)
- CBC (Cipher Block Chaining) mode
- Randomly generated IV (Initialization Vector)

> In real-world PQC systems, AES-256 is often used alongside lattice-based key exchange mechanisms like Kyber.

---

## ⚙️ How It Works

### 🔑 1. Key Generation
- AES key and IV are generated using secure random functions.
- Keys are stored in memory and used for a single encryption session.

### 🔒 2. Encryption
- Plaintext input is taken via a web form.
- Message is padded and encrypted using AES CBC mode.
- Encrypted output is displayed in base64 for easy readability.

### 🔓 3. Decryption
- User provides the ciphertext and key.
- App decrypts the message using AES and removes padding.
- Original message is shown on screen.

--

##  How to Run

```bash
# Create virtualenv
python -m venv flaskenv
source flaskenv/bin/activate

# Install dependencies
pip install flask pycryptodome

# Run the app
python app.py
