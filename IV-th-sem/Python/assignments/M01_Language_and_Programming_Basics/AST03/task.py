def Student_Grade_System(name: str, n1: int, n2: int, n3: int) -> str:
    avg = (n1 + n2 + n3) / 3

    if avg >= 50:
        status = "Pass"
        avg = round(avg, 1)
    else:
        status = "fail"
        avg = int(avg * 100) / 100

    return f"Average grade: {avg}, Status: {status}"


if __name__ == '__main__':
    name = input()
    n1, n2, n3 = list(map(int, input().split()))
    print(Student_Grade_System(name, n1, n2, n3))