l=list(map(int,input("Enter elements of list separated using space:").split()))
while (1):
    print("\t\tMenu")
    print("1.Maximum value")
    print("2.Minium value")
    print("3.Slice of list")
    print("4.count occurrence")
    print("5.First occurrence")
    print("6.exit")
    ch=int(input("Enter choice:"))
    if ch ==1:
        print("Maximum:",max(l))
    elif ch==2:
        print("Minimum:",min(l))
    elif ch==3:
        print("Slice the list")
        s=int(input("Enter starting index:"))
        e=int(input("Enter ending index:"))
        print("Slice list:",l[s:e])
    elif ch==4:
        item=int(input("Enter item to be found:"))
        print("Occurrence :",l.count(item))
    elif ch==5:
        item=int(input("Enter item to be found:"))
        if item in l:
            print("First occurrence index:",l.index(item))
        else:
            print("Item not found")
    elif ch==6:
        print("Exit")
        break
    else:
        print("Invalid choice")
