tip_input = raw_input("Be honest... how much did you tip? \n")
tip = float(tip_input)

bill_input = raw_input("How much was the bill? \n")
bill = float(bill_input)

tip_ratio = tip / bill

is_stingy = tip_ratio < 0.10
is_generous = tip_ratio > 0.20

message = "You're %s tipper!"

if is_stingy:
    print message % "a stingy"
elif is_generous:
    print message % "a generous"
else:
    print message % "an average"