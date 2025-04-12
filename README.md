

# Simple License Key Validator

A simple Python script that simulates license key validation for a fictional piece of software.  
The license key must be a **9-digit number divisible by 7**.

## Features

- Prompts user for a license key
- Validates:
  - Key is exactly 9 digits
  - Key is numeric only
  - Key is divisible by 7
- Retry loop until valid key is entered
- Clean command-line interface

## How to Use

1. Clone or download this repository.
2. Run the script using Python:

```bash
python license_validator.py
```

3. Enter a 9-digit license key when prompted.

## Example

```
=== Welcome to FictionalSoft Activation ===
Please enter your 9-digit license key: 123456789
❌ Invalid license key. Please try again.

Please enter your 9-digit license key: 123456721
✅ License key is valid. Thank you for activating!
```

## Requirements

- Python 3.x

## Notes

This is a fictional example meant for educational or entertainment purposes only.  
It was inspired by the simple validation algorithms used in early software like Windows 95.
