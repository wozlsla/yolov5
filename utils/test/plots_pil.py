# import torch
# import pathlib

# font_url = "https://ultralytics.com/assets/Arial.ttf"
# font_filename = "Arial.ttf"
# # path = "."

# # Download the font file
# torch.hub.download_url_to_file(font_url, font_filename)

# # Confirm the file download
# if not pathlib.Path(font_filename).is_file():
#     print("Failed to download the font file.")
# else:
#     print("Font file downloaded successfully.")

# # Optional: Clean up the font file from the destination folder
# # os.remove(font_file)
# ------------------------------------------------------------------------------

from PIL import Image, ImageDraw, ImageFont

textbound = 100
start_color = (0, 0, 255)  # blue
end_color = (255, 0, 0)  # red
step = 5  # Level 5


# Function to find color between two colors
def interpolate_color(color1, color2, step, steps):
    r1, g1, b1 = color1
    r2, g2, b2 = color2

    r = int(r1 + (r2 - r1) * step / steps)
    g = int(g1 + (g2 - g1) * step / steps)
    b = int(b1 + (b2 - b1) * step / steps)

    return (r, g, b)


# Text Area Draw
def draw_text(image, texts, rectangle, border_width, font_path, font_size, step_value):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)

    font_highlight = ImageFont.truetype(font_path, font_size)

    # texts = texts.reverse()
    max_width, max_height = image.size
    line_height = font.getsize("A")[1]  # 폰트의 높이

    multi_text = ""
    # position = (rectangle[2], rectangle[1])  # 50-LB_x, 150-RT_y (LT coords)
    # position = (rectangle[2], rectangle[1])  # 50, 150
    position = (rectangle[0], rectangle[1])  # 50, 200

    y = rectangle[1]  # 150

    for text in reversed(texts):
        if multi_text != "":
            multi_text += "\n"
        multi_text += text

    offset = border_width + 3

    # calculate the size (width and height) of a multiline text string before drawing it on an image.
    text_width, text_height = draw.multiline_textsize(multi_text, font=font)

    # 텍스트의 가로 크기를 벗어나면 좌측 모서리에 우측 정렬
    if rectangle[0] + rectangle[2] + text_width > max_width:  # x1 + x2 + text_width > img_width
        if rectangle[1] + text_height > max_height:
            position = (rectangle[0] - text_width - offset, max_height - text_height - 7)
        else:
            position = (rectangle[0] - text_width - offset, y)
        align = "right"
    else:
        if rectangle[1] + text_height > max_height:
            position = (rectangle[2] + offset, max_height - text_height - 7)
        else:
            position = (rectangle[2] + offset, y)
        align = "left"

    # 텍스트의 색상 계산
    text_color = interpolate_color(start_color, end_color, step_value, step)

    # 텍스트 highlight
    # draw.multiline_text(position, multi_text, font=font, align=align, stroke_width=1, fill=(255, 255, 255),spacing=2)
    # for i in range(3):
    #     draw.multiline_text(
    #         (position[0] - i - 1, position[1]), multi_text, font=font, align=align, fill=(255, 255, 255)
    #     )
    # for i in range(3):
    #     draw.multiline_text(
    #         (position[0], position[1] - i - 1), multi_text, font=font, align=align, fill=(255, 255, 255)
    #     )
    draw.multiline_text(position, multi_text, font=font, align=align, fill=text_color)


# Bounding Box, Caption Draw
def draw_rectangle_with_text(
    image, rectangle, border_width, caption, texts, font_path, font_size, box_step_value, text_step_value
):
    title = "caption"

    draw = ImageDraw.Draw(image)
    box_border_color = interpolate_color((255, 0, 0), end_color, box_step_value, step)
    draw.rectangle(rectangle, outline=box_border_color, width=border_width)  # tagging bbox
    # draw.rectangle((50, 100, 200, 200), outline=(0, 255, 0), width=border_width)  # (x1, y1, ) G
    # draw.rectangle((100, 150, 200, 200), outline=(0, 0, 255), width=border_width)  # B

    # box_rect = (rectangle[0], rectangle[1], rectangle[2], rectangle[1] + 20)
    # draw.rectangle(box_rect, fill=box_border_color)
    font = ImageFont.truetype(font_path, font_size)
    # for i in range(2): # caption
    # draw.text((rectangle[2] + i + 2, rectangle[1] - 1), title, font=font, fill=(255, 255, 255))
    draw_text(image, texts, rectangle, border_width, font_path, font_size, text_step_value)


image_path = "/home/yolov5/static/exp/images/stream2_0.jpg"

# 사각형 좌표(Bounding Box)
# rectangle = (100, 150, 50, 200)  # org RT : x1, y1, LB : x2, y2
rectangle = (50, 150, 100, 200)  # LT : x1, y1, RB : x2, y2 defualt !!
rectangle = (250, 200, 500, 300)
# rectangle = (50, 200, 100, 150)
# rectangle = (50, 100, 150, 200)

# 텍스트 내용
texts = [
    "Object: PersonPersonPersonPersonPerson",
    "Size: 50 * 50",
    "Distance: 35",
    "Status: Normal",
    "Object: Person",
    "Size: 50 * 50",
    "Distance: 35",
    "Status: Normal",
    "Object: Person",
    "Size: 50 * 50",
    "Distance: 35",
    "Status: Normal",
]

# 폰트 파일 경로
# font_path = "arial.ttf"  # "malgun.ttf" #한글
# font_path = "Arial.Unicode.ttf"
font_path = "Arial.ttf"
font_path = "/home/dataset/yolov5/Arial.ttf"


# 폰트 크기
font_size = 16
box_step_value = 9
text_step_value = 2
border_width = 4
caption = "person"
image = Image.open(image_path)
draw_rectangle_with_text(
    image, rectangle, border_width, caption, texts, font_path, font_size, box_step_value, text_step_value
)
# image.show() # window
image.save("sample_0.jpg")