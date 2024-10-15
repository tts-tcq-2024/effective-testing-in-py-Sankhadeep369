def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'

# Strengthening the test cases
assert(size(37) == 'S')  # Valid
assert(size(38) == 'M')  # Added test for edge case that will fail (should return M but it's unhandled)
assert(size(40) == 'M')  # Valid
assert(size(43) == 'L')  # Valid

print("All is well (maybe!)\n")
