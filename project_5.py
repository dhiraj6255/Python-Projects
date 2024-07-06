# QRcode using python

import qrcode as qr
img = qr.make("https://github.com/dhiraj6255")
img.save("Diraj_github_profile.png")