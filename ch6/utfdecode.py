bArr = b'\xe2\x82\xb9'
bArr1 = b'\x20\xb9'

bArr2 = bytearray()

bArr2 += (72).to_bytes(1, 'little')

print(bArr2)
print(bArr2.hex())

# strTxt =  bArr1.decode("utf-16be")
strTxt =  bArr2.decode("utf-8")

print(strTxt)


var = 8377



bArr4 = var.to_bytes(2, 'little')

print(bArr4)
print(bArr4.hex())

strTest = bArr4.decode("utf-16le")
print("strTest: " + strTest)
