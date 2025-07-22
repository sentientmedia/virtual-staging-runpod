import runpod
import os
from dotenv import load_dotenv

load_dotenv()
runpod.api_key = os.getenv("RUNPOD_API_KEY")


deployment = runpod.serverless.create_endpoint({
    "name": "virtual-staging",
    "source": "./runpod_serverless",
    "entrypoint": "handler",
    "gpu": "NVIDIA A10G",
    "accelerator": "GPU",
    "memory": 4,
    "timeout": 300,
    "idleTimeout": 60,
})

print("✅ Endpoint created:")
print("ID:", deployment['id'])
print("Status:", deployment['status'])