## Divisor Development Conventions

This document outlines the conventions to be followed during the development of the Divisor tool.

### Code Style

- All Python code should follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide.
- Use type hints for all function signatures.
- Use `black` for code formatting and `isort` for import sorting.

### Commit Messages

- Commit messages should follow the [Conventional Commits](https://www.conventionalcommits.org/) specification.
- The subject line should be 50 characters or less.
- The body should explain the "what" and "why" of the change.

### Testing

- All new features should be accompanied by unit tests.
- All tests should be placed in the `tests` directory.
- Run the test suite using `pytest`.

### Documentation

- All public functions and classes should have docstrings.
- The documentation should be written in Markdown and placed in the `docs` directory.
- Use a clear and concise writing style.
