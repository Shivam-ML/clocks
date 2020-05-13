"""Shivam Pandey @13-05-2020"""
"""Below code is to find Angle between hands on a clock face where input is taken from clock_input.txt file and output 
is stored result.txt"""

# Fuction to calculate Angle
def AngleCalculator(h,m): 
    if (h < 0 or m < 0 or h > 12 or m > 60): 
        print('Wrong input') 
        return

    if (h == 12): 
        h = 0
    if (m == 60): 
        m = 0

    hour_angle = 0.5 * (h * 60 + m) 
    minute_angle = 6 * m 
    angle = abs(hour_angle - minute_angle) 
    angle = min(360 - angle, angle) 
    return angle 

## read time from file
clock_data = []
with open("clock_input.txt", "r") as filestream:
    for line in filestream:
        clock_data.append(list(map(int,line.rstrip("\n").split(','))))

#calculate Angle       
result_angle=[]
for i in clock_data:
    result_angle.append(AngleCalculator(i[0],i[1]))

#Store result to file
with open('result.txt', 'w') as file:
    for data in result_angle:
        file.write("%i\n" % data)