from nose.tools import *
from mock import Mock, MagicMock, patch, call

import os

HERE = os.path.dirname(__file__)


def fixture(name):
    return open(os.path.join(HERE, 'fixtures', name)).read()


class CollectdConfig(object):
    def __init__(self, key, vals, children):
        self.key = key
        self.values = (vals,)
        self.children = [
            CollectdConfig(k,v,c)
            for k,v,c in children
        ]
