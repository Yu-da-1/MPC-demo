from common.key_management import generate_keys, split_secret
from common.utils import evaluate_polynomial, lagrange_interpolation
from hashlib import sha256

def sign_message(secret_share, message):
    h = sha256(message.encode()).hexdigest()
    return (secret_share * int(h, 16)) % 257

def node_b_process(share, message):
    return sign_message(share[1], message)