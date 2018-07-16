#!/usr/bin/env python

__author__ = "Richard Clubb"
__copyrights__ = "Copyright 2018, the python-uds project"
__credits__ = ["Richard Clubb"]

__license__ = "MIT"
__maintainer__ = "Richard Clubb"
__email__ = "richard.clubb@embeduk.com"
__status__ = "Development"


from abc import ABCMeta, abstractmethod


class iTp:
    __metaclass__ = ABCMeta

    ##
    # @brief interface method
    @classmethod
    def send(self, payload):
        raise NotImplementedError("send function not implemented")

    ##
    # @brief interface method
    @classmethod
    def recv(self, timeout_ms):
        raise NotImplementedError("receive function not implemented")