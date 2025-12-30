import random

easy = ['ball', 'road', 'apple', 'pen', 'dog']
medium = ['snake', 'ediot', 'laptop', 'elephant', 'pegion']
hard = ['access', 'bucket', 'gear', 'shirt', 'build']

print('Welcome to guessing game...')
print('Please choose the difficulty level (easy, medium, hard) : ')

level = input('Enter difficulty level : ').lower()
if level == 'easy':
    secret = random.choice(easy)
elif level == 'medium':
    secret = random.choice(medium)
elif level == 'hard':
    secret = random.choice(hard)
else:
    print('Invalid difficulty level..!, choice switched to easy.')
    secret = random.choice(easy)

attempts = 0
print('Guess the word...')

while True :
    guess = input('Enter your word : ').lower()
    attempts += 1
    if guess == secret:
        print(f'Congratulations ! You guessed correct word in {attempts} attempts.')
        break

    hint = ''

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"
    print('Hint :', hint)

print('Game Over !')