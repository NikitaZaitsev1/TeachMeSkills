words = ('aassdd', 'ddsdsad', 'qqwwqq')
result = (tuple(filter(lambda x: x == x[::-1], words)))
print(result)
