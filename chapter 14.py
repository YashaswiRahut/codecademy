def count(sequence, item):
  c=0
  for i in sequence :
    if i==item:
      c+=1
  return c

def purify(l):
  new=[]
  for i in l:
    if i%2==0:
      new.append(i)
  return new

def product(l):
  p=1;
  for i in l:
    p=p*i
  return p
