# MCP Installer CLI

A command-line interface tool for managing MCP (Master Control Program) servers with an intuitive, multi-step installation process.

## Features

- **Interactive Commands**: Easily add and list MCP servers through guided prompts
- **Rich Terminal UI**: Beautiful, color-coded interface for better visibility
- **Environment Variable Management**: Define environment variables with descriptions and optional default values
- **Repository Configuration**: Link servers to their source repositories

## Installation

### Prerequisites

- Python 3.7+
- uv package manager (recommended) or pip

### Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd mcp-installer

# Using uv (recommended)
uv venv
source .venv/bin/activate  # On Unix/macOS
# OR .venv\Scripts\activate  # On Windows
uv pip install -e .

# Or using pip
pip install -e .
```

## Usage

### Adding a Server

```bash
python main.py add
```

This will walk you through a multi-step process to configure:
- Server name
- Repository URL
- Command to execute
- Optional command arguments
- Optional environment variables with descriptions and default values

### Listing Servers

```bash
python main.py list
```

Displays a formatted table of all configured MCP servers.

### Help

```bash
python main.py --help
```

## Example

```bash
$ python main.py add

# You'll be prompted to provide:
# - Server Name: my-mcp-server
# - Repository URL: https://github.com/example/mcp-server
# - Command: ./start.sh
# - Command args (optional): --port 8080
# - Environment Variables (optional):
#   - API_KEY: "API key for authentication"
#   - DB_CONNECTION: "Database connection string"
```

## Project Structure

```
mcp-installer/
├── main.py           # Main CLI application
├── pyproject.toml    # Project configuration and dependencies
├── uv.lock           # Dependency lock file
└── README.md         # This documentation
```

## Dependencies

- [Typer](https://typer.tiangolo.com/): For creating the CLI interface
- [Rich](https://rich.readthedocs.io/): For beautiful terminal formatting

## License

[MIT License](LICENSE)