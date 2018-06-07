def combine(list_a, list_b, delim=""):
    if len(list_a) != len(list_b):
        raise Exception("List must have the same size!")

    result_list = []

    for i in xrange(len(list_a)):
        a = list_a[i]
        b = list_b[i]

        result_list.append(str(a) + delim + str(b))

    return result_list


def value_append(l, value):
    return ["{}{}".format(e,value) for e in l]


def value_prepend(l, value):
    return ["{}{}".format(e,value) for e in l]


def unique(l):
    return list(set(l))


def unique_with_order(seq):
    seen     = set()
    seen_add = seen.add

    return [x for x in seq if not (x in seen or seen_add(x))]


