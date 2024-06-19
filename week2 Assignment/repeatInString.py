def repfree(s):
    seen_chars = set()
    for char in s:
        if char in seen_chars:
            return False
        seen_chars.add(char)
    return True

def main():
    string = input("Enter any string you want to check :")
    print(repfree(string))

if __name__ == "__main__":
    main()