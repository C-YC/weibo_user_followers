#coding:utf-8
"""
author:C-YC
target:对存储好的关注数据进行去重处理
"""
import sys
import re
import os
reload(sys)
sys.setdefaultencoding("utf-8")


def demo_follower(useful_follower):
    for follower in useful_follower:
        with open('../demo.txt', 'a+') as m:
            m.write(follower + '\n')


def re_write(id):
    with open('../de_follower/' + id + '.txt', 'w+')as m:
        m.write('<id>' + id + '</id>' + '\n' + '<follow_list>' + '\n')
    with open('../demo.txt', 'r') as n:
        all_lines = n.readlines()
        for all_line in all_lines:
            lines = all_line.replace('<star>', '<star>\n').replace('</star_nickname>',
                                                                   '</star_nickname>\n').replace(
                '</star_info>', '</star_info>\n').replace('</star_way>', '</star_way>\n').replace('</star_area>',
                                                                                                  '</star_area>\n')
            line = lines.replace('</star_type>', '</star_type>\n').replace('</star_gender>','</star_gender>\n').replace(
                '</star_follow_num>', '</star_follow_num>\n').replace('</star_fan_num>', '</star_fan_num>\n')
            l = line.replace('</star_weibo_num>', '</star_weibo_num>\n').replace('</star_level>',
                                                                                 '</star_level>\n')
            with open('../de_follower/'+id+'.txt', 'a+') as a:
                a.write(l)
    with open('../de_follower/' + id + '.txt', 'a+') as f:
        f.write('</follow_list>')


def main_follow_info():
    # 创建文件夹，存储去重后的数据
    if not os.path.exists("../de_follower"):
        os.mkdir("../de_follower")
    # 创建错误日志
    if not os.path.exists("../follower_error.log"):
        f = open("../follower_error.log", 'w')
        f.write("error user\n")
        f.close()
    # 需要去重的数据的文件夹路径
    path = r'../follower'
    for i in os.walk(path):
        for r in range(8):
            with open('../follower/' + i[2][r]) as f:
                fp = f.read().replace('\n', '')
                pre_id = re.findall('<id>(.*?)</id>', fp)
                id = pre_id[0]
                with open('../de_follower/' + id + '.txt', 'w')as m:
                    m.write('')
                all_follower = re.findall('<star>.*?</star>', fp)
                useful_follower = set(all_follower)
                with open('../demo.txt', 'w') as n:
                    n.write('')
                if len(all_follower) > len(useful_follower):
                    demo_follower(useful_follower)
                    re_write(id)
                else:
                    with open('../follower/'+i[2][r], 'r') as fs:
                        fp = fs.readlines()
                        for line in fp:
                            with open('../de_follower/'+id+'.txt', 'a+')as n:
                                n.write(line)


if __name__ == '__main__':
    main_follow_info()

