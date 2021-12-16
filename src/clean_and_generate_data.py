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
