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
