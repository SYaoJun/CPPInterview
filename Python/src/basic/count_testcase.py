import os
"""
从一个文件按行读入替换掉另一个文件中的单词
"""

def read_file(fullpath):
    line_number = 0
    with open(fullpath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip('\n')
            if line.startswith("#") or line.find("/") != -1:
                continue
            words_path = "/data/yaojun/MogDB-server/src/test/regress/mix"
            temp_words_path = "/data/yaojun/MogDB-server/src/test/regress/temp_mix.txt"
            res = "sed 's/{}//g' {} > {}".format(line, words_path, temp_words_path)
            try:
                os.system(res)
                line_number += 1
                mv_cmd = "mv -f {} {}".format(temp_words_path, words_path)
                os.system(mv_cmd)
                print("line %d finished!=============" % line_number)
            except Exception:
                print(Exception)
                print(line)


if __name__ == '__main__':
    filepath = "/data/yaojun/MogDB-server/src/test/regress/all_in_one.txt"
    read_file(filepath)
