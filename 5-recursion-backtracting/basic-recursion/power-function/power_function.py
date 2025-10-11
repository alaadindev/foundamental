def power_function(num, pow):
    if pow ==1:
        return num
    return num * power_function(num, pow-1)

print(power_function(3, 4))