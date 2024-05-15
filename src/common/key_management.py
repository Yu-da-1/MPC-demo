import random

# 秘密鍵の生成
def generate_keys():
    return random.randint(1, 256)

#シャミアの秘密分散方を使用して秘密鍵の分散
def split_secret(secret, threshold, num_shares):
    coeffs = [secret] + [random.randint(1, 256) for _ in range(threshold - 1)]
    shares = [(i, sum(coeff * (i ** idx) for idx, coeff in enumerate(coeffs))) for i in range(1, num_shares + 1)]
    return shares