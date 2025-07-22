import runpod

runpod.api_key = "rpa_2BA6UHNALWDDVKBFRO2CNOXKN4GF2I05FOTERXL7dnze9z"  # ← paste your key here

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