import string
str1 = "hey!!! my name ...is Pranchal.."
str2 = str1.translate
(str.maketrans('', '', string.punctuation))
print(str2)