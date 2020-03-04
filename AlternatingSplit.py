def decrypt(encrypted_text, n):
    result = encrypted_text
    if n <= 0:
        return encrypted_text
    if encrypted_text is None:
        return None

    for i in range(0, n):
        a = len(encrypted_text)/2
        z = 0
        counter = 0
        loopresult = ""

        while z < len(encrypted_text):
            loopresult= loopresult+result[int(a)]
            if counter % 2 == 0:
                a -= len(encrypted_text)/2
            else:
                a += len(encrypted_text)/2 + 1
            counter = counter + 1
            z = z +1        
          
        result = loopresult

    return result



def encrypt(text, n):
    result = text

    if n <= 0:
        return text
    if text is None:
        return None

    for i in range(0, n):
        loopresult = ""
        for x in range(1, len(text), 2):
            loopresult = loopresult + result[x]
        for x in range(0, len(text), 2):
            loopresult = loopresult + result[x]
        result = loopresult

    return result