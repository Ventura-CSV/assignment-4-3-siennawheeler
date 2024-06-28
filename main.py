def main():
    number = int(input('Enter your input: '))
    result = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    
    while number > 0:
        result.append(number % 2)
        number = number // 2


    print(*result)
    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
