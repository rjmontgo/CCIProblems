#
# 1.9
# Assume you have a method isSubstring which checks if one word is a
# substring of another. Given two strings, s1 and s2, write code to check if s2 is
# a rotation of s1 using only one call to isSubstring (e.g., "waterbottle" is a
# rotation of "erbottlewat").
#
def isRotation(s1, s2):
    concat = s2 + s2
    return s1 in concat

# Parameters -> (String: s1, String: s2) -> Can I trust correct input? Yes
# Return value -> True if s2 is a rotation of s1; else False

# Simplest Problem
# IN - ("a", "a")
# OUT - True

# V2
# IN - ("ba", "ab")
# OUT - True

# V3
# IN - ("watermelon", "lonwaterme")
# OUT - True

# V4
# IN - ("reduce", "ucered")
# OUT - True

# V5
# IN - ("waterbottle", "erbottlewat")
# OUT - True

# V6
# IN - ("testing", "testin")
# OUT - False

# V7
# IN - ("testing", "tesitng")
# OUT - False

# Patterns
# - Perhaps better to think of it as swapping parts of the string rather than
# rotating (i.e bottlewater is waterbottle when swapping 'bottle' and 'water'
# - Adding bottlewater + bottlewater we have bottlewaterbottlewater
#   - The original string is a substring

#
# Solution / complexity where n is the length of s2
# 1. Concatenate s2 and check if it has s1 as a substring
#    / O(n) - time due to substring check and concatenation.
#    / O(n) - space due to having to make a new string to hold the result of
#             concatenation.
#
# 2. Rotate s2 by one char until we reach the original string or we equal s1
#    / O(n^2) - time because we must loop the rotate operation n times and the
#               rotate operation states we
