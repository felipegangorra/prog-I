import sys
import random

random.seed(0)
arq = open("dados.dat", mode="w")
num = 100_000_000
for i in range(num):
    arq.write(f"{random.randint(0, 1000000000)}\n")
