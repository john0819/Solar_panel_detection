'''

    临时：把RGB转换为HSV

'''

import cv2

def convert_rgb_to_hsv(image_path):
    # 加载图片
    image = cv2.imread(image_path)

    # 将图片从BGR格式转换为HSV格式
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    return hsv_image

hsv_image = convert_rgb_to_hsv('image/img_3.png')
cv2.imshow("test", hsv_image)
cv2.waitKey(0)
