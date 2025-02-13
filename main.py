import time

def compute_factorial(n):
    """Simple function to compute factorial iteratively."""
    result = 1
    for i in range(1, n + 1):
        result *= i
        time.sleep(0.1)  # Simulating processing time
    return result

def main():
    print("Starting energy-intensive computation...")
    
    for i in range(5, 10):
        print(f"Factorial of {i} is {compute_factorial(i)}")
    
    print("Computation finished.")

if __name__ == "__main__":
    main()
