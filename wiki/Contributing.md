# Contributing

We welcome contributions! Please follow these guidelines.

## Development Environment

1.  **Clone the repo**:
    ```bash
    git clone https://github.com/yourusername/fitgirl.git
    cd fitgirl
    ```

2.  **Install with uv**:
    ```bash
    uv sync
    ```

3.  **Run Tests**:
    ```bash
    uv run pytest
    ```

## Code Style

See [CODE-STYLE.md](../CODE-STYLE.md) for detailed rules.

*   **Linting**: Run `uv run ruff check .`
*   **Formatting**: Run `uv run ruff format .`
*   **Type Checking**: Run `uv run mypy .`

## Documentation

*   Update the Wiki if you change the public API.
*   Add NumPy-style docstrings to all new methods.
