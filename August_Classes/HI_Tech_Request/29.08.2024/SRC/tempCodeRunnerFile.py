if modified_times[0][1] > modified_times[1][1]:
    first_file = modified_times[1][0]
    last_file = modified_times[0][0]
else:
    first_file = modified_times[0][0]
    last_file = modified_times[1][0]