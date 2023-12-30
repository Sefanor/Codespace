sample_list = [25, 14, 56, 15, 36, 56, 77, 18, 29, 49]

max = sample_list[0]
min = sample_list[0]
for i in sample_list:
    if i < min:
        min = i
    if i > max:
        max = i
    
print(f"Maximum value for the above list: {max}")
print(f"Minimum value for the above list: {min}")