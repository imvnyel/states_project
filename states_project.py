import pandas as pd
#import PySimpleGUI as sg

filename = 'C:/Users/ekaunda/Downloads/Date-Year-State-Flow-Country-HS6.csv'

df_to_export = []

def create_dataframe(filename):

	if '.csv' in filename:
		df = pd.read_csv(filename)
	elif '.xlsx' in filename:
		df = pd.read_excel(filename)
	else:
		print('INVALID FILE FORMAT!\n use .csv or .xlsx files')

	return df


def parse_dataframes(df):
	cols = [str(i) for i in df.columns.tolist()]

	for x in range(len(cols)):
		print(x+1, cols[x])

	choice = input('Choose a column to groupby: ')
	s = int(choice) - 1
	print('You have chosen to group columns by {0}'.format(cols[s]))

	column_name = cols[s]

	names = [x for x in df[column_name].unique()]
	grouped = []

	for name in names:
		grouped_df = df[df[column_name] == name]
		grouped.append(grouped_df)
	return grouped, names

#Export dataframes to csv files
def csv_exporter(frames, names):
    export_folder = 'C:/Users/ekaunda/Desktop/outputs/'
    file_out = [export_folder + name + '.csv' for name in names]
    df_dict = [{k:v} for k,v in zip(names, frames)]

    for i in range(len(df_dict)):
        for k,v in df_dict[i].items():
            v.to_csv(file_out[i])
            print('Successfully exported {0} data to {1}'.format(k, export_folder))

#Export dataframes to excel files
def excel_exporter(frames, names):
	export_folder = 'C:/Users/ekaunda/Desktop/outputs/'
	file_out = [export_folder + name + '.excel' for name in names]
	df_dict = [{k:v} for k,v in zip(names, frames)]

	for i in range(len(df_dict)):
		for k,v in df_dict[i].items():
			v.to_excel(file_out[i])
			print('Successfully exported {0} data to {1}'.format(k, export_folder))


#######RUN PROGRAM#######
df = create_dataframe(filename)
frames, names = parse_dataframes(df)
if '.csv' in filename:
	csv_exporter(frames, names)
elif '.xlsx' in filename:
	excel_exporter(frames, names)