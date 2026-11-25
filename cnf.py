def eliminate_implication(expr):
    expr = expr.replace("->", "|")
    return expr


def cnf(p, q, r):
    return f"({p} OR {q}) AND ({p} OR {r})"


print("Enter logical expression:")
print("Example: P -> (Q AND R)")

p = input("Enter P: ")""" vwdu9ygjfn jnhjhuvbuuu8 """
q = input("Enter Q: ")
r = input("Enter R: ")

result = cnf("NOT " + p, q, r)

print("CNF Expression:")
print(result)