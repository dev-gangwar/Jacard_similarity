Name="Dev Kumar Gangwar"
Sec='Q-1'
Roll='25'
uni_Roll='191550027'
set1 = "Jack London traveled to Ockland"
set2 = "Jack london traveled to city of Ockland"
set3="Jack traveled from Ockland to LOndon"

def shingle(set1,n):
    return [set1[i:i+n] for i in range(len(set1)-n+1)]
s1=shingle(set1,2)
s2=shingle(set2,2)
s3=shingle(set3,2)
def Jaccard(set1, set2,set3):
    set1=set(s1)
    set2=set(s2)
    set3=set(s3)
    a  = len(set1.intersection(set2)) / len(set1.union(set2))
    b  = len(set1.intersection(set3)) / len(set1.union(set3))
    liASt=[a,b]
    return liASt
print(Jaccard(s1,s2,s3))