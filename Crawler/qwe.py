from PIL import Image, ImageDraw

# Create a new image with a white background
image = Image.new('RGB', (200, 200), 'white')

# Get a drawing context
draw = ImageDraw.Draw(image)

# Draw the head
draw.ellipse((50, 20, 150, 120), fill='lightgrey')

# Draw the ears
draw.polygon((20, 40, 50, 20, 50, 60), fill='lightgrey')
draw.polygon((150, 40, 180, 20, 180, 60), fill='lightgrey')

# Draw the eyes
draw.ellipse((70, 50, 90, 70), fill='black')
draw.ellipse((110, 50, 130, 70), fill='black')

# Draw the nose
draw.polygon((95, 75, 105, 95, 85, 95), fill='black')

# Draw the mouth
draw.arc((85, 100, 115, 110), 0, 180, fill='black')

# Display the image
image.show()
