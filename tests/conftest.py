import pytest
from typing import AsyncGenerator
from fitgirl.client import FitGirlClient


@pytest.fixture
async def client() -> AsyncGenerator[FitGirlClient, None]:
    """
    Fixture providing a FitGirlClient instance.
    Ensures the client is closed after the test.
    """
    async with FitGirlClient() as c:
        yield c
