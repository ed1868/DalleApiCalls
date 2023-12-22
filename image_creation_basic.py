import openai
from dotenv import dotenv_values
config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]
res = openai.Image.create(
    prompt="an female astronaut lounging in a tropical resort in space, very detailed, she is curvy, blonde and is smoking a joint",
    size="1024x1024",
    n=5
)
res["data"]

picture_array= res["data"];

print(picture_array)