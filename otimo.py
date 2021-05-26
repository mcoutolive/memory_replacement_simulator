print("Digite o numero de frames: ",end="")
capacity = int(input())
f,fault,pf = [],0,'Nao'
print("E' importante que os numeros digitados sejam separados por um espaco. Digite a string de referencia: ",end="")
s = list(map(int,input().strip().split()))
print("\nString|Frame →\t",end='')
for i in range(capacity):
    print(i,end=' ')
print("Houve page fault?\n   ↓\n")
occurance = [None for i in range(capacity)]
for i in range(len(s)):
    if s[i] not in f:
        if len(f)<capacity:
            f.append(s[i])
        else:
            for x in range(len(f)):
                if f[x] not in s[i+1:]:
                    f[x] = s[i]
                    break
                else:
                    occurance[x] = s[i+1:].index(f[x])
            else:
                f[occurance.index(max(occurance))] = s[i]
        fault += 1
        pf = 'Sim'
    else:
        pf = 'Nao'
    print("   %d\t\t"%s[i],end='')
    for x in f:
        print(x,end=' ')
    for x in range(capacity-len(f)):
        print(' ',end=' ')
    print(" %s"%pf)
print("\nTotal de solicitacoes: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(s),fault,(fault/len(s))*100))
