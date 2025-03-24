# passsword_strength_checker
# Author: Seán Harkin
# Description: Terminal-based password strength tester with estimated crack time.

import time
from getpass import getpass
from zxcvbn import zxcvbn

# Password Rule Functions
# -----------------------
def has_length(password):
    return len(password) >= 8
def has_lowercase(password):
    return any(c.islower() for c in password)
def has_uppercase(password):
    return any(c.isupper() for c in password)
def has_digit(password):
    return any(c.isdigit() for c in password)
def has_special(password):
    return  any(c in "!@#$%^&*()" for c in password)

# Dictionaries
# ------------
# Output rule names
display_names = {
    'length': "Minimum length (8)",
    'lower': "Lowercase letter",
    'upper': "Uppercase letter",
    'digit': "Number",
    'special': "Special character"
}
# Suggestions to improve failed checks
suggestions = {
    'length': "Use at least 8 characters.",
    'lower': "Include at least one lowercase letter.",
    'upper': "Include at least one uppercase letter.",
    'digit': "Add at least one number.",
    'special': "Use at least one special character (e.g. !@#$%)."
}
# Score-to-label map from zxcvbn
strength_levels = {
    0: "Very Weak",
    1: "Weak",
    2: "Moderate",
    3: "Strong",
    4: "Very Strong"
}

# Main loop
# ---------
while True: 
    # Initialise results dictionary for checker
    test_results = {
    'length' : '',
    'lower': '',
    'upper': '',
    'digit': '',
    'special': '',
    }

    print("\n\n================ New Test =================\n")
    userPassword = getpass("Enter the password you would like to test: ")

    # Run checks using Password Rule Functions
    test_results["length"] = "Passed" if has_length(userPassword) else "Failed"
    test_results['lower'] = "Passed" if has_lowercase(userPassword) else "Failed"
    test_results['upper'] = "Passed" if has_uppercase(userPassword) else "Failed"
    test_results['digit'] = "Passed" if has_digit(userPassword) else "Failed"
    test_results['special'] = "Passed" if has_special(userPassword) else "Failed"
   
    # Use zxcvbn to analyse password strength and crack time
    result = zxcvbn(userPassword)
    score = result['score']
    crack_time = result['crack_times_display']['offline_slow_hashing_1e4_per_second']

    # Final Ouput
    # -----------
    print("-------------------------------------------")
    print("Password Audit Report")
    print("-------------------------------------------")

     # Print each check with status icon
    for key in test_results:
        status = test_results[key]
        icon = "✓" if status == "Passed" else "✗"
        print(f"[{icon}] {display_names[key]}".ljust(37) + test_results[key])

    time.sleep(2)
    print("-------------------------------------------")
    print("Suggested Improvements:")
    suggested = False
    for key, result in test_results.items():
        if result == "Failed":
            print("-", suggestions[key])
            suggested = True
    if not suggested:
        print("✓ All checks passed!")

    time.sleep(2)
    print("-------------------------------------------")
    print(f"Overall Strength: {strength_levels[score]}")
    print(f"Estimated Crack Time: {crack_time}")

    # Clear userPassword for peace of mind
    userPassword = None
    time.sleep(2)

    # Try Again Prompt
    # ------------
    while True:
        try_again = input("\nTest another password? (yes/no): ").lower().strip()
        if try_again in ["yes", "no"]:
            break
        else:
            print("Please enter 'yes' or 'no'.")

    if try_again == "no":
        break