"""
Name- Dev Kumar Gangwar
class- Sec(q)
roll- 191550027{25} 
"""

def jacard(d1, d2):
    """
    Calculates the jacard similarity between two documents.
    """
    d1 = set(d1)
    d2 = set(d2)
    return len(d1.intersection(d2)) / len(d1.union(d2))

d1=(0,1,2,5,6)
d2=(0,2,3,5,7,9)
print(jacard(d1, d2))