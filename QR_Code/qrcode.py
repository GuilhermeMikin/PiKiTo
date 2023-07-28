from segno import helpers

qrcode = helpers.make_mecard(
name='Pikito', 
email=('pikito.python@gmail.com', 'guilhermebalopes@ufu.br'),
phone='34991979386',
url=['https://www.youtube.com/@pikito5165/featured', 'https://www.instagram.com/pykito.ig/']
)

qrcode.save('pikitocard.png', scale=9)