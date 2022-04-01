import numpy as np

class LogisiticRegression():
    def __init__(self, learning_rate, n_iterations):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations

    def logistic(self, W, X, b):
        return 1 / (1 + np.exp(-(W.dot(X) + b)))

    def fit(self, X, Y):
        # m = no. of training examples
        # n = no. of features
        self.m, self.n = X.shape

        self.X = X
        self.Y = Y
        self.W = np.zeros(self.n)
        self.b = 0

        # Graident descent
        for _ in range(self.n_iterations):
            self.train()

    def train(self):
        A = self.logistic(self.W, self.X, self.b)

        self.W = self.W - self.learning_rate * dW
        self.b = self.b - self.learning_rate * db
