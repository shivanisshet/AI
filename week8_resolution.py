
# Knowledge Base using Propositional Logic
# Proving a query using Resolution

def negate(literal):
    """Return the negation of a literal."""
    if literal.startswith("~"):
        return literal[1:]
    return "~" + literal


def resolve(ci, cj):
    """Resolve two clauses."""
    resolvents = []

    for literal in ci:
        opposite = negate(literal)

        if opposite in cj:
            new_clause = (ci - {literal}) | (cj - {opposite})

            # Ignore tautological clauses
            if not any(negate(x) in new_clause for x in new_clause):
                resolvents.append(frozenset(new_clause))

    return resolvents


def resolution(kb, query):
    """Prove query using resolution refutation."""

    clauses = set(kb)

    # Add negation of query to the knowledge base
    clauses.add(frozenset([negate(query)]))

    print("\nInitial Clauses:")
    for clause in clauses:
        print(clause)

    new = set()

    while True:
        clause_list = list(clauses)

        for i in range(len(clause_list)):
            for j in range(i + 1, len(clause_list)):

                resolvents = resolve(
                    clause_list[i],
                    clause_list[j]
                )

                for resolvent in resolvents:
                    if not resolvent:
                        print("\nEmpty clause obtained!")
                        print("Query is PROVED using Resolution.")
                        return True

                    new.add(resolvent)

        if new.issubset(clauses):
            print("\nNo new clauses generated.")
            print("Query cannot be proved.")
            return False

        print("\nNew clauses:", new)
        clauses.update(new)


# Main program
print("KNOWLEDGE BASE USING PROPOSITIONAL LOGIC")

# Knowledge Base:
# P -> Q
# Q -> R
# P

# Convert implications into CNF:
# (~P OR Q)
# (~Q OR R)
# P

kb = [
    frozenset(["~P", "Q"]),
    frozenset(["~Q", "R"]),
    frozenset(["P"])
]

# Given Query
query = "R"

# Display Knowledge Base
print("\nKnowledge Base:")
for clause in kb:
    print(clause)

print("\nQuery:", query)

# Apply Resolution
resolution(kb, query)
