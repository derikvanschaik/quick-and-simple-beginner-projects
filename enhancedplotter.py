import PySimpleGUI as sg
import random 

BG = 'white'

def draw_y_ticks(canvas, size):
	for i in range(0, size+50, 50):
		if i!= 0:
			canvas.draw_text(i, (-40, i))
			canvas.draw_line((-10, i), (0, i))

def draw_x_ticks(canvas, size):
	for i in range(0, size+50, 50):
		if i!= 0:
			canvas.draw_text(i, (i, -40))
			canvas.draw_line((i, -10), (i, 0))


def plot_points(num_points, max,trend, canvas, y_range):
	points = [] 
	step = max//num_points
	x = 0 
	for i in range(num_points):
		point = None
		if trend == 1:
			point = (x, random.randint(x, x +y_range))
		else:
			point = (x, random.randint(max-x-y_range, max-x))

		points.append(canvas.draw_point(point, size=7, color = 'green'))
		x += step 
	return points 
	

def main():
	sg.theme('Material1')
	size = (600,600)
	bott_left, top_right = (-100, -100), (500,500)
	num_points = 40
	y_range = 40

	canvas = sg.Graph(size, bott_left, top_right, enable_events = True, key='canvas', background_color=BG)
	trend_radios = [
		sg.Text('Trend: '), 
		sg.Radio('Upwards', group_id='trend-radio', enable_events=True, key='Upwards'),
		 sg.Radio('Downwards', group_id='trend-radio', enable_events=True, key='Downwards')
	 ]
	var_slider = [
		sg.Text(f'Variability:'),
	 	sg.Slider(range = (1, 100), default_value = y_range, 
	 	key='var', enable_events=True, orientation='h')
	 ]
	num_point_slider = [
		sg.Text(f'Number of Observations:'),
		sg.Slider(range = (1, 400), default_value = num_points, key='obs', enable_events=True, orientation='h')
	 ]

	layout = [trend_radios,var_slider,num_point_slider,  [canvas] ] 

	window = sg.Window('', layout).finalize()
	y_axis = canvas.draw_line((0,0), (0,400))
	x_axis = canvas.draw_line((0,0), (400,0))
	draw_y_ticks(canvas, 400)
	draw_x_ticks(canvas, 400)
	points = plot_points(num_points, 400, 1, canvas, y_range)
	# points = [(x, random.randint(x-50, x+50)) for x in range(50, 400, 50)]
	# for point in points:
	# 	canvas.draw_point(point, size=7, color = 'green')




	while True:
		
		event, values = window.read()
		# print(values[event])

		if event == sg.WIN_CLOSED:
			break

		if event in ('Upwards', 'Downwards', 'var', 'obs'):
			print("here")
			num_points = int(values['obs'])
			y_range = int(values['var'])
			trend = 1 if values['Upwards'] else -1
			for point in points:
				canvas.delete_figure(point)

			points = plot_points(num_points, 400, trend, canvas, y_range) #max is always 400 
		# print(event)

	

	window.close()

if __name__ == '__main__':
	main()