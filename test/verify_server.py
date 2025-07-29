import requests
import base64
import os
d = r'D:\\Users\\wuquancheng\\Downloads\\打码正常'

error_count = 0
success_count = 0
for filename in os.listdir(d):
    image = os.path.join(d, filename)
    code = filename[0:4]
    with open(image, "rb") as f:
        image_data = base64.b64encode(f.read()).decode()
    server = 'https://ocr.yoyorpa.com'
    response = requests.post(f"{server}/ocr", json={"image": image_data})
    result = response.json()
    result = result["data"]["text"]
    if result.lower() == code.lower():
        # print(filename, result, 'ok')
        success_count = success_count + 1
        pass
    else:
        print(filename, result, 'error')
        error_count = error_count + 1
    
print('Error count:', error_count, 'Success count:', success_count, 'Total count:', error_count + success_count, 'Success Rate:', success_count / (success_count + error_count))
