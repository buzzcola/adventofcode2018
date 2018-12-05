import itertools, datetime, dateutil.parser, re
with open('input','r') as f: input = f.read()

records = [(dateutil.parser.parse(line[1:17]), line[19:])  for line in input.split('\n')]
records.sort(key=lambda x: x[0])

sleepy_times = {} # (guard,minute) : sleep count per guard per minute
totals = {} # guard : total minutes asleep

guard = None
awake = True
current_time = records[0][0]

while any(records):
    (time, instruction) = records.pop(0)
    while current_time < time:
        if awake == False:
            key = (guard, current_time.minute)
            sleepy_times[key] = sleepy_times.get(key, 0) + 1
            totals[guard] = totals.get(guard, 0) + 1
        current_time += datetime.timedelta(minutes = 1)

    if instruction[0] == 'w': awake = True
    elif instruction[0] == 'f': awake = False
    else:
        guard = int(re.search(r'(\d+)', instruction).groups()[0])
        awake = True

# part 1:
sleepy_guard = max(totals.items(), key=lambda x: x[1])[0]
minutes =  [x for x in sleepy_times.items() if x[0][0] == sleepy_guard]
sleepy_minute = max(minutes, key=lambda x: x[1])[0][1]
print '1: %d' % (sleepy_minute * sleepy_guard)

#part 2:
sleepiest = max(sleepy_times.items(), key=lambda x: x[1])
print '2: %d' % (sleepiest[0][0] * sleepiest[0][1])