import PySimpleGUI as sg 

BG_COL = 'white'
def main():
	sg.theme('Material1')
	layout = [
		[sg.T('chars left: 25', key='char-out', background_color=BG_COL, size=(10,1))],
		[sg.Multiline('', key='input', size=(50, 5), background_color = BG_COL, enable_events=True)],
		[sg.B('Post')]
	]

	window = sg.Window('', layout, background_color=BG_COL)
	MAX_CHARS = 25
	while True:
		
		event, values = window.read()
		if event == sg.WIN_CLOSED:
			break

		text = values['input'].replace('\n', '')
		char_count = len(text)
		window['input'].update("")
		window['char-out'].update(f'chars left: {MAX_CHARS-char_count}')
		window['Post'].update(disabled= char_count > MAX_CHARS)
		window['input'].print(text[:MAX_CHARS], text_color='black', end="")
		window['input'].print(text[MAX_CHARS:] if len(text) > MAX_CHARS else '', text_color='white', background_color='red', end="")

	window.close()

if __name__ == '__main__':
	main()