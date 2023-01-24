# Vigenère Cipher for Python
An example of the Vigenère Cipher algorithm (ROT0) based on Python 3
## Encryption
```
#encrypt.py
def main():
    
    key = 'BLOCKCHAIN'
    text = 'TEST, CAR. HOUSE + CRYPTO'
    
    print(f"\n  Key:           {key}")
    print(f"  Original:      {text}")
    print(f"  Cipherogram:   {encrypt(text, key)}\n", end='')

            
if __name__ == "__main__":
    main()
    
```
## Decryption
```
#decrypt.py
def main():

    key = 'BLOCKCHAIN'
    text = 'UPGV, MCY. HWHTP + QTIRAO'
    
    print(f"\n  Key:           {key}")
    print(f"  Cipherogram:   {text}")
    print(f"  Original:      {decrypt(text, key)}\n", end='')

            
if __name__ == "__main__":
    main()
    
```

