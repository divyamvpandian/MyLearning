table={}
def main():
    str = "abcde"
    value = minInsertions(str, 0, len(str) - 1)
    print(value)

def minInsertions(str, l, h):
    if l >= h:
        return 0
    if l == h - 1:
        return 0 if (str[l] == str[h]) else 1
    if (l,h) in table:
        return table[(l,h)]

    if str[l] == str[h]:
        table[(l,h)] = minInsertions(str, l + 1, h - 1)
    else:
        table[(l,h)] =  min(minInsertions(str, l, h - 1), minInsertions(str, l + 1, h))+1
    return table[(l,h)]

def minInsertionsDP(str, l, h):
    if l >= h:
        return 0
    if l == h - 1:
        return 0 if (str[l] == str[h]) else 1
    if (l,h) in table:
        return table[(l,h)]

    if str[l] == str[h]:
        table[(l,h)] = minInsertions(str, l + 1, h - 1)
    else:
        table[(l,h)] =  min(minInsertions(str, l, h - 1), minInsertions(str, l + 1, h))+1
    return table[(l,h)]


if __name__ == '__main__':
    main()