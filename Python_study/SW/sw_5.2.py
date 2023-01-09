class Multi:
    def __init__(self):
        pass
    def mutilply(self):
        result = []
        for i  in range(2, 10):
            sub_result = []
            if i % 3 == 0 or i % 7 == 0:
                continue
            for j in range(1, 10):
                if j % 3 == 0 or j % 7 == 0:
                    continue
                sub_result.append(i*j)
                
            result.append(sub_result) 
        return result

m = Multi()
print(m.mutilply())