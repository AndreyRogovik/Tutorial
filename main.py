import rembg
from PIL import Image
import io

def remove_background(input_image_path, output_image_path):
    with open(input_image_path, "rb") as f:
        img = f.read()
    result = rembg.remove(img)
    img = Image.open(io.BytesIO(result)).convert("RGBA")

    # Create a new image with a transparent background
    transparent_img = Image.new("RGBA", img.size, (0, 0, 0, 0))
    transparent_img.paste(img, (0, 0), mask=img)

    transparent_img.save(output_image_path, "PNG")

# Provide the input and output paths
input_path = "C:\\Users\\AR\\Desktop\\New folder\\alina.jpg"
output_path = "C:\\Users\\AR\\Desktop\\New folder\\output.png"

# Call the remove_background function
remove_background(input_path, output_path)

# Print the output path
print("Output saved at:", output_path)
