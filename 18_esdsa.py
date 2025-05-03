from ecdsa import SigningKey, SECP256k1, util
import hashlib

# Generate a private key
private_key = SigningKey.generate(curve=SECP256k1)

# Get the public key from the private key
public_key = private_key.get_verifying_key()

# Message to be signed
message = b"Hello, world!"

# Sign the message using the private key (default method)
signature = private_key.sign(message)

# Verify the signature with the public key
assert public_key.verify(signature, message)

# Hash the message with SHA-256 (as Bitcoin does)
hashed_message = hashlib.sha256(message).digest()

# ---- Option 1: Get DER-encoded signature and decode r, s ----
der_signature = private_key.sign_digest(
    hashed_message, sigencode=util.sigencode_der_canonize
)

# Decode r and s from DER signature
r1, s1 = util.sigdecode_der(der_signature, private_key.privkey.order)
print("DER-encoded signature (hex):", der_signature.hex())
print("Decoded r:", hex(r1))
print("Decoded s:", hex(s1))

# ---- Option 2: Get raw r and s directly ----
r_bytes, s_bytes = private_key.sign_digest(
    hashed_message, sigencode=util.sigencode_strings
)

print("Raw r (hex):", r_bytes.hex())
print("Raw s (hex):", s_bytes.hex())

