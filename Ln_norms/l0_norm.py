"""
May 23rd, 2024
Today, during the CTL session for CS221, Bidipta explained the various L-n norms that AI folks incorporate in their code.
So I decided to look more into it, and discovered this really cool Medium article:
https://montjoile.medium.com/l0-norm-l1-norm-l2-norm-l-infinity-norm-7a7d18a4f40c

According to this article, L0 norm can be used to check if login username and password match!

Hence, I decided to write a simple code that simulates this. Gonna invest 10-20 minutes cuz I'm still 
working on organizing notes from other office hours.

"""

import numpy as np
from typing import List

def l0_norm(x: np.ndarray) -> float:
    return np.sum(x != 0)

def l0_distance(x: np.ndarray, y: np.ndarray) -> float:
    return np.sum(x!=y) if len(x) == len(y) else 0.0

def login(true_info: np.ndarray, input_info: np.ndarray) -> int:
    check = l0_distance(true_info,input_info)
    if check == 0:
        print("Login Successful!")
    elif check == 1:
        print("Error: Either ID or Password is Incorrect")
    elif check == 2:
        print("Error: Both ID and Password Incorrect")
    return check

def string_to_ASCII(input_str: str) -> int:
    ascii_list = [str(ord(char)) for char in input_str]
    return int(''.join(ascii_list))

if __name__ == '__main__':
  """
  > python l0_norm.py
  > Correct ID: ilovemath
  > Correct PW: ireallyamanerd
  > Case sensitive
  """
  print("Hello!")
  stop_check = -1
  while (stop_check != 0):
    user_input_ID = input("Enter your ID: ")
    user_input_PW = input("Enter your Password: ")
    _true_info = [string_to_ASCII('ilovemath'),string_to_ASCII('ireallyamanerd')]
    input_info = [string_to_ASCII(user_input_ID),string_to_ASCII(user_input_PW)]
    stop_check = login(np.array(_true_info),np.array(input_info))

#it works!! wahoo
  

