def Reverse_String(s: str) -> str:
    #task 4
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


if __name__ == '__main__':
    s = input()
    print(Reverse_String(s))