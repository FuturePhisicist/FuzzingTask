from regex_mutator_my import *

f_a = bytearray(b"asdhgfcg")
f_b = bytearray(b"")

print(fuzz(f_a, f_b, 10000).decode())