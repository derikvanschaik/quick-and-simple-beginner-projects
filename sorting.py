import PySimpleGUI as sg 
import random 

def create_array(max_height, num_of_rects):
	rand_values= [] 
	for i in range( int(num_of_rects) ):
		value = random.choice(range(1, int( max_height) )) 
		rand_values.append(value )
	return rand_values 


def insertion_sort(arr): 
	list_of_stages = [] # list of each stage list
	# grab initial stage prior to any sorting for animation 
	stage_list = [] 
	for value in arr:
		stage_list.append(value)
	list_of_stages.append(stage_list) 
  
	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):
  
		key = arr[i]
  
		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i-1
		while j >=0 and key < arr[j] :
				arr[j+1] = arr[j]
				j -= 1
		arr[j+1] = key
		# grab stage 
		stage_list = [] 
		for value in arr:
			stage_list.append(value)
		list_of_stages.append(stage_list)

	return list_of_stages

  

def selection_sort(A): 
	list_of_stages = [] # list of each stage list
	# grab initial stage prior to any sorting for animation 
	stage_list = [] 
	for value in A:
		stage_list.append(value)
	list_of_stages.append(stage_list) 

	# selection sort copied and pasted from  geeks for geeks
	for i in range(len(A)):
	  
		# Find the minimum element in remaining 
		# unsorted array
		min_idx = i
		for j in range(i+1, len(A)):
			if A[min_idx] > A[j]:
				min_idx = j
				  
		# Swap the found minimum element with 
		# the first element        
		A[i], A[min_idx] = A[min_idx], A[i]
		# copy current stage's array 
		stage_list = [] 
		for value in A:
			stage_list.append(value)
		list_of_stages.append(stage_list)

	return list_of_stages 


def animate_sort(stages_array, stage, canvas, width_of_rect):
	
	start = 0
	if stage < len(stages_array):
		canvas.erase()  
		for index, value in enumerate(stages_array[stage]):  
			top_left = (start, value)
			bott_right = (start + width_of_rect, 0)  
			start += width_of_rect

			canvas.draw_rectangle( top_left, bott_right) 


def main():
	layout = [
	[sg.Input("", key='-user-input-')],
	[sg.T('values in random array'), sg.Slider(range = (1, 250), key = '-slider-', enable_events=True, orientation="horizontal")], 
	[sg.Button("start animation:")], 
	[sg.Input("", key = "speed", enable_events=True)],
	[sg.Text("selection sort: ")],
	[sg.Graph((250, 250), (0, 0), (250, 250), background_color = "white", enable_events = True, key = "-canvas-selection-")],
	[sg.Text("insertion sort: ")],
	[sg.Graph((250, 250), (0, 0), (250, 250) , background_color = "white", enable_events = True, key = "-canvas-insertion-")]   
	]
	window = sg.Window("tester", layout)
	animating = False
	stage = 0
	stages_array = []
	stages_array_insertion = [] 
	width_of_rect = None
	new_max_screen_size = 250 #init value 
	num_of_rects = None
	speed = 500 

	while True:
		event, values = window.read(timeout = speed if animating else None)  
		canvas = window['-canvas-selection-'] 

		if event in (None, sg.WIN_CLOSED): 
			break
		if event == "start animation:":  

			if values['-user-input-']:  
				series_to_sort = [ int(element) for element in values['-user-input-'].split(" ") if element ]
				num_of_rects = len(series_to_sort)
				new_max_screen_size = max(series_to_sort)
			else:
				num_of_rects = values['-slider-']
				series_to_sort = create_array(new_max_screen_size, int(values['-slider-'])  ) 

			init_series_to_sort = [value for value in series_to_sort] #snapshots unsorted array 
			stages_array = selection_sort(series_to_sort)
			stages_array_insertion = insertion_sort(init_series_to_sort)  
			new_max_screen_size += new_max_screen_size/10     
			width_of_canvas = 500 # fixed variable 
			width_of_rect = width_of_canvas/num_of_rects
			# apply changes to both canvases 
			canvas.change_coordinates( (0, 0), (width_of_canvas, new_max_screen_size))
			window['-canvas-insertion-'].change_coordinates( (0, 0), (width_of_canvas, new_max_screen_size))
			animating = True

		if event == "speed":
			speed = int(values[event]) 

		if animating:
			animate_sort(stages_array, stage, canvas, width_of_rect)
			animate_sort(stages_array_insertion, stage, window['-canvas-insertion-'], width_of_rect)
			stage += 1   

			if (stage >= len(stages_array)):  
				animating = False
				stage = 0 


	window.close()

if __name__ == '__main__': 
	 main() 