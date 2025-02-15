import asyncio
import os
from pathlib import Path

import orjson
from pysmartthings import Capability, SmartThings
import yaml

async def main():
    json_root = Path("json")
    json_root.mkdir(exist_ok=True)
    yaml_root = Path("yaml")
    yaml_root.mkdir(exist_ok=True)
    async with SmartThings() as client:
        client.authenticate("")
        for capability in [Capability.VALVE]:
            standard_namespace = "." not in capability
            namespace = "standard" if standard_namespace else capability.split(".")[0]
            schema = await client.get_capability(capability)
            json_path = json_root / namespace
            json_path.mkdir(exist_ok=True)
            (json_path / f"{capability}.json").write_text(schema)
            yaml_path = yaml_root / namespace
            yaml_path.mkdir(exist_ok=True)
            with open(yaml_path / f"{capability}.yaml", "w") as f:
                yaml.dump(orjson.loads(schema), f, sort_keys=False)
            await asyncio.sleep(1)

    os.system("npm run prettier")


if __name__ == '__main__':
    asyncio.run(main())