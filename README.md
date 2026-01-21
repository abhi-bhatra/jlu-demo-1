# Simple Block Buster Game

A very basic and simple block buster (breakout) game - now available as a web version that works in Docker!

## Requirements

- Python 3.6 or higher
- Flask (for web version)

## Installation

1. Install Flask:
```bash
pip install -r requirements.txt
```

Or directly:
```bash
pip install flask
```

## How to Run (Web Version - Recommended for Docker)

Run the Flask server:
```bash
python app.py
```

Then open your browser and go to:
```
http://localhost:8080
```

## How to Play

- Use **LEFT** and **RIGHT** arrow keys to move the paddle
- The ball bounces off the paddle, walls, and blocks
- Break all the blocks to win!
- If the ball falls off the bottom, you lose

## Game Features

- Simple paddle at the bottom
- Bouncing ball
- 5 rows of colorful blocks to break
- Score tracking
- Win/lose conditions
- Web-based (works in browser, perfect for Docker!)

## Code Structure

The code is very simple and well-commented:
- `app.py`: Flask web server
- `templates/game.html`: HTML5 Canvas game with JavaScript
- Simple game logic: paddle, ball, blocks, and collision detection

Perfect for learning game development and Docker basics!

## Docker

### Build the Docker Image

```bash
docker build -t blockbuster-game .
```

### Run the Container

```bash
# Map container port 8080 to host port 8080
docker run -d -p 8080:8080 blockbuster-game
```

**Note:** The `-d` flag runs in detached mode (background), and `-p 8080:8080` maps the container port to your host port.

### Access the Game

After running the container, open your browser and go to:
```
http://localhost:8080
```

### Check Container Status

To see if your container is running:

```bash
# List all running containers and their ports
docker ps

# You should see output like:
# CONTAINER ID   IMAGE              PORTS
# abc123def456   blockbuster-game   0.0.0.0:8080->8080/tcp
```

The `PORTS` column shows `HOST_PORT->CONTAINER_PORT`, so `0.0.0.0:8080->8080/tcp` means the container port 8080 is mapped to host port 8080.

### Stop the Container

```bash
# Find container ID
docker ps

# Stop the container
docker stop <container_id>
```

### Port Mapping Explained

The `-p` flag maps ports: `-p HOST_PORT:CONTAINER_PORT`
- `-p 8080:8080` means host port 8080 maps to container port 8080
- You can use any host port: `-p 3000:8080` maps host port 3000 to container port 8080
- Then access via `http://localhost:3000`

### Dockerfile Explanation

The Dockerfile is very simple and perfect for learning:
- `FROM python:3.11-slim` - Uses Python base image
- `WORKDIR /app` - Sets working directory
- `COPY requirements.txt .` - Copies dependency file
- `RUN pip install...` - Installs dependencies
- `COPY app.py .` - Copies Flask app
- `COPY templates/ templates/` - Copies HTML template
- `EXPOSE 8080` - Documents which port the app uses
- `CMD ["python", "app.py"]` - Runs the Flask server
# jlu-demo-1
