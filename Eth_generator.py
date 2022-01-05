from mnemonic_utils import mnemonic_to_private_key

private_key = mnemonic_to_private_key("wheel tide pool gate have traffic behind possible lab liberty spike invite")

print("Private key is: ",private_key.hex())
print("Address for private key is: ",addr)
