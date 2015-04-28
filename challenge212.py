#DailyProgrammer Challenge 212 R�varspr�ket

import sys,re
output = ""
pattern = "[AEIOUY������! ]"

for char in "Jag talar R�varspr�ket!":
        if re.match(pattern,char,re.IGNORECASE):
            output += char
        elif re.match("[a-z]",char,re.IGNORECASE):
            output += char+"o"+char.lower()

def encode_robber(input):
    encode = lambda x: x.group(0)+"o"+x.group(0).lower()
    return re.sub(r'(?i)[^AEIOUY������! ]',encode,input)


print encode_robber("Jag talar R�varspr�ket!")
print output
