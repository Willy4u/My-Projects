import re

pattern = r'([0])'

nums = str(input())

match = re.match(pattern,nums)


if match and len(nums)== 10:
    print('Valid')
else:
    print('Invalid')
