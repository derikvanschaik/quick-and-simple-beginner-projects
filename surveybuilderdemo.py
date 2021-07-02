import PySimpleGUI as sg

sg.theme('Material2')
# parameters - question_layout - list of lists 
def build_layout(question_layout):
	column_layout = [] 
	for layout in question_layout: 
		question_type = layout[-1]
		question = layout[0]
		col_layout = [[sg.Text(question)]] 
		if question_type == 'input':
			col_layout.append([sg.Input(key = question)])
			
		elif question_type == 'radio':

			options = layout[1]
			radios = []
			for option in options:
				radio = sg.Radio(option, question, key = option)
				radios.append(radio)
			col_layout.append(radios)

		else:
			options = layout[1]
			checkboxes = []
			for option in options:
				checkbox = sg.Checkbox(option, key = option)
				checkboxes.append(checkbox)
			col_layout.append(checkboxes)

		column_layout += col_layout

	return sg.Column(column_layout, scrollable = True, size = (400, 400))

def ending_page(question_layout, values):
	column_layout = []
	for q_info in question_layout:
		q_type = q_info[-1]
		q = q_info[0]
		question_title = ["You answer to", q_info[0], "was:"]
		question_title = list(map(lambda q: sg.Text(q, font = "default 9 italic" if question_title.index(q) == 1 else "default 9"), question_title))
		column_layout.append(question_title)
		# [sg.Text(f"Your answer(s) to '{q.upper()}' was:")]

		if q_type == 'input':
			column_layout.append( [ sg.Text(f"\t-{values[q]}")])
			
		else:
			options = q_info[1]
			answered = [] 
			for option in options:
				if values[option]: #if it was the answer...
					answered.append(option)
			for answer in answered:
				column_layout.append( [ sg.Text(f"\t-{answer}")])

	layout = [[sg.Column(column_layout,scrollable = True, size = (400, 400))]]
	return sg.Window('Thank you for completing the survey!', layout)

def main():
	list_of_q_list = [
		['what is your name', 'input'],
		['what is your age', 'input'],
		['select your favorite', ['one', 'two'], 'radio'], 
		['select all that apply', ['i love coding', 'i like python', 'pysimplegui is the best library ever'], 'checkbox'], 
		['How are you today', ['great', 'not so great'], 'radio'], 
		['sldfjsdfs', ['sdkfsdf', 'sdlkfsldfj'], 'radio'], 
		['selectsdfsdfsde', ['ororor', 'skfjsdlskd'], 'radio'], 
		['selsdfsdfdsf', ['onsdfsdfsd', 'twsdfsdfo'], 'radio'], 
		['selectsdfsdfsdffds', ['offffne', 'twddo'], 'radio'], 
		['selectsdfsdfse33333', ['onfffffe', 'tffffwo'], 'radio'], 
		['select3333333333333rite', ['onsdfsdsdfe', 'twsdfsdfso'], 'radio'], 
	]

	layout = [[build_layout(list_of_q_list)]] + [[sg.Button('Submit')]]
	window = sg.Window('', layout)
	while True:
		event, values = window.read()
		if event in (None, sg.WIN_CLOSED):
			break
		if event == 'Submit':
			# validate the inputs
			answered_all = True
			for question_info in list_of_q_list:
				question_type = question_info[-1]
				keys = [] 
				if question_type == 'input': 
					keys = [question_info[0]]
				else:
					keys = question_info[1] 
				answered_question = False
				for key in keys:
					answered_question = answered_question or values[key]
				answered_all = answered_all and  answered_question 

			if answered_all:
				window.close()
				window = ending_page(list_of_q_list, values)
			else:
				sg.popup("You did not answer all questions.")

	window.close()
if __name__ == '__main__':
	main()