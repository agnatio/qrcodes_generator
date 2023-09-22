# FastAPI QR Code Generator

## Introduction

This FastAPI application provides a simple API to generate QR codes. It serves an HTML interface where users can input data to generate a QR code, and it also exposes an API endpoint (`/generate_qr_code`) for QR code generation.

## Features

- HTML interface for generating QR codes.
- API endpoint for QR code generation.
- Uses `fastapi` for API and `qrcode` for QR code generation.
  
## Prerequisites

- Python 3.6+
- FastAPI
- Uvicorn (ASGI server)
- Jinja2 (for HTML templates)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    ```

2. Navigate into the project directory:
    ```bash
    cd yourrepository
    ```

3. Install the project dependencies using Poetry:
    ```bash
    poetry install
    ```

## Usage

### Running the server

To run the server, execute the following command:

```bash
uvicorn main:app --host localhost --port 8000
```

Then visit `http://localhost:8000/` in your web browser to access the HTML interface.

### API Endpoint

To generate a QR code programmatically, make a GET request to `/generate_qr_code`:

```
GET /generate_qr_code?data=yourdata
```

Replace `yourdata` with the data you want to encode in the QR code. The API will return the QR code as a PNG image.

## File Structure

- `main.py`: Contains FastAPI application and API endpoints.
- `qr_gen.py`: A module for generating QR codes.
- `templates/`: Folder containing Jinja2 HTML templates.
- `static/`: Folder for static files.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
