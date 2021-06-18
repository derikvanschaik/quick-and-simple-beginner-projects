import PySimpleGUI as sg 

BG = 'white'

def update_cur_pos_label(cur_pos, label, label_pos, canvas):
	canvas.delete_figure(label)
	return canvas.draw_text(f"Point current position: {cur_pos}", label_pos)

def main():
	sg.theme('Material1')
	size = (400,400)
	bott_left, top_right = (0, 0), (400,400)
	canvas = sg.Graph(size, bott_left, top_right, enable_events = True, key='canvas')
	# If we use the return keyboard events we cannot simply hold down a key and have a new event occur
	# so this is a hack to make holding down a key trigger events: 
	keyboard_input = sg.Input('', key='keyboard_input', enable_events = True, background_color = BG, text_color=BG)
	layout = [[canvas],[keyboard_input]]
	window = sg.Window('', layout, background_color=BG).finalize()
	keyboard_input.Widget.config(insertbackground=BG) #makes the cursor color the background color, now this is invisible
	window['canvas'].draw_line(bott_left, top_right)
	cur_pos = (5,5)
	point = canvas.draw_point(cur_pos, size=20, color='red')
	label_pos = (150,350)
	point_label = canvas.draw_text(f'Point current position: {cur_pos}', label_pos, font='digital') 
	UP_KEY = 'j'
	DOWN_KEY = 'k'
	while True:
		
		event, values = window.read()
		if event == sg.WIN_CLOSED:
			break
		if event == 'keyboard_input':
			key_pressed = values['keyboard_input'][-1]#last char pressed 
			shift = 0 
			if key_pressed == UP_KEY and cur_pos < top_right:
				shift = 1
			elif key_pressed == DOWN_KEY and cur_pos > bott_left:
				shift = -1 
			cur_pos = tuple(map(lambda point: point + shift ,cur_pos) ) #shifts both points by one (going up the line)
			canvas.move_figure(point, shift, shift)
			point_label = update_cur_pos_label(cur_pos, point_label, label_pos, canvas) #updates the label 

	window.close()

if __name__ == '__main__':
	main()