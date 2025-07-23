import cv2
import os
import sys


def image_to_gray(dir):
    index = 0
    for filename in os.listdir(dir):
        f = os.path.join(dir, filename)
        img = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
        cv2.imwrite(f, img)
        index = index + 1
        print(f'{index} {f}')


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('缺少文件夹参数')
        exit()
    dir = sys.argv[1]
    print(dir)
    if not os.path.exists(dir):
        print(f'文件夹{dir}不存在')
    image_to_gray(dir=dir)
