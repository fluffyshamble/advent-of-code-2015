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
    print "Floor: %s" % floor


if __name__ == "__main__":
    lift_sequence("test_instructions.txt")
