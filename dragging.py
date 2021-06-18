import PySimpleGUI as sg 

BG = 'white'

def in_bounds(canvas_size, loc):
	max_x, max_y = canvas_size[0], canvas_size[1]
	x, y = loc[0], loc[1]
	return 0<x<max_x and 0<y<max_y

def main():
	sg.theme('Material1')
	size = (400,400)
	bott_left, top_right = (0, 0), (400,400)
	canvas = sg.Graph(size, bott_left, top_right, enable_events = True, drag_submits=True, key='canvas', background_color= BG)
	layout = [[canvas]]
	window = sg.Window('', layout).finalize()
	figure = canvas.draw_point((200,200), size=20, color='RoyalBlue')
	fig_loc = (200,200)
	dragging = False
	dragging_texts = {False: 'Not currently dragging', True:'currently dragging'}
	user_action_feedback = canvas.draw_text(f'You are {dragging_texts[dragging]}.', (200, 375), font='digital')

	while True:
		
		event, values = window.read()
		dragged_loc = values['canvas']
		#print(event) <- THE MOST HELPFUL DEBUGGER WHEN IT COMES TO THE GRAPH ELEMENT
		if event == sg.WIN_CLOSED:
			break

		deltas = (dragged_loc[0]-fig_loc[0],dragged_loc[1]-fig_loc[1])
		dragging = all(map(lambda delta: abs(delta) in range(0, 25), deltas)) and not event.endswith('+UP')# if the object is within a 25 point range---then you are dragging

		if dragging and in_bounds(size, dragged_loc):
			delta_x, delta_y = deltas
			canvas.move_figure(figure, delta_x, delta_y)
			fig_loc = (dragged_loc[0], dragged_loc[1])

		canvas.delete_figure(user_action_feedback)
		user_action_feedback = canvas.draw_text(f'You are {dragging_texts[dragging]}.', (200, 375), font='digital')
		canvas.send_figure_to_back(user_action_feedback)


	window.close()

if __name__ == '__main__':
	main()