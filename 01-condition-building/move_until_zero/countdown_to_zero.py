"""Problem Statement — Rocket Launch Countdown

A space agency starts a launch countdown from a number N.

The system prints the countdown value every second.

When the countdown reaches 0, print:

Launch
Example
Input:
5

Output:
5
4
3
2
1
Launch"""


def countdown(n):
    while(n != 0):
        print(n)
        n -= 1

countdown(5)

# time complexity -> O(n)
# space complexity -> O(1)
