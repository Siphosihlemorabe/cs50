def convert(text):
    
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text
def main():
    
    user_input = input("Enter a message: ")
    
    converted = convert(user_input)
    print(converted)
    
   
main()