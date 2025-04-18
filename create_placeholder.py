from PIL import Image, ImageDraw

# Create a new image with a white background
size = (200, 200)
img = Image.new('RGB', size, 'white')
draw = ImageDraw.Draw(img)

# Draw a gray circle for the avatar
circle_color = '#E0E0E0'
draw.ellipse([40, 40, 160, 160], fill=circle_color)

# Draw a lighter gray circle for the head
head_color = '#F5F5F5'
draw.ellipse([70, 60, 130, 120], fill=head_color)

# Draw the body
body_color = '#F5F5F5'
draw.ellipse([70, 100, 130, 180], fill=body_color)

# Save the image
img.save('neo infra/app/static/images/avatar-placeholder.png', 'PNG') 