import re

rs=re.findall('abc','abc')
rs=re.findall('a.c','abc')
rs=re.findall('a\.c','a.c')
rs=re.findall('a[bc]d','acd')

rs=re.findall('\d','123')
rs=re.findall('\w','az1233gg哈哈')

#  * : \d出现0次或多次
rs=re.findall('a\d*','a')
#  + : \d出现一次或多次
rs=re.findall('a\d+','a')
#  ? : a出现0次或1次
rs=re.findall('a\d?','a123')
#  ? : a出现{n}次
rs=re.findall('a\d{2}','a123')

print(rs)


#findall方法
rs=re.findall('\d+','zhang12wang45')
print(rs)

rs=re.findall('a.bc','a\nbc')
rs=re.findall('a.bc','a\nbc',re.DOTALL)
rs=re.findall('a.bc','a\nbc',re.S)
print(rs)

rs=re.findall("a.+bc","a\nbc",re.DOTALL)
rs=re.findall("a(.+)bc","a\nbc",re.DOTALL)
print(rs)


#\\转义字符
rs=re.findall("a\nb","a\nb")
rs=re.findall("a\\nb","a\\nb")
rs=re.findall('a\\\\nb','a\\nb')
rs=re.findall(r'a\\\nb','a\\\nb')
print(rs)









