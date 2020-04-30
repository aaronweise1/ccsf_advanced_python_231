def deco_func(orig_func):
 def wrap_func():

  return orig_func()
 return wrap_func
@deco_func
def display():
 user = input(" please enter words: ")
 while user:
  if user[11:]:
   print(user)
   break 
  else:
   print(" You are entered more than 10 charactors")
   break
display()
