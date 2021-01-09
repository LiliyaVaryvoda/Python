import sys
a="gasg"
string=str("")
string2=str("")
for element in a:
    if element==" ":
        None
    else:
        string+=element
for i in reversed(string):
    string2+=i
string=string.lower()
string2=string2.lower()
if string==string2:
    print "Yes"
else:
    print "No"