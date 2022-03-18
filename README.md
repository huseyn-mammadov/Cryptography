# Cryptography

bsgs.py - Computing a discrete log. Using the "baby step, giant step" approach.


sdesmitm.py - MITM attack on 2DES. This program carry out a meet-in-the-middle attack on 2DES. This system encrypts a plaintext first with one key and then again with a different key. Main reason is to prove that what is DES, why we don't use double DES.


aesencryptround.py - Implement the first round of AES with a 128-bit key. 
For example
Performing a bitwise XOR with the plaintext and the key
Applying byte substitution for each byte in the state
Applying shift rows on the state table rows
Applying mix columns on the state table columns
