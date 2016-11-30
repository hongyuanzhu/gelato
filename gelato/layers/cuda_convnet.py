import sys
from lasagne.layers.cuda_convnet import __all__
import lasagne.layers.cuda_convnet as __cloned
from .base import bayes
__module = sys.modules[__name__]
del sys
for obj_name in __all__:
    try:
        setattr(__module, obj_name, bayes(getattr(__cloned, obj_name)))
    except TypeError:
        setattr(__module, obj_name, getattr(__cloned, obj_name))