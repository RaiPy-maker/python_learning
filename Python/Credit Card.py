# CREDIT CARD


cc_info = input("Please input your credit card number: \n")
cc_info_4_digits = cc_info[-1:-5]
cc_info_blurred = "*" * 12 + cc_info[12:] 


if len(cc_info) != 16:
    print("\nPlease recheck the credit card")
elif cc_info.isdigit() == False:
    print("\nOnly use numbers!")
else:
    fname = input("Please enter your first name: ")
    sname = input("Please enter your second name: ")

    if not fname.isalpha() or not sname.isalpha():
        print("Please do not use symbols/numbers ")

    else:
        verify = input(f"\n\n\nHey, {fname} {sname} please confirm that \n {cc_info_blurred} {cc_info_4_digits} is correct Y/N: ")
        if verify == 'y':
            print("Purchase was successful")
        else:
            print("Please try again")

