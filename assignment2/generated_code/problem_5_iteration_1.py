def differ_At_One_Bit_Pos(num1, num2):
    bin_str_num1 = bin(num1)[2:]
    bin_str_num2 = bin(num2)[2:]
    if bin_str_num1 == bin_str_num2:
        return True
    else:
        return False