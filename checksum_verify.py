hexinput = '0x'+input('Input hex checksum to verify:')
hexinput = "".join(hexinput.split())
quads = [int(hexinput[i:i+4],16) for i in range(2, len(hexinput), 4)]
sumstuff = sum(quads)
if len(hex(sumstuff)) > 6:
  manip = str(hex(sumstuff))
  sumstuff = int(manip[2],16)+int(manip[3:],16)

print("Sum of 16bit groups is: "+ (hex(sumstuff))[2:])
if str((hex(sumstuff))[2:]) == 'ffff' :
  print("No Error")
else:
  print("Error")
