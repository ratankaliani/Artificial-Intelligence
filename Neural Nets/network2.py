import numpy as np
import sys,re
def extractNNSpecs():
    args = sys.argv[1:]  # command line arguments
    if len(args) < 1 or re.compile("^\\d+$").search(args[-1]) is not None:
        args += [sys.argv[0] + "..\\..\\XOR.txt"]  # append the ...
    fileLoc = args[-1]  # training set location
    aTraining = open(fileLoc, "r").read().splitlines()  # make a list of the training set
    aInitial, aFinal = [], []  # We'll separate the input and output
    for idx in range(len(aTraining)):  # For each training set item
        strIn, strOut = aTraining[idx].split("=>")  # separate it into input and output
        aInitial.append([float(mynum) for mynum in re.split("\\s+,?\\s*|\\s*,?\\s+", strIn.strip())] + [
            1.0])
        aFinal.append([float(mynum) for mynum in re.split("\\s+,?\\s*|\\s*,?\\s+", strOut.strip())])
    aLayerCt = [len(aInitial[0])] + [int(n) for n in args[:-1]] + [len(aFinal[0])]

    return aInitial, aFinal, aLayerCt
def makeNPArr():
    specs = extractNNSpecs()
    xorInputOutput = {}
    inputs = []
    outputs = []
    for x in range(len(specs[0])):
        #xorInputOutput[(specs[0][x][0], specs[0][x][1], specs[0][x][2])] = specs[1][x][0]
        inputs.append([specs[0][x][0], specs[0][x][1]])
        outputs.append(specs[1][x][0])
    #print(inputs)
    #print(outputs)
    return inputs,outputs
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


def sigmoid_prime(x):
    return sigmoid(x) * (1.0 - sigmoid(x))


def tanh(x):
    return np.tanh(x)


def tanh_prime(x):
    return 1.0 - x ** 2


class NeuralNetwork:
    def __init__(self, layers, activation='tanh'):
        if activation == 'sigmoid':
            self.activation = sigmoid
            self.activation_prime = sigmoid_prime
        elif activation == 'tanh':
            self.activation = tanh
            self.activation_prime = tanh_prime

        # Set weights
        self.weights = []
        # layers = [2,2,1]
        # range of weight values (-1,1)
        # input and hidden layers - random((2+1, 2+1)) : 3 x 3
        for i in range(1, len(layers) - 1):
            r = 2 * np.random.random((layers[i - 1] + 1, layers[i] + 1)) - 1
            self.weights.append(r)
        # output layer - random((2+1, 1)) : 3 x 1
        r = 2 * np.random.random((layers[i] + 1, layers[i + 1])) - 1
        self.weights.append(r)

    def fit(self, X, y, learning_rate=0.1, epochs=100000):
        # Add column of ones to X
        # This is to add the bias unit to the input layer
        ones = np.atleast_2d(np.ones(X.shape[0]))
        X = np.concatenate((ones.T, X), axis=1)

        for k in range(epochs):
            i = np.random.randint(X.shape[0])
            a = [X[i]]

            for l in range(len(self.weights)):
                dot_value = np.dot(a[l], self.weights[l])
                activation = self.activation(dot_value)
                a.append(activation)
            # output layer
            error = y[i] - a[-1]
            deltas = [error * self.activation_prime(a[-1])]

            # we need to begin at the second to last layer
            # (a layer before the output layer)
            for l in range(len(a) - 2, 0, -1):
                deltas.append(deltas[-1].dot(self.weights[l].T) * self.activation_prime(a[l]))

            # reverse
            # [level3(output)->level2(hidden)]  => [level2(hidden)->level3(output)]
            deltas.reverse()

            # backpropagation
            # 1. Multiply its output delta and input activation
            #    to get the gradient of the weight.
            # 2. Subtract a ratio (percentage) of the gradient from the weight.
            for i in range(len(self.weights)):
                layer = np.atleast_2d(a[i])
                delta = np.atleast_2d(deltas[i])
                self.weights[i] += learning_rate * layer.T.dot(delta)

            if k % 10000 == 0: print('epochs:', k)

    def predict(self, x):
        a = np.concatenate((np.ones(1).T, np.array(x)), axis=0)
        for l in range(0, len(self.weights)):
            a = self.activation(np.dot(a, self.weights[l]))
        return a


if __name__ == '__main__':
    makeNPArr()
    nn = NeuralNetwork([2, 2,2, 1])
    X,y = makeNPArr()
    print(len(X))
    print(len(y))
    # X = np.array([[0, 0],
    #               [0, 1],
    #               [1, 0],
    #               [1, 1]])
    # y = np.array([0, 1, 1, 0])
    nn.fit(np.array(X), np.array(y))
    right=0
    wrong=0
    for e in range(len(X)):
        est=nn.predict(X[e])
        real = y[e]
        if (est>1 and 1>real>0) or (1>est>0 and 1>real):
            wrong+=1
    print(wrong)

    # for e in X:
    #     print(e, nn.predict(e))