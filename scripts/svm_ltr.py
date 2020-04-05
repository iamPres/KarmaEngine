from tqdm import tqdm
import numpy as np
from sklearn.metrics import accuracy_score


print("-------------------------------------")
choice = input("Train or Test: ")
print("-------------------------------------")

if choice == "Train":
    epochs = 10000

    print("Serializing Data...")

    file = open('train.txt')
    data = file.read().splitlines()
    data = data[:100]
    file.close()

    features = []
    query = []

    alpha = np.full(136, 0.0001)
    weights = np.zeros((len(data), 136))
    output = np.zeros((len(data), 136))
    score = np.zeros((len(data), 136))

    for i in tqdm(range(len(data))):
        elements = data[i].split(' ')
        if int(elements[0]) < 3:
            score[i] = [-1] * 136
        else:
            score[i] = [1] * 136

        query.append(int(elements[1].split(':')[1]))
        features.append([float(feature.split(':')[1]) for feature in elements[2:138]])

    features = np.asarray(features)

    print("-------------------------------------")

    print("Training Initialized...")

    for i in tqdm(range(epochs)):
        for sample in range(len(data)):
            output[sample] = weights[sample]*features[sample]
            output[sample] = np.full((136), np.sum(output[sample]))

        output = output*score

        count = 0
        for val in output:
            if(val[0] >= 1):
                cost = 0
                weights = weights - alpha * (2 * 1/epochs * weights)
            else:
                cost = 1 - val[0]
                weights = weights + alpha * (features[count] * score[count] - 2 * 1/epochs * weights)

            count += 1

    out_file = open('weights.txt', 'a+')
    for i in weights[0]:
        out_file.write(str(i)+'\n')
    out_file.close()

elif choice == "Test":

    print("Serializing Data...")

    file = open('train.txt')
    data = file.read().splitlines()
    data = data[100:200]
    file = open('weights.txt', 'r').read().splitlines()
    weights = np.zeros((len(data), 136))
    for i in range(len(weights)):
        weights[i] = file
    features = []
    query = []
    output = np.zeros((len(data), 136))
    score = np.zeros((len(data), 136))

    for i in tqdm(range(len(data))):
        elements = data[i].split(' ')
        if int(elements[0]) < 3:
            score[i] = np.full(136, -1)
        else:
            score[i] = np.full(136, 1)

        query.append(int(elements[1].split(':')[1]))
        features.append([float(feature.split(':')[1]) for feature in elements[2:138]])

    features = np.asarray(features)

    for sample in range(len(data)):
        output[sample] = weights[sample]*features[sample]
        output[sample] = np.full((136), np.sum(output[sample]))

    predictions = []
    for val in output:
        if(val[0] > 1):
            predictions.append(1)
        else:
            predictions.append(-1)
    print("-------------------------------------")
    print("Predicting...")
    print("-------------------------------------")
    print("Prediction finished with "+str(accuracy_score(score[:,0], predictions)*100)+"% accuracy.")
