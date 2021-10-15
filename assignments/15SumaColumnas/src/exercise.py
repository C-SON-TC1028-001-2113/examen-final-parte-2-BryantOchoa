def crearm():
    lista = []
    row = int(input())
    column = int(input())
    if row > 0 and column > 0: 
        for i in range(row):
            lista.append([])
            for j in range(column):
                n = int(input())
                lista[i].append(n)
    else: 
        print('Error')
    return lista

def main():
    m = crearm()
    collist = []
    if len(m) > 0:
        for i in range(len(m[0])):
            count = 0
            for j in range(len(m)):
                count += m[j][i] 
            collist.append(count)
        print(collist)

if __name__=='__main__':
    main()
