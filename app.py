from flask import Flask, render_template, request
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Store keys and IVs in memory for demo purposes (do NOT do this in production)
key_storage = {"key": None, "iv": None}

def pad(message):
    pad_len = 16 - len(message) % 16
    return message + chr(pad_len) * pad_len

def unpad(message):
    pad_len = ord(message[-1])
    return message[:-pad_len]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_key', methods=['POST'])
def generate_key():
    key = get_random_bytes(16)  # 128-bit AES key
    iv = get_random_bytes(16)   # Initialization Vector
    key_storage['key'] = key
    key_storage['iv'] = iv
    return render_template('index.html',
                           key_b64=base64.b64encode(key).decode(),
                           iv_b64=base64.b64encode(iv).decode())

@app.route('/encrypt', methods=['POST'])
def encrypt():
    message = request.form['message']
    key = key_storage['key']
    iv = key_storage['iv']

    if not key or not iv:
        return render_template('index.html', error="Please generate a key first.")

    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded = pad(message).encode()
    ciphertext = cipher.encrypt(padded)
    return render_template('index.html',
                           encrypted=base64.b64encode(ciphertext).decode(),
                           key_b64=base64.b64encode(key).decode(),
                           iv_b64=base64.b64encode(iv).decode())

@app.route('/decrypt', methods=['POST'])
def decrypt():
    ciphertext_b64 = request.form['ciphertext']
    key_b64 = request.form['key']
    iv_b64 = request.form['iv']

    try:
        ciphertext = base64.b64decode(ciphertext_b64)
        key = base64.b64decode(key_b64)
        iv = base64.b64decode(iv_b64)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(ciphertext)
        message = unpad(decrypted.decode())
    except Exception as e:
        return render_template('index.html', error="Decryption failed. Check your inputs.")

    return render_template('index.html', decrypted=message)

if __name__ == '__main__':
    app.run(debug=True)
