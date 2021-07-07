def permutation(n):
    fact = 1
    # compute n!
    if n < 0:
        return "undefined"
  
    while n >= 1 :
        fact = fact * n
        n = n-1

    return fact

def n_take_k(n,k):
    p = permutation(n)/permutation(n-k)
    return p 
    # find n take k
    return k


if __name__ == "__main__":
        print(permutation(5))
        print(n_take_k(5,3))        