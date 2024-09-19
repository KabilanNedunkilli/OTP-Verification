# OTP-Verification

## Overview
This Python-based OTP (One-Time Password) Verification system enhances security by generating and verifying OTPs for user authentication via email. It provides a simple yet effective way to integrate secure authentication processes into any application. The system sends OTPs to a user’s email and verifies them upon input, ensuring a robust and secure login process.

## Features
- **OTP Generation**: Dynamically generates a secure, random OTP.
- **Email-Based Authentication**: Sends OTP directly to the user's email for verification.
- **OTP Validation**: Verifies OTP within a specified time frame.
- **Error Handling**: Handles invalid OTP entries, expired OTPs, and resends if required.

## Tech Stack
- **Language**: Python
- **Libraries Used**: 
  - `smtplib` for sending OTP emails
  - `random` for OTP generation
- **Email Service**: Works with SMTP servers like Gmail or custom configurations.

## Prerequisites
To run the OTP verification system, you'll need:
- Python 3.x installed
- Internet connection for sending emails via SMTP

## Setup Guide
1. Clone this repository:
   ```bash
   git clone https://github.com/KabilanNedunkilli/OTP-Verification.git
   cd OTP-Verification
   ```

2. Install necessary libraries (if not already installed):
   ```bash
   pip install smtplib
   ```

3. Configure your email credentials in the script for the SMTP service.

4. Run the Python script:
   ```bash
   python otp_verification.py
   ```

## How It Works
1. The user initiates the OTP verification process by providing their email address.
2. The system generates a 6-digit random OTP.
3. The OTP is sent to the user's email.
4. The user enters the received OTP in the application.
5. The system verifies the entered OTP, checking for both correctness and expiration.

## Customization
- **OTP Length**: You can adjust the OTP length by changing the random number generator settings.
- **OTP Expiration**: Modify the expiration time by tweaking the timer logic in the script.

## Potential Use Cases
- User registration or login
- Two-factor authentication (2FA)
- Resetting passwords
- Transaction verification

## Contributions
Feel free to fork this repository, create issues, or submit pull requests for improvements and bug fixes.
