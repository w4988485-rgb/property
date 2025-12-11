import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Display all files in the repository."""
    # Get the root directory of the project
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Get all files and directories
    files = []
    # Directories to exclude
    excluded_dirs = {'.git', '__pycache__', 'venv', 'node_modules', '.vscode', '.idea'}
    
    for root, dirs, filenames in os.walk(root_dir):
        # Skip hidden directories and common excluded directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in excluded_dirs]
        
        # Get relative path from root
        rel_root = os.path.relpath(root, root_dir)
        if rel_root == '.':
            rel_root = ''
        
        for filename in filenames:
            # Skip hidden files
            if not filename.startswith('.'):
                file_path = os.path.join(rel_root, filename) if rel_root else filename
                files.append(file_path)
    
    # Sort files for better readability
    files.sort()
    
    return render_template('index.html', files=files)

if __name__ == '__main__':
    # Use environment variable to control debug mode
    # Set FLASK_DEBUG=False in production
    debug_mode = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    # In production, use a WSGI server like Gunicorn or uWSGI instead
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
