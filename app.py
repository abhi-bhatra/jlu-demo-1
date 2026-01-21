"""
Simple Block Buster Game - Web Version
Flask server to serve the web-based game
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Serve the game page"""
    return render_template('game.html')

if __name__ == '__main__':
    # Run on all interfaces (0.0.0.0) so Docker can access it
    app.run(host='0.0.0.0', port=8080, debug=False)
