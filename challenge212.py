#DailyProgrammer Challenge 212 Rövarspråket

import sys,re
output = ""
pattern = "[AEIOUYÅÄÖåöä! ]"

for char in "Jag talar Rövarspråket!":
        if re.match(pattern,char,re.IGNORECASE):
            output += char
        elif re.match("[a-z]",char,re.IGNORECASE):
            output += char+"o"+char.lower()

def encode_robber(input):
    encode = lambda x: x.group(0)+"o"+x.group(0).lower()
    return re.sub(r'(?i)[^AEIOUYÅÄÖåöä! ]',encode,input)


print encode_robber("Jag talar Rövarspråket!")
print output
