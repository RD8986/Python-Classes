import os

path = "./random.txt"

def generate_random_string(seed):
    characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz~!@#$%^&*()))_+'
    length = (seed % 6) + 11

    result = ''
    for i in range(length):
        seed = seed + (i * 7)
        index = seed % len(characters)
        result += characters[index]
    
    return result

def is_unique(random_string, existing_strings):
    return random_string not in existing_strings

def load_existing_strings():
    if not os.path.exists(path):
        return set()
    
    with open(path, 'r') as file:
        return set(line.strip() for line in file)

def save_to_file(random_string):
    with open(path, 'a') as file:
        file.write(random_string + '\n')

choice = input("Would you like to have a random string? (yes/no): ")

if choice.lower() == "yes":
    existing_strings = load_existing_strings()
    seed = 12345

    while True:
        random_string = generate_random_string(seed)
        if is_unique(random_string, existing_strings):
            save_to_file(random_string)
            print("Generated and saved random string:", random_string)
            break
        seed += 1
else:
    print("You have chosen no. You are exiting the program.")
