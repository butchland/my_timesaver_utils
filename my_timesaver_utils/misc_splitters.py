# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/06_misc_splitters.ipynb (unless otherwise specified).

__all__ = ["FASTAI_AVAILABLE", "DumbFixedSplitter", "SubsetPercentageSplitter"]


# Cell
# from my_timesaver_utils.profiling import *

# Cell
import warnings

FASTAI_AVAILABLE = True
try:
    from fastcore.foundation import L
except ImportError as e:
    FASTAI_AVAILABLE = False
    warnings.warn("fastai package not installed, callback simulated")

# Cell
if not FASTAI_AVAILABLE:

    def L(*args, **kwargs):
        return list(*args)


# Cell
def DumbFixedSplitter(train_pct):
    "A splitter that takes the 1st `train_pct` as the train elements"
    assert 0 < train_pct < 1

    def _inner(o):
        o_len = len(o)
        train_len = int(o_len * train_pct)
        idxs = L(list(range(o_len)))
        return idxs[:train_len], idxs[train_len:]

    return _inner


# Cell


def SubsetPercentageSplitter(
    main_splitter, train_pct=0.5, valid_pct=None, randomize=False, seed=None
):
    "Take fixed pct of `splits` with `train_pct` and `valid_pct` from main splitter"
    assert main_splitter is not None
    assert 0 <= train_pct <= 1
    valid_pct = train_pct if valid_pct is None else valid_pct
    assert 0 <= valid_pct <= 1
    if randomize:
        if seed is not None:
            rng = random.Random(seed)
        else:
            rng = random.Random(random.randint(0, 2**32 - 1))

    def _inner(o):
        train_idxs, valid_idxs = main_splitter(o)
        train_len = int(len(train_idxs) * train_pct)
        valid_len = int(len(valid_idxs) * valid_pct)
        if randomize:
            train_idxs = rng.sample(train_idxs, train_len)
            valid_idxs = rng.sample(valid_idxs, valid_len)
        return train_idxs[:train_len], valid_idxs[:valid_len]

    return _inner
