from segno import helpers

# data = "https://www.youtube.com/@pikito5165/featured"

# qrcode = segno.make(data)
# qrcode.save('qr.png', scale=9)


qrcode = helpers.make_mecard(name='Pikito', 
                             email=('pikito.python@gmail.com', 'guilhermebalopes@ufu.br'),
                             phone='34991979386',
                             url=['https://www.youtube.com/@pikito5165/featured', 'https://www.instagram.com/pykito.ig/'])
qrcode.save('pikitocontact.png', scale=5)