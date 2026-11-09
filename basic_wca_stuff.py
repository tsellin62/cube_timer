import random
import datetime

def generate_3x3_scramble():
    SCRAMBLES = [
        "R U2 F' D L2 B U' R2 F D2 L' U B2 R' D' F2 L U2 R2 B'",
        "D2 B' R U F2 L' D R2 B U' L2 F' R' U2 D' B2 L F U R2",
        "F U' L2 D B2 R F' U2 L' B D2 R' U L F2 D' R2 B' U' L2",
        "L' D2 F R2 U B' L U2 F2 D' R B2 U' L2 D F' R' U B L'",
        "B2 L U' R' F D2 B' U L2 R2 D' F2 U2 L' B R U' D F' L2",
        "U R2 B' D L' F2 U' R D2 B L2 U2 F' R' D' L B2 U R' F2",
        "D' F2 L R' U2 B D R2 F' L2 U' B2 D2 R U F L' D B' R2",
        "R' B2 U L2 D' F R2 B' U2 L D2 F' U' R B L' U F2 D R'",
        "F' D L2 B U2 R' F2 D' L U' B2 R2 F L' D2 U R B' D' F2",
        "L2 U' F R D2 B' U2 L' F2 R' D B2 U R2 F' L D' B U' R'"]
    return random.choice(SCRAMBLES)

def timer():
    input("Press Enter to start the timer...")
    start_time = datetime.datetime.now()
    print("Timer started. Press Enter to stop the timer.")
    input()
    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    elapsed_seconds = elapsed_time.total_seconds()
    print(f"Elapsed time: {elapsed_seconds:.2f} seconds")
    return elapsed_seconds

def ao5(times):
    if len(times) != 5:
        print("You need exactly 5 times to calculate an average of 5.")
        return None
    times_sorted = sorted(times)
    times_trimmed = times_sorted[1:-1]  # Remove the fastest and slow
    return sum(times_trimmed) / len(times_trimmed)

def main():
    times = []

    while True:
        user_input = input("Enter 's' to generate a scramble, 't' to start the timer, or 'q' to quit: ").strip().lower()
        if user_input == 's':
            scramble = generate_3x3_scramble()
            print(f"Generated 3x3 scramble: {scramble}")
        elif user_input == 't':
            times.append(timer())
            if len(times) >= 5:
                print(f"ao5: {ao5(times[-5:]):.2f} seconds")
        elif user_input == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()