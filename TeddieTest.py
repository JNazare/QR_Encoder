from QRprepData_ak import *
alphanumeric = "0010" # Alpha-numeric mode 'b0010
text = "WHAT UP WORLD"
messageBits = GenerateMessage(alphanumeric, text)
print messageBits
