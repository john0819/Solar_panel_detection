'''

    1. 框选矩形框，获取坐标点

'''

import cv2

import cv2

# 初始化变量
rect_endpoint_tmp = []
drawing = False
rectangles = []  # 新增：用于存储所有的矩形

def select_rectangle(event, x, y, flags, param):
    global rect_endpoint_tmp, drawing, rectangles  # 在此处添加 rectangles

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        rect_endpoint_tmp = [(x, y)]

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            rect_endpoint_tmp[1:] = [(x, y)]

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        rect_endpoint_tmp[1:] = [(x, y)]
        rectangles.append(rect_endpoint_tmp)  # 将当前矩形添加到列表中


def main():
    # 读取图片文件
    image = cv2.imread('image_test/img_3.png')
    image_copy = image.copy()

    cv2.namedWindow('image')
    cv2.setMouseCallback('image', select_rectangle)

    while True:
        # 判断是否开始画图
        if len(rect_endpoint_tmp) == 2:
            rect_cpy = image_copy.copy()
            start_xy = tuple(map(int, rect_endpoint_tmp[0]))
            end_xy = tuple(map(int, rect_endpoint_tmp[1]))
            cv2.rectangle(rect_cpy, start_xy, end_xy, (255, 0, 0), 1)
        else:
            rect_cpy = image_copy.copy()

        cv2.imshow('image', rect_cpy)

        # 'q' 键退出
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

    print(f'所有矩形区域坐标：{rectangles}')  # 所有操作完成后打印所有的矩形

if __name__ == '__main__':
    main()

'''
区域：
img:
    dirty: [[(171, 168), (215, 189)], [(172, 92), (192, 104)], [(329, 166), (385, 195)], [(333, 94), (360, 111)]]
    clean: [[(13, 75), (52, 103)], [(16, 27), (59, 52)], [(66, 104), (94, 119)], [(79, 35), (94, 56)]]

img_1:
    dirty: [[(190, 224), (197, 246)], [(53, 121), (72, 137)], [(247, 199), (261, 214)], [(108, 109), (118, 120)], [(183, 256), (197, 268)]]
    clean: [[(111, 180), (134, 198)], [(99, 254), (126, 274)], [(146, 170), (163, 185)], [(18, 93), (38, 115)]]
    
img_3:
    dirty: [[(186, 125), (218, 148)], [(265, 4), (288, 15)], [(194, 67), (210, 80)], [(295, 137), (315, 152)], [(278, 253), (297, 271)]]
    clean: [[(61, 99), (96, 122)], [(10, 63), (38, 90)], [(75, 81), (105, 100)], [(20, 292), (52, 317)]]
    
'''
