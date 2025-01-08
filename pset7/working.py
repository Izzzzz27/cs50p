import re, sys

def main():
    print(convert(input("Hours: ")))

def s_is_valid_format(s):
    if (matches := re.search(r'^(1?[1-9](:[0-5][0-9])? [AP]M to 1?[1-9](:[0-5][0-9])? [AP]M)$', s)) == None:
        return True
    return False

def return_time(s):
    return re.search(r'^(1?[1-9]):?([0-5][0-9])? ([AP]M) to (1?[1-9]):?([0-5][0-9])? ([AP]M)$', s).groups()

def check_valid_time(time):
    if int(time[0]) < 1 or int(time[0]) > 12:
        raise ValueError
    if int(time[3]) < 1 or int(time[3]) > 12:
        raise ValueError

def convert_hour(hour, meridian):
    if meridian == 'AM':
        if int(hour) == 12:
            return '0'.rjust(2, '0')
        return hour.rjust(2, '0')
    elif meridian == 'PM':
        if int(hour) == 12:
            return '12'
        return str(int(hour) + 12).rjust(2, '0')

def convert(s):
    if s_is_valid_format(s):
        raise ValueError("Invalid format")

    time = return_time(s)

    check_valid_time(time)

    if None in time:
        return f'{convert_hour(time[0], time[2])}:00 to {convert_hour(time[3], time[5])}:00'
    else:
        return f'{convert_hour(time[0], time[2])}:{time[1]} to {convert_hour(time[3], time[5])}:{time[4]}'

if __name__ == '__main__':
    main()
