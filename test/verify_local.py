import ddddocr
# ocr = ddddocr.DdddOcr(show_ad = False, beta=True)
import os


m_dir = "E:\\Project\\Lifting\\dddd_trainer\\projects\\vcode_0\\models"
name = 'vcode_0_1.0_23_6000_2025-07-28-19-47-18.onnx'

m_dir = "D:\\Users\\wuquancheng\\Desktop\\vcode_4"
name = 'vcode_4_1.0_3824_2295000_2025-07-31-23-20-10.onnx'

import_onnx_path = os.path.join(m_dir, name)
charsets_path = os.path.join(m_dir, 'charsets.json')
ocr = ddddocr.DdddOcr(show_ad=False, import_onnx_path=import_onnx_path, charsets_path=charsets_path)

image_dir = os.path.join(m_dir, 'image_set')

# ocr = ddddocr.DdddOcr(show_ad=False)

# # image = open('img/5.jpg', 'rb').read()

# image = open('D:\\Users\\wuquancheng\\Desktop\\vocde\\test\\8BbX_1548a75d6cedb64980bb84af4980d94d4fb396f3.png', 'rb').read()

error_count = 0
success_count = 0
for filename in os.listdir(image_dir):
    image = os.path.join(image_dir, filename)
    code = filename[0:4]
    image = open(image, 'rb').read()
    result = ocr.classification(image)
    
    if result.lower() == code.lower():
        # print(filename, result, 'ok')
        success_count = success_count + 1
        pass
    else:
        print(filename, result, 'error')
        error_count = error_count + 1
    
print('Error count: ', error_count, 'Success count:', success_count, 'Total count:', error_count + success_count, 'Success Rate:', success_count / (success_count + error_count))
