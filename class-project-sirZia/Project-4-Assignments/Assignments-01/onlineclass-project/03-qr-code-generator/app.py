import qrcode
data = 'Qr code generator'
img = qrcode.make(data)
with open('D:\learning\Quarter-3-python\class-project-sirZia\Project-4-Assignments\Assignments-01\onlineclass-project\qr-code-generator/abc.png', 'wb') as f:
    img.save(f)





















# pip install qrcode
#just run play btn and code generate
# if need
    # pip install qrcode[pil]