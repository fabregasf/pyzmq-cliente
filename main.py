from ecdh import ECDH
import subprocess, os, sys

if sys.platform.startswith('win32'):
		trng = str(subprocess.check_output('wmic csproduct get uuid'),'utf-8').split('\n')[1].strip().replace('-','')
		print("estamos no windows")
elif sys.platform.startswith('linux'):
		print("estamos no Linux")

print("Bob, insira sua mensagem: ")
text = input("Digite sua mensagem: ")

alice = ECDH()
bob = ECDH()

print("Algoritmo de chaves de alice: "+alice.tipo)

encrypted_message = bob.encrypt(alice.public_key, bytearray(text, encoding='utf-8'))
print(encrypted_message)

decrypted_message = alice.decrypt(bob.public_key, encrypted_message, bob.IV)
print(decrypted_message)

