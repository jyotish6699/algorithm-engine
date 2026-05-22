"""Problem Statement — Dungeon Energy Simulation

A game character enters a dungeon with an initial energy level N.

The dungeon contains rooms represented as:

1 = enemy room
0 = empty room

Energy rules:

entering an enemy room consumes 5 energy
entering an empty room consumes 2 energy

Traverse rooms one-by-one in order.

Stop traversal immediately if the character’s energy becomes less than or equal to 0.

For each room visited, print:
room number
remaining energy
Example
rooms = [1, 0, 1, 1, 0]
energy = 15
Expected Output
Room 1 -> Energy: 10
Room 2 -> Energy: 8
Room 3 -> Energy: 3
Room 4 -> Energy: -2"""

def energy_depletion(e: any, rooms: list):
    for i in range(len(rooms)):
        
        if e<0:
            break

        if rooms[i] == 0:
            e -= 2
            print(f"Room {i+1} -> Energy: {e}")
        elif rooms[i] == 1:
            e -= 5
            print(f"Room {i+1} -> Energy: {e}")
        else:
            pass

        

energy_depletion(15, [1, 0, 1, 1, 0])

# time complexity --------
# O(n) -> because in the worst case the loop may visits all romms once. because in O always count worst case.
# space complexity ---------
# O(1) -> because here only i variable is using for iteration so no extra vaiable is using per iteration so take constant space complexity.

        