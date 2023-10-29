import math

class Addr(int):
    LEN = 20

    @property
    def KB(self):
        return math.ceil(self/1024)

    def __str__(self):
        return hex(self)

    @property
    def bin(self):
        return bin(self)[2:].zfill(self.LEN)

    @property
    def A19(self):
        return int(self.bin[0])

    @property
    def A18(self):
        return int(self.bin[1])

    @property
    def A17(self):
        return int(self.bin[2])
    
    @property
    def A16(self):
        return int(self.bin[3])

VALS = (
    0x10000,
    0x1ffff,
    0x20000,
    0x3ffff,
    0x40000,
    0x6ffff,
    0x80000,
    0xa0000,
    0xc0000,
    0xdffff,
    0xe0000,
    0xf0000,
)

# MEMCS	= /A19 * /A18 + A19 * A18 * A17 + /RES
F = lambda p: ((not p.A19) and (not p.A18)) or (p.A19 and p.A18 and p.A17)

# MEMCS	= /A19 * /A18 * /A17 + A19 * A18 * A17 + /RES
F = lambda p: ((not p.A19) and (not p.A18) and (not p.A17)) or (p.A19 and p.A18 and p.A17)

for v in VALS:
    p = Addr(v)
    print(p, "%3dKB" % p.KB, f"A[19..17] = [{p.A19}{p.A18}{p.A17}]", F(p) and 'D' or 'E')
