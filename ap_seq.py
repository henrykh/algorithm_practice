def find_missing_val(a_list, n):
    diff = (a_list[-1] - a_list[0]) / n
    for i in range(n-2):
        if(a_list[i+1] != a_list[i]+diff):
            print (a_list[i] + diff)
            break

if __name__ == "__main__":
    find_missing_val([1, 3, 5, 9, 11], 5)
