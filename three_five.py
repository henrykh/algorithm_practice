def three_or_five(top):
    the_sum = 0
    for num in xrange(top):
        if num % 3 == 0 or num % 5 == 0:
            the_sum += num

    return the_sum


if __name__ == "__main__":
    print three_or_five(1000)
