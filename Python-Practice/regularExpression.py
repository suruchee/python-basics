import re
pattern = r"suru"
if re.match(pattern,"asuruchi"):
    print('Match found')
else:
    print('No match found')

if re.search(pattern,"asuruchi"):
    print('Match found')
else:
    print('No match found')
print(re.findall(pattern,"asuruchisuru"))
#find and replace

import  re
string = "My name is John, Hi I'am John"
pattern = r"John"
newstring = re.sub(pattern,"Rob",string)
print(newstring)
#dot metacharacter
import re
pattern = r"gr.y"
if re.match(pattern, "gray"):
    print("Match found")
#caret^(match must start from this particular point, here gr) and dollar metacharacter $
import  re
pattern = r"^gr.y$"
if re.match(pattern,"grby"):
    print("Match 1")

#character class
import  re
pattern = r"[A-Z][a-z][0-9]"
if re.search(pattern,"AH6"):
    print("Matched")
#star metacharacter
import re
pattern = r"eggs(bacon)*"
if re.match(pattern,"eggsbaconbacon"):
    print("match found")
#plus meta character
import re
pattern = r"eggs(bacon)+"
if re.match(pattern,"eggsbaconbacon"):
    print("match found")
#curly braces- repeating n numbers of times
import re
pattern = "ab{2}"
if re.match(pattern,"abb"):
    print("match found")
#wildcard . a.b means we can place any character between a and b also matches (acbb)
import re
pattern = r"a.b"
if re.match(pattern,"acb"):
    print("match found")
#optional? may or may not be occuring
#for - to be optional in opt-cdf
#pattern=  opt-?cdf
################################
#string should be digits of length 5 (\d{5})
#string should be any non digits of length 5 (\D{5})
#string should be any alphanumeric character of length 5 (\w{5})