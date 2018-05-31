
def has_cycle(head):
    T={}
    while(head!=None):
        if head not in T.keys():
            T[head]=1
        else:
            return 1
        head=head.next
    return 0
        