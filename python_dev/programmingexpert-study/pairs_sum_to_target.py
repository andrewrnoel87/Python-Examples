def pairs_sum_to_target(list1, list2, target):
    
    pairs_list = []

    for i in range(len(list1)):

        for j in range(len(list2)):  # go through each index combination

            if (list1[i] + list2[j]) == target:  

                pairs_list.append([i, j])   # add index pair whose summation equals target to new list
    
    return pairs_list


