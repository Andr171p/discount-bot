import json
import aiofiles
from typing import Dict
from pathlib import Path


async def load_json(path: Path | str) -> Dict[str, str]:
    async with aiofiles.open(
        file=path,
        mode='r',
        encoding='utf-8'
    ) as file:
        data = await file.read()
        return json.loads(data)
