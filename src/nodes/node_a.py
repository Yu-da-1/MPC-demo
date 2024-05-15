from common.key_management import generate_keys, split_secret
from common.utils import evaluate_polynomial, lagrange_interpolation
from hashlib import sha256

# メッセージのハッシュ化し、署名をしている
def sign_message(secret_share, message):
    h = sha256(message.encode()).hexdigest()
    return (secret_share * int(h, 16)) % 257

#受け取った秘密鍵のシェアとメッセージを使って分割署名を生成
def node_a_process(share, message):
    return sign_message(share[1], message)