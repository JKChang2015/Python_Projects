# -*- coding: UTF-8 -*-
# File name: Barcode_detector
# Created by JKChang
# 04/12/2020, 18:38
# Tag:
# Description: Detecting Barcodes in Images with Python and OpenCV

import cv2
from pyzbar import pyzbar
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

barcodes = pyzbar.decode(image)

# 循环检测到的条形码
for barcode in barcodes:
    # 提取条形码的边界框的位置
    # 画出图像中条形码的边界框
    (x, y, w, h) = barcode.rect
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # 条形码数据为字节对象，所以如果我们想在输出图像上
    # 画出来，就需要先将它转换成字符串
    barcodeData = barcode.data.decode("utf-8")
    barcodeType = barcode.type

    # 绘出图像上条形码的数据和条形码类型
    text = "{} ({})".format(barcodeData, barcodeType)
    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
# 展示输出图像
cv2.imshow("Image", image)
cv2.waitKey(0)
