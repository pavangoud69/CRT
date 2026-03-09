def calculate_result(name: str, grades: list) -> str:
    average = sum(grades) / len(grades)
    status = "Pass" if average >= 40 else "Fail"
    return f"Average grade: {average:.2f}, Status: {status}"


if __name__ == "__main__":
    name = input().strip()
    grades = list(map(int, input().split()))
    
    print(calculate_result(name, grades))