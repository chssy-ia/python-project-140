def welcome_user():
    import prompt

    nombre1 = prompt.string('May I have your name? ')
    print(f"Hello, {nombre1}!")

if __name__ == "__main__":
    welcome_user()


    
