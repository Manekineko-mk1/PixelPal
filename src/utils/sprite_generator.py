from PIL import Image
import random

def generate_pet_sprite(size=32, color=None):
    """Generate a simple pixel art sprite for the pet."""
    if color is None:
        color = (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))
    
    image = Image.new('RGB', (size, size), (255, 255, 255))  # White background
    pixels = image.load()
    
    # Draw body
    for x in range(size//4, size*3//4):
        for y in range(size//4, size*3//4):
            pixels[x, y] = color
    
    # Draw eyes
    eye_color = (0, 0, 0)  # Black eyes
    pixels[size//3, size//3] = eye_color
    pixels[size*2//3, size//3] = eye_color
    
    # Draw mouth
    mouth_color = (200, 0, 0)  # Red mouth
    pixels[size//2, size//2] = mouth_color
    
    return image

def save_pet_sprite(image, filename='pet_sprite.png'):
    """Save the generated pet sprite."""
    image.save(f'resources/images/{filename}')

if __name__ == '__main__':
    pet_image = generate_pet_sprite()
    save_pet_sprite(pet_image)
    print(f"Pet sprite saved as 'resources/images/pet_sprite.png'")