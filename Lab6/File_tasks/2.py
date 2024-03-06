import os

file = input()

print('Exist:', os.access(file, os.F_OK))
print('Readable:', os.access(file, os.R_OK))
print('Writable:', os.access(file, os.W_OK))
print('Executable:', os.access(file, os.X_OK))