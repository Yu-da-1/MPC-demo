from hashlib import sha256
from sympy import symbols, prod

def evaluate_polynomial(coeffs, x):
    return sum(coeff * (x ** i) for i, coeff in enumerate(coeffs))

#ラグランジュ保管を使用して与えられた点から多項式を保管し、X=0での多項式の値(秘密鍵)を復元する
def lagrange_interpolation(x_values, y_values):
    x = symbols('x')
    lagrange_poly = sum(
        y_values[i] * prod((x - x_values[j]) / (x_values[i] - x_values[j]) for j in range(len(x_values)) if i != j)
        for i in range(len(x_values))
    )
    return lagrange_poly.subs(x, 0)
x_values = [1, 2, 3]
y_values = [146, 15, 35]  # この部分は実際の分割署名に置き換えてください
print("Lagrange Interpolation Result:", lagrange_interpolation(x_values, y_values))

def sign_message(secret_share, message):
    h = sha256(message.encode()).hexdigest()
    return (secret_share * int(h, 16)) %257

#署名の検証
def verify_signature(public_key, message, signature):
    h = sha256(message.encode()).hexdigest()
    excepted_signature = (public_key * int(h, 16)) % 257
    return excepted_signature == signature

public_key = 123  # 実際の公開鍵に置き換えてください
message = "Hello, MPC!"
full_signature = 298  # 実際の全体の署名に置き換えてください
print("Verification for Full Signature:", verify_signature(public_key, message, full_signature))