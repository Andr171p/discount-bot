from fastapi import FastAPI

from contextlib import asynccontextmanager
from contextlib import AbstractAsyncContextManager


@asynccontextmanager
async def lifespan(
        app: FastAPI
) -> AbstractAsyncContextManager[None]:
    pass
