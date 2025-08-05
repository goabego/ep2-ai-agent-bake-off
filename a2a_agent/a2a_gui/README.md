# A2A GUI

This is a graphical user interface (GUI) for interacting with A2A (Agent-to-Agent) agents. It provides a simple and intuitive chat interface for sending and receiving messages, as well as a debug panel for inspecting the raw JSON responses from the agent.

## Prerequisites

- Python 3.11+
- `uv`

## How to Run

1.  **Install Dependencies**: Install the necessary dependencies using `uv`:

    ```bash
    uv pip install -e .
    ```

2.  **Run the Server**: Run the FastAPI server using `uv`:

    ```bash
    uv run uvicorn server:app --host 0.0.0.0 --port 8000
    ```

3.  **Open the GUI**: Open your browser and navigate to `http://localhost:8000` to start using the GUI.

## Disclaimer

This is not an officially supported Google product. The code is provided as-is, without any warranty or support.

This application is designed to interact with A2A agents. As with any application that communicates with external services, it is important to be aware of the potential security risks. Always treat data received from an agent as untrusted input. Failure to do so may lead to security vulnerabilities, including but not limited to prompt injection.