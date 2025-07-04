R = 1.097e-2
for n1 in range(1,3+1):
    print(f"Line series for n1 = {n1}")
    for i in range(1,5+1):
        n2 = n1 + i
        lambda_inv = R*(1./n1**2 - 1./n2**2)
        print(f"\t{1/lambda_inv}, nm")