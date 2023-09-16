from PIL import Image, ImageDraw, ImageFont
import socket
import ctypes
import os
import getpass
from datetime import datetime

moment_now = datetime.now()
moment_formatted = moment_now.strftime("%d/%m/%Y %H:%M:%S") # pt-BR format

user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

image = Image.new("RGB", (screen_width, screen_height), "darkblue")

ip = socket.gethostbyname(socket.gethostname())

username = getpass.getuser()

font = ImageFont.truetype("arial.ttf", 25)

draw = ImageDraw.Draw(image)
text_width = int(25)
text_height = int(25)
text_x = (screen_width - text_width) // 2 * (1.60)
text_y = (screen_height - text_height) // 2 * (0.10)
draw.text((text_x, text_y), 'IP      : ' + ip, font=font, fill="white")

text_y += text_height + 10
draw.text((text_x, text_y), 'User  : ' + username, font=font, fill="white")

text_y += text_height + 20
draw.text((text_x, text_y), 'Since : ' + moment_formatted, font=font, fill="white")

actual_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(actual_path, "dinamyc_wallpaper_temp.png")
image.save(image_path)

# set background
ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
