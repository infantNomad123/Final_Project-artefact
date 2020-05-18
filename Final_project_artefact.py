import random
#Sets mode
ENC =0
DEC =1

#creates key
#The key values are constituted with numbers rather than alphabet
def parseKey(key):        
    tmp = []
 
    for i, k in enumerate(str(key)):
        tmp.append((i,k))

    tmp = sorted(tmp, key=lambda x:x[1])

    enc_table = {}
    dec_table = {}
    
    for i, c in enumerate(tmp):
        enc_table[c[0]] = i
        dec_table[i] = c[0]

    return enc_table, dec_table

#Transposes values
#Makes encryption and decryption tables
def transposition(msg, key, mode):

    #Sets the length of the plaintext message
    msgsize = len(msg)
    
    #Sets the length of the key
    keysize = len(str(key))
    ret = ''

    filler = ''
    #Fills any left out space if the length of the message is not the multiple of keysize
    if msgsize%keysize != 0:
        code = ['5', '2', '#', '8', '1', '3','4', '6', '0', '9', '*', '%', '=', '(', ')']
        random_code = random.choice(code)
        filler = '0' * (keysize - msgsize%keysize)
        
    #Sets the texts to an upper case and fills out the space
    msg = msg.upper()
    msg+=filler
    
    #calls encryption and decryption table from the function parsekey(key)
    enc_table, dec_table = parseKey(key)
    
    #Decides the action to be taken on the basis of mode - ENC ord DEC
    #If it is in ENC mode call the encryption table
    if mode == ENC:
        table = enc_table
    #If not call the decryption table
    else:
        table = dec_table
    #Encrypts the text
    if mode == ENC:
        buf = [''] * keysize
        for i,c in enumerate(msg):
            col = i%keysize
            index = table[col]
            buf[index] += c

        for text in buf:
            ret += text
            
    #Decrypts the text
    else:
        blocksize = int(msgsize/keysize)
        buf = ['']*keysize
        pos = 0
        for i in range(keysize):
            text = msg[pos:pos+blocksize]
            index= table[i]
            buf[index] += text
            pos += blocksize

        for i in range(blocksize):
            for j in range(keysize):
                if buf[j][i] != 0:
                    ret += buf[j][i]

    return ret
#Displays the result
def main():
    #set key values
    key = 12012
    
    #Print out the plaintext
    msg = "ATTACKATDAWN"
    print('Original:%s' %msg.upper())
    
    #Writes encrypted file on 'encryption.txt' file 
    ciphertext = transposition(msg, key, ENC)
    filename = open('encryption.txt','wt+')
    filename.write(ciphertext)
    
    #Reads the content from 'encryption.txt'
    filename = open('encryption.txt','rt')
    content = filename.read()
    
    #Writes decrypted text on 'decryption.txt' file
    deciphertext = transposition(content, key, DEC)
    filename = open('decryption.txt','wt+')
    filename.write(deciphertext)
    
main()
        
      
