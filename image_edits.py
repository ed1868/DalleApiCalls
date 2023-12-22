import openai
from dotenv import dotenv_values
config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

from IPython.core.display import Image
wave_image = open("./public/images/great_wave.png", "rb").read()
Image(data=wave_image, width=256)

wave_image_mask = open("./public/images/great_wave_mask.png", "rb").read()
Image(data=wave_image_mask, width=256)

response = openai.Image.create_edit(
    image=wave_image,
    mask=wave_image_mask,
    prompt="a surfer riding a surfboard down the Great Wave",
    n=1,
    size="1024x1024"
)

Image(url=response["data"][0]["url"])