### This is the dictionary containing the characteristics of each color and shape ###

# class Object_Dictionary:
#     def __init__(self):
#         pass

    # def color_ranges(self):

# The 'HSV' lies and deceives. it is actually RGB in disguise cuz the detect code doesn't bother to change it to to RGB for bitwise and. LIIIIES
colors = { 
    'HSV':
        { 
        'red':([165, 27, 74], [255, 255, 255]),
        'orange':([11, 153, 172], [24, 255, 255]),
        'yellow':([25, 32, 234], [31, 255, 255]),
        'green':([32, 27, 72], [83, 255, 255]),
        'blue':([82, 27, 72], [129, 255, 255]),
        'purple':([130, 27, 91], [149, 255, 255]),
        'pink':([150, 27, 142], [164, 255, 255]),
        'brown':([11, 80, 53], [24, 255, 171]),
        'black':([0, 0, 0], [255, 255, 38]),
        'white':([0, 0, 204], [255, 25, 255])
        },    
    'RGB': 
        { 
        'red':([10, 10, 120], [104, 104, 255]),
        'orange':([0, 100, 200], [104, 175, 255])
        },
    'Modified_RGB':
        { #needs to be finely tuned later, for more images but ye. lower and upper bound for colormasking
         'red': ([0,0,120],[80,80,255]), #works for testim
         'orange': ([0,100,120],[10,200,255]), #works for testim5
         'yellow': ([0,180,180],[100,255,255]),  #reduce blue to get rid of background color works for testim8 and testim6
         'green': ([0,0,0],[0,0,0]), #same as red 0,100,0 120,2550,120
         'blue': ([120,0,0],[255,150,100]), #same
         'purple': ([100,0,100],[150,100,150]), #untuned
         'pink': ([200,0,200],[255,100,255]), #untuned
         'brown': ([100,0,100],[150,100,150]), #untuned
         'black': ([0,0,0],[0,0,0]), #untuned 0,0,0 20,20,20
         'white': ([0,0,0],[0,0,0]) #untuned 220,220,220 255,255,255
        }
    }


        

