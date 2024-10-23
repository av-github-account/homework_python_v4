# Очистка экрана
import subprocess
subprocess.run("printf '\033c'", shell=True)


#============================================================================
# result = supervisor()
# print(f"Answer: {result}")

def main() -> None:
    result = supervisor()
    print(f"Answer: {result}")

if __name__ == '__main__':
    main()
