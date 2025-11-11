def differ_At_One_Bit_Pos(num1, num2):
    bin_str1 = bin(num1)[2:]
    bin_str2 = bin(num2)[2:]
    diff_at_one_bit_pos = bin_str1 != bin_str2
    return diff_at_one_bit_pos