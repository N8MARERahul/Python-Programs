def pythagoras(upper_range):
    c, m = 0, 2
 
    # Limiting c would limit
    # all a, b and c
    while c < upper_range :
         
        # Now loop on n from 1 to m-1
        for n in range(1, m) :
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
 
            # if c is greater than
            # limit then break it
            if c > upper_range :
                break
 
            print(a, b, c)
 
        m = m + 1

# Driver Code
upper_range = int(input("Enter the upper_range: "))
pythagoras(upper_range)
