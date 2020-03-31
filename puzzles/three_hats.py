# source: https://puzzling.stackexchange.com/questions/91722/three-people-wearing-hats

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or k == i:
                continue
            if k % i == 0 and k % j == 0:
                print('((i, j, k, )')
                print((i, j, k, ))
                print('===========')