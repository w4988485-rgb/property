# Property Project

A simple web application that displays all files in the repository on the root path.

## Features

- Web interface to view all files in the repository
- Clean and simple UI
- Real-time file listing

## Requirements

- Python 3.8+
- Flask

## Installation

```bash
# Clone this repository
git clone https://github.com/w4988485-rgb/property.git

# Navigate into the project directory
cd property

# Install dependencies
pip install -r requirements.txt
```

## Usage

To run the application in development mode:

```bash
python app.py
```

To run in production mode (without debug):

```bash
FLASK_DEBUG=False python app.py
```

Then open your browser and navigate to `http://localhost:5000/` to see all files in the repository.

**Note**: For production deployments, it's recommended to use a production WSGI server like Gunicorn or uWSGI instead of the built-in Flask development server.

---

## Contributing

1. Fork the repository.
2. Create a new branch.
3. Submit your changes as a pull request.

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
