# -*- coding: UTF-8 -*-
# File name: qrcode
# Created by JKChang
# 01/06/2020, 18:25
# Tag:
# Description: 

from MyQR import  myqr

myqr.run('https://github.com/JKChang2015', picture='./resources/shy.png',colorized=True,save_name='linkedin.png',save_dir='./results/')

'''
version, level, qr_name = myqr.run(
words,  str，输入链接或者句子作为参数
version = 1, int，控制边长，范围是1到40，数字越大边长越大,默认边长是取决于你输入的信息的长度和使用的纠错等级
level = 'H', str，控制纠错水平，范围是L、M、Q、H，从左到右依次升高，默认纠错等级为'H'
picture = None, str，将QR二维码图像与一张同目录下的图片相结合，产生一张黑白图片
colorized = False, bool，使产生的图片由黑白变为彩色的
contrast = 1.0, float，调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0
brightness = 1.0, float，调节图片的亮度，其余用法和取值与 contrast 相同
save_name = None, str，默认输出文件名是"qrcode.png"
save_dir = os.getcwd() str，默认存储位置是当前目录
)
'''