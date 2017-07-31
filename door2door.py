import csv
import time
from time import gmtime, strftime
import json

#Specify path to .csv file with pickups and dropoffs data on local machine
pickup_dropoff_data = ''
#Specify path to .json file with events data on local machine
events_data = ''
#Specify path and name mask for output .csv file. Pattern: %PATH TO DIRECTORY%/Your_output_file_name_w/o_extension
file_for_result_data = ''

#Converts '2017-07-30T15:44:33.000+02:00' -> '2017-07-30 15:44:33'
def timestamp2datetime (timestamp):
    decomposed_timestamp = time.strptime(timestamp[:19], '%Y-%m-%dT%H:%M:%S')
    datetime = time.strftime('%Y-%m-%d %H:%M:%S', decomposed_timestamp)
    return datetime

#Finds difference in minutes between given timestamps
def timedifference (estimation_timestamp, actual_timestamp):
    if not estimation_timestamp or not actual_timestamp:
        timedifference = 'NaN'
    else:
        decomposed_et = time.strptime(estimation_timestamp[:19], '%Y-%m-%dT%H:%M:%S')
        decomposed_at = time.strptime(actual_timestamp[:19], '%Y-%m-%dT%H:%M:%S')
        timedifference = (time.mktime(decomposed_et) - time.mktime(decomposed_at))/60
    return str(timedifference)

#Creates list of closed bookings filtering out cancelled ones
with open(events_data) as jsonfile:
    bookings = json.load(jsonfile)
    bookings_to_process = []
    for booking in bookings:
        if booking['status'] == 'closed':
            bookings_to_process.append(booking['booking_id'])

#Saves output results to selected directory
output = file_for_result_data+strftime('%Y-%m-%d_%H-%M-%S', gmtime())+'.csv'
file_for_output = open(output, 'w')
file_for_output.write('pickup_et,pickup_at,pickup_delta,dropoff_et,dropoff_at,dropoff_delta,TSG,area_start,area_stop,booking_id' + '\n')

#Loop takes entries for every selected booking_id
for booking_id in bookings_to_process:
    processed_bookings = []
    if booking_id not in processed_bookings:
        pickup_et = []
        dropoff_et = []
        processed_row = []
        with open(pickup_dropoff_data, newline='') as csvfile2:
            spamreader = csv.DictReader(csvfile2, delimiter=',', quotechar='|')
            #Searching for initial ETA and ATA for pickups&dropoffs
            for row in spamreader:
                if row['booking_id'] == booking_id and row['status'] == 'open' and row['type'] == 'pickup':
                    pickup_et.append([row['estimated_time_utc_0'], row['datetime_utc_0']])
                    area_start = row['postal']
                elif row['booking_id'] == booking_id and row['status'] == 'open' and row['type'] == 'dropoff':
                    dropoff_et.append([row['estimated_time_utc_0'], row['datetime_utc_0']])
                    area_stop = row['postal']
                elif row['booking_id'] == booking_id and row['status'] == 'closed' and row['type'] == 'pickup':
                    pickup_at = row['actual_time_utc_0']
                elif row['booking_id'] == booking_id and row['status'] == 'closed' and row['type'] == 'dropoff':
                    dropoff_at = row['actual_time_utc_0']
            #Creates list with pickup_et,pickup_at,pickup_delta,dropoff_et,dropoff_at,dropoff_delta,booking_id data
            if pickup_et:
                initial_estimation_pickup = (min(pickup_et, key = lambda x: x[1]))
                processed_row.append(timestamp2datetime(initial_estimation_pickup[0]))
            else:
                processed_row.append('NaN')
            if pickup_at:
                processed_row.append(timestamp2datetime(pickup_at))
            else:
                processed_row.append('NaN')
            pickup_delta = timedifference(initial_estimation_pickup[0],pickup_at)
            processed_row.append(pickup_delta)
            if dropoff_et:
                initial_estimation_dropoff = (min(dropoff_et, key = lambda x: x[1]))
                processed_row.append(timestamp2datetime(initial_estimation_dropoff[0]))
            else:
                processed_row.append('NaN')
            if dropoff_at:
                processed_row.append(timestamp2datetime(dropoff_at))
            else:
                processed_row.append('NaN')
            dropoff_delta = timedifference(initial_estimation_dropoff[0],dropoff_at)
            processed_row.append(dropoff_delta)
            #TSG calculation [Trip Schedule Gap]
            processed_row.append(str(float(dropoff_delta) - float(pickup_delta)))
            if area_start:
                processed_row.append(area_start)
            else:
                processed_row.append('NaN')
            if area_stop:
                processed_row.append(area_stop)
            else:
                processed_row.append('NaN')
            processed_row.append(booking_id)
            #Writes list to .csv file
            file_for_output.write(','.join(processed_row) + '\n')
    processed_bookings.append(booking_id)

file_for_output.close()


        
