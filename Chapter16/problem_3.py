

def lineIntersection(l1, l2):
    l1.startPoint, l1.endPoint = (l1.startPoint, l1.endPoint) if \
                                  l1.startPoint[0] < l1.endPoint[0] else \
                                 (l1.endPoint, l1.startPoint)

    l2.startPoint, l2.endPoint = (l2.startPoint, l2.endPoint) if \
                                  l2.startPoint[0] < l2.endPoint[0] else \
                                 (l2.endPoint, l2.startPoint)
    domainLower = max(l1.startPoint[0], l2.startPoint[0])
    domainUpper = min(l1.endPoint[0], l2.endPoint[0])
    if domainUpper < domainLower:
        return False

    slope1 = (l1.startPoint[1] - l1.endPoint[1]) / (l1.startPoint[0] - \
                                                    l1.endPoint[0])
    slope2 = (l2.startPoint[1] - l2.endPoint[1]) / (l2.startPoint[0] - \
                                                    l2.endPoint[0])
    yint1 = -slope1 * l1.startPoint[0] + l1.startPoint[1]
    yint2 = -slope2 * l2.startPoint[0] + l2.startPoint[1]

    if slope1.as_integer_ratio() == slope2.as_integer_ratio():
        return yint1.as_integer_ratio() == yint2.as_integer_ratio()
    else:
        interpoint = (yint1 - yint2) / (slope2 - slope1)
        return interpoint >= domainLower and interpoint <= domainUpper
