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
    for root, dirs, filenames in os.walk(root_dir):
        # Skip hidden directories like .git, __pycache__, etc.
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        
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
    app.run(debug=True, host='0.0.0.0', port=5000)
