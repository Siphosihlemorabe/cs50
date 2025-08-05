def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    if len(s) > 6 or len(s) < 2:
        return False
    if not s.isalnum():
        return False

    num_started = False
    for i in range(len(s)):
        if s[i].isdigit():
            if not num_started:
                num_started = True
                if s[i] == "0":
                    return False
            
        elif num_started:
            return False

    return True


main()
