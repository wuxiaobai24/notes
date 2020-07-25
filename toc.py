import os
import sys


def main():
    if len(sys.argv) < 1:
        print("python toc.py dir_path")
    dir_path = sys.argv[1]
    print(dir_path)

    title = "## {}\n\n".format(os.path.basename(dir_path))

    a = []
    for file in os.listdir(dir_path):
        name, ext = os.path.splitext(file)
        a.append("- [{}](./{})\n".format(name, file))
    
    
    print(title + "".join(a))
    with open(os.path.join(dir_path, "README.md"), 'w') as f:
        f.write(title + "".join(a))

if __name__ == "__main__":
    main()
