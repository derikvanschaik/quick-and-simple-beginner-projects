import PySimpleGUI as sg
import math 

def main():
    canvas = sg.Graph((500, 500), (-500,-(500)), (500, (500)), key='CANV', enable_events = True,  background_color='white')
    slider = sg.Slider(range = (1, 10), enable_events= True, key = 'Slider', default_value= 10, orientation="horizontal")
    layout = [[sg.Text("speed: "), slider], [canvas]]
    window = sg.Window('hello', layout=layout).finalize()
    radius = 250
    canvas.draw_circle((0,0), radius)
    angle = 0 
    # the math for the line: 
    # x = r*cos(angle) 
    # y = r*sin(angle)
    x = radius*math.cos(math.radians(angle))
    y = radius*math.sin(math.radians(angle))
    line = canvas.draw_line( (0, 0), (x, y) )
    points = []
    angle_text = canvas.draw_text(f"{angle}°", (30,15), color="red") 
    slider_val = 1 #default timeout value 
    while(True):
        event, values = window.read(timeout = slider_val)
        if event == sg.WIN_CLOSED:
            break
        if event == 'Slider':
            slider_val = 10 - int(values[event]) #update speed 

        angle = (angle + 1)%360
        #delete figures 
        if angle != 1:
            canvas.delete_figure(line)
        else:
            for point in points:
                canvas.delete_figure(point)
        canvas.delete_figure(angle_text)
        # recalculate x and y pos from new incremented angle 
        x = radius*math.cos(math.radians(angle))
        y = radius*math.sin(math.radians(angle))

        line = canvas.draw_line( (0, 0), (x, y) )
        points.append(canvas.draw_point( (x/4, y/4) , size=1))
        angle_text = canvas.draw_text(f"{angle}°", (30,15), color="red") 

    window.close() 
if __name__ == "__main__":
    main() 