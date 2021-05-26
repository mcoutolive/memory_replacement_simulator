print("Digite o numero de frames: ",end="")
capacity = int(input())
f,st,fault,pf = [],[],0,'Nao'
print("E' importante que os numeros digitados sejam separados por um espaco. Digite a string de referencia: ",end="")
s = list(map(int,input().strip().split()))
print("\nString|Frame →\t",end='')
for i in range(capacity):
    print(i,end=' ')
print("Houve page fault?\n   ↓\n")
for i in s:
    if i not in f:
        if len(f)<capacity:
            f.append(i)
            st.append(len(f)-1)
        else:
            ind = st.pop(0)
            f[ind] = i
            st.append(ind)
        pf = 'Sim'
        fault += 1
    else:
        st.append(st.pop(st.index(f.index(i))))
        pf = 'Nao'
    print("   %d\t\t"%i,end='')
    for x in f:
        print(x,end=' ')
    for x in range(capacity-len(f)):
        print(' ',end=' ')
    print(" %s"%pf)
print("\nTotal Requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(s),fault,(fault/len(s))*100))
