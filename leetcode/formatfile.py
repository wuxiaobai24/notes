#/bin/python

'''
Format filename:
    Just replace space to '-'
'''
import os

def main():
    for file in os.listdir('./'):
        newfile = file.replace(' ', '-')
        if newfile != file:
            os.rename(file, newfile)

if __name__ == '__main__':
    main()
