"""Problem Statement — API Retry Mechanism

A backend service attempts to connect to an external API.

The connection succeeds only after a specific attempt number.

Given:

maximum retry attempts
success attempt number

Simulate the retry process.

For every failed attempt, print:

Retrying...

If connection succeeds:

Connected successfully

If maximum retries are exhausted:

Connection failed
Example
max_retries = 5
success_at = 4
Expected Output
Attempt 1 -> Retrying...
Attempt 2 -> Retrying...
Attempt 3 -> Retrying...
Attempt 4 -> Connected successfully"""


def network_retry(max_re, suc_at):
    for i in range(1, max_re):
        if i != suc_at:
            print(f"Attempt {i} -> Retrying...")
        else:
            print(f"Attempt {i} -> Connected successfully...")


network_retry(5, 4)

# time complexity -> O(n)
# space complexity -> O(1)