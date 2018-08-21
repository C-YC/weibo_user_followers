#coding:utf-8
"""
author:C-YC
target:使用正则匹配，匹配出微博用户所有关注者的所有信息
"""
import sys
import re
import os
import datetime
reload(sys)
sys.setdefaultencoding("utf-8")


def macth_wb_block(ori_str):
    contents = re.findall('<li class="follow_item S_line2" action-type="itemClick".*?>.*?</li>', ori_str)
    return contents


def match_wb_follow(contents, id):
    contents_str = ''
    for content in contents:
        contents_str += content + '\n'
        star_nickname = re.findall('<a class="S_txt1" target="_blank".*?>(.*?)</a>', content)[0]
        star_info = re.findall('<div class="info_intro">.*?<span>(.*?)</span></div>', content)
        if len(star_info) < 1:
            star_info = ['None']
        star_area = re.findall('<em class="tit S_txt2">地址</em><span>(.*?)</span>', content)
        if len(star_area) < 1:
            star_area = ['None']
        star_way = re.findall('<div class="info_from">.*?href=.*? class="from">(.*?)</a>.*?</div>', content)
        if len(star_way) < 1:
            star_way = ['None']
        star_follow_num = re.findall('<span class="conn_type">关注 <em class="count"><a target=.*?>(.*?)</a></em></span>',
                                     content)
        if len(star_follow_num) < 1:
            star_follow_num = ['None']
        star_fan_num = re.findall(
            '<span class="conn_type W_vline S_line1">粉丝<em class="count"><a target=.*?>(.*?)</a></em></span>', content)
        if len(star_fan_num) < 1:
            star_fan_num = ['None']
        star_weibo_num = re.findall(
            '<span class="conn_type W_vline S_line1">微博<em class="count"><a target=.*?>(.*?)</a></em></span', content)
        if len(star_weibo_num) < 1:
            star_weibo_num = ['None']
        star_gender = re.findall(
            '<li class="follow_item S_line2" action-type="itemClick" action-data=".*?;sex=(.*?)">.*?</li>', content)
        star_type = re.findall('<i title="(.*?)" class="W_icon.*?"></i>', content)
        if len(star_type) < 1:
            star_type = ['None']
        if star_type == ['微博达人']:
            star_type = ['None']
        star_level = re.findall('<em class=\"W_icon icon_member(.*?)\"><\/em>', content)
        if len(star_level) < 1:
            star_level = ['None']
        totle = ['<star>', '<star_nickname>'+star_nickname+'</star_nickname>', '<star_info>'+star_info[0]+'</star_info>', '<star_way>'+star_way[0]+'</star_way>', '<star_area>'+star_area[0]+'</star_area>', '<star_type>'+star_type[0]+'</star_type>', '<star_gender>'+star_gender[0]+'</star_gender>', '<star_follow_num>'+star_follow_num[0]+'</star_follow_num>', '<star_fan_num>'+star_fan_num[0]+'</star_fan_num>', '<star_weibo_num>'+star_weibo_num[0]+'</star_weibo_num>', '<star_level>'+star_level[0]+'</star_level>', '</star>']
        totle_str = ''
        for each in totle:
            totle_str += each + '\n'
        # totle_str = totle_str.strip()
        with open('../follower/'+id+'_like.txt', 'a+') as m:
            m.write(totle_str)
        # print totle_str
        # print star_nickname,
        # print star_info[0],
        # print star_way[0],
        # print star_area[0],
        # print star_type[0],
        # print star_gender,
        # print star_follow_num[0],
        # print star_fan_num[0],
        # print star_weibo_num[0],
        # print star_level[0]


def match_follower_info(data_dir):
    # 创建文件夹
    if not os.path.exists("../follower"):
        os.mkdir("../follower")
    # 创建错误日志
    if not os.path.exists("../follower_error.log"):
        f = open("../follower_error.log", 'w')
        f.write("error user\n")
        f.close()
    for path, dirs, filelist in os.walk(data_dir):
        for d in dirs:
            # 获取id
            try:
                with open(data_dir +"/" + d + '/infomation.html', 'r') as f:
                    fp = f.read().replace('\n', '')
                id = re.findall('<h1 class="username">(.*?)</h1>', fp)[0]
                print id
                # 创建文件
                with open('../follower/' + id + '_like.txt', 'w') as m:
                    m.write('<id>' + id + '</id>' + '\n' + '<follow_list>' + '\n')
                for r in range(1, 6):
                    # print r
                    with open(data_dir + '/' + d + '/like_0' + str(r) + '.html', 'r') as f:
                        fp = f.read().replace('\n', '')
                    contents = macth_wb_block(fp)
                    match_wb_follow(contents, id)
                with open('../follower/' + id + '_like.txt', 'a+') as m:
                    m.write('</follow_list>')
            except:
                f = open("../follower_error.log", "a+")
                f.write("{} error\n".format(d))
                f.close()
                print ('error, {}'.format(d))


if __name__ == '__main__':
    startime = datetime.datetime.now()
    data_dir = "../data"
    match_follower_info(data_dir)
    endtime = datetime.datetime.now()
    print endtime - startime
