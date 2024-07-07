from PIL import Image, ImageDraw, ImageFont
import requests
import base64
import cv2 as cv
import numpy as np
def vehicle_detect(img):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect"
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image)
    params = {"image": base64_image}
    access_token = '24.a74b77ee0d41a8a34770bfc85398a400.2592000.1722731746.282335-89936970'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    num = 0
    if response:
        data = response.json()
        #print(data)
        num = data['vehicle_num']['car']

        vehicle_results = data['vehicle_info']
        car_names = []
        print(vehicle_results)
        for vehicle_data in vehicle_results:
            location = vehicle_data.get('location', {})
            x1 = location.get('left', 0)
            y1 = location.get('top', 0)
            x2 = x1 + location.get('width', 0)
            y2 = y1 + location.get('height', 0)

            # 使用车辆的裁剪图像进行车型识别
            cropped_img = img[y1:y2, x1:x2]
            #cv.imshow('1',cropped_img)
            #cv.waitKey(0)
            _, cropped_encoded_image = cv.imencode('.jpg', cropped_img)
            base64_cropped_image = base64.b64encode(cropped_encoded_image).decode()

            car_request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/car"
            car_params = {"image": base64_cropped_image}
            car_response = requests.post(car_request_url + "?access_token=" + access_token, data=car_params,
                                         headers=headers)
            car_name = 'null'
            if car_response:
                car_data = car_response.json()

                car_result = car_data.get('result', {})
                #print(car_result)
                if car_result:
                     car_name = car_result[0]['name']

                     # 如果识别结果为'非车类'，则跳过标注
                     #if car_name != '非车类':
                     car_names.append((car_name))
                     img = cv.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
                     '''
                    # 转换OpenCV图像为PIL图像
                     pil_img = Image.fromarray(img)
                     draw = ImageDraw.Draw(pil_img)

                     # 加载中文字体文件
                     font = ImageFont.truetype('微软雅黑.ttf', 30)

                     # 使用PIL添加中文文本
                     position = (x1, y1 - 10)
                     draw.text(position, car_name, font=font, fill=(0, 0, 255))

                        # 将PIL图像转换回OpenCV格式
                     img = np.array(pil_img)

                     '''
                     position = (x1, y1 - 10)
                     img = cv.putText(img, str(car_name), position, cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                                      cv.LINE_AA)


                     with open('data/information.txt', 'a') as file:
                         file.write(
                             f"'车辆型号' {str(car_name)} \n")

        return img,num,car_names
