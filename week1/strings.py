#string declarationn
str1 = "Hello Welcome to klh university"

str2 = """
    Myself lalitha mahisri
    i am from kl uni
    jjdkdjf
    kksjfnsnsn i luv harry potterrrrrrrrrrrrrrrrrrrr

"""
print(str1)
print(str2)

#slicing the stringsss
s = "My name is lalitha. I am studying in klh"

print(s[11:18])
print(s[:18])
print(s[19:])

#negative indexing

s = "Harry potter is a book adaption"
print(s[4:10])
print(s[-10:-4])


#functions
st = "KONERU LAKSHMAIAHA EDUCATIONAL FOUNDATION"

print(st.lower())
print(st.find("I"))
print(st.capitalize())
print(st.swapcase())
print(len(st))


#concatenation of two stirngs
a = "klh"
b = "bowrampet"
c = a+b
print(c)
c = a+" "+b
print(c)


#string formattiong
txt1 = "My name is {fname}. I'm {age}".format(fname="John",age=26)
txt2 = "My name is {0}. I'm {1} ".format("John",26)
txt3 = "My name is {}. I'm {}".format("john",36)
print(txt1)
print(txt2)
print(txt3)