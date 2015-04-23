def smallest_multiple():
    num = 2520
    while True:
        for factor in xrange(1, 21):
            if num % factor != 0:
               # print "Break at {} / {}".format(num, factor)
                break
        else:
            return num
        num += 20
