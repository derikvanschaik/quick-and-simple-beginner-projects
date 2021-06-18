import PySimpleGUI as sg 

BG = 'white'

def update_cur_pos_label(cur_pos, label, label_pos, canvas):
	canvas.delete_figure(label)
	return canvas.draw_text(f"Point current position: {cur_pos}", label_pos)

def main():
	sg.theme('Material1')
	size = (600,600)
	bott_left, top_right = (-100, -100), (500,500)
	canvas = sg.Graph(size, bott_left, top_right, enable_events = True, drag_submits=True, key='canvas')
	# If we use the return keyboard events we cannot simply hold down a key and have a new event occur
	# so this is a hack to make holding down a key trigger events: 
	keyboard_input = sg.Input('', key='keyboard_input', enable_events = True, background_color = BG, text_color=BG)
	layout = [[canvas],[keyboard_input]]

	window = sg.Window('', layout, background_color=BG).finalize()
	keyboard_input.Widget.config(insertbackground=BG) #makes the cursor color the background color, now this is invisible

	y_axis = canvas.draw_line((0,0), (0,400))
	x_axis = canvas.draw_line( (0,0), (400, 0))
	upwards_plotted_line = canvas.draw_line((0,0), (400,400))
	downwards_plotted_line = canvas.draw_line((0,350), (350, 0))
	demand_point_loc = (0,350)
	demand_point = canvas.draw_point(demand_point_loc, size=15, color='red')
	cursor_loc = (0,0)
	cursor = canvas.draw_point(cursor_loc, size=15, color='RoyalBlue')
	rect_area = None
	y_line = None
	x_line = None
	vert_line = None
	horiz_line = None
	SHIFT_AMOUNT = 2
	UP_KEY, DOWN_KEY = 'j', 'k'

	while True:
		
		event, values = window.read()
		print(event)
		figures = [y_line, x_line, horiz_line, vert_line]
		if event == sg.WIN_CLOSED:
			break
		if event == 'keyboard_input':
			key_pressed = values['keyboard_input'][-1]#last char pressed 
			user_shift = (0,0)
			demand_shift = (0,0)

			if key_pressed == UP_KEY and cursor_loc < (400,400): #top of our graph within the canvas				
				user_shift = (SHIFT_AMOUNT, SHIFT_AMOUNT)
				demand_shift = (SHIFT_AMOUNT, -SHIFT_AMOUNT)

			elif key_pressed == DOWN_KEY and cursor_loc > (0,0): #bottom of our math graph within canvas
				user_shift = (-SHIFT_AMOUNT, -SHIFT_AMOUNT)
				demand_shift = (-SHIFT_AMOUNT, SHIFT_AMOUNT)

			#move the point on the y=x (upwards sloping curve) in the direction of user input
			cursor_loc = tuple(map(lambda loc, delta: loc+delta,  cursor_loc, user_shift))
			canvas.move_figure(cursor, user_shift[0], user_shift[1])
			#move the point on the downwards sloping curve by the same corresponding amounts mapped to that curve
			demand_point_loc = tuple(map(lambda loc, delta: loc+delta,  demand_point_loc, demand_shift))
			print(f"demand point at location: {demand_point_loc}")
			canvas.move_figure(demand_point, demand_shift[0], demand_shift[1])

			#delete previously drawn figures 
			figs_to_del = filter(lambda line: line is not None,[y_line, x_line, horiz_line, vert_line, rect_area]) 
			for fig in figs_to_del:
				canvas.delete_figure(fig)

			#draw the lines 
			y_line = canvas.draw_line((0,cursor_loc[1]), cursor_loc, color='orange')
			x_line = canvas.draw_line((cursor_loc[0], 0), cursor_loc, color='orange')
			horiz_line = canvas.draw_line((0, demand_point_loc[1]), (cursor_loc[0], demand_point_loc[1]), color='red')
			vert_line = canvas.draw_line((cursor_loc), (demand_point_loc), color='red')
			rect_area = canvas.draw_rectangle((0, cursor_loc[1]),(demand_point_loc), fill_color='red')

			for line in [y_line, x_line, horiz_line, vert_line, rect_area]:
				canvas.send_figure_to_back(line)


	window.close()

if __name__ == '__main__':
	main()