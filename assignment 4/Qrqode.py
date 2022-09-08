#in the name of god

import qrcode
qr_text = input('Enter the desired text : ')
qr_address = input('Enter the desired address : ')

Qr =qrcode.make(qr_text)
Qr.save(qr_address)
