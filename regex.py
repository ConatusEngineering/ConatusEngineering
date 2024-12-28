import re
total = 0
fileHandle = open('regex_sum_1075014.txt')
for line in fileHandle:
    line = line.rstrip()
    embeddedNumbers = re.findall('[0-9]+', line)
    for number in embeddedNumbers:
        total = total + int(number)

print(total)


str = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
print(re.findall('http://.*',str))
