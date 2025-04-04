# Majestic Currency Converter

A stylish web-based currency converter built with Python and Flask, featuring real-time exchange rates and a regal design with golden and purple tones.

## Features
- Real-time conversion using [CurrencyAPI](https://currencyapi.com/).
- Elegant UI with a frosted glass effect and serif typography (Cinzel).
- Dynamic currency list fetched from the API, with fallback.
- Robust error handling for invalid inputs or API issues.
- API key stored via environment variable for security.

## Requirements
- Python 3.6+
- Dependencies: `flask`, `requests` (`pip install flask requests`)
- API Key. (use env var recommended)

## Setup
1. Clone the repo: `git clone <repo-url>`
2. Install dependencies: `pip install flask requests`
3. (Optional) Set API key.

## Usage
### Windows (with batch):
- Double-click `start_conversor.bat` to launch and open `http://127.0.0.1:5000/`.

### Manual:
- Navigate to `flask_currency_converter/`.
- Run: `python app.py`.
- Open `http://127.0.0.1:5000/` in your browser.

Enter a value, select currencies, and click "Convert" to see the result or error.

## Styling
- Colors: Purple gradient (#1a0b2e to #3a1c71), gold (#ffd700, #d4af37), dark purple (#1a0b2e), white (#fff).
- Font: Cinzel (elegant serif).
- Effects: Frosted glass, golden shadows, smooth transitions.

## Notes
- `debug=True` is enabled for development; disable in production.
- API usage limits may apply.
