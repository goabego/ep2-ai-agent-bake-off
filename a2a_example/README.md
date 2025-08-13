# A2A Example Agents & GUI

This directory contains example implementations of A2A (Agent-to-Agent) agents and a GUI tool for testing and demonstration purposes.

## 📋 Prerequisites

- **Python 3.11+** (required for all projects)
- **UV package manager** - [Install UV](https://docs.astral.sh/uv/getting-started/installation/)
- **Google Cloud CLI** - [Install gcloud](https://cloud.google.com/sdk/docs/install)
- **Docker/Podman** (optional, for containerized deployment)

## 🚀 Quick Start

### 1. Install UV Package Manager

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Verify installation
uv --version
```

### 2. Clone and Setup

```bash
cd a2a_example
```

## 🤖 Agent Examples

### A2A Bake Off Agent

A basic A2A agent implementation for the bake-off competition.

**Setup:**
```bash
cd a2a_bake_off_agent

# Create virtual environment and install dependencies
uv venv
uv pip install -r requirements.txt

# Activate virtual environment
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate     # Windows
```

**Run:**
```bash
# Run the agent locally
uvicorn main:app --host 0.0.0.0 --port 8000

# Or using Python directly
python main.py
```

**Environment Variables:**
```bash
export GOOGLE_GENAI_USE_VERTEXAI=FALSE
export GOOGLE_API_KEY=MyKeyGoesHere
```

### A2A Cymbal Bank Agent

A specialized financial advisor agent with banking capabilities.

**Setup:**
```bash
cd a2a_cymbal_bank_agent

# Create virtual environment and install dependencies
uv venv
uv pip install -r requirements.txt

# Activate virtual environment
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate     # Windows
```

**Run:**
```bash
# Run the agent locally
uvicorn main:app --host 0.0.0.0 --port 8001

# Or using Python directly
python main.py
```

## 🖥️ GUI Tool

A web-based interface for testing A2A agents.

**Setup:**
```bash
cd a2a_ui_tool

# Create virtual environment and install dependencies
uv venv
uv pip install -r requirements.txt

# Activate virtual environment
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate     # Windows
```

**Run:**
```bash
# Start the GUI server
uvicorn server:app --host 0.0.0.0 --port 8080 --reload

# Or using Python directly
python server.py
```

**Access GUI:**
Open your browser and navigate to: `http://localhost:8080`

