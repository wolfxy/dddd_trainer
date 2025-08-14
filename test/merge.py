import onnx

if __name__ == '__main__':
    model_1 = onnx.load("E:\\aicode\\vcode_2\\vcode_1.0_46_3000_2025-07-29-15-54-42.onnx")
    model_2 = onnx.load("E:\\aicode\\vcode_3\\vcode_3_1.0_126_29000_2025-08-11-11-15-25.onnx")
    model_1_new = onnx.compose.add_prefix(model=model_1, prefix="G1_")
    model_2_new = onnx.compose.add_prefix(model=model_2, prefix="G2_")
    model_1_new.graph.input.extend(model_2_new.graph.input)
    model_1_new.graph.node.extend(model_2_new.graph.node)
    model_1_new.graph.initializer.extend(model_2_new.graph.initializer)
    model_1_new.graph.output.extend(model_2_new.graph.output)
    onnx.save(model_1_new, "D:\\Users\\wuquancheng\\Desktop\\vcode_3\\new_model.onnx")
