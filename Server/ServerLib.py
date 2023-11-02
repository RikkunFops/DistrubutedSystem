from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
import socket




# Create Diffie-Hellman parameters (server)
parameters = dh.generate_parameters(generator=2, key_size=2048)
private_key_server = parameters.generate_private_key()
public_key_server = private_key_server.public_key()

# Serialize the server's public key and parameters
dh_params_server = parameters.parameter_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)
dh_public_key_server = public_key_server.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)

# Simulate the client's side
parameters_client = dh.generate_parameters(generator=2, key_size=2048)
private_key_client = parameters_client.generate_private_key()
public_key_client = private_key_client.public_key()

# Serialize the client's public key and parameters
dh_params_client = parameters_client.parameter_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)
dh_public_key_client = public_key_client.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)

# Exchange public keys and parameters (simulated network communication)
# In a real system, you would send the client's public key to the server and vice versa

# Server receives the client's public key and parameters
received_dh_params_client = serialization.load_pem_parameters(dh_params_client)
received_public_key_client = received_dh_params_client.generate_private_key()
shared_key_server = private_key_server.exchange(received_public_key_client.public_key())

# Client receives the server's public key and parameters
received_dh_params_server = serialization.load_pem_parameters(dh_params_server)
received_public_key_server = received_dh_params_server.generate_private_key()
shared_key_client = private_key_client.exchange(received_public_key_server.public_key())

# Now, both the server and client have the same shared key
print("Shared Key (Server):", shared_key_server)
print("Shared Key (Client):", shared_key_client)
