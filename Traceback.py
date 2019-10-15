import traceback
def inverse(a):
    return 1/a
try:
    inverse(0)
except Exception:
    traceback.print_exc(file=open('Body.txt','w'))

print("BY")
