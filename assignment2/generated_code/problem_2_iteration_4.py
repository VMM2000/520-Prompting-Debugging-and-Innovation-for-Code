def is_not_prime(n):
    chain_of_thought = []
    if n <= 1:
        chain_of_thought.append("Not prime. Number is less than or equal to 1")
    elif n <= 3:
        chain_of_thought.append("Not prime. Number is 2 or 3")
    elif n % 2 == 0:
        chain_of_thought.append("Not prime. Number is even and not divisible by 2")
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                chain_of_thought.append("Not prime. Number is divisible by i (a prime number)")
                break
    return chain_of_thought
