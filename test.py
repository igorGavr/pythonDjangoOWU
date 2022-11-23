import os

# print(os.uname())
# print(os.environ)
# os.system('htop')
# print(os.getcwd())

# print(os.listdir())
# os.mkdir('first')
# os.mkdir('second')
# c:\folder\222\1.txt
# /folder
# print(os.path.join('folder', '222', '1.txt'))

# os.rename('test2.py', os.path.join('first', 'test.py'))
for root, folder, files in os.walk('.'):
    print(f'{root=} {folder=} {files=}')