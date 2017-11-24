#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa 

from cryptography.hazmat.primitives import serialization

private_key=rsa.generate_private_key(
    65537,2048,default_backend()
    )
public_key=private_key.public_key()

pem_private=private_key.private_bytes(
    serialization.Encoding.PEM,
    serialization.PrivateFormat.TraditionalOpenSSL,
    serialization.NoEncryption()
    )

pem_public=public_key.public_bytes(
    serialization.Encoding.PEM,
    serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
with open("private.pem","w") as f:
    f.write(pem_private.decode("utf-8"))

with open("public.pem","w") as f:
    f.write(pem_public.decode("utf-8"))

with open("private.pem","rb") as f:
    private_key1=serialization.load_pem_private_key(
        f.read(),
        None,
        default_backend()
        )

with open("public.pem","rb") as f:
    public_key1=serialization.load_pem_public_key(
        f.read(),
        default_backend()
        )


from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

testdata="how are you!"
entext=public_key1.encrypt(
    testdata.encode(),
    padding.OAEP(
        padding.MGF1(hashes.SHA256()),
        hashes.SHA256(),
        None
        )
    )
text=private_key.decrypt(
    entext,
    padding.OAEP(
        padding.MGF1(hashes.SHA256()),
        hashes.SHA256(),
        None
        )
    ).decode()

print(testdata)
print(text)

from Crypto.Cipher import AES 
from Crypto.Random import random 

print(random.getrandbits(5))
cipher=AES.new(
    "1234567890abcdef",AES.MODE_CFB,b'1234567890abcdef'
    )
cipher1=AES.new(
    "1234567890abcdef",AES.MODE_CFB,b'1234567890abcdef'
    )
help(AES.new)

msg=b'how are you!'
msg1=cipher.encrypt(msg)
msg2=cipher1.decrypt(msg1)

print(msg2.decode())












