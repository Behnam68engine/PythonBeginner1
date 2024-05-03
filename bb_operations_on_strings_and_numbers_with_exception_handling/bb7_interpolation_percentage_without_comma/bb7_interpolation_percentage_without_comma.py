# Copyright (c) 2024 Behnam

# This script is authored by Behnam and is created on May 2, 2024.
# It demonstrates various aspects of Python programming.


# bb7_interpolation_percentage_without_comma

"""
This script demonstrates different ways of string interpolation
without using commas.
"""

def main():
    """
    Main function to demonstrate different ways of string interpolation without using commas.
    """
    a_value = 222  # Assigns integer value 222 to variable a_value.
    b_value = -23.97653  # Assigns float value -23.97653 to variable b_value.
    c_value = 143  # Assigns integer value 143 to variable c_value.
    d_value = 'A'  # Assigns character 'A' to variable d_value.
    e_value = 'Hello my world'  # Assigns string 'Hello my world' to variable e_value.
    f_value = 0x8f  # Assigns hexadecimal value 0x8f (143 in decimal) to variable f_value.


    # print('b_1:mmd%d    mmd   %f mmd b_3=%x  b_4=%c  b_5=%s b_6=%d' %
    # (a_value, b_value, c_value, d_value, e_value, f_value))
    # without , or comma

    print('\n\n' f'b_1:mmd{a_value}    mmd   {b_value} mmd '\
        f'b_3={c_value:x}  b_4={d_value}  '\
            f'b_5={e_value} b_6={f_value}' '\n\n')

    print('\n\n' f'b_1:mmd{a_value}    mmd   {b_value} mmd '
        f'b_3={c_value:x}  b_4={d_value}  '
        f'b_5={e_value} b_6={f_value}' '\n\n')




    # s1_value = ('b_1=%.4d  b_2=%+09.3f  b_3=%06.3x b_4=%c b_5=%.11s b_6=%.5d'
    #            % (a_value, b_value, c_value, d_value,
    #           e_value, f_value))
    # %.3x & %.3f ...b3=%+06.3x

    # s1_value = f'b_1={a_value:04d}
    # b_2={b_value:+09.3f}  b_3={c_value:06x} b_4={d_value}
    # b_5={e_value[:11]} b_6={f_value:05d}'
    # all must be written in one long line

    # s1_value = ('b_1=%.4d  b_2=%+09.3f  b_3=%06.3x b_4=%c '
    #        'b_5=%.11s b_6=%.5d' % (a_value, b_value, c_value, d_value, e_value, f_value))
    # care to single code in each new line
    # also work but it's not recommended

    s1_value = (f'b_1={a_value:04d}  b_2={b_value:+09.3f}  '
            f'b_3={c_value:06x} b_4={d_value}  '
            f'b_5={e_value[:11]} b_6={f_value:05d}')

    
    print('''s_1:
    ''', s1_value)  # Prints s_1 string and its value s1_value.

    # print('b_1=%d  ' ' b_2=%.2f' ' b_3=%11.3x'
    #  'b_4=%c' 'b_5=%s' % (a_value, b_value, c_value, d_value, e_value))
    # Concatenates multiple strings without commas.
    # not recommended

    # print('b_1=%d  ' ' b_2=%.2f' ' b_3=%11.3x' 'b_4=%c' 'b_5=%s' % (a_value, b_value, c_value, d_value, e_value))
    # print(f'b_1={a_value}  b_2={b_value:.2f}
    # b_3={c_value:11} b_4={d_value} b_5={e_value}') # not recommended
    print(f'b_1={a_value}  b_2={b_value:.2f} ' \
      f'b_3={c_value:11} b_4={d_value} b_5={e_value}')


    #better version in multiple line, care to f' ' in each line

    # s2_value = 'v_1=%d  ' ' v_2=%f' \
    # ' v_3=%x' 'v_4=%c' 'v_5=%s'\
    # % (a_value, b_value, c_value, d_value, e_value)
    s2_value = (f'v_1={a_value} ' f'v_2={b_value} '\
            f'v_3={c_value:x} '\
                f'v_4={d_value} '\
                    f'v_5={e_value}')


    print('''\n\n\ns_2:''', s2_value)  # with , or comma
    # print("seperator")

    # print('\n\n\n%.5x' % 270) # not recommended
    print(f'\n\n\n{270:05x}')
    # "16 ** 2 +14(e) = 256 + 14" in hexadecimal radix with total 5 digits

if __name__ == "__main__":
    main()

# copyright
# The copyright command in the code serves as a marker indicating
# the ownership or copyright of the script.
