import openai
import base64
from dotenv import dotenv_values
config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

def save_image(url, image_name):
    image_directory_name = "public/images"
    image_directory = os.path.join(os.curdir, image_directory_name)

    if not os.path.isdir(image_directory):
        os.mkdir(image_directory)
        
    image_filepath = os.path.join(image_directory, image_name)
    
    image_content = requests.get(url).content
    
    with open(image_filepath, "wb") as image_file:
        image_file.write(image_content)
        
def get_image(prompt, image_name):
    res = openai.Image.create(
        prompt=prompt,
        size="512x512",
        n=1
    )
    image_url = res["data"][0]["url"]
    save_image(image_url, image_name)
    
get_image(
    prompt="a sunset from a graveyard with a skeleton reading a novel",
    image_name="graveyard.png"
)
get_image(
    prompt="a 3d rendering of a melting peach popsicle against a gradient background",
    image_name="popsicle.png"
)

def get_and_save_image(prompt, image_name):
    res = openai.Image.create(
        prompt=prompt,
        size="512x512",
        n=1,
        response_format="b64_json"
    )
    image_data = res["data"][0]["b64_json"]
    
    image_directory_name = "images"
    image_directory = os.path.join(os.curdir, image_directory_name)

    if not os.path.isdir(image_directory):
        os.mkdir(image_directory)
        
    image_filepath = os.path.join(image_directory, image_name)
    
    decoded_img = base64.b64decode(image_data)
    
    with open(image_filepath, "wb") as f:
        f.write(decoded_img)
    

get_and_save_image("a friendly cactus sitting in a pot, digital art", "cactus.png")

get_and_save_image("a painting of a vase full of lollipops in the style of van gogh", "vangogh.png")