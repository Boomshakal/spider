for i in range(1,148):
    y=148.0/(3*i+1)
    if 148%(3*i+1)==0:
        print("每人种{}树，同学有{}位".format(y,3*i))