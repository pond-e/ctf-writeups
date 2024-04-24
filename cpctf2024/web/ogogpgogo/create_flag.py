# flag.pngを作るためのツールでしかなく、問題には関係ないです！！！！
from PIL import Image, ImageDraw, ImageFont
import os


def createTextImage(text: str) -> Image.Image:
    ret = Image.new("RGB", (300, 100), color=(255, 255, 255))
    ImageDraw.Draw(ret).text(
        (20, 30),
        text,
        fill=(0, 0, 0),
        font=ImageFont.truetype("GenShinGothic-Bold.ttf", 15),
    )
    return ret


if os.environ["FLAG"] is None:
    print("FLAG environment variable is not set")
    assert False


createTextImage(os.environ["FLAG"]).save("flag.png")
print("Flag created")
