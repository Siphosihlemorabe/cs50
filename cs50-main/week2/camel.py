def main():
    camel=input("input camel case: ")
    snake=convert_to_snakecase(camel)
    print(snake)


def convert_to_snakecase(camelCase):
    snake_case=""
    for i in camelCase:
        if i.isupper():
            snake_case+="_"
        snake_case+=i
    return snake_case.lower()
main()