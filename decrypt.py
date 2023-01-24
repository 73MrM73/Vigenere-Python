alf_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def dict_gen(alf_dict, k):         #Creating a dictionary for encryption
    dec = {}
    for i in range(len(alf_dict)):
        if len(alf_dict) > i+k:
            dec[alf_en[i]] = alf_dict[i+k]
        elif len(alf_dict) <= i+k:
            dec[alf_en[i]] = alf_dict[-1*(len(alf_dict)-i-k)]
    return dec

def alf(s):           #Checking the letters
    for i in alf_en:
        if i == s:
            return True
    return 'symb'
            
def gen_key_text(text, key):              #Creating text from a key
    count = 0
    mas = []
    for i in text:
        if alf(i) == True:
            if count < len(key):
                mas.append(key[count])
                count += 1
            else:
                count = 0
                mas.append(key[count])
                count += 1
        elif alf(i) == 'symb':
            mas.append(i)
    return mas

def gen_number(alf):                     #Creation of the dictionary of the alphabet
    dec = {}
    for i in range(len(alf)):
        dec[alf[i]] = i 
    return dec
    
def decrypt(text, key):             #decryption function
    en_dict = gen_number(alf_en)
    key_text = gen_key_text(text, key)
    count = 0
    mas = []
    for i in text:
        if alf(i) == True:
            count2 = 0
            for n in en_dict:
                if n == key_text[count]:
                    dec = dict_gen(alf_en, count2)
                    for c in dict(zip(dec.values(), dec.keys())):                    #Dictionary change for decryption
                        if c == i:
                            mas.append(dict(zip(dec.values(), dec.keys()))[i])
                count2 += 1
        elif alf(i) == 'symb':    
            mas.append(i)
        count += 1
    return ''.join(mas)
            
def main():           #main function

    key = 'BLOCKCHAIN'
    text = 'UPGV, MCY. HWHTP + QTIRAO'
    
    print(f"\n  Key:           {key}")
    print(f"  Cipherogram:   {text}")
    print(f"  Original:      {decrypt(text, key)}\n", end='')

            
if __name__ == "__main__":
    main()

