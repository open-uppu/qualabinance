"""Purged / embargoed cross-validation splits (Lopez de Prado, AFML ch.7).

Two tools:
- walk_forward_folds: contiguous out-of-sample segments for strategy
  validation without training. Indicator warmup context before each fold
  is legitimate (past data only); no future information crosses a boundary.
- purged_kfold_indices: k-fold with purge + embargo for future ML
  meta-labeling, where overlapping label horizons leak across folds.
"""

from __future__ import annotations

from typing import Iterator, List, Tuple

import numpy as np


def walk_forward_folds(n_bars: int, n_folds: int, warmup_bars: int) -> List[Tuple[int, int]]:
    """Split [warmup_bars, n_bars) into n_folds contiguous (start, end) ranges."""
    if n_folds < 1 or n_bars <= warmup_bars:
        return []
    edges = np.linspace(warmup_bars, n_bars, n_folds + 1).astype(int)
    return [(int(edges[k]), int(edges[k + 1])) for k in range(n_folds)
            if edges[k + 1] > edges[k]]


def fold_index_for_bar(folds: List[Tuple[int, int]]):
    """Return fn(bar_idx) -> fold index or None (outside all folds)."""
    def fn(bar: int):
        for k, (s, e) in enumerate(folds):
            if s <= bar < e:
                return k
        return None
    return fn


def purged_kfold_indices(
    n_samples: int, n_folds: int, purge_bars: int, embargo_bars: int = 0
) -> Iterator[Tuple[np.ndarray, np.ndarray]]:
    """Yield (train_idx, test_idx) with purge around test block + embargo after.

    purge_bars must cover the maximum label/trade horizon so no training
    sample overlaps the test period's information set.
    """
    if n_folds < 2:
        raise ValueError("n_folds must be >= 2")
    edges = np.linspace(0, n_samples, n_folds + 1).astype(int)
    all_idx = np.arange(n_samples)
    for k in range(n_folds):
        ts, te = int(edges[k]), int(edges[k + 1])
        if te <= ts:
            continue
        test = all_idx[ts:te]
        lo = max(0, ts - purge_bars)
        hi = min(n_samples, te + purge_bars + embargo_bars)
        mask = np.ones(n_samples, dtype=bool)
        mask[lo:hi] = False
        yield all_idx[mask], test