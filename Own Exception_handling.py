class E(Exception):
    pass


try:
    raise E("My Fault ")
except Exception as i:
    print(i)
