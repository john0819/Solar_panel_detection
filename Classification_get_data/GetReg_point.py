'''

    2. 获取矩形框内的像素值 RGB
        进行划分 block size
'''

import cv2
import numpy as np


def extract_pixels(image_path, rectangles, block_size=3):
    # 加载图片
    image = cv2.imread(image_path)

    # 注意：OpenCV读取的图像是BGR格式，需要转换为RGB格式
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    pixel_values = []

    for rectangle in rectangles:
        start_xy, end_xy = rectangle
        start_x, start_y = start_xy
        end_x, end_y = end_xy

        # 提取矩形区域内的像素
        region = image[start_y:end_y, start_x:end_x]

        # 将每块区域分割为 block_size x block_size 的小块，对每块取平均值
        shape_y = (region.shape[0] // block_size) * block_size
        shape_x = (region.shape[1] // block_size) * block_size
        region = region[:shape_y, :shape_x]
        region = region.reshape(shape_y // block_size, block_size, shape_x // block_size, block_size, 3).mean(
            axis=(1, 3))

        # 将像素值添加到列表
        pixel_values.extend(region.reshape(-1, 3).tolist())
        # 获取整数而不是浮点数（都可）
        pixel_values = [list(map(int, pixel)) for pixel in pixel_values]

    return pixel_values


image_path = 'image_test/img_3.png'
rectangles = [[(61, 99), (96, 122)], [(10, 63), (38, 90)], [(75, 81), (105, 100)], [(20, 292), (52, 317)]]
pixels = extract_pixels(image_path, rectangles, 5)
print(len(pixels))
print(pixels)

'''
测试：
img: 110 
    dirty: [[(171, 168), (215, 189)], [(172, 92), (192, 104)], [(329, 166), (385, 195)], [(333, 94), (360, 111)]]
    clean: [[(13, 75), (52, 103)], [(16, 27), (59, 52)], [(66, 104), (94, 119)], [(79, 35), (94, 56)]]

img_1:
    dirty: [[(190, 224), (197, 246)], [(53, 121), (72, 137)], [(247, 199), (261, 214)], [(108, 109), (118, 120)], [(183, 256), (197, 268)]]
    clean: [[(111, 180), (134, 198)], [(99, 254), (126, 274)], [(146, 170), (163, 185)], [(18, 93), (38, 115)]]

img_3:
    dirty: [[(186, 125), (218, 148)], [(265, 4), (288, 15)], [(194, 67), (210, 80)], [(295, 137), (315, 152)], [(278, 253), (297, 271)]]
    clean: [[(61, 99), (96, 122)], [(10, 63), (38, 90)], [(75, 81), (105, 100)], [(20, 292), (52, 317)]]


'''

'''
训练
4. 
rectangles = [[(193, 99), (207, 108)], [(137, 142), (150, 153)], [(138, 81), (151, 93)], [(168, 135), (182, 144)]]
3. 
rectangles = [[(212, 84), (225, 97)], [(207, 105), (220, 115)], [(59, 111), (67, 121)], [(49, 133), (62, 124)]]
2.
rectangles = [[(119, 64), (132, 74)], [(145, 70), (164, 79)], [(187, 76), (202, 86)], [(215, 81), (231, 88)]]
1. 
rectangles = [[(116, 63), (136, 80)], [(209, 77), (229, 92)], [(126, 150), (146, 165)], [(66, 98), (83, 108)]]


'''
