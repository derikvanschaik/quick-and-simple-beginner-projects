import PySimpleGUI as sg

def draw_rectangles(canvas, num_of_part, range_tup, func):
    (a,b) = range_tup #unpack tuple 
    increment = (b-a)/num_of_part # the width of each rectangle d
    drawn_figs = [] # list keeping the ids of drawn_figures in order to delete them later
    i = a  
    while(i + increment <= b): #cannot use range function as increment is a float 
        midpoint = (i + i + increment)/ 2
        midpoint_val = func(midpoint) #this will be the height of the rectangle
        # draw_rectangle takes bott_left point and top_right 
        drawn_figs.append(
            canvas.draw_rectangle((i, 0), (i+increment, midpoint_val), line_color="purple", fill_color="beige")
                        )
        canvas.send_figure_to_back(drawn_figs[-1])
        i += increment # increment i to next interval in partition 
        #draw point at intersection of curve and rectangle - (midpoint, midpoint_val)
    return drawn_figs # return list of reference ids

def calculate_area(num_of_part, range_tup, func):
    (a,b) = range_tup #unpack tuple 
    increment = int((b-a)/num_of_part) # the width of each rectangle d
    sum = 0 # sum of areas 
    i = a
    while(i+increment<=b):
        midpoint = (i + i + increment)/ 2
        midpoint_val = func(midpoint) #this will be the height of the rectangle
        # calculate the area of the rectangle 
        height = midpoint_val 
        len = increment
        sum += height*len
        i += increment  
    return sum 

def main():
    num_of_part = 4 # number of partitions
    range_interv = (5,95) # [a,b] for reimen sum approx 
    canvas = sg.Graph((500, 500), (0,0),(100,100), key='CANV', enable_events = True,  background_color='white', float_values=True)

    slider = sg.Slider(range=(4,80), default_value=num_of_part, key="SLIDER", orientation="horizontal", enable_events=True)
    layout = [[sg.T("Number of partitions: "), slider, sg.T("<- Slide to right to increase num of rectangles")],[canvas]]
    window = sg.Window('Midpoint Reimen sum approximation', layout=layout).finalize()
    # drawing figures on canvas 
    canvas.draw_line((0,0), (100,100), color='red', width=2) # this is the y =x line 
    #draw endpoints for the interval [a,b] for reimen sum approx 
    canvas.draw_point((5,5), color='blue', size=1) 
    canvas.draw_point( (95,95), color='blue', size=1)
    # draw initial rectangles for our number of partitions currently at 4 
    rectangles = draw_rectangles(canvas, num_of_part, range_interv, lambda x: x) # y = x is our callback function arg
    area = calculate_area(num_of_part, range_interv, lambda x: x)
    error_text = canvas.draw_text(
        f"Error: |4500-{area}| = |{4500-area}| = {abs(4500-area)}",
         (10, 90), text_location=sg.TEXT_LOCATION_LEFT, color="red" if int(area) != 4500 else "green"
    )
    area_text = canvas.draw_text(
        f"Area over interval [{range_interv[0]}, {range_interv[1]}] for y=x: {area}",
         (10, 80), text_location= sg.TEXT_LOCATION_LEFT, font="digital",
        )
    

    while(True):
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "SLIDER":
            num_of_part = int(values[event])
            for rect in rectangles:
                canvas.delete_figure(rect) # delete the currently drawn rectangles 
            # redraw the rectangles with new num of partitions 
            rectangles = draw_rectangles(canvas, num_of_part, range_interv, lambda x: x)
            # recalculate the area 
            area = calculate_area(num_of_part, range_interv, lambda x: x)
            print("AREA:", area)
            # delete and redraw the area text
            canvas.delete_figure(area_text)
            canvas.delete_figure(error_text)
            area_text = canvas.draw_text(
                f"Area over interval [{range_interv[0]}, {range_interv[1]}] for y=x: {area}",
                 (10, 80), text_location=sg.TEXT_LOCATION_LEFT, font="digital"
                        )
            error_text = canvas.draw_text(
                f"Error: |4500-{area}| = |{4500-area}| = {abs(4500-area)}",
                (10, 90), text_location=sg.TEXT_LOCATION_LEFT, color="red" if int(area) != 4500 else "green"
            )

    window.close() 
if __name__ == "__main__":
    main() 