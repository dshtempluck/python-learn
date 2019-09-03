
db = {}
cache = []

def init_cache(m, n):
    global cache
    n_range = range(0, n + 1)
    m_range = range(0, m + 1)
    cache = [[0] * (n + 1) for i in m_range]
    for m in m_range:
        #print(m) if m % 1000 == 0 else None
        for n in n_range:
            if m == 0 or n == 0:
                cache[m][n] = 0
            elif m == 1:
                cache[m][n] = n
            elif n == 1:
                cache[m][n] = 1
            else:
                cache[m][n] = cache[m][n - 1] + cache[m - 1][n -1] + 1


def height(m, n):
    if m == 0 or n == 0:
        return 0
    init_cache(m, n)
    return cache[m][n]

def height2(m, n):
    key = str(m) + ':' + str(n)
    if key in db:
        return db[key]
    if m == 0 or n == 0:
        return 0
    if m == 1:
        return n
    if n == 1:
        return 1
    db[key] = height(m, n - 1) + height(m - 1, n - 1) + 1
    return db[key]



def induction_match(m, n):
    if m == 0 or n == 0:
        return True
    if m == 1:
        return True
    if n == 1:
        return True
    return False

def init_cache_backtrace(m, n):
    m_range = range(0, m + 1)
    cache = [[-1] * (n + 1) for _ in m_range]
    unsolved_path = [[(m, n)]]
    curr_line = [(m, n)]
    _m = m
    _n = n
    while 1:
        next_line = []
        for i in curr_line:
            _m, _n = i
            if cache[_m][_n] == -2:
                continue
            if induction_match(_m, _n):
                continue
            cache[_m][_n] = -2
            next_line.append((_m, _n - 1))
            next_line.append((_m - 1, _n - 1))
        if len(next_line) == 0:
            break
        unsolved_path.append(next_line)
        curr_line = next_line
 
    lst = unsolved_path[::-1]
    for _level in lst:
        for (num, tries) in _level:
            if num == 0 or tries == 0:
                cache[num][tries] = 0
            elif num == 1:
                cache[num][tries] = n
            elif tries == 1:
                cache[num][tries] = 1
            else:
                cache[num][tries] = cache[num][tries - 1] + cache[num - 1][tries - 1] + 1
    return cache[m][n]

       
#print(height(2, 14))
#print(height2(4477, 10000))
#print(height(477, 10000))
#print(init_cache_backtrace(2, 14))
print(init_cache_backtrace(4477, 10000))