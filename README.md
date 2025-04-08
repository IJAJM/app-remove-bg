
# Background Remover Web App

A simple Flask-based web application to remove image backgrounds using the `rembg` library.

## Features

- Upload an image via web interface
- Automatically remove the background using AI
- View and download the processed image
- Built-in simple UI with HTML templates

## Demo

Upload an image, remove its background, and download the processed image in one click.

## Requirements

- Python 3.7+
- pip

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/background-remover-webapp.git
   cd background-remover-webapp
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   python app.py
   ```

   Or for production:
   ```bash
   waitress-serve --host=0.0.0.0 --port=8000 app:app
   ```

5. **Access the app**
   Open your browser and go to `http://localhost:8000`

## Project Structure

```
.
├── app.py
├── static/
│   └── processed_images/
├── templates/
│   ├── index.html
│   └── download.html
├── requirements.txt
└── README.md
```

## Dependencies

- Flask
- rembg
- Pillow (PIL)
- waitress (for production server)

## Notes

- Output images are saved in `static/processed_images/output.png`.
- Make sure the `static/processed_images/` directory is writable.
- This app processes one image at a time and overwrites the output.

## License

MIT License. Feel free to use and modify for personal or commercial use.
