from PIL import Image, ImageDraw, ImageFont
import os

def create_whatsapp_image():
    # Load base image
    img = Image.open('renata-160.jpg').convert('RGBA')
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Increase font size significantly
    try:
        font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 54)
    except:
        font = ImageFont.load_default()

    bubbles = [
        {"text": "Insegurança.", "pos": (120, 250)},
        {"text": "Falta de organização.", "pos": (img.width - 600, 500)},
        {"text": "Casa \"insuficiente\".", "pos": (150, 750)}
    ]
    
    # Style parameters
    bg_color = (40, 30, 20, 180) # Dark semi-transparent
    border_color = (245, 236, 216, 110) # Beige semi-transparent
    text_color = (245, 236, 216, 255) # Beige text
    dot_color = (139, 175, 124, 255) # Green dot #8BAF7C
    
    padding_x = 45
    padding_y = 35
    radius = 45
    
    for bubble in bubbles:
        text = bubble["text"]
        
        # Measure text
        try:
            bbox = font.getbbox(text)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
        except AttributeError:
            text_width, text_height = draw.textsize(text, font=font)
        
        box_width = text_width + (padding_x * 2) + 30 # +30 for the dot
        box_height = text_height + (padding_y * 2)
        
        x = bubble["pos"][0]
        y = bubble["pos"][1]
        
        # Prevent going off-screen on the right
        if x + box_width > img.width - 50:
            x = img.width - box_width - 50
            
        # Draw pill background
        draw.rounded_rectangle([x, y, x + box_width, y + box_height], radius=radius, fill=bg_color, outline=border_color, width=3)
        
        # Draw green dot
        dot_radius = 10
        dot_x = x + padding_x
        dot_y = y + (box_height // 2)
        draw.ellipse([dot_x - dot_radius, dot_y - dot_radius, dot_x + dot_radius, dot_y + dot_radius], fill=dot_color)
        
        # Draw text
        text_x = dot_x + dot_radius + 20
        text_y = y + padding_y - 2
        draw.text((text_x, text_y), text, font=font, fill=text_color)
        
    # Save output
    out = img.convert('RGB')
    out.save('whatsapp_renata_160.jpg', quality=95)
    print("Image saved as whatsapp_renata_160.jpg")

create_whatsapp_image()
