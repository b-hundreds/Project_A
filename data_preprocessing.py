# Importing libraries
import pandas as pd
import os

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


# Handle time data


def handle_time_data(data_frame):
    for frame in data_frame:
        # day in week
        frame['day_of_week'] = frame[0].dt.dayofweek
        # month in year
        frame['month'] = frame[0].dt.month
        # hour in day
        frame['hour'] = frame[0].dt.hour
        # drop columns 0
        frame.drop(columns=0, inplace=True)
    return data_frame


# Get information of data, return list of data frame has NaN and its index


def get_info(data_frame):
    neg_num = 0  # Number of negative value
    num_nan = 0  # Number of NaN value
    list_have_nan = []
    index_list_nan = []  # list index of data frame has NaN in list of data frame
    index = 0  # Variable add to list index when detect a data frame has NaN
    for frame in data_frame:
        a = frame.isnull().sum().sum()
        neg_num += frame.iloc[:, 1:][frame.iloc[:, 1:] < 0].notna().sum().sum()
        num_nan += a
        if a != 0:
            list_have_nan.append(frame)
            index_list_nan.append(index)
        index += 1
    print('NaN value number: %d' % num_nan)
    print('Negative value number: %d' % neg_num)
    index_list_nan.sort(reverse=True)
    return list_have_nan, index_list_nan


# Handle number data


def handle_number_data(data_frame):
    for frame in data_frame:
        # add lag_1 feature
        frame['lag_feature_1'] = frame[1].shift(1)
        frame['lag_feature_2'] = frame[2].shift(1)
        frame['lag_feature_3'] = frame[3].shift(1)
        frame['lag_feature_4'] = frame[4].shift(1)
        frame['lag_feature_5'] = frame[5].shift(1)
        frame['lag_feature_6'] = frame[6].shift(1)
        # Fill nan value when create lag feature
        frame.fillna(7, inplace=True)
    return data_frame


# Drop NaN

def drop_nan(data_frame, list_nan):
    for i in list_nan:  # i is index of data frame has nan in list of data frame
        del data_frame[i]
    return data_frame


# Data preprocessing

def data_preprocessing(list_direction):
    data1 = read_all_file_from_folder(list_direction)
    have_nan, index_nan = get_info(data1)
    data1 = drop_nan(data1, index_nan)
    handle_number_data(data1)
    handle_time_data(data1)
    list_of_label = []
    for frame in data1:
        label1 = frame.iloc[:, 0:6]
        list_of_label.append(label1)
    return data1, list_of_label
