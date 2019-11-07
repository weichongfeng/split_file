# -*- coding=utf-8 -*-

import os,math


def split_file(file_path,file_num,save_path):
    # 获取要分割的文件大小
    file_size = get_file_size(file_path,file_num)
    # 获取文件名称,扩展名
    file_name,file_ext_name = os.path.splitext(os.path.basename(file_path))

    try:
        # 打开文件
        file_obj = open(file_path, 'r')
        # 分割文件
        size = 0
        for index in range(1, file_num + 1):
            new_file = open((save_path + '/' + file_name + str(index) + file_ext_name),'a')
            while size < index * file_size:
                content = file_obj.read(1024 * 1024)
                new_file.write(content)
                size += 1024 * 1024
            new_file.close()
    except:
        return False
    else:
        file_obj.close()
        return True

def get_file_size(file_path,file_num):
    # 获取要分割的文件大小
    file_size = os.path.getsize(file_path)
    return math.ceil(int(file_size)/int(file_num))

