import re
a='aaasjebsh123-1346'
aa = re.match(r'\w',a).group()
print(aa)