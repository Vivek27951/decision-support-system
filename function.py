import o
import c
n=0.2
def union(a,b,i):
      if a>=b:
            o.Q['m'+i]=b
      else:
            o.Q['m'+i]=a

def fuzzy(m,s,w,g,we):
      if g==5:
            return ((1-m)*(w/s))
      else:
            g+=1
            st=str(g)
            return ((1-m)*(w/s))+ fuzzy(abs(o.M['m'+st]-o.A['m'+st]),s,o.W[we][g],g,we)
      
def ct(F,cf):
      return F*cf

def result(we,ve,sums,cf):
      
      for j in range(6):
            
            k=str(j)
            union(o.M['m'+k],o.A['m'+k],k)

##      print(o.Q)
      g=0
      st=str(g)
      F1=fuzzy(abs(o.M['m'+st]-o.A['m'+st]),sums,o.W[we][g],g,we)
##      print(F1)
      print('\n\n---------------------------------------THE REPORT CARD-----------------------------------------------\n')
      t=o.Q['m0']+o.Q['m1']+o.Q['m2']+o.Q['m3']+o.Q['m4']+o.Q['m5']
      if t>0:
            if F1>n:
                  certainty=ct(F1,cf)
                  ce=c.certainty(certainty)
                  print('# the patient might have the diseas',o.V[ve],'with the digree of certainty of about',certainty,'that is (',ce,')\n\n')
            else:
                  print('\t\t# patient is good\n\n')

      else:
            print('\t\t# NO DISEASES FOUND\n\n')
