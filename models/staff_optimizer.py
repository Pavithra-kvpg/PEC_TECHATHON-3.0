from pulp import LpProblem, LpVariable, lpSum, LpMinimize

def optimize_staff(required=[5, 6, 4], available=15):
    prob = LpProblem("StaffAllocation", LpMinimize)
    shifts = ["morning","evening","night"]
    staff = LpVariable.dicts("staff", shifts, lowBound=0, cat="Integer")

    prob += lpSum(staff[s] for s in shifts)
    for i,s in enumerate(shifts):
        prob += staff[s] >= required[i]
    prob += lpSum(staff[s] for s in shifts) <= available

    prob.solve()
    return {s:int(staff[s].value()) for s in shifts}

if __name__ == "__main__":
    print(optimize_staff())
