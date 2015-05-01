# Hugo Hromic - http://github.com/hhromic
#
# Extended BCubed algorithm taken from:
# Amigo, Enrique, et al. "A comparison of extrinsic clustering evaluation
# metrics based on formal constraints."
# Information retrieval 12.4 (2009): 461-486.

"""Generate extended BCubed evaluation for clustering."""

import numpy

def mult_precision(el1, el2, cdict, ldict):
    """Computes the multiplicity precision for two elements."""
    return min(len(cdict[el1] & cdict[el2]), len(ldict[el1] & ldict[el2])) \
        / float(len(cdict[el1] & cdict[el2]))

def mult_recall(el1, el2, cdict, ldict):
    """Computes the multiplicity recall for two elements."""
    return min(len(cdict[el1] & cdict[el2]), len(ldict[el1] & ldict[el2])) \
        / float(len(ldict[el1] & ldict[el2]))

def precision(cdict, ldict):
    """Computes overall extended BCubed precision for the C and L dicts."""
    return numpy.mean([numpy.mean([mult_precision(el1, el2, cdict, ldict) \
        for el2 in cdict if cdict[el1] & cdict[el2]]) for el1 in cdict])

def recall(cdict, ldict):
    """Computes overall extended BCubed recall for the C and L dicts."""
    return numpy.mean([numpy.mean([mult_recall(el1, el2, cdict, ldict) \
        for el2 in cdict if ldict[el1] & ldict[el2]]) for el1 in cdict])
