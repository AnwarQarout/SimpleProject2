text_to_be_converted=''


def convert_text_using_lower_method(text_to_be_converted):
    return text_to_be_converted.lower()


def convert_text_using_loop_method(text_to_be_converted):
    converted_text=''
    for i in text_to_be_converted:
        if(i>='A' and i <='Z'):
            converted_text=converted_text+chr((ord(i)+32))
        else:
            converted_text=converted_text+i
    return converted_text


def main_menu():
    convert_method_choice = int(input("Hello! Please enter 1 for the lower() convertion method,"
                                      " or 2 for the loop convertion method.\n"))

    text_to_be_converted = input("Please enter the text you would like to convert"
                                 " to lowercase.")
    converted_text = method_chooser_executor(convert_method_choice,text_to_be_converted)
    print(converted_text)


def method_chooser_executor(convert_method_choice,text_to_be_converted):
    if (convert_method_choice == 1):
        text_to_be_converted = convert_text_using_lower_method(text_to_be_converted)
    elif (convert_method_choice == 2):
        text_to_be_converted = convert_text_using_loop_method(text_to_be_converted)

    return text_to_be_converted

"""
convert_method_choice = int(input("Hello! Please enter 1 for the method,"
                              " or 2 for the method.\n"))
text_to_be_converted = input("Please enter the text you would like to convert"
                             " to lowercase.")
print(text_to_be_converted)
if(convert_method_choice == 1):
    text_to_be_converted = convert_text_using_lower_method(text_to_be_converted)
    print(text_to_be_converted)
elif(convert_method_choice ==2):
    text_to_be_converted = convert_text_using_loop_method(text_to_be_converted)
    print(text_to_be_converted)"""




