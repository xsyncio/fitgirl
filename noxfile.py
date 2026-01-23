import nox

nox.options.sessions = ["tests", "lint", "type_check"]


@nox.session
def tests(session):
    """Run the test suite."""
    session.install("-e", ".", "pytest", "pytest-asyncio")
    session.run("pytest", *session.posargs)


@nox.session
def lint(session):
    """Run linters."""
    session.install("ruff")
    session.run("ruff", "check", ".")
    session.run("ruff", "format", "--check", ".")


@nox.session
def type_check(session):
    """Run type checking."""
    session.install(
        "-e", ".", "mypy", "msgspec", "curl-cffi", "selectolax", "playwright", "pytest"
    )
    session.run("mypy", "src")
