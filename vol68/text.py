from inky import Inky
from PIL import Image, ImageFont, ImageDraw

DEFAULT_FONT = '/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'
FONT_SIZE = 24
LINE_HEIGHT = 26

ink = Inky()
# 2値イメージの作成
image = Image.new('P',(ink.width, ink.height))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(DEFAULT_FONT, FONT_SIZE)

# 文字描画
draw.text((0, 0), "シェルスクリプト"  , font=font, fill=1)
draw.text((0,26), "マガジン"          , font=font, fill=1)
draw.text((0,52), "ゼロ・ワンシリーズ", font=font, fill=1)
draw.text((0,78), "電子ペパーモニタ"  , font=font, fill=1)
# セットして表示
ink.set_image(image)
ink.show()