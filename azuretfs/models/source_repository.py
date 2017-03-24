# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 1.0.1.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SourceRepository(Model):
    """SourceRepository.

    :param identifier:
    :type identifier: str
    :param properties: The properties cannot be IEnumerable/IList, since XML
     serializer does not work well with interfaces. This object gets passed as
     job parameter which uses XML serializer.
    :type properties: list of :class:`Property <azuretfs.models.Property>`
    :param repository_type:
    :type repository_type: object
    """

    _attribute_map = {
        'identifier': {'key': 'identifier', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '[Property]'},
        'repository_type': {'key': 'repositoryType', 'type': 'object'},
    }

    def __init__(self, identifier=None, properties=None, repository_type=None):
        self.identifier = identifier
        self.properties = properties
        self.repository_type = repository_type