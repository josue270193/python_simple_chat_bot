
var_a = int(input())
var_b = int(input())
var_h = int(input())

if var_a <= var_h <= var_b:
    print("Normal")
else:
    if var_h > var_b:
        print("Excess")
    else:
        print("Deficiency")
