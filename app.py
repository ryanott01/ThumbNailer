import os
from PIL import Image, ImageFilter

def create_thumbnail(input_path, output_path, thumbnail_size=(650, 424)):
    img = Image.open(input_path)
    img_fill = img.resize(thumbnail_size, Image.LANCZOS)
    img_fill_blur = img_fill.filter(ImageFilter.GaussianBlur(15))

    img_thumbnail = Image.new('RGB', thumbnail_size)
    img_thumbnail.paste(img_fill_blur, (0, 0))

    img_fit = img.copy()
    img_fit.thumbnail(thumbnail_size, Image.LANCZOS)
    
    x_offset = (img_thumbnail.width - img_fit.width) // 2
    y_offset = (img_thumbnail.height - img_fit.height) // 2
    img_thumbnail.paste(img_fit, (x_offset, y_offset))
    
    img_thumbnail.save(output_path)

def bulk_thumbnail(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.png', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            create_thumbnail(input_path, output_path)

# Usage
input_folder = "input"
output_folder = "output"

bulk_thumbnail(input_folder, output_folder)
