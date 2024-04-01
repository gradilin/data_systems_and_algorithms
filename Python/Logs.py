with open('./var/logs/syslog') as log_file:
    log_file_lines = log_file.readlines()

for line in log_file_lines: 
    # figure out what patterns are being looked for
    t = line.split(",")
    milliseconds = t[4][:-2]


