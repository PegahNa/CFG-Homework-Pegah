# Your boss really likes calculating VAT on their purchases. It is their favourite
# hobby. They've written this code to calculate VAT and needs your help to fix it.
# def calculate_vat(amount):
# return amount * 1.2
#
# calculate_vat(100)
# When your boss runs the program nothing is output back.
# Your boss expects the program to output the value ‘120’. What is wrong? What is
# the best way to fix the problem?


def calculate_vat(amount):
    return amount * 1.2
vat_amount = calculate_vat(100)
print(vat_amount)