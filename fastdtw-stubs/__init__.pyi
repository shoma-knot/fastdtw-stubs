import numpy as np
import numpy.typing as type_np
from typing import Callable

# Docstring was copy-pasted from fastdtw sources.

def fastdtw(
    x: type_np.NDArray[np.float64],
    y: type_np.NDArray[np.float64],
    radius: int = 1,
    dist: Callable[[type_np.NDArray[np.float64], type_np.NDArray[np.float64]], float]
    | int
    | None = None,
) -> tuple[float, list[tuple[float, float]]]:
    """return the approximate distance between 2 time series with O(N)
    time and memory complexity

    Parameters
    ----------
    x : array_like
        input array 1
    y : array_like
        input array 2
    radius : int
        size of neighborhood when expanding the path. A higher value will
        increase the accuracy of the calculation but also increase time
        and memory consumption. A radius equal to the size of x and y will
        yield an exact dynamic time warping calculation.
    dist : function or int
        The method for calculating the distance between x[i] and y[j]. If
        dist is an int of value p > 0, then the p-norm will be used. If
        dist is a function then dist(x[i], y[j]) will be used. If dist is
        None then abs(x[i] - y[j]) will be used.

    Returns
    -------
    distance : float
        the approximate distance between the 2 time series
    path : list
        list of indexes for the inputs x and y

    Examples
    --------
    >>> import numpy as np
    >>> import fastdtw
    >>> x = np.array([1, 2, 3, 4, 5], dtype='float')
    >>> y = np.array([2, 3, 4], dtype='float')
    >>> fastdtw.fastdtw(x, y)
    (2.0, [(0, 0), (1, 0), (2, 1), (3, 2), (4, 2)])
    """
    pass

def dtw(
    x: type_np.NDArray[np.float64],
    y: type_np.NDArray[np.float64],
    radius: int = 1,
    dist: Callable[[type_np.NDArray[np.float64], type_np.NDArray[np.float64]], float]
    | int
    | None = None,
) -> tuple[float, list[tuple[float, float]]]:
    """return the distance between 2 time series without approximation

    Parameters
    ----------
    x : array_like
        input array 1
    y : array_like
        input array 2
    dist : function or int
        The method for calculating the distance between x[i] and y[j]. If
        dist is an int of value p > 0, then the p-norm will be used. If
        dist is a function then dist(x[i], y[j]) will be used. If dist is
        None then abs(x[i] - y[j]) will be used.

    Returns
    -------
    distance : float
        the approximate distance between the 2 time series
    path : list
        list of indexes for the inputs x and y

    Examples
    --------
    >>> import numpy as np
    >>> import fastdtw
    >>> x = np.array([1, 2, 3, 4, 5], dtype='float')
    >>> y = np.array([2, 3, 4], dtype='float')
    >>> fastdtw.dtw(x, y)
    (2.0, [(0, 0), (1, 0), (2, 1), (3, 2), (4, 2)])
    """
    pass
