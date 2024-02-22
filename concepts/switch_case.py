# python version must be 3.10 or above for runnning this code


def number_to_string(arg):
    match arg:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case 3:
            return "three"
        case default:
            return "something"


head = number_to_string(0)
print(head)
