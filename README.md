# python-bcubed

Simple extended BCubed implementation in Python for (non-)overlapping clustering evaluation.

More information on BCubed and details of the algorithm can be found in the following publication:

> Amigó, Enrique, et al.: A comparison of Extrinsic Clustering Evaluation Metrics based on Formal Constraints. In: Information Retrieval 12.4 (2009): 461-486.

## Installation

You can simply use `pip` (or any similar package manager) for installation:

    pip install bcubed

or, if you prefer a local user installation:

    pip install --user bcubed

## Usage

To evaluate any clustering output you will need **ground-truth data** (also called gold-standard data). We call this the `ldict`. The ground-truth is represented in a dictionary where the keys are items in the gold-standard and the values are sets of annotated categories for those items. For example:

```python
ldict = {
    "item1": set(["gray", "black"]),
    "item2": set(["gray", "black"]),
    "item3": set(["gray"]),
    "item4": set(["black"]),
    "item5": set(["black"]),
    "item6": set(["dashed"]),
    "item7": set(["dashed"]),
}
```

In the above example, `item1` is assigned two categories in the ground-truth: `gray` and `black`. For the case of `item6` and `item7`, both are assigned the single annotation `dashed`. This representation supports modelling overlapping and non-overlapping ground-truth data.

The **clustering output** to be evaluated is called the `cdict` and is also represented as a dictionary in the same way as the `ldict`. In this case, the keys are items in the clustering output and the values are the sets of assigned clusters for those items. For example:

```python
cdict = {
    "item1": set(["A", "B"]),
    "item2": set(["A", "B"]),
    "item3": set(["A"]),
    "item4": set(["B"]),
    "item5": set(["B"]),
    "item6": set(["C"]),
    "item7": set(["C"]),
}
```

Please note that the clusters names (or IDs) **do not need** to be the same as in the ground-truth data because the algorithm only considers the groupings, it does not try to match the names of clusters to the ground-truth categories.

Once you have defined the `ldict` (ground-truth data) and the `cdict` (clustering output to evaluate), you can simply do the following to obtain the extended BCubed precision and recall metric values:

```python
import bcubed

precision = bcubed.precision(cdict, ldict)
recall = bcubed.recall(cdict, ldict)
fscore = bcubed.fscore(precision, recall)
```

There is also included an [F-score](http://en.wikipedia.org/wiki/F1_score) (also called F-measure) function for your convenience. This function accepts non-standard values for the beta parameter if you need, as follows:

```python
fscore = bcubed.fscore(precision, recall, beta=2.0)  # weights recall higher
fscore = bcubed.fscore(precision, recall, beta=0.5)  # weights precision higher
```

A complete example can be found in the included `example.py` file, where the examples of the source publication are used.

## License

This software is under the **Apache License 2.0**.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

