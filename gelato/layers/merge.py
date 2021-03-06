import sys
import lasagne.layers.merge as __cloned
from .base import bayes as __bayes
__module = sys.modules[__name__]
del sys
__all__ = [
    "autocrop",
    "autocrop_array_shapes",
    "ConcatLayer",
    "concat",
    "ElemwiseMergeLayer",
    "ElemwiseSumLayer",
]
for obj_name in __all__:
    try:
        setattr(__module, obj_name, __bayes(getattr(__cloned, obj_name)))
    except TypeError:
        setattr(__module, obj_name, getattr(__cloned, obj_name))
