from BinaryReader import BinaryReader
from Lz4ChainDecoder import Lz4ChainDecoder
import os

src = "test/test.lz4"
dst = "test/uncompressed.txt"

file1 = open(src,"rb")

br = BinaryReader(file1)
length = os.path.getsize(src)
num = 0
cpsLength = 0
decompressor = Lz4ChainDecoder()

while num < length:
	cpsLength = br.ReadInt32() & 0x7FFFFFFF
	decps = decompressor.Decode(br,cpsLength)
	num += cpsLength + 4

file1.close()

file2 = open(dst,"wb")
file2.write(bytes(decompressor.decompressed))
file2.close()