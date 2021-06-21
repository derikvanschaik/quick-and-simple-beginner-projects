import PySimpleGUI as sg
import random 

BG = 'white'



def plot_function(range_tuple, canvas, function, color = 'blue'):
	a, b = range_tuple
	lines = []
	points = [] 
	for x in range(a,b+1):
		point = (x, function(x) ) #Plots the function that was given as a callback parameter
		if points:
			last_point = points[-1]
			lines.append(canvas.draw_line(last_point, point, color))
		points.append(point)
	return lines #may want to delete these lines when plotting the tangency line

# need to import or create a function to calculate the slopes if we wish to program other functions 
# --for now this returns the function of x^2. 
def get_slope(x):
	return 2*x 

def main():
	sg.theme('Material1')
	size = (400,400)
	bott_left, top_right = (-25, -50), (25, 25**2)
	canvas = sg.Graph(size, bott_left, top_right, enable_events = True, key='canvas', background_color=BG)
	keyboard_input = sg.Input('', key='keyboard_input', enable_events = True, background_color = BG, text_color=BG)
	layout = [[canvas],[keyboard_input]]
	window = sg.Window('', layout).finalize()

	keyboard_input.Widget.config(insertbackground=BG) #makes the cursor color the background color, now this is invisible
	canvas.draw_text("Press 'j' key to increase x, press 'k' to decrease x ",(0, 20**2))
	plot_function((-25, 25), canvas, lambda x: x**2)
	point_loc = (-15, (-15)**2)
	point = canvas.draw_point((-15, (-15)**2), size=1)
	# Plot the initial tangency line
	a, b = point_loc[0] -5, point_loc[0] +5
	slope = get_slope(point_loc[0])
	constant = point_loc[1] - slope*point_loc[0] # y = mx + B --> B = y -mx 
	tangency_line_points = plot_function((a,b), canvas, lambda x: slope*x + constant, color='red')

	while True:
		
		event, values = window.read()

		if event in (None, sg.WIN_CLOSED):
			break
		if event == 'keyboard_input':
			slope = get_slope(point_loc[0])
			key = values[event][-1]
			shift = 0
			if key == 'j':
				shift = 1 
			elif key == 'k':
				shift = -1
			x, y = point_loc
			point_loc = (x + shift, (x+shift)**2)
			a, b = point_loc[0] -5, point_loc[0] +5
			constant = point_loc[1] - slope*point_loc[0] # y = mx + B --> B = y -mx 
			#delete the previously drawn tangency line (comprised of many lines)
			if tangency_line_points:
				for tangency_line in tangency_line_points:
					canvas.delete_figure(tangency_line)

			tangency_line_points = plot_function((a,b), canvas, lambda x: slope*x + constant, color='red')
			canvas.relocate_figure(point, point_loc[0], point_loc[1])	

	window.close()

if __name__ == '__main__':
	main()