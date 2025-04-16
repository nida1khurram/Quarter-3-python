import time
print("Welcome To Countdown Timer")
def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"\rTime remaining: {mins:02d}:{secs:02d}", end="")
        time.sleep(1)
        seconds -= 1
    print("\rTime's up!      ")

if __name__ == "__main__":
    try:
        t = int(input("Enter countdown time in seconds: "))
        countdown(t)
    except ValueError:
        print("Please enter a valid number.")