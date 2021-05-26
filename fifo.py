print("Digite o numero de frames: ",end="")
capacidade = int(input())

f,fault,top,pf = [],0,0,'Nao'

print("E' importante que os numeros digitados sejam separados por um espaco. Digite a string de referencia: ",end="")
s = list(map(int,input().strip().split()))

print("\nString|Frame →\t",end='')
for i in range(capacidade):
    print(i,end=' ')
print("Houve page fault?\n   ↓\n")
for i in s:
    if i not in f:
        if len(f)<capacidade:
            f.append(i)
        else:
            f[top] = i
            top = (top+1)%capacidade
        fault += 1
        pf = 'Sim'
    else:
        pf = 'Nao'
    print("   %d\t\t"%i,end='')
    for x in f:
        print(x,end=' ')
    for x in range(capacidade-len(f)):
        print(' ',end=' ')
    print(" %s"%pf)
print("\nTotal de solicitacoes: %d\nPage Fault Total = %d\nFault Rate: %0.2f%%"%(len(s),fault,(fault/len(s))*100))
