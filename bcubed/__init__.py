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

"""Extended BCubed evaluation for clustering."""

from bcubed.extended import precision
from bcubed.extended import recall

def fscore(p_val, r_val, beta=1.0):
    """Computes the F_{beta}-score of given precision and recall values.

    Parameters
    ==========
    p_val: float
        The precision value to use for the F-score
    r_val: float
        The recall value to to use for the F-score
    beta: float
        The beta parameter for computing the F-score
    """
    return (1.0 + beta**2) * (p_val * r_val / (beta**2 * p_val + r_val))
