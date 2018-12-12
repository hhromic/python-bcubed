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

"""Examples for computing extended BCubed.

   cdict: dictionary representing a particular clustering output
   ldict: dictionary representing the ground-truth or gold-standard data

   Format for both dictionaries: {item: set of assigned clusters/real categories}

   The values are sets to support overlapping clustering and ground-truth categories.
"""

import bcubed

def compute(title, cdict, ldict):
    """Compute extended BCubed precision and recall, and print the results."""
    precision = bcubed.precision(cdict, ldict)
    recall = bcubed.recall(cdict, ldict)
    fscore = bcubed.fscore(precision, recall)
    print("{}: precision={:.2f}, recall={:.2f}, fscore={:.2f}".format(
        title, precision, recall, fscore))

# example ground-truth data (ldict)
ground_truth = {
    "item1": set(["gray", "black"]),
    "item2": set(["gray", "black"]),
    "item3": set(["gray"]),
    "item4": set(["black"]),
    "item5": set(["black"]),
    "item6": set(["dashed"]),
    "item7": set(["dashed"]),
}

# example clustering (cdict) in page 24, figure 16
clustering = {
    "item1": set(["A", "B"]),
    "item2": set(["A", "B"]),
    "item3": set(["A"]),
    "item4": set(["B"]),
    "item5": set(["B"]),
    "item6": set(["C"]),
    "item7": set(["C"]),
}
compute("page 24, figure 16", clustering, ground_truth)

# example clustering (cdict) in page 24, figure 17
clustering = {
    "item1": set(["ADup", "A", "B"]),
    "item2": set(["ADup", "A", "B"]),
    "item3": set(["ADup", "A"]),
    "item4": set(["B"]),
    "item5": set(["B"]),
    "item6": set(["C"]),
    "item7": set(["C"]),
}
compute("page 24, figure 17", clustering, ground_truth)

# example clustering (cdict) in page 24, figure 18
clustering = {
    "item1": set(["ADup2", "ADup", "A", "B"]),
    "item2": set(["ADup2", "ADup", "A", "B"]),
    "item3": set(["ADup2", "ADup", "A"]),
    "item4": set(["B"]),
    "item5": set(["B"]),
    "item6": set(["C"]),
    "item7": set(["C"]),
}
compute("page 24, figure 18", clustering, ground_truth)

# example clustering (cdict) in page 24, figure 19
clustering = {
    "item1": set(["A"]),
    "item2": set(["A"]),
    "item3": set(["A"]),
    "item4": set(["B"]),
    "item5": set(["B"]),
    "item6": set(["C"]),
    "item7": set(["C"]),
}
compute("page 24, figure 19", clustering, ground_truth)

# example clustering (cdict) in page 25, figure 20
clustering = {
    "item1": set(["A", "B"]),
    "item2": set(["A", "B"]),
    "item3": set(["A"]),
    "item4": set(["D"]),
    "item5": set(["D"]),
    "item6": set(["C"]),
    "item7": set(["C"]),
}
compute("page 25, figure 20", clustering, ground_truth)

# example clustering (cdict) in page 25, figure 21
clustering = {
    "item1": set(["A"]),
    "item2": set(["A"]),
    "item3": set(["A"]),
    "item4": set(["A"]),
    "item5": set(["A"]),
    "item6": set(["B"]),
    "item7": set(["B"]),
}
compute("page 25, figure 21", clustering, ground_truth)
