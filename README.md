# COREVISTA SOFTWARE LLC

Responsive Flask website for COREVISTA SOFTWARE LLC, covering software and
platform development, AI training and engineering, technology solutions, and
company contact information.

## Requirements

- Python 3.9 or newer

## Run locally

From this directory, create and activate a virtual environment, then install
the application dependency:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in a browser. The contact
form is available at `/contact` and from the home page.

The form validates the required name, email, and message fields and displays a
confirmation page. It does not deliver or store submissions; connect an
approved email or CRM service before using the form for production inquiries.

## Pages

- `/` — company overview, services, process, differentiators, and contact form
- `/contact` — contact form and company registration details
