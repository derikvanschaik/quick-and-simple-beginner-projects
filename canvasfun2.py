from textwrap import fill
import PySimpleGUI as sg
# animating a circle which gets smaller and smaller after every click on canvas element
# to notify the user where they clicked ! 
def main():
    bott_left, top_right, centre = (0,0), (100,100), (50,50)
    canvas = sg.Graph(
        (500, 500), bott_left, top_right, key='CANV',
        background_color='white',
        enable_events = True, drag_submits=True
         )
    layout = [[canvas]]
    window = sg.Window('tester', layout)
    # timeout varialble 
    animation_timeout = None 
    click_cursor = {'location': None, 'radius': None, 'figure-id': None} # init the click_cursor object 
    while(True):
        event, values = window.read(timeout = animation_timeout)
        # print(animation_timeout)
        if event == "CANV":
            animation_timeout = 25 #  ms timeout
            click_cursor['location'] = values[event]
            init_radius = 8 # initial length of radius of cirlce
            click_cursor['radius'] = init_radius

        if event == sg.WIN_CLOSED:
            break 
        if click_cursor['radius']: 
            canvas.delete_figure( click_cursor['figure-id'] )
            click_cursor['radius'] -= 1 

        if click_cursor['radius'] == 0:
            click_cursor['location'] = None
            click_cursor['radius'] = None
            click_cursor['figure-id'] = None
            animation_timeout = None
        else:
            try: 
                click_cursor['figure-id'] = canvas.draw_circle(
                    click_cursor['location'],
                    click_cursor['radius'],
                    line_color='RoyalBlue'
                )
            except Exception as e:
                print(f"ERROR DELETING: {e}")

    window.close() 
if __name__ == "__main__":
    main() 