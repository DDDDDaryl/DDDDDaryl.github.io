import os
import sys
import re

cwd = os.getcwd()
cwd = os.path.join(cwd, 'source/_posts')
re_digits = re.compile(r'(\d+)')

def embedded_numbers(s):
    pieces = re_digits.split(s)                 # 切成数字和非数字
    pieces[1::2] = map(int, pieces[1::2])       # 将数字部分转成整数
    return pieces

if __name__ == '__main__':
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print('Usage: python new.py path/to/directory.\n')
        print('Or: python new.py path/to/directory new_filename\n')
        exit(1)
    path = os.path.join(cwd, sys.argv[1])
    path = os.path.abspath(path)
    if not os.path.exists(path):
        print('Directory does not exist!!')
        exit(1)
    if len(sys.argv) == 3:
        newfile = os.path.join(path, sys.argv[2])
        if not os.path.exists(newfile):
            with open(newfile, 'w', encoding='utf-8') as f:
                f.write('---\n')
                f.write('title: ' + os.path.splitext(sys.argv[2])[0] + '\n')
                f.write('toc: true\n')
                f.write('categories:\n')
                f.write('- \n')
                f.write('tag:\n')
                f.write('- \n')
                f.write('---\n')
                f.write('\r\n\r\n<!--more-->\r\n\r\n')
                f.close()
        else:
            print('File already exists!')
    lst = os.listdir(path)
    lst = sorted(lst, key=embedded_numbers)
    name_list = []
    url_list = []
    title_list = []
    for item in lst:
        if not os.path.isdir(item):
            if item == 'Contents.md':
                continue
            name_list.append(item) # 文件名
            url_list.append('./'+item) # url
            title_list.append(os.path.splitext(item)[0]) # title


    with open(os.path.join(path, 'Contents.md'), 'w', encoding='utf-8') as f:
        print()
        f.write('---\n')
        f.write('title: 目录\n')
        f.write('categories:\n')
        f.write('- Leetcode\n')
        f.write('---\n')
        f.write('\r\n\r\n')
        f.write('# Contents \r\n')
        f.write('我的Leetcode刷题思路整理：\r\n\r\n')
        for name, url, title in zip(name_list, url_list, title_list):
            f.write('['+title+']' + '(' + url + ')' + '\r\n')
        f.close()
        print('Done.\r\n')






