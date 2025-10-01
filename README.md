# Website_Security_Breach_Analyzing-the_Code_and_Attack

A small, self-contained lab to demonstrate how seemingly “simple” authentication code can be broken in practice, and how to think about hardening it.

This repository contains:

- A minimal Flask login page with intentionally weak security controls (for learning).
- A simulated “attacker” script that brute-forces credentials against the local demo server.

Use this only in your own, isolated test environment. Never point the attack script at systems you do not own or lack explicit permission to test.

---

## Video tutorial

Watch the walkthrough video here: - https://www.facebook.com/share/v/1a9eWZyEM7/

---

## Repository structure

- `LoginPage/`
  - `Login_Page.py` — Flask app serving a basic login at `http://localhost:8080/login`.
  
- `Attack (Open with other vsCode window)/`
  - `Attcking Code.py` — A simple credential enumeration script (lab-only) that tries common username/password pairs against the local login page.
  
---

## What you’ll learn

- Why input validation (e.g., regex checks) is not the same as authentication.
- Typical auth weaknesses in demo code: plain-text credentials, no rate limiting, no account lockout, and no password hashing.
- How trivial credential stuffing/brute-force works in a controlled lab.
- Concrete hardening steps for real applications.

---

## Prerequisites

- Windows with PowerShell (examples use PowerShell)
- Python 3.8+ installed and on PATH

Install Python packages with `pip`; a `requirements.txt` is included for convenience.

---

## Quick start (local, lab-only)

1. Create and activate a virtual environment (recommended)

```powershell
# From the repo root
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies

```powershell
pip install -r requirements.txt
```

3. Start the vulnerable login demo

```powershell
python ".\LoginPage\Login_Page.py"
```

You should see the app start and bind to `http://localhost:8080`. Visit this URL in your browser and open `/login` to see the form.

4. In a separate terminal, run the simulated attacker (again: lab-only, against your local instance)

```powershell
python ".\Attack (Open with other vsCode window)\Attcking Code.py"
```

Expected behavior: the script tries a small list of username/password pairs; with the default demo settings, it will eventually print a successful login (e.g., `administrator_` / `admin_123`).

---

## How the demo works

- The Flask app stores a single user in memory:
  - Username: `administrator_`
  - Password: `admin_123`
  
- The username field is superficially validated via a regex: `^[a-zA-Z0-9_]+$`.
  - This illustrates a common misconception: input validation helps with hygiene, but it does not prevent credential stuffing or brute force.
  
- Missing controls by design (for learning):
  - No password hashing (plain-text in memory)
  - No rate limiting or exponential backoff
  - No account lockout or CAPTCHA
  - No CSRF/token protections for form posts
  - No logging/alerting for repeated failures

---

## Security takeaways and hardening ideas

- Don’t rely on regex validation for security. It’s hygiene, not a control against abuse.
- Always hash passwords (e.g., with `werkzeug.security` or `passlib`) and never store them in plain text.
- Add rate limiting and lockout policies (e.g., `Flask-Limiter`).
- Enforce strong passwords and consider MFA for sensitive accounts.
- Use CSRF protections for form submissions.
- Add monitoring/logging for repeated failures and unusual patterns.
- Bound input sizes and prefer regexes with linear-time behavior to avoid regex DoS; also cap request rates and payload sizes at the web server/WAF level.

If you’d like, open issues/PRs to turn these ideas into concrete improvements in this demo.

---

## Troubleshooting

- “Address already in use” on port 8080: either stop the existing process or change the port in `Login_Page.py` (e.g., `app.run(host='localhost', port=8090)`) and update the attacker script URL accordingly.
- `pip` not found: ensure Python is on PATH or use the full interpreter path (`py -m pip ...` on Windows).
- Import errors for `flask` or `requests`: re-run `pip install -r requirements.txt` in the active virtual environment.

---

## Ethical use disclaimer

This project is for educational and defensive purposes in a controlled environment you own. Do not use any part of this repository to access systems without explicit authorization. You are solely responsible for complying with all applicable laws and policies.

---

## Author and links

- Repository: Website_Security_Breach_Analyzing-the_Code_and_Attack
- Maintainer: [Sagar Biswas](https://github.com/SagarBiswas-MultiHAT)

If this helped, consider starring the repo and sharing feedback or improvements.
