"""
Simple Block Buster Game - Web Version
Flask server to serve the web-based game
"""

import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Serve the game page"""
    return render_template('game.html')

if __name__ == '__main__':
    # Use PORT from environment (Heroku provides this) or default to 8080
    port = int(os.environ.get('PORT', 8080))
    # Run on all interfaces (0.0.0.0) so Docker/Heroku can access it
    app.run(host='0.0.0.0', port=port, debug=False)
