from PIL import Image, ImageDraw, ImageFont

# Open an image
image = "/home/yolov5/static/exp/images/stream2_0.jpg"
image = Image.open(image)

# Create an ImageDraw object
draw = ImageDraw.Draw(image)

# Define the multiline text string
multiline_text = "This is a\nmultiline text."

# Define the font to be used
font = ImageFont.truetype("Arial.ttf", size=20)

# Calculate the size of the multiline text
text_width, text_height = draw.multiline_textsize(multiline_text, font=font)

# Print the size of the multiline text
print("Text width:", text_width)
print("Text height:", text_height)
print(multiline_text)

max_width, max_height = image.size
print(max_width, max_height)

sz = image.shape
print(sz)