def school_location(arr):
    
    m = len(arr) // 2
    return m


if __name__ == '__main__':

    """ Input: n = number of students, coord = coordinates of students' houses.
        Find the coordinate of the school to minimize the sum of distances 
        from houses to the school of all students. """

    n = int(input())
    coord = [int(x) for x in input().split()]
    res = school_location(coord)
    print(coord[res])