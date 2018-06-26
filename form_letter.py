first_name = raw_input("Person's first name: ")
last_name = raw_input("Person's last name: ")

message = "Hello, %s %s! Please get in touch. We want to hire YOU!" % (first_name, last_name)
length = len(message)

print length
print message