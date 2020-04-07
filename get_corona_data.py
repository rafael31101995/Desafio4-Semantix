import sys
import requests
import re
import csv
import datetime


def get_request(country_name):
    if country_name is not None:
        request_data = requests.get('https://www.worldometers.info/coronavirus/country/{}'.format(country_name))
    else:
        request_data = requests.get('https://www.worldometers.info/coronavirus')

    string_data_requested = request_data.text
    matches = match_corona_cases(string_data_requested)
    updating_csv(matches, country_name)


def match_corona_cases(str_content):
    # This regular expression matches until the number reach 999.999.999.999
    pattern = re.compile(r'<span(\sstyle="color:#aaa")?>([0-9]+.[0-9]+(.[0-9]+)?)')
    list_values = []
    matches = pattern.finditer(str_content)
    for match in matches:
        list_values.append(match.group(2).replace(',', '.'))
    print(list_values)
    return list_values


def updating_csv(data, country):
    # Getting date and hour.
    x = datetime.datetime.now()
    date = x.strftime("%x")
    hour = x.strftime("%X")

    data.append(date)
    data.append(hour)

    dict_list = {
        'Coronavirus Cases': data[0], 'Deaths': data[1], 'Recovered': data[2], 'Data': data[3], 'Hour': data[4]
    }
    if country is not None:
        ground = country
    else:
        ground = 'world'
    with open('corona_{}.csv'.format(ground), 'a', newline='') as csv_file:
        fieldnames = ['Coronavirus Cases', 'Deaths', 'Recovered', 'Data', 'Hour']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        header_or_not = False
        try:
            # Looking for a header inside the csv.
            sniffer = csv.Sniffer()
            sample_bytes = 32
            header_or_not = (sniffer.has_header(open("corona_{}.csv".format(ground)).read(sample_bytes)))
        except:
            print("Was Handled")

        if header_or_not:
            writer.writerow(dict_list)
        else:
            writer.writeheader()
            writer.writerow(dict_list)


if __name__ == '__main__':

    try:
        country_name = sys.argv[1]
    except:
        country_name = None

    get_request(country_name)

