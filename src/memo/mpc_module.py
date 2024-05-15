from ecdsa import SigningKey, NIST256p
from secretsharing import SecretSharer

# ECDSAを使用して鍵の生成
def generate_ecdsa_key():
    sk =SigningKey.generate(curve=NIST256p)
    vk = sk.get_verifying_key()
    return sk.to_string().hex(), vk.to_string().hex()

#シャミアの秘密分散を用いて秘密をシェアに分割する
def split_secret(secret, n, k):
    shares = SecretSharer.split_secret(secret, k, n)
    return shares

#鍵の生成
def handle_key_generation():
    secret_key, public_key = generate_ecdsa_key()
    print("Generated ECDSA Secret Key", secret_key)
    print("Generated ECDSA Public Key", public_key)

#秘密鍵を分割
def handle_secret_sharing(secret_key, n, k):
    shares = split_secret(secret_key, n, k)
    print("Secret shares:")
    for share in shares:
        print(share)

#秘密鍵の復元
def reconstruct_secret(shares):
    return SecretSharer.recover_secret(shares)

def main():
    secret_key = handle_key_generation()
    n = 5 #シェアの総数
    k = 3 # 復元に必要な最小シェア数
    handle_secret_sharing(secret_key, n, k)

    #秘密鍵を復元
    reconstructed_key = reconstruct_secret(shares)
    print("Reconstructed Secret Key:", reconstruct_secret)

    assert secret_key == reconstructed_key, "一致していない"

if __name__=="__main__":
    main()