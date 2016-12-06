def lift_sequence(filename):
    floor = 0
    instructions = open(filename, "r").read()
    number_of_instructions = len(instructions)
    for i in range(0,number_of_instructions):
        if instructions[i] == "(":
            floor += 1
        elif instructions[i] == ")":
            floor -= 1
        else:
            print "Invalid instruction in instructions"
        if floor == -1:
            # use i + 1 to conform with AoC index rules
            print "Entered basement at instruction %s" % (i+1)
    print "Floor: %s" % floor


if __name__ == "__main__":
    lift_sequence("instructions.txt")
