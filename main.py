import time

def progress_bar(max_value):
    for i in range(max_value + 1):
        print(f"\rProgress: {i * 100 // max_value}% [{'*' * (i * 100 // max_value)}{'-' * (max_value - i * 100 // max_value)}]", end='')
        time.sleep(0.1)
    print()

progress_bar(100)
