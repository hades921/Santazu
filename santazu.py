import time
import string
import hashlib
from colorama import init, Fore
init()

GREEN = Fore.GREEN
RED   = Fore.RED
RESET = Fore.RESET
BLUE  = Fore.BLUE
PURP  = Fore.MAGENTA

print(f"""{PURP}
 ::::::::      :::     ::::    ::: :::::::::::     :::     ::::::::: :::    ::: 
:+:    :+:   :+: :+:   :+:+:   :+:     :+:       :+: :+:        :+:  :+:    :+: 
+:+         +:+   +:+  :+:+:+  +:+     +:+      +:+   +:+      +:+   +:+    +:+ 
+#++:++#++ +#++:++#++: +#+ +:+ +#+     +#+     +#++:++#++:    +#+    +#+    +:+ 
       +#+ +#+     +#+ +#+  +#+#+#     +#+     +#+     +#+   +#+     +#+    +#+ 
#+#    #+# #+#     #+# #+#   #+#+#     #+#     #+#     #+#  #+#      #+#    #+# 
 ########  ###     ### ###    ####     ###     ###     ### #########  ######## 

Raidforums Exclusive

Coded by: 3Subs
Idea by: backyaro

""")
ready = False
start = time.time()
chars = list(string.printable)[:95]
base = len(chars)
n = 0
hashmethod = 0
password = ""
solved = False
quit = ""
while ready != True:
    password = input("Enter a valid MD5 or SHA-1 hash: ")

    if len(password) == 32:
        ready = True
    elif len(password) == 40:
        ready = True
        hashmethod = 2
    else:
        print("Please make sure that u actually used a MD5 or SHA1 hash. If you did then make sure its lowercase :). ")

def numberToBase(n, b):
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

if password == '':
    print('Your password is empty')
    solved = True

# checking passwords
while not solved:
    lst = numberToBase(n, base)
    word = ''
    for x in lst:
        word += str(chars[x])
    if hashmethod == 2:
        hashedGuess = hashlib.sha1(bytes(word, 'utf-8')).hexdigest()

    else:
        hashedGuess = hashlib.md5(bytes(word, 'utf-8')).hexdigest()

    if password == hashedGuess:
        solved = True
        print('-Stats-')
        print('Pass: ' + word)
        print('Attempts: ' + str(n))
        print('Time: ' + str((time.time() - start)) + ' sec')

    else:
        n += 1