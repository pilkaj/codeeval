"""Sample code to read in test cases:
"""
import sys

class TimeStamp():
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.totaltime = hours*3600 + minutes*60 + seconds
        return
        
    def get_totaltime(self):
        return self.totaltime
        
    def get_time(self):
        return (self.hours, self.minutes, self.seconds)
        
        
def sort(stamps_list):
    sorted_list = [stamps_list.pop(0)]
    for timestamp in stamps_list:
        i = 0
        while i < len(sorted_list):
            if timestamp.get_totaltime() < sorted_list[i].get_totaltime():
                i += 1
            else:
                break
        sorted_list.insert(i, timestamp)
    return sorted_list
    
def print_timestamps(stamps_list):
    for time_stamp in stamps_list:
        h, m, s = time_stamp.get_time()
        print("%02d:%02d:%02d" % (h, m, s), end=' ')
    return

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        # ignore test if it is an empty line
        # 'test' represents the test case, do something with it
        # ...
        # ...
        timestamps = []
        test = test.split()
        for each in test:
            h, m, s = each.split(':')
            stamp = TimeStamp(int(h), int(m), int(s))
            timestamps.append(stamp)
        timestamps = sort(timestamps)
        print_timestamps(timestamps)
        print()
