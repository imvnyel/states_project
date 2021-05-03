import pandas as pd
import Easy_df as edf
import PySimpleGUI as sg


filename = 'C:/Users/ekaunda/Downloads/Date-Year-State-Flow-Country-HS6.csv'

df_to_export = []

def GeoGui():
	columns = []
	menu_def = [['File', 'Exit'],
	['Help', 'About']]

	#Theme 
	sg.theme('dark grey 9')


	#set GUI layout
	layout = [[sg.Menu(menu_def, )],
	[sg.Text('Select File (.xlsx or .csv): '), sg.In(key='Report'), sg.FileBrowse(target='Report', size=(10, 1))],
	[sg.Button('Intialize', size=(72, 1))],
	[sg.Text('Group by column: '), sg.Combo(columns, key='ChoiceColumn', size=(30, 6)), sg.Button('Group', size=(35, 1))],
	[sg.Button('Export to Excel', size=(35, 1)), sg.Button('Export to CSV', size=(35, 1))],
	[sg.Multiline(size=(100,20), autoscroll=True, write_only=True, auto_refresh=True, reroute_stdout=True, key='print_output')]]

	window = sg.Window('Excel Parser', layout, auto_size_buttons=True, auto_size_text=True ,resizable=True)

		#Loop
	while True:
		event, values = window.read()
		#db_init()

		#Initialize project. Open file, convert into a Pandas dataframe, return cleaned dataframe. 
		if event == 'Intialize':
			file_to_read = values['Report']
			window['print_output']('')
			try:
				d = edf.Dataframe()
				new_df = d.create_df(file_to_read)
				columns = [str(i) for i in new_df.columns.tolist()]
				print('Preview\n', new_df.head())
				window.Refresh()
				window.FindElement('ChoiceColumn').Update(values=columns)
			except Exception as e: print(e)

		#Initialize project. Open file, convert into a Pandas dataframe, return cleaned dataframe. 
		if event == 'Group':
			column_name = values['ChoiceColumn']
			window['print_output']('')
			try:
				d.group_df(column_name)
				print('{0} Dataframes ready for export'.format(len(d.dataframes)))
				print('Content: ')
				for i in d.dataframes:
					print(i.keys())
				window.Refresh()
			except Exception as e: print(e)

		#Export dataframe with completed DM columns to Excel
		if event == 'Export to Excel':
			file_to_read = values['Report']
			try:

				#export dataframe(s)
				print('Staring Excel Exporter...')
				d.excel_exporter()

				print('Exporting New Excel...')
				print('Successful!')

				#log_db(file_to_read)
				window.Refresh()
			except Exception as e: print(e)

		#Export dataframe with completed DM columns to Excel
		if event == 'Export to CSV':
			file_to_read = values['Report']
			try:

				#export dataframe(s)
				print('Staring CSV Exporter...')
				d.csv_exporter()

				print('Exporting to Database...')
				print('Successful!')
				#log_db(file_to_read)
				window.Refresh()


			except Exception as e: print(e)

		if event == 'About':      
			sg.popup('About this program', 'Version 1.0', 'Created by Emmanuel Kaunda')

		if event == sg.WINDOW_CLOSED or event == 'Exit':
			#c.close()
			#l.close()
			break

#######RUN PROGRAM#######

GeoGui()

'''df = edf.Dataframe(filename)
df.create_dataframe()
output = df.group_df()
df.csv_exporter(output)'''

'''df = create_dataframe(filename)
frames, names = parse_dataframes(df)
if '.csv' in filename:
	csv_exporter(frames, names)
elif '.xlsx' in filename:
	excel_exporter(frames, names)'''