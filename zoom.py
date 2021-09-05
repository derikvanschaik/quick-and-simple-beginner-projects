import PySimpleGUI as sg

def main():
	layout = [
	# slider for zooming in and out 
	[sg.Slider(range= (-100, 23), default_value = 0 , key="zoom", enable_events = True, orientation="horizontal")],  
	[sg.Graph((450, 450), (0,0), (450, 450), enable_events = True, key="canvas", background_color = "white"), ], 
	]
	window = sg.Window("tester", layout)
	figures = [] # track figures drawn onto screen 
	while True:
		event, values = window.read()  

		if event in (None, sg.WIN_CLOSED): 
			break
		# user is clicking canvas 
		if event == "canvas":
			# draw a circle where user clicks on canvas
			figure = {}
			figure['location'] = values[event]
			figure['id'] = window[event].draw_circle( values[event], radius = 10) 
			figures.append(figure)  

		# user is zooming in or out 
		if event == "zoom":
			offset = int(values[event]) *10 
			top_right = (450-offset, 450-offset)
			bott_left = (0 +offset, 0+offset) 
			window['canvas'].change_coordinates(bott_left,top_right) 
			# delete and draw the figures on canvas to create zoom out effect
			for figure in figures: 
				window['canvas'].delete_figure(figure['id']) # delete circle
				# draw new circle at location and save it to id property of fig obj 
				figure['id'] = window['canvas'].draw_circle( figure['location'], radius = 10)


	window.close()

if __name__ == '__main__': 
	 main() 