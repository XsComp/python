# stringplay.py


from datetime import datetime

# Input string provided in the task
string = "device    type    dateadded    IP Address \ncomputer    pc    1591259971    192.168.100.1 \nandroid phone    phone    1591259971    192.168.100.3 \nsamsung phone    phone    1591259971    192.168.100.4"

# We convert "timestamp" to a human readable format
def format_date(timestamp):
    return datetime.fromtimestamp(int(timestamp)).strftime("%Y-%m-%d %H:%M:%S")

# We then split, and structure the string
lines = string.strip().split('\n')
header = [h.strip().upper() for h in lines[0].split("    ")]
data_rows = [line.strip().split("    ") for line in lines[1:]]
for row in data_rows:
    row[2] = format_date(row[2])

# We format the output to match provided output (in the question)
col_widths = [25, 15, 30, 20]  # Aproximate match of output in the question

# We then print our results to screen
print("-" * 83)
print(f"{header[0]:<{col_widths[0]}}{header[1]:<{col_widths[1]}}{header[2]:<{col_widths[2]}}{header[3]:<{col_widths[3]}}")
print("-" * 83)
for row in data_rows:
    print(f"{row[0]:<{col_widths[0]}}{row[1]:<{col_widths[1]}}{row[2]:<{col_widths[2]}}{row[3]:<{col_widths[3]}}")
    print("-" * 83)
