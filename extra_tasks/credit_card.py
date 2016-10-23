def is_credit_card_valid(number):
    num_list = []
    num_sum = 0
    while number > 0:
        num_list.append(number % 10)
        number //= 10
    if len(num_list) % 2:
        for i in range(len(num_list)):
            if i % 2:
                num_list[i] *= 2
        for i in num_list:
            if i > 9:
                num_sum += i % 10 + 1
            else:
                num_sum += i
        if num_sum % 10:
            return False
        else:
            return True
    else:
        return False

print(is_credit_card_valid(79927398713))
print(is_credit_card_valid(79927398715))
print(is_credit_card_valid(79927398713))
