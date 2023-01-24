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
![encrypt](https://user-images.githubusercontent.com/123471749/214316608-8110f254-307a-4815-bba3-e6d76f07127a.png)

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
![decrypt](https://user-images.githubusercontent.com/123471749/214316540-bd9bfd19-e0b0-46d5-9082-c83c5dfa35b9.png)

