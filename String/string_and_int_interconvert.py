def str_convert():
    global str_to_conv
    res_int = 0
    for cnt in range (len(str_to_conv)//2):
        res_int += ord(str_to_conv[cnt]) * 10 ** len(str_to_conv)
        res_int += str_to_conv[~cnt] * 10 ** cnt


str_to_conv = "32498322"
int_to_conv = 2343210
str_convert()
print(str_to_conv)