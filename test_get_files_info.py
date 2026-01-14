from functions.get_files_info import get_files_info

results = get_files_info("calculator", ".")
print("Result for current directory:")
print(results)

result = get_files_info("calculator", "pkg")
print("Result for 'pkg' directory:")
print(results)

result = get_files_info("calculator", "/bin")
print("Result for '/bin' directory:")
print(results)

result = get_files_info("calculator", "../")
print("Result for '../' directory:")
print(results)