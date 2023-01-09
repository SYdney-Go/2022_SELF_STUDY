test_case = 89, 90, 100

class score:
    def __init__(self, k_score, e_score, m_score):
        self.k_score = k_score
        self.e_score = e_score
        self.m_score = m_score
    def sum(self):
        return self.k_score + self.e_score + self.m_score

if __name__ == "__main__":
    korean, english, math = test_case
    S = score(korean, english, math)
    total = S.sum()
    print("국어, 영어, 수학의 총점:", total)
    