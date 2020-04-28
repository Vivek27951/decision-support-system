import o
import f
print('-----------------------WELCOME TO THE THE DSS---------------------------\n\n')
print('     *****SYMPTOMS*****                       *****SEVERITY*****\n')
for i in range(6):
      s=str(i)
      o.A['m'+s]=float(input('enter the severity of the symptom M'+s+'\t\t'))
#print(o.A)
      
if o.A==o.user['u1']:
      cf=0.98
      sum1=sum(o.W['w1'])
      #print(sum1)
      we='w1'
      f.result(we,0,sum1,cf)

elif o.A==o.user['u2']:
      cf=0.90
      sum2=sum(o.W['w2'])
      #print(sum2)
      we='w2'
      f.result(we,1,sum2,cf)

elif o.A==o.user['u3']:
      cf=0.92
      sum3=sum(o.W['w3'])
      #print(sum3)
      we='w3'
      f.result(we,2,sum3,cf)

elif o.A==o.user['u4']:
      cf=0.95
      sum4=sum(o.W['w4'])
      #print(sum4)
      we='w4'
      f.result(we,3,sum4,cf)

elif o.A==o.user['u5']:
      cf=0.96
      sum5=sum(o.W['w5'])
      #print(sum5)
      we='w5'
      f.result(we,4,sum5,cf)

else:
      print('\n\n\t\twell done you are fine with no diseases')
      












