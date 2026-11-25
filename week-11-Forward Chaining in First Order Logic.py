
# Forward Chaining in First Order Logic

# Knowledge Base (Facts)
knowledge_base = [
    ("American", "Robert"),
    ("Enemy", "A", "America"),
    ("Owns", "A", "T1"),
    ("Missile", "T1")
]

# Forward Chaining Rules
def forward_chaining(kb):

    # Rule 1: Enemy(x, America) -> Hostile(x)
    for fact in kb[:]:
        if fact[0] == "Enemy" and fact[2] == "America":
            new_fact = ("Hostile", fact[1])
            if new_fact not in kb:
                kb.append(new_fact)
                print("Derived:", new_fact)

    # Rule 2: Missile(x) -> Weapon(x)
    for fact in kb[:]:
        if fact[0] == "Missile":
            new_fact = ("Weapon", fact[1])
            if new_fact not in kb:
                kb.append(new_fact)
                print("Derived:", new_fact)

    # Rule 3: Missile(x) AND Owns(A,x) -> Sells(Robert,x,A)
    for fact1 in kb[:]:
        for fact2 in kb[:]:
            if fact1[0] == "Missile" and fact2[0] == "Owns":
                if fact1[1] == fact2[2] and fact2[1] == "A":
                    new_fact = ("Sells", "Robert", fact1[1], "A")
                    if new_fact not in kb:
                        kb.append(new_fact)
                        print("Derived:", new_fact)

    # Rule 4: American(x) AND Weapon(y) AND
    # Sells(x,y,z) AND Hostile(z) -> Criminal(x)

    for fact1 in kb[:]:
        for fact2 in kb[:]:
            for fact3 in kb[:]:
                for fact4 in kb[:]:

                    if (fact1[0] == "American" and
                        fact2[0] == "Weapon" and
                        fact3[0] == "Sells" and
                        fact4[0] == "Hostile"):

                        if (fact1[1] == fact3[1] and
                            fact2[1] == fact3[2] and
                            fact3[3] == fact4[1]):

                            new_fact = ("Criminal", fact1[1])

                            if new_fact not in kb:
                                kb.append(new_fact)
                                print("Derived:", new_fact)

    return kb


# Execute Forward Chaining
print("Initial Knowledge Base:")
for fact in knowledge_base:
    print(fact)

print("\nForward Chaining:")
knowledge_base = forward_chaining(knowledge_base)

# Check Goal
goal = ("Criminal", "Robert")

if goal in knowledge_base:
    print("\nGoal Proved: Robert is Criminal")
else:
    print("\nGoal Not Proved")
