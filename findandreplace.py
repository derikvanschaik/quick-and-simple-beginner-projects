import PySimpleGUI as sg 

BG = 'white'
def main():
	sg.theme('Material1')
	layout = [
		[sg.T('Find:', size=(15,1), background_color = BG), sg.Input('', k ='find', size=(15,1)),sg.Button('Find') ],
		[sg.T('Replace with:', size=(15,1), background_color = BG), sg.Input('', k ='replace', size=(15,1)), sg.Button('Replace')],
		[sg.Text('', size=(40, 1), key='replace-info', background_color = BG)], 
		[sg.Multiline('', key='input', size=(50, 10), background_color = BG, enable_events = True)],
		]

	window = sg.Window('', layout, background_color=BG ).finalize() 
	window['input'].set_focus()
	MAX_CHARS = 25
	while True:
		
		event, values = window.read()
		if event == sg.WIN_CLOSED:
			break

		#Only works for when the text was actually typed directly into the multiline input, if you 
		# copy and paste something from online you will notice that there is odd behaviour, this is due to 
		# new lines and other whitespace being present. 
		
		if event == 'Find':
			text = values['input'] 
			window['input'].update("")
			word_count = 0 
			for word in text.split(" "):
				color = 'black'
				if word.lower().startswith(values['find'].lower()):
					color = 'purple'
					word_count += 1
				window['input'].print(word, text_color=color, end=" ")
				window['replace-info'].update(f'found {word_count} instances of {values["find"]}.')


		if event == 'Replace':
			text = values['input'].replace('\n', '')
			window['input'].update("")
			replace_count = 0
			for word in text.split(" "):
				color = 'black'
				if word.lower().startswith(values['find'].lower()):
					word = values['replace']
					color = 'green'
					replace_count += 1
				window['input'].print(word, text_color=color, end=" ")
				window['replace-info'].update(f'Replaced {replace_count} instances of `{values["find"]} to {values["replace"]}.')



	window.close()

if __name__ == '__main__':
	main()