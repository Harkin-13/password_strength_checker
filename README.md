# Password Strength Checker 🔐

A terminal-based password strength checker built with Python.  
Evaluates the quality of a password, offers improvement suggestions, and estimates the time it would take to crack using [zxcvbn](https://github.com/dropbox/zxcvbn) — a realistic password strength estimator developed by Dropbox.

---

## Author

**Seán Harkin**  
2nd Year Computing & IT (Software) student.  

---

## Features

- Secure input using `getpass` (password is hidden in terminal)
- Evaluates:
  - Minimum length (8 characters)
  - Presence of lowercase letters
  - Presence of uppercase letters
  - Presence of numbers
  - Presence of special characters
- Clean report style output with pass/fail indicators
- Suggests improvements for missing password traits
- Estimates crack time using the `zxcvbn` library
- Replayable loop with validation and memory clearing
- Clean, readable structure with functional logic and inline assignment

---

## Sample Output
```
================ New Test =================

Enter the password you would like to test: 
-------------------------------------------
Password Audit Report
-------------------------------------------
[✓] Minimum length (8)               Passed
[✓] Lowercase letter                 Passed
[✓] Uppercase letter                 Passed
[✗] Number                           Failed
[✗] Special character                Failed
-------------------------------------------
Suggested Improvements:
- Add at least one number.
- Use at least one special character (e.g. !@#$%).
-------------------------------------------
Overall Strength: Weak
Estimated Crack Time: 1 second

Test another password? (yes/no):
```

---

## How to Run

1. Make sure you have Python 3 installed.
2. Install `zxcvbn` via pip:
   ```bash
   pip install zxcvbn
3. Download or clone this repository.

4. Run the script from terminal:
    ```bash
    python password_strength_checker.py