# TLE-Converter CLI
from __future__ import print_function
import re
import ephem


def type_tle():
    global tle_rec, type_name, type_line1, type_line2
    type_name = "name"
    type_line1 = input("Enter Line 1 of TLE")
    type_line2 = input("Enter Line 2 of TLE")
    try:
        tle_rec = ephem.readtle(type_name, type_line1, type_line2)
        tle_rec.compute()
        print("Converting to Longitude: ", tle_rec.sublong)
        print("Converting to Latitude: ", tle_rec.sublat)
    except Exception as error:
        print("Unable to convert TLE {0}".format(error))


def plot_lat_lon():
    global target_line_1, target_line_2, lat, lon
    type_tle()
    try:
        lat = str(tle_rec.sublat) + '"E'
    except NameError as line_1_fail:
        print("TLE format error {0}.".format(line_1_fail))
    deg, minutes, seconds, direction = re.split('[::\'"]', lat)
    # print((float(deg) + float(minutes) / 60 + float(seconds) / (60 * 60)) * (-1 if direction in ['W', 'S'] else 1))
    target_line_1 = (float(deg) + float(minutes) / 60 + float(seconds) / (60 * 60)) * (-1 if direction in ['W', 'S'] else 1)
    try:
        lon = str(tle_rec.sublong) + '"E'
    except NameError as line_2_fail:
        print("TLE format error {0}".format(line_2_fail))
    deg, minutes, seconds, direction = re.split('[::\'"]', lon)
    # print((float(deg) + float(minutes) / 60 + float(seconds) / (60 * 60)) * (-1 if direction in ['W', 'S'] else 1))
    target_line_2 = (float(deg) + float(minutes) / 60 + float(seconds) / (60 * 60)) * (-1 if direction in ['W', 'S'] else 1)


def plot_cords():
    plot_lat_lon()
    target_result = "Lat: " + str(target_line_1), "Lon: " + str(target_line_2)
    print("Converted:", str(target_result).strip("()"))


if __name__ == '__main__':
    plot_cords()
