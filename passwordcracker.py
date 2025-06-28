import itertools
import time

target=input("Enter a Target : ")
posible_value="abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()+_=- "
max_lenght=len(target)
def brute_force_password_cracker():
    attempts=0
    st=time.time()
    for i in range(1,max_lenght+1):
        for guess in itertools.product(posible_value,repeat=max_lenght):
            attempts+=1
            guess="".join(guess)
            print(guess)
            if guess==target:
                print(f"password found :{guess}")
                print(f"Time Taken:{time.time()-st} seconds")
                print(f"Total attempts :{attempts}")
                return
brute_force_password_cracker()