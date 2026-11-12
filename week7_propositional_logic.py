
from itertools import product

# Generate all possible truth-value combinations
values = [False, True]

print("TRUTH TABLE")
print("-" * 100)
print(f"{'P':<8}{'Q':<8}{'R':<8}{'Q -> P':<12}{'P -> ~Q':<12}{'Q OR R':<12}{'KB':<8}")

models = []

for P, Q, R in product(values, repeat=3):

    # Evaluate each sentence in the knowledge base
    s1 = (not Q) or P          # Q -> P
    s2 = (not P) or (not Q)   # P -> ~Q
    s3 = Q or R               # Q OR R

    # Knowledge base is true when all sentences are true
    KB = s1 and s2 and s3

    print(f"{str(P):<8}{str(Q):<8}{str(R):<8}"
          f"{str(s1):<12}{str(s2):<12}{str(s3):<12}{str(KB):<8}")

    # Store models where KB is true
    if KB:
        models.append((P, Q, R))

print("\nMODELS OF KB:")
for model in models:
    print(f"P={model[0]}, Q={model[1]}, R={model[2]}")

# Check entailments
entails_R = all(R for P, Q, R in models)

entails_R_implies_P = all((not R) or P for P, Q, R in models)

entails_Q_implies_R = all((not Q) or R for P, Q, R in models)

print("\nENTAILMENT RESULTS:")
print("ii) KB entails R:", entails_R)
print("iii) KB entails R -> P:", entails_R_implies_P)
print("iv) KB entails Q -> R:", entails_Q_implies_R)
