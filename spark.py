print ("hi")

# /request_invite ivan.avanessov@gmail.com Ivan_Avanessov 1 en SPARK

# setOfWords is as set of strings
# prefix is a string
def checkPrefix (prefix, setOfWords):
    ans = set()
    for word in setOfWords:
        if word.startswith(prefix):
            ans.add(word)
    return ans

print (checkPrefix ("a", ("aaa", "bbb")))