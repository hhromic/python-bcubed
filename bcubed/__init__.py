# Hugo Hromic - http://github.com/hhromic
#
# Extended BCubed algorithm taken from:
# Amigo, Enrique, et al. "A comparison of extrinsic clustering evaluation
# metrics based on formal constraints."
# Information retrieval 12.4 (2009): 461-486.

"""Extended BCubed evaluation for clustering."""

from bcubed.extended import precision
from bcubed.extended import recall

def fscore(p_val, r_val, beta=1.0):
    """Computes the F_{beta}-score of given precision and recall values."""
    return (1.0 + beta) * (p_val * r_val / (beta**2 * p_val + r_val))
