class LamportClock:
    def __init__(self):
        self.time = 0

    def increment(self):
        """Increment the logical clock."""
        self.time += 1

    def send_event(self):
        """Simulate sending a message by incrementing the clock and returning its value."""
        self.increment()
        return self.time

    def receive_event(self, received_time):
        """
        Update the clock on receiving a message.
        Logical clock is set to the maximum of its current value and the received timestamp, then incremented.
        """
        self.time = max(self.time, received_time) + 1

    def __str__(self):
        return f"Logical Clock: {self.time}"


# Simulating two processes exchanging messages
if __name__ == "__main__":
    # Initialize clocks for two processes
    process1 = LamportClock()
    process2 = LamportClock()

    # Events in process1
    print("Process 1 performs an event.")
    process1.increment()
    print(process1)

    # Process 1 sends a message to Process 2
    print("\nProcess 1 sends a message to Process 2.")
    sent_time = process1.send_event()
    print(f"Process 1 clock after sending: {process1}")

    # Process 2 receives the message
    print("\nProcess 2 receives the message from Process 1.")
    process2.receive_event(sent_time)
    print(f"Process 2 clock after receiving: {process2}")

    # Process 2 performs an event
    print("\nProcess 2 performs another event.")
    process2.increment()
    print(process2)

    # Process 2 sends a message back to Process 1
    print("\nProcess 2 sends a message to Process 1.")
    sent_time = process2.send_event()
    print(f"Process 2 clock after sending: {process2}")

    # Process 1 receives the message
    print("\nProcess 1 receives the message from Process 2.")
    process1.receive_event(sent_time)
    print(f"Process 1 clock after receiving: {process1}")