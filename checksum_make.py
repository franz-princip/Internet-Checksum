hexinput = '0x'+input('Input hex to add checksum:')
hexinput = "".join(hexinput.split())
quads = [int(hexinput[i:i+4],16) for i in range(2, len(hexinput), 4)]
sumstuff = hex(sum(quads))
print(sumstuff)
if len(sumstuff) > 6:
  manip = str(sumstuff)
  sumstuff = hex(int(manip[2],16)+int(manip[3:],16))
print("16 bit ops sum : " + sumstuff)
print("1's complement (the checksum) is: " + hex(int(sumstuff,16) ^ 0xffff)[2:])
