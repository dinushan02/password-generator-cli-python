# 🔐 Password Generator CLI (Python)

A customizable and user-friendly **command-line password generator** built with Python.  
This tool allows users to generate secure passwords based on their preferences, including uppercase letters, numbers, and special symbols.

---

## 🚀 Features

- ✅ Generate passwords of custom length  
- ✅ Option to include:
  - Uppercase letters (A–Z)
  - Numbers (0–9)
  - Special characters (!@#$...)  
- ✅ Ensures at least **one character from each selected type**  
- ✅ Input validation for better user experience  
- ✅ Loop-based interface (generate multiple passwords easily)  
- ✅ Optional: Copy password to clipboard  

---

## 🛠️ Technologies Used

- Python 3  
- Built-in modules:
  - `random`
  - `string`
- Optional:
  - `pyperclip` (for clipboard support)

---

## 📂 Project Structure
password-generator-cli-python/
│
├── main.py
└── README.md

---

## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/dinushan02/password-generator-cli-python.git
cd password-generator-cli-python
```

2. Run the program:
- main.py

---

🧪 Example Usage
- 🔐 Password Generator

* Enter password length: 10
* Include uppercase? (y/n): y
* Include numbers? (y/n): y
* Include symbols? (y/n): n

* Generated Password: aB7kLm92Qp

* Generate another password? (y/n): n
* Goodbye 👋

---

📋 Optional Feature: Copy to Clipboard
Install dependency:
```
pip install pyperclip
```
* The generated password will automatically be copied to your clipboard.

---

🎯 Learning Outcomes
This project helped me practice:
* Python fundamentals (loops, conditionals, functions)
* Input validation and error handling
* Modular programming
* Working with built-in libraries (random, string)
* Writing clean and maintainable code
* Building real-world CLI applications

---

📌 Future Improvements
* Add GUI version (Tkinter / PyQt)
* Add password strength checker
* Save generated passwords securely
* Add configuration file support

👨‍💻 Author
Developed by M.Dinushan
Aspiring AI Engineer 🚀

⭐ Support
If you found this project helpful, consider giving it a ⭐ on GitHub!
