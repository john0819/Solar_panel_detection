'''

    4. 计算准确率和召回率

'''

from sklearn.metrics import accuracy_score, recall_score

def calculate_metrics(y_true, y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)

    return accuracy, recall

if __name__ == "__main__":
    # 1. 根据区域点的数量生成这样的list，脏区域为全1
    y_true = [0, 0, 0, 1, 1, 1]  # 真实值：前三个区域干净，后三个区域脏
    # 2. 根据分类器结果生成 0 和 1
    y_pred = [0, 0, 1, 1, 1, 0]  # 预测结果：将第三个干净区域预测为脏，将最后一个脏区域预测为干净

    accuracy, recall = calculate_metrics(y_true, y_pred)

    print(f'准确率: {accuracy}')
    print(f'召回率: {recall}')