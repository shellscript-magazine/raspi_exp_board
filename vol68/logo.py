from inky import Inky
from PIL import Image

ink = Inky()

img = Image.open("shelllogo.png")
# サイズ変換
img = img.resize((ink.width, ink.height))
# 2値画像への変換
img = img.convert('1', dither=True)
# セットして表示
ink.set_image(img)
ink.show()