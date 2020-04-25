import csv
import time
from datetime import datetime
from subprocess import check_output

def main():
    filename = 'csv/thermal_data_{}.csv'.format(int(time.time()))
    # write headers
    with open(filename, 'w') as out_f:
        csv_writer = csv.writer(out_f)
        csv_writer.writerow(['timestamp', 'temperature'])
    while True:
        with open(filename, 'a') as out_f:
            csv_writer = csv.writer(out_f)
            csv_writer.writerow([datetime.now(), get_current_cpu_temp()])
        time.sleep(1)

def get_current_cpu_temp():
    return check_output('vcgencmd measure_temp'.split(' ')).decode('utf8').replace('temp=', '').replace('\'C', '').replace('\n', '')

if __name__ == '__main__':
    main()