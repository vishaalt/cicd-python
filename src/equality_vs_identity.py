def nonconformant_eq_operator():
    a = ''
    # expect finding: equality vs identity
    if a == None:
        print("a eq None")

def nonconformant_is_operator():
    a = [1, 2, 3]
    b = a.copy()
    # expect finding: equality vs identity
    if a is b :
        return True
