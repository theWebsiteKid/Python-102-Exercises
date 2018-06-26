print "Let's play a game :O"

name = raw_input("What is your name?\n")
number = raw_input("Hello, %s! What is your favorite number?\n" % name)
color = raw_input("Cool! Now, what color is your shirt?\n")

template = "%s has %s %s dragons!"
message = template % (name, number, color)

print message