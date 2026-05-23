"""
Problem Statement — Cascading Load Balancer

A distributed backend system receives incoming request loads.

Each server has a maximum processing threshold.

You are given:

- an initial active load
- a list representing incoming traffic spikes

Process traffic spikes one-by-one.

Rules:

1. Add current spike to active load.

2. If active load becomes divisible by 4:
      immediately redistribute half the load
      using integer division.

3. If active load becomes greater than 3 times
   the current spike:
      skip the next traffic spike entirely.

4. If active load becomes exactly divisible by 9:
      rollback active load to previous load state
      before current spike was applied.

5. Continue processing until:
      - all spikes are processed
      OR
      - active load becomes less than or equal to 0.

Print active load after every processed spike.


Example

Input:
load = 11
spikes = [5, 8, 2, 7, 9, 3]

Expected Output:
Spike 5  -> Load: 8
Spike 2  -> Load: 5
Spike 7  -> Load: 12
Spike 9  -> Load: 21
"""


def cascading_load_balancer(load: any, spikes: list):
      i = 0
      while i <len(spikes) and load > 0:
            previous_load = load

            raw_load = load + spikes[i]
            load = raw_load

            if load % 4 == 0:
                  load //= 2

            if load % 9 == 0:
                  load = previous_load

            print(f"Spike {spikes[i]} -> Load: {load}")

            if raw_load > spikes[i]*3:
                  i += 2
            else:
                  i += 1
            
            

cascading_load_balancer(11, [5, 8, 2, 7, 9, 3])