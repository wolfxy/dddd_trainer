
import torch

if __name__ == '__main__':
    charset = ' 0123456789abcdefjhijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lst = list(charset)
    print(lst)
    # path = "D:\\Users\\wuquancheng\\Desktop\\vcode_3\\checkpoint_vcode_3_126_29000.tar"
    # param = torch.load(path, map_location=torch.device('cpu'))
    # print(param)

    # onnx_model = onnx.load('E:\\aicode\\vcode_3\\vcode_3_1.0_65_15000_2025-07-29-16-13-21.onnx')
    # print(onnx_model.state_dict())
    # from onnx2torch import convert
    # pytorch_model = convert(onnx_model)
    # state_dict = pytorch_model['net']
    # # optimizer = param['optimizer']
    # print(pytorch_model)
