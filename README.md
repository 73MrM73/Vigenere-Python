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
    
    ![Безымянный3](https://user-images.githubusercontent.com/123471749/214316085-f366ffff-8897-42eb-a28a-905ef01695ec.png)
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
    
    ![Безымянный4](https://user-images.githubusercontent.com/123471749/214316299-89225e15-090c-41ba-acab-55c12259b2f1.png) 
    
```

