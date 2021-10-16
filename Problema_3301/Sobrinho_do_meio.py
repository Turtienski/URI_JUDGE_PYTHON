H, Z, L = input().split()


if (H < Z and H > L) or (H < L and H > Z):
    print('huguinho')
elif (Z < H and Z > L) or (Z < L and Z > H):
    print('zezinho')
else: print ('luisinho')