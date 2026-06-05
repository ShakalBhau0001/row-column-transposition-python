# 🔐 Row–Column Transposition Cipher Implementation (Python)

A complete and educational Python implementation of the Row–Column Transposition Cipher encryption algorithm.
This project demonstrates column-based permutation encryption and decryption using structured logic.

It is created as a learning and academic project to understand how classical columnar transposition cryptography works internally, not as a production-ready security system.

---

## 🧱 Project Structure

```bash
row-column-transposition-python/
│
├── app.py              # Basic CLI version
├── interactive.py      # Rich-powered CLI
├── requirements.txt    # Dependencies
├── LICENSE             # Project license
└── README.md           # Project documentation
```

---

## ✨ Features

### 🔑 Keyword-Based Column Permutation
- Uses a keyword as the encryption key
- Determines column order based on alphabetical ranking
- Rearranges plaintext using column permutation
- Demonstrates structured transposition logic

### 🔒 Encryption
- Removes spaces before processing
- Arranges plaintext row-wise in a matrix
- Reorders columns according to keyword
- Reads column by column to generate ciphertext

### 🔓 Decryption
- Reconstructs the column structure using the same keyword
- Restores original row-wise message order
- Reverses the permutation algorithm accurately

### 🧮 Educational Focus
- Clean and readable logic
- Matrix-based column handling
- Ideal for beginners in cryptography
- No external dependencies

### 🎨 Rich CLI (Interactive Mode)
- Beautiful colored terminal UI using Rich
- Structured panels for output display
- Interactive prompts with validation
- Enhanced user experience compared to standard CLI

### ⚡ Dual Mode Support
- 🧼 Basic CLI → Lightweight, no dependencies
- 🎨 Rich CLI → Enhanced UI with colors and panels

---

## 🛠 Technologies Used

| Technology              | Role                        |
| ----------------------- | --------------------------- |
| **Python 3**            | Core programming language   |
| **List & Matrix Logic** | Column permutation handling |
| **Rich**             | Styled CLI, colors, panels     |

---

## 📌 Purpose of This Project

This project is built to:
- Understand classical columnar transposition ciphers
- Learn permutation-based encryption logic
- Explore matrix-based cryptographic techniques
- Study reversible transformation algorithms

> ⚠️ This project is intended strictly for learning and demonstration purposes.

---

## ▶️ How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/ShakalBhau0001/row-column-transposition-python.git
```

### 2️⃣ Navigate to the project folder
```bash
cd row-column-transposition-python
```

### 3️⃣ Install Dependencies

```bash
pip install rich
```

**OR**

```bash
pip install -r requirements.txt
```

### 4️⃣ Running the Project

#### Basic CLI Version

```bash
python app.py
```

#### Rich Interactive Version

```bash
python interactive.py
```

### 5️⃣ Follow the prompts for Basic CLI Version
- Choose direction:
  - `E` → Encrypt
  - `D` → Decrypt
- Enter your message
- Enter keyword
- View the result

---

## 🔎 Example

> Encryption :

```bash
Encrypt or Decrypt (E/D): E
Enter message: MEET ME TOMORROW
Enter keyword: ZEBRA

Encrypted message: EMRMOETEWROTMEO
```

> Decryption :

```bash
Encrypt or Decrypt (E/D): D
Enter message: EMRMOETEWROTMEO
Enter keyword: ZEBRA

Decrypted message: MEETMETOMORROWX
```

> (Note: Padding character may appear during decryption.)

---

## ⚠️ Limitations

- Not secure for real-world use
- Classical cipher (easily breakable)
- May include padding characters
- Removes spaces during processing
- CLI-based interaction only

---

## 🌟 Future Improvements

- Preserve spaces and formatting
- Improve duplicate-letter handling in keywords
- Add frequency analysis support
- Add input validation enhancements
- Create GUI version
- Combine into a classical cryptography toolkit

---

## ⚠️ Disclaimer

This implementation is created **for educational and learning purposes only.**
The Row–Column Transposition Cipher is historically significant but cryptographically insecure and must not be used to protect real-world sensitive data.

---

## 📸 Preview

![Rich CLI Preview](assets/screenshot.png)

---

## 🪪 Author

> **Shakal Bhau**

> **GitHub: [ShakalBhau0001](https://github.com/ShakalBhau0001)**

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

---
