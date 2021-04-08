def solution(t, logs):
    running_p = {}
    for line in logs:
        ts, p, status = line.split(' ')
        if int(ts) < t:
            if status != 'terminated':
                running_p[p] = status
            else:
                running_p.remove(p)
    result = []
    for p, status in running_p.items():
        if status != 'waiting':
            result.append(p)
    if len(result) > 1 or len(result) == 0:
        print('-1')
    else:
        print(result[0])


solution(t=15,
         logs=[
             '0 A created',
             '1 B created',
             '2 C created',
             '3 D created',
             '10 A running',
             '11 A waiting',
             '12 B waiting',
             '13 B running',
             '14 C running',
             '17 B terminated',
             '18 A terminated',
         ])
