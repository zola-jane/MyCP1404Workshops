def main():
    print("Area of a Rectangle Calculator")

    width = int(input("Enter width in m:"))
    height = int(input("Enter height in m:"))
    depth = int(input("Enter depth in m:"))

    area = calc_area(width,height)
    volume = calc_volume(area,depth)
    print("Area: {} m ^2\nVolume: {} m^3".format(area,volume))


def calc_area(w,h):
    a = w * h
    return a


def calc_volume(a,d):
    v = a * d
    return v


main()