sample_list = [20, 30, 25, 35, -16, 60, -100]

tot = 0
for i in sample_list:
    tot += i
    
print(f"The average is: {tot/len(sample_list)}")