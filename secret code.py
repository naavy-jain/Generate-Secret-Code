import random
import string
import pwinput
A = 4
B = 4
print("Authentic Work By Navya Jain")
user_input = pwinput.pwinput(prompt="Enter Your String : ", mask="*")
length = len(user_input)
a = int(input("Enter 1 for Coding\n "))
if (a == 1 and len(user_input) >= 3):
    print("Coding is in process....\n Please wait till it is generated\n")
    remove_input = user_input[0]
    user_input = user_input[1::]
    after_conc = user_input.lower() + remove_input.lower()
    res = ''.join(random.choices(string.ascii_lowercase, k=A))
    ser = ''.join(random.choices(string.ascii_lowercase, k=B))
    secret_code = str(res) + after_conc + str(ser)
    print("\nYour secret code is : \n", secret_code)
    print("Do You want to decode the following Code ?\n ")
    b = input("Enter 2 for decoding the following code\n")
    if (b == '2'):
        # Decode the Encrypted Code
        new_code = secret_code[4:]
        get_code = new_code[:length+1]
        final_code = get_code[:-1]

        last_word = final_code[::-1]
        last_word = last_word[0]
        final_code = final_code[:-1]
        final_output = last_word+final_code
        print("\nYour secret code was : ", final_output)
else:
    reverse_input = user_input[::-1]
    print("Secret code is", reverse_input)
