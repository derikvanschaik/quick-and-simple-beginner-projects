import PySimpleGUI as sg

def draw_rectangles(canvas, num_of_part, range_tup, func):
    (a,b) = range_tup #unpack tuple 
    increment = (b-a)/num_of_part # the width of each rectangle d
    drawn_figs = [] # list keeping the ids of drawn_figures in order to delete them later
    i = a
    count = 0 # need to keep track of the number of loops for a special case 
    while(i + increment <= b): #cannot use range function as increment is a float 
        midpoint = (i + i + increment)/ 2
        midpoint_val = func(midpoint) #this will be the height of the rectangle
        # draw_rectangle takes bott_left point and top_right 
        drawn_figs.append(
            canvas.draw_rectangle((i, 0), (i+increment, midpoint_val), line_color="purple", fill_color="beige")
                        )
        canvas.send_figure_to_back(drawn_figs[-1])
        i += increment # increment i to next interval in partition
        count += 1 
        #draw point at intersection of curve and rectangle - (midpoint, midpoint_val)

     # In order for smooth animation we need to have the same amount of rectangles 
     # as partitions 
    allowable_error = 0.3
    if (count < num_of_part and i + increment <= b + allowable_error):
        midpoint = (i + i + increment)/ 2
        midpoint_val = func(midpoint) #this will be the height of the rectangle
        # draw_rectangle takes bott_left point and top_right 
        drawn_figs.append(
            canvas.draw_rectangle((i, 0), (i+increment, midpoint_val), line_color="purple", fill_color="beige")
                        )
        canvas.send_figure_to_back(drawn_figs[-1])

    return drawn_figs # return list of reference ids


def draw_label(loc, canvas_size, canvas):
    bott_left, top_right = canvas_size
    canvas_height = top_right[1] - bott_left[1]
    label_height = 10 # we let the label height be 10 
    label_text_size = 5
    label_pad = 5
    vertical_pad = 5
    if canvas_height - (loc[1]+label_height+label_text_size+label_pad) >= vertical_pad:
        return (
            canvas.draw_line((loc), (loc[0], loc[1] + label_height)),
            canvas.draw_text(f"{loc}", (loc[0],loc[1] +label_height+label_pad ))
        )
    # else case
    return (
        canvas.draw_line(loc, (loc[0] - label_height, loc[1])), 
        canvas.draw_text(f"{loc}", (loc[0] - label_height-label_pad, loc[1] ))
        )


def in_bounds(loc,canvas_size):
    (x_0, y_0), (x_1, y_1) = canvas_size
    x,y = loc 
    # bott left,top right of canvas
    inside_canvas = (x >= x_0 and y >= y_0) and (x <= x_1 and y <= y_1)
    return inside_canvas

def main():
    num_of_part = 4 # number of partitions
    range_interv = (5,95) # [a,b] for reimen sum approx
    bott_left, top_right = (0,0), (100,100)
    canvas = sg.Graph(
        (500, 500), bott_left, top_right, key='CANV',
        background_color='white', float_values=True,
        enable_events = True, drag_submits=True
         )

    slider = sg.Slider(range=(4,80), default_value=num_of_part, key="SLIDER", orientation="horizontal", enable_events=True)
    layout = [[sg.T("Number of partitions: "), slider, sg.T("<- Slide to right to increase num of rectangles")],[canvas]]
    window = sg.Window('Midpoint Reimen sum approximation', layout=layout).finalize()
    # drawing figures on canvas 
    canvas.draw_line((0,0), (100,100), color='red', width=2) # this is the y =x line 
    #draw endpoints for the interval [a,b] for reimen sum approx 
    point_a = canvas.draw_point((5,5), color='blue', size=2 ) 
    point_b = canvas.draw_point( (95,95), color='blue', size=2)
    # draw initial rectangles for our number of partitions currently at 4 
    rectangles = draw_rectangles(canvas, num_of_part, range_interv, lambda x: x) # y = x is our callback function arg
    # variables to track where the points in interval (a,b) are
    loc_a,loc_b  = (range_interv[0], range_interv[0]), (range_interv[1], range_interv[1])
    label_a = draw_label(loc_a, (bott_left, top_right), canvas)
    label_b = draw_label(loc_b, (bott_left, top_right), canvas)


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


        if event == 'CANV':
            print(values[event])
            (a, b) = range_interv #unpack the values from the tuple 
            (x,y) = values[event] # x and y coordinates of click on canvas
            threshold = 9 # the points 'hotspot'
            dragged = False 
            if abs(x-a) < threshold and abs(y-a) < threshold: # clicked and are dragging lower interval a 
                loc_a = (x,x)
                if in_bounds(loc_a,(bott_left,top_right)):
                    # delete figures  
                    canvas.delete_figure(point_a)
                    label_line, label_text = label_a
                    canvas.delete_figure(label_line)
                    canvas.delete_figure(label_text)
                    # since the function is y = x we draw at (x,x) or else point would be swivelling to wherver mouse goes
                    # -- we want it to stay fixed on the y = x line
                    point_a= canvas.draw_point(loc_a, size=2, color="blue")
                    label_a = draw_label(loc_a, (bott_left, top_right), canvas)
                    range_interv = (x, range_interv[1]) 
                    dragged = True
            elif abs(x-b) < threshold and abs(y-b) < threshold: #clicked and are dragging higher interval b
                loc_b = (x,x)
                if in_bounds(loc_b, (bott_left,top_right)): 
                    #delete the figures 
                    canvas.delete_figure(point_b)
                    label_line, label_text = label_b
                    canvas.delete_figure(label_line)
                    canvas.delete_figure(label_text)
                    point_b = canvas.draw_point(loc_b, size=2, color="blue")
                    label_b = draw_label(loc_b, (bott_left, top_right), canvas)
                    range_interv = (range_interv[0], x) 
                    dragged = True 
            # if we changed either points we need to draw new rectangles re update text on canvas 
            if dragged:
                for rect in rectangles:
                    canvas.delete_figure(rect) # delete the currently drawn rectangles 
                # redraw the rectangles with new num of partitions 
                rectangles = draw_rectangles(canvas, num_of_part, range_interv, lambda x: x)
                

            

    window.close() 
if __name__ == "__main__":
    main() 