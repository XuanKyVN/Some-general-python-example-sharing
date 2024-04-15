def get_key(val):
    for key, value in my_dict.items():
        if val == value:
            return key

    return "key doesn't exist"


# Driver Code
my_dict = {"Java": 110, "Python": 119, "C": 15}

print(get_key(100))
print(get_key(11))