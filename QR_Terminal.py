import pyqrcode
import os
def print_qr(link):
	link = os.getenv("URL")
	url = pyqrcode.create(link)
	print(url.terminal())
