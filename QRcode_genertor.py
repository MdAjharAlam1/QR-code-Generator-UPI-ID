import qrcode
import PIL

# takin input for upi id
upi_id  = input("Enter Your Upi id :- ")

#upi://pay?pa=UPI_ID&apn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
patym_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
googlepay_url = f'upi://pay??pa={upi_id}&pn=Recipient%20Name&mc=1234'

phonepe_qr = qrcode.make(phonepe_url)
patym_qr = qrcode.make(patym_url)
googlepay_qr  = qrcode.make(googlepay_url)

phonepe_qr.save('phonepe_qr.png')
patym_qr.save('patym_qr.png')
googlepay_qr.save('googl_pat.png')

phonepe_qr.show()
patym_qr.show()
googlepay_qr.show()