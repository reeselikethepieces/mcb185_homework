(1) Write a function that turns negative numbers into positive numbers and vice versa. 
    Give your function a name that is simultaneously simple and descriptive.
    (-) --> (+) 
    (+) --> (-)
        --> to make a neg#, should we x by -1
        --> name: inverse
        def inverse(a): 
            return -1 * a


(2) Write functions that compute the areas, circumferences, or volumes of simple shapes 
    like squares, rectangles, circles, spheres, etc.
    - circles - pier2
        - area - circle_area
     a = math.pi*(r**2)      
         def area_circle(r):
            return math.pi * r**2
   
   
(3) Write functions that convert temperature (whichever scales you prefer).
    F --> K 
        C = K - 273.15
        C = (F - 32) * 5/9
        C = C 
            K - 273.15 = (F - 32) * 5/9
              + 273.15 = + 273.15
              -------------------
            K = (F - 32) * 5/9 + 273.15     # def Karenheit ~a joke
        def Farenheit_Kelvin(F):    
            return (F - 32) * 5/9 + 273.15

(4) Write functions that convert speeds (mph, kph, fps, mps, etc).
    mph --> kph 
         def mk(m):
            return (m*1.60934)
    
(5) Write a function that computes DNA concentration from OD260.
    # this was before looking up OD260, and seeing "people also asked" how to calc [DNA] from OD260
    OD260 --> DNA 
        let DNA = d and OD260 = o
        def dna_OD260 (d):
            return (d/o)
    # this was after
        [dsDNA] = 50 ug/mL * OD260 * dilution factor(df)
        let d = [dsDNA] and OD260 = o and dilution factor = df 
        def od260_dna (d):
            return (50 ug/mL * o * df) 
    
(6) Write a function that computes the distance between two points in a graph.
    #from memory
    given two coordinate points (x1, y1) and (x2, y2)
    d = sqrt.((x2 - x1)**2 + (y2 - y1)**2)
        def distance_twopoints (x1, y1, x2, y2):
            return (sqrt.((x2 - x1)**2 + (y2-y1)**2))
    #checks actual formula - yes. after seeing below, I want to change distance_twopoints to distance 
        def distance_twopoints (x1, y1, x2, y2):
            return (sqrt.((x2 - x1)**2 + (y2-y1)**2))
    
(7) Write a function that computes the midpoint between two points. Note that this function 
    must return values for x and y. Your return statement will have two values separated by a comma. 
    Your function will look something like this.
        def midpoint(x1, y1, x2, y2):
            # b4 looking anything up - skip 
                midpoint = d/2 
                m = sqrt.(((x2 - x1)**2 + (y2 - y1)**2))2)
                #scratch
                d = d 
                sqrt.(((x2 - x1)**2 + (y2 - y1)**2))2) = sqrt.(((x2 - x1)**2 + (y2 - y1)**2))2)
                    solve for x2 
                    solve for y2
                        then you'll have to **2 both sides, *2 both sides
                    (x2-x1)**2 + (y2-y1)**2 .. no 
                #too long, fun to play with later
                is it legal to use midpoint = distance/2
                m = sqrt.(((x2 - x1)**2 + (y2 - y1)**2))2)
                set m = 0 --> this is the questionable legal move 
                    solve for x2 
                    solve for y2
            # looked at graph 
                find slope of the line with the two points
                    point a (6,4) point b (2,3) - a graph on google images 
                equation of the line using the two points
                    y2 - y1 = m(x2-x1) 
                    solve for x2 
                    solve for y2 
                 #goofed and was looking at a real graph 
            #donalds ex - two points on y axis (x = 0) - reese brain fart
                #donald, "okay lets put it in bio talk" - two values from repeatable experiment and you want
                    #one number that describes... - reese - the average????
                        #d/2? WAIT is this the first thing i did 
            #midpoint formula look up 
                
            return mx, my
    Call your function like this: x, y = midpoint(x1, y1, x2, y2).
