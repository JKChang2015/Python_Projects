# -*- coding: UTF-8 -*-
# File name: barcode_scanner_video.py
# Created by JKChang
# 04/12/2020, 23:40
# Tag:
# Description: Real-time barcode and QR code reading with OpenCV
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default="barcodes.csv",
                help="path to output CSV file containing barcodes")
args = vars(ap.parse_args())

print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

csv = open(args["output"], "w")
found = set()

while True:
    # loop over the frames from the video stream
    # have a maximum width of 800 pixels
    frame = vs.read()
    frame = imutils.resize(frame, width=800)

    # find the barcodes in the frame and decode each of the barcodes
    barcodes = pyzbar.decode(frame)

    # loop over the detected barcodes
    for barcode in barcodes:
        # extract the bounding box location of the barcode and draw
        # the bounding box surrounding the barcode on the image
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # the barcode data is a bytes object so if we want to draw it
        # on our output image we need to convert it to a string first
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        # draw the barcode data and barcode type on the image
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(frame, text, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        # if the barcode text is currently not in our CSV file, write
        # the timestamp + barcode to disk and update the set
        if barcodeData not in found:
            csv.write("{},{}\n".format(datetime.datetime.now(),
                                       barcodeData))
            csv.flush()
            found.add(barcodeData)

    # show the output frame
    cv2.imshow("Barcode Scanner", frame)
    key = cv2.waitKey(1) & 0xFF

    # press 'q' to quit loop
    if key == ord("q"):
        break


print("[INFO] cleaning up...")
csv.close()
cv2.destroyAllWindows()
vs.stop()