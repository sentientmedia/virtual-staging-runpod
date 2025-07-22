from model import Predictor

predictor = Predictor()

def handler(event):
    inputs = event["input"]

    # Required fields
    prompt = inputs["prompt"]
    init_image = inputs["init_image"]

    # Optional fields with defaults
    strength = inputs.get("strength", 0.75)
    guidance_scale = inputs.get("guidance_scale", 7.5)

    output = predictor.predict(
        prompt=prompt,
        init_image=init_image,
        strength=strength,
        guidance_scale=guidance_scale
    )
    return {"output": output}
