from queue import Full
import numpy as np

class FullyConnectedLayer(object):
    """A simple fully-connected NN layer.
    Args:
        num_inputs (int) : 입력 벡터의 크기 / 입력 값의 개수
        layer_size (int) : 출력 벡터의 크기 / 뉴런의 개수
        activation_fn (callable) : 이 계층에 사용될 활성화 함수
    Attributes:
        W (ndarray) : 입력값에 대한 가중치
        b (ndarray) : 가중합에 더해질 편향값
        acrivation_fn (callable) : 뉴런에 적용할 활성화 함수
        """
        
    def __init__(self, num_inputs, layer_size, activation_fn):
        super().__init__()
        # 임의로 매개변수를 초기화 (정규분포)
        self.W = np.random.standard_normal((num_inputs, layer_size))
        self.b = np.random.standard_normal(layer_size)
        self.size = layer_size
        self.activation_fn = activation_fn
        
    def forward(self, x):
        """계층을 통해 입력 신호를 전달"""
        z = np.dot(x, self.W) + self.b
        return self.activation_fn(z)
    
np.random.seed(42)

# 두개의 값을 갖는 입력 칼럼 벡터
x1 = np.random.uniform(-1, 1, 2).reshape(1, 2)
print("x1 : ", x1)
x2 = np.random.uniform(-1, 1, 2).reshape(1, 2)
print("x2 : ", x2)

relu_fn = lambda y: np.maximum(y, 0)
layer = FullyConnectedLayer(2, 3, relu_fn)

# 계층은 x1이나 x2를 따로 처리할 수 있고
out1 = layer.forward(x1)
print("out1 : ", out1)
out2 = layer.forward(x2)
print("out2 : ", out2)

# 혹은 같이 처리할 수도 있다.
x12 = np.concatenate((x1, x2))
print("x12 : ", x12)
out12 = layer.forward(x12)
print("out12 : ", out12)