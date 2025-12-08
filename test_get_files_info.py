import os
from functions.get_files_info import get_files_info

def main():
    #print(f"cwd: {os.getcwd()}")
    #print(os.path.join("calculator", "/pkg"))
    #print(f"cwd: {os.listdir("/calculator/pkg")}")

    print("Result for current directory:")
    print(get_files_info("calculator", "."))

    print("Result for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"))

    print("Result for '/bin' directory:")
    print(get_files_info("calculator", "/bin"))

    print("Result for '../' directory:")
    print(get_files_info("calculator", "../"))
main()
