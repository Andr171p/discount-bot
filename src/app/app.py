from fastapi import FastAPI
from contextlib import AbstractAsyncContextManager


async def lifespan(
        app: FastAPI
) -> AbstractAsyncContextManager[None]:
    pass
