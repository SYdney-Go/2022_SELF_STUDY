import numpy as np

class Nueron(object):
    """"간단한 전방 전달 인공 뉴런
    Args:
        num_inputs (int): 입력 벡터 크기 / 입력 값 개수.
        activation_fn (callable): 활성화 함수.
        
    Attributes:
        W (ndarray) : 각 입력에 대한 가중치.
        b (float) : 편향값, 가중합에 더해짐
        activation_fn (callable) : 활성화 함수.
    """
    
    def __init__(self, num_inputs, activation_fn):
        super().__init__()
        # 랜덤값으로 가중치 벡터와 편향값을 초기화함:
        self.W = np.random.rand(num_inputs)
        self.b = np.random.rand(1)
        self.activation_fn = activation_fn
        
    def forward(self, x):
        """뉴런을 통해 입력 신호를 전달"""
        z = np.dot(x, self.W) + self.b
        return self.activation_fn(z)
    
# 결과를 복제할 수 있도록 랜덤 숫자 생성기의 시드 값을 고정
np.random.seed(42)
# 3개의 랜덤 입력을 갈럼으로 받을 수 있는 배열 생성
x = np.random.rand(3).reshape(1, 3)
print(x.size)
# 활성화 함수로 계단함수 정의, threshold 0.5
step_fn = lambda y: 0 if y <= 0 else 1
perceptron = Nueron(num_inputs=x.size, activation_fn=step_fn)
print("perceptron.W : ", perceptron.W)
print("perceptron.b : ", perceptron.b )
out = perceptron.forward(x)
print("out : ", out)