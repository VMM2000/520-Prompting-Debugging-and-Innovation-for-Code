def differ_At_One_Bit_Pos(num1, num2):
    binary_num1 = bin(num1)[2:]
    binary_num2 = bin(num2)[2:]
    if binary_num1 != binary_num2:
        return False
    else:
        return True