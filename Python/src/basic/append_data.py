import os

def read_file(fullpath):
    target_file = "/data/yaojun/MogDB-server/src/test/regress/mix"
    line_number = 0
    with open(fullpath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip('\n')
            if line.startswith("#"):
                continue
            res = "echo 'test: {}' >> {}".format(line, target_file)
            try:
                os.system(res)
                line_number += 1
                print("line %d finished!=============" % line_number)
            except Exception:
                print(Exception)


if __name__ == '__main__':
    filepath = "/data/yaojun/MogDB-server/src/test/regress/all_in_one.txt"
    read_file(filepath)