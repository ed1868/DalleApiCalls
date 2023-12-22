import openai
from dotenv import dotenv_values
config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

def save_image(url, image_name):
    image_directory_name = "images"
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
    
res = openai.Image.create_variation(
    image=open("./images/popsicle.png", "rb"),
    n=6
)


for idx, img in enumerate(res["data"]):
    save_image(img["url"], f"popsicle-{idx}.png")
    
res