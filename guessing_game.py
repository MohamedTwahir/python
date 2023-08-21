# creating a secret word
secret_word = "Python"

#creating a guess variable through an input statement
guess = input('Guess what the Secret Word is: ')
# loop to ensure the game keeps on going
while guess != secret_word:
    print('Oops ! Wrong guess. Try again')
    guess = input('Try a new Guess!: ')

print('Nice! you guessed right. Great job')
