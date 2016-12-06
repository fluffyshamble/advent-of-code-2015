def lift_sequence(filename):
    floor = 0
    instructions = open(filename, "r").read()
    for instruction in instructions:
        if instruction == "(":
            floor += 1
        elif instruction == ")":
            floor -= 1
        else:
            print "Invalid instruction in instructions"
    print "Floor: %s" % floor


if __name__ == "__main__":
    lift_sequence("instructions.txt")
