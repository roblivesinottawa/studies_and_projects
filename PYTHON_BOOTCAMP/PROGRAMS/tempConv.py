def temp_conversion(scale=None,source_temp=None):
    if (scale == 'F') or (scale == 'f'):
        return 'C', (source_temp - 32.0) * (5.0 / 9.0)
    elif (scale == 'C') or (scale == 'c'):
        return 'F', (source_temp * 9.0 / 5.0) + 32.0
    else:
        print("please enter (F) or (C)")

scale = input("Select (F) or (C): ")
source_temp = int(input("Please, enter temperature: "))
s, m = temp_conversion(scale, source_temp)
print(f"{source_temp} degrees {scale.title()} is {m} degrees {s}")