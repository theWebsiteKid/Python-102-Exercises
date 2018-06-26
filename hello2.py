name = raw_input("WHAT IS YOUR NAME?\n")
name_length = len(name)
name_length = str(name_length)

hello = ("Hello, %s!" % name).upper()
message = ("Your name has %s letters in it! Awesome!" % name_length).upper()

print hello
print message