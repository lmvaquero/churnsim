import networkx as nx

class FailureGenerator():

    _failure_lib = {}
    _immutable = {}

    def add_failure_mode(self, failure_mode, failure_name, protected=False):
        """
        Adds a new failure mode to the set of available Failure Generators; Does not add anything if the name already exists;
        Use replace failure mode to overwrite a pre-existing one
            inputs:
                failure_mode_name: unique name of the failure mode to be added
                failure_mode: function that maps from a given topology into a subset of that topology where some nodes
                                and edges have been deleted or modified
                protected: is it an immutable failure mode? If so, set this param to true and it cannot be overwritten

            return: boolean indicating if the failure mode was successfully added or not
        """
        if(not self._valid_params(failure_mode, failure_name) or failure_name in self._failure_lib.keys()):
            return False

        self._failure_lib[failure_name]= failure_mode
        self._immutable[failure_name] = protected
        return True

    def replace_failure_mode(self, failure_mode, failure_name):
        """
        Replaces previously existing failure mode to the set of available Failure Generators
            inputs:
                failure_mode_name: unique name of the failure mode to be added
                failure_mode: function that maps from a given topology into a subset of that topology where some nodes
                                and edges have been deleted or modified

            return: boolean indicating if the failure mode was successfully replaced or not
        """
        if (not self._valid_params(failure_mode, failure_name)
                or failure_name not in self._failure_lib.keys()
                or self._immutable[failure_name]):
            return False

        self._failure_lib[failure_name] = failure_mode
        return True

    def delete_failure_mode(self, failure_name):
        """
        Removes failure mode from the set of available Failure Generators
            inputs:
                failure_mode_name: unique name of the failure mode to be removed
        """
        if (failure_name is "" or not failure_name in self._failure_lib.keys()):
            return

        del self._failure_lib[failure_name]
        del self._immutable[failure_name]

    def get_failure_mode_names(self):
        return self._failure_lib.keys()

    def _valid_params(self, failure_name, failure_mode):
        return failure_name is not "" and failure_mode is not None
