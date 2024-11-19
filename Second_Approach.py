class LamportClock:
    def __init__(self, process_id):
        self.time = 0
        self.process_id = process_id

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
        return f"Process {self.process_id} Clock: {self.time}"


def simulate_event(processes):
    print("\nChoose an event to simulate:")
    print("1. Internal event")
    print("2. Send message")
    print("3. Receive message")
    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        # Internal event
        process_id = int(input("Enter process ID (e.g., 1, 2, etc.): "))
        processes[process_id].increment()
        print(processes[process_id])

    elif choice == 2:
        # Send message
        sender_id = int(input("Enter sender process ID: "))
        receiver_id = int(input("Enter receiver process ID: "))
        sent_time = processes[sender_id].send_event()
        print(f"Process {sender_id} after sending: {processes[sender_id]}")

        # Simulate the receiver receiving the message
        processes[receiver_id].receive_event(sent_time)
        print(f"Process {receiver_id} after receiving: {processes[receiver_id]}")

    elif choice == 3:
        # Receive message
        receiver_id = int(input("Enter receiver process ID: "))
        received_time = int(input("Enter the timestamp received: "))
        processes[receiver_id].receive_event(received_time)
        print(processes[receiver_id])

    else:
        print("Invalid choice. Try again.")


if __name__ == "__main__":
    # Initialize processes
    num_processes = int(input("Enter the number of processes: "))
    processes = {i: LamportClock(i) for i in range(1, num_processes + 1)}

    print("\nInitialized processes:")
    for process in processes.values():
        print(process)

    # Simulate events
    while True:
        simulate_event(processes)
        continue_simulation = input("\nDo you want to simulate another event? (yes/no): ").lower()
        if continue_simulation != "yes":
            break