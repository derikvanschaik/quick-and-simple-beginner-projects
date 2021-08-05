from textwrap import fill
import PySimpleGUI as sg


def get_selected_color(colors, values):
    for key, val in values.items():
        if key in colors:
            if val: #selected
                return key # return the selected color - note that we by default always have one selected. 

def main():
    bott_left, top_right, centre = (0,0), (100,100), (50,50)
    canvas = sg.Graph(
        (500, 500), bott_left, top_right, key='CANV',
        background_color='white',
        enable_events = True, drag_submits=True
         )
    colors = ("Blue", "Red", "Green", "Yellow")
    layout = [[sg.Button("Draw Circle"), sg.Button("Draw Rectangle")],
            [sg.Radio(text= color, group_id = "colors", default=(color=="Blue"), key=color) for color in colors],
            [canvas]
             ]
    window = sg.Window('tester', layout)
    shapes = {} # dictionary where the key is the id of the shape drawn, and value is list: [location, shape_type]
    while(True):
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event in ("Draw Circle", "Draw Rectangle"):
            color_of_shape = get_selected_color(colors, values)
            shape_type = event.split(" ")[-1]
            shape_id = None
            
            if shape_type == "Circle": 
                radius = 2
                shape_id = canvas.draw_circle(centre, radius, fill_color = color_of_shape)

            elif shape_type == "Rectangle":
                height, width = 4, 8 # arbitrary values we set for the dimensions of all rectangles 
                centre_x, centre_y = centre 
                top_left = (centre_x + (width//2), centre_y - (height//2))
                bott_right = (centre_x - (width//2), centre_y + (height//2))
                shape_id = canvas.draw_rectangle(top_left, bott_right, fill_color=color_of_shape)

            shapes[shape_id] = [centre, shape_type]
        
        if event == "CANV":
            location_of_click = values[event] # (x,y) of click
            x_click, y_click = location_of_click
            for fig, [loc, shape_type] in shapes.items():
                current_location = loc 
                x_shape,y_shape = current_location
                threshold = 3 # sort of like a radius hotspot we will use to determine if user is dragging an object
                # move the figure to x_click and y_click if shape within threshold 
                if abs(x_click-x_shape) <=threshold and abs(y_click-y_shape)<= threshold:
                    canvas.relocate_figure(fig, x_click, y_click) 
                    shapes[fig] = [location_of_click, shape_type]
                    break # this stops us from 'eating' other shapes 

                

    window.close() 
if __name__ == "__main__":
    main() 