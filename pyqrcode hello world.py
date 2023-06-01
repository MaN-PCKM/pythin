import pyqrcode

# Generate QR code for a string
qr_code = pyqrcode.create('https://raw.githubusercontent.com/UncleEngineer/RaspberryPi4/main/test-iot.json')

# Save the QR code as a PNG image
qr_code.png('test_link_qr.png', scale=8)
