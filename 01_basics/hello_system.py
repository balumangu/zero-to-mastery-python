import sys
import platform

def main():
    print("--- Python Learning Journey: Day 1 ---")
    print(f"Python Version: {sys.version}")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print("--------------------------------------")
    print("Ready to start automating!")

if __name__ == "__main__":
    main()