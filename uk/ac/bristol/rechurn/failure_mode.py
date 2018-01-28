import abc

class FailureMode(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_new_topology(self, topology):
        """
        Gets the current topology and kocks down some nodes
            inputs:
                topology: current Topology
            return: derived Topology with knocked down nodes
        """
        raise NotImplementedError('users must define this method to use this base class')