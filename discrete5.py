def matrix_intersection(m1,m2):
    m_i = []
    r,c = len(m1),len(m1[0])
    for i in range(r):
        m_i.append([m1[i][j] and m2[i][j] for j in range(c)])
    return m_i
def matrix_union(m1,m2):
    m_u = []
    r,c = len(m1),len(m1[0])
    for i in range(r):
        m_u.append([m1[i][j] or m2[i][j] for j in range(c)])
    return m_u
m1 = [[1,1,1],[1,0,1],[0,1,0]]
m2 = [[1,0,1],[0,1,1],[1,1,0]]
min = matrix_intersection(m1,m2)
mu = matrix_union(m1,m2)
print("matrix intersection :",min)
print("matrix union : ",mu)