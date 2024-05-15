from nodes.node_a import node_a_process
from nodes.node_b import node_b_process
from nodes.node_c import node_c_process
from common.key_management import generate_keys, split_secret
from common.utils import lagrange_interpolation, verify_signature

def adjust_signature_range(signature, modulus):
    return (signature % modulus + modulus) % modulus

def main():
    secret_key = generate_keys()
    shares = split_secret(secret_key, 3, 3)
    message = "Hello, MPC!"

    sig_a = node_a_process(shares[0], message)
    sig_b = node_b_process(shares[1], message)
    sig_c = node_c_process(shares[2], message)

    full_signature = lagrange_interpolation([1, 2, 3], [sig_a, sig_b, sig_c])
    full_signature = adjust_signature_range(full_signature, 257)

    public_key = secret_key
    is_valid = verify_signature(public_key, message, full_signature)

    print(f"Full Signature: {full_signature}")
    print(f"Signature Valid: {is_valid}")

if __name__ == "__main__":
    main()