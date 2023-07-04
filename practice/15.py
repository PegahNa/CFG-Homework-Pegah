# Let’s imagine that we are at the A&E “walk-in” hospital. There are many patients that have medical issues of different complexity and each of those patients needs to be seen by a doctor. There is only one doctor at the hospital. Whilst one patient is being attended by a doctor, the rest of the patients are waiting. It takes different amount of time to see one patient (depends on their medical issue).
# You are given a non-empty array of positive integers representing the amounts of time it takes to attend a specific patient. Only one patient can be seen at a time, but the patents can be called-in to be seen in any order.
# Patient’s waiting time is defined as the amount of time that he/she must wait before their session with the doctor starts. In other words, if a patient is being seen second, then their waiting time is the duration of the first patient’s session. If a patient is seen third, then their waiting time is the sum of the durations of the first two patients.
# Write a function that returns the minimum amount of total waiting time for all of the patients.
# For example, if there are three patients with sessions durations [1 min, 4 min, 5 min] and, let’s say, those patients are being seen by the doctor in the order of [5, 1, 4], then the total waiting time of all patients would be (0) + (5) + (5 +1) = 11
# • The first patient with duration 5 min would be attended to immediately, so their waiting time would be 0
# • The second patient of duration 1min would have to wait 5 min (the duration of the first patient) to be attended by medical staff.
# • The last patient would have to wait the duration of the first two patient before they get to see a doctor.
# NB: You are allowed to mutate the input array, if you need to do so for your solution
# Sample Input
# queries = [ 3, 2, 1, 2, 6]
# Sample Output
# 17
def waiting_time(arr):
    # Sort the array in ascending order
    arr.sort()

    # Initialize a variable to store the total waiting time
    total_waiting_time = 0

    # Iterate over the sorted array
    for i in range(1, len(arr)):
        # Calculate the waiting time for the current patient
        waiting_time = arr[i-1]

        # Add the waiting time to the total waiting time
        total_waiting_time += waiting_time

        # Update the duration of the current patient by adding the waiting time
        arr[i] += waiting_time

    # Return the total waiting time
    return total_waiting_time

result = waiting_time([3, 2, 1, 2, 6])
print(result)
