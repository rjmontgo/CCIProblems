#
# 1.8
# Assume you have a method isSubstring which checks if one word is a
# substring of another. Given two strings, s1 and s2, write code to check if s2 is
# a rotation of s1 using only one call to isSubstring (e.g., "waterbottle" is a
# rotation of "erbottlewat").
#
def isRotation(s1, s2):


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
