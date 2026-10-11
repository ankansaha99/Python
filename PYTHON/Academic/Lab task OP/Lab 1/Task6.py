def add_m(m1,m2):
    if len(m1)!=len(m2) or len(m1[0]) != len(m2[0]):

        return "MMMMMMM"

    res=[[0 for _ in range(len(m1[0]))] for _ in range(len(m1))]


    for i in range(len(m1)):
        for j in (len(m1[0])):
            res[i][j]= m1[i][j]+m2[i][j]
    return res
m1=[[1,2,3],[4,5,6],[7,8,9]]

m2=[[11,21,31],[41,51,61],[71,81,91]]


res_m= add_m(m1,m2)

for r in res_m:
    print(r)