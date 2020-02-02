import pandas as pd
import datetime

stop_name = raw_input('Enter stop name: ')
#stop_name = 'HIGHLAND AVE AT PENN AVE'
time = datetime.datetime.strptime(raw_input('specify time in HHMMSS format: '), "%H%M%S")
#time0 = datetime.datetime(1900, 1, 1, 0, 0)
# route = input('Enter route (71B):')
route = '71B'
direction = raw_input('Enter direction (In / Out): ')
#direction = 'Out'
print

stops_name_id = pd.read_csv('StopIDName.csv')
stop_id = stops_name_id[stops_name_id['stop_Name']==stop_name].iloc[0]['stop_ID']

TimeTable = pd.read_csv('Bus_71B_TimeTables_'+direction+'.csv',index_col=0)

TimeTable[stop_id] =  pd.to_datetime(TimeTable[stop_id], format='%H:%M:%S')
trip_id = TimeTable.iloc[(TimeTable[stop_id]-time).abs().argsort()[:1]].index[0]

FullnessTable = pd.read_csv('Bus_71B_FullnessTables_'+direction+'.csv',index_col=0)

check_stop_id = stops_name_id.loc[stops_name_id[stops_name_id['stop_ID']==stop_id].index-1]['stop_ID'].iloc[0]

if FullnessTable.loc[trip_id][check_stop_id] == 'Full':
    print 'Estimated fullness for the coming bus is Full'
    print
else:
    print 'Estimated fullness for the coming bus is', str(int(float(FullnessTable.loc[trip_id][check_stop_id])*100))+'%'
    print