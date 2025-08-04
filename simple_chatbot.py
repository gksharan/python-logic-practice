bot_name: str = 'bob'
print(f'{bot_name}: Hello, how can I help you?')

while True:
    user_input: str = input('you: ').lower()

    if user_input in ['hi', 'hello']:
        print(f'{bot_name}: Hello sir, how was your day?')

    elif user_input in ['bye', 'goodbye']:
        print(f'{bot_name}: Bye sir, see you soon!')
        break  # stop the loop when saying bye

    elif user_input in ['love u']:
        print(f'{bot_name}: Love you too sir.')

    elif '+' in user_input or 'math' in user_input:
        print(f'{bot_name}: Lets add some numbers')
        try:
            num1: float = float(input('Enter first number: '))
            num2: float = float(input('Enter second number: '))
            print(f'{bot_name}: The sum is {num1 + num2}')
        except ValueError:
            print(f'{bot_name}: That wasnt a valid number')

    else:
        print(f'{bot_name}: I don’t understand. Bye!')
