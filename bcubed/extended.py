# Simple extended BCubed implementation in Python for clustering evaluation
# Copyright 2015 Hugo Hromic
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Extended BCubed algorithm taken from:
# Amigo, Enrique, et al. "A comparison of extrinsic clustering evaluation metrics
# based on formal constraints." Information retrieval 12.4 (2009): 461-486.

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
    """Computes overall extended BCubed precision for the C and L dicts.

    Parameters
    ==========
    cdict: dict(item: set(cluster-ids))
        The cluster assignments to be evaluated
    ldict: dict(item: set(cluster-ids))
        The ground truth clustering
    """
    return numpy.mean([numpy.mean([mult_precision(el1, el2, cdict, ldict) \
        for el2 in cdict if cdict[el1] & cdict[el2]]) for el1 in cdict])

def recall(cdict, ldict):
    """Computes overall extended BCubed recall for the C and L dicts.

    Parameters
    ==========
    cdict: dict(item: set(cluster-ids))
        The cluster assignments to be evaluated
    ldict: dict(item: set(cluster-ids))
        The ground truth clustering
    """
    return numpy.mean([numpy.mean([mult_recall(el1, el2, cdict, ldict) \
        for el2 in cdict if ldict[el1] & ldict[el2]]) for el1 in cdict])
