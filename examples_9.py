#projectEuler problem 9 
#problem address : https://projecteuler.net/problem=9
#This code finds Pythagorean triples for which a+b+c=1000

def PytogranTriples():
    a,b,c=0,0,0
    while (a+b+c)!=1000:
        for a in range(334):
            for b in range(a+1,500):
                c=1000-a-b
                if(a**2+b**2==c**2):
                    print(a,b,c)
                    return 0
                    
            
            
            
PytogranTriples()