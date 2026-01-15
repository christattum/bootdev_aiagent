from functions.get_file_content import get_file_content

result = get_file_content("calculator", "main.py")
print("Result for main.py:")
print(result)

result = get_file_content("calculator", "pkg/calculator.py")
print("Result for pkg/calculator.py:")
print(result)

result = get_file_content("calculator", "/bin/cat")
print("Result for /bin/cat")
print(result)

result = get_file_content("calculator", "pkg/does_not_exist.py")
print("Result for pkg/does_not_exist.py")
print(result)
