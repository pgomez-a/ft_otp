# ft_otp

<img width="1163" alt="ft_otp" src="https://user-images.githubusercontent.com/74931024/166148833-a791b2cd-327b-42bf-ae4b-b1e75fb4fac4.png">

**If you want to learn more about IT topics, visit my website:** [**IA Notes**](https://ia-notes.com/)

### 2-Factor Authentication
**2FA** enhances the security of a system by adding an additional layer of security. When a user tries to access a system (such as a server or a service) they must **authenticate with a password and an additional token** that the user must have in order to access the system.<br>
Thus, with 2FA, there are two layers of security that the user must go through to access private data. Without that second token, a hacker cannot access the system even if the first password is known. One way to achieve this 2FA is through the use of **One-Time-Passwords**, which will be described below.

### One-Time-Passwords
A **One Time Password (OTP)** is an automatically generated sequence of numeric or alphanumeric characters to authenticate users for a single sign-on. An OTP is a multi-factor authentication factor used to guarantee access to private data. The main characteristics of an OTP are the following:
- **It expires quickly.**
- **It can't be reused.**

One-time passwords are generated using a random code that is generated each time a new password request is made. There are three different ways that allow a user to obtain their OTP:
- An authentication token.
- A unique time-based password, also known as **TOTP**.
- A unique password based on HMAC, also known as **HOTP**.
