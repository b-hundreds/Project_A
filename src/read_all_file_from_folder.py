# Reading files


def read_all_file_from_folder(list_folder_direction):
    load_data = []
    for folder_direction in list_folder_direction:
        # Load direction all file txt in folder

        # Define list of file txt name
        data1 = os.listdir(folder_direction)
        path = []
        # Join direction of folder and file txt name
        for data_dic in data1:
            path.append(os.path.join(folder_direction, str(data_dic)).replace('\\', '/'))
        # Read file txt from direction
        for data_file in path:
            file1 = pd.DataFrame(pd.read_csv(data_file, header=None, sep="    ", decimal=',', engine='python',
                                             na_values='X'))
            # Convert time column to standard type of time data in pandas
            file1[0] = pd.to_datetime(file1[0], format='%d/%m/%Y %Hh%M')
            # Convert number data to float64
            file1.iloc[:, 1:] = file1.iloc[:, 1:].astype(float)
            load_data.append(file1)
    return load_data