from calendar import isleap
from re import findall, sub


# text_with_dates = 'agvdavsdvbb01-04-1991-01-12-2000'


def find_all_dates(text):
    pattern = r'(?<!\d)(?:0?[1-9]|[12][0-9]|3[01])-(?:0?[1-9]|1[0-2])-(?:1[0-9][0-9][0-9]|20[0-2][0-9])(?!\d)' # noqa
    found_dates = (findall(pattern, text))
    filtered_list = []
    days31 = ('3', '03', '5', '05', '7', '07', '8', '08', '10', '12')
    days30 = ('1', '01', '4', '04', '6', '06', '9', '09', '11')
    days28_29 = ('2', '02')
    for one_date in found_dates:
        temp_date = (one_date.split('-'))
        if temp_date[1] in days31:
            filtered_list.append(one_date)
        elif temp_date[1] in days30:
            if int(temp_date[0]) <= 30:
                filtered_list.append(one_date)
        elif temp_date[1] in days28_29:
            if int(temp_date[0]) <= 28:
                filtered_list.append(one_date)
            elif int(temp_date[0]) == 29 and isleap(int(temp_date[2])):
                filtered_list.append(one_date)
    return filtered_list


# print(find_all_dates(text_with_dates))

floats = '-12.3-10-da3.-1-1-1-11.1/-'


def sum_floats(text):
    pattern = r'(-?\d+\.\d+|-?\d+)'
    found_row_floats = (findall(pattern, text))
    floats_list = [float(element) for element in found_row_floats]
    return floats_list


# print(sum_floats(floats))


def delete_negative_floats(text):
    pattern = r'(-\d+\.\d+|-\d+)'
    new_text = sub(pattern, '', text)
    return new_text


# print(delete_negative_floats(floats))
