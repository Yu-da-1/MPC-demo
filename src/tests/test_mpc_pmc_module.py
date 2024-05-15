import pytest
from memo.mpc_module import generate_ecdsa_key, split_secret, reconstruct_secret

def test_generate_ecdsa_key():
    secret_key, public_key = generate_ecdsa_key()
    assert len(secret_key) > 0
    assert len(public_key) > 0

def test_split_secret():
    secret_key, _ = generate_ecdsa_key()
    shares = split_secret(secret_key, 5, 3)
    assert len(shares) == 5, "5つのシェアが生成されること"
    
    print("Generated shares:")
    for share in shares:
        print(share)
        
def test_secret_sharing_and_reconstruction():
    secret_key, _ = generate_ecdsa_key()
    n = 5
    k = 3
    shares = split_secret(secret_key, n, k)
    assert len(shares) == n, "正しい数のsharesを生成する必要がある"

    reconstructed_key = reconstruct_secret(shares[:k])
    assert secret_key == reconstructed_key, "一致していない"