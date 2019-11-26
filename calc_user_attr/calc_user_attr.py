def calc_user_attr(choose_data):
    data_amount = len(choose_data)
    totsum = choose_data.pop()
    while choose_data:
        temp = choose_data.pop()
        for i, val in enumerate(temp):
            totsum[i] += val

    mean_list = [x / data_amount for x in totsum]

    return mean_list

