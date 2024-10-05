def process_log_file(filename):
    keyword = "ERROR"
    count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            if keyword in line:
                count += 1

    print(f"Number of lines containing '{keyword}': {count}")

# Example usage
process_log_file('logfile.txt')  # Replace 'logfile.txt' with the actual filename
