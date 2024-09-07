from abc import ABC, abstractmethod, abstractclassmethod

# TODO -- Add support for standard exceptions.


class DataDataService(ABC):
    """
    Abstract base class for data service that defines the interface of concrete
    data service classes. This approach allows writing application logic that is
    independent from specific database choices.
    """

    def __init__(self, context):
        """
        This is a simple approach to dependency injection. The context will contain references
        to configuration information that an instance needs.
        :param context:
        """
        self.context = context

    @abstractmethod
    def _get_connection(self):
        """
        Create and return a connection to the database instance for this data services.
        :return: A connection.
        """
        raise NotImplementedError('Abstract method _get_connection()')

    @abstractmethod
    def get_data_object(self,
                        database_name: str,
                        collection_name: str,
                        key_field: str,
                        key_value: str):
        """
        Gets a single data object from a table in a database. Collection is an abstraction of a
        table in the relational model, collection in MongoDB, etc.

        :param database_name: Name of the database or similar abstraction.
        :param collection_name: The name of the collection, table, etc. in the database.
        :param key_field: A single column, field, ... that is a unique key/identifier.
        :param key_value: The value for the column, field, ... ...
        :return: The single object identified by the unique field.
        """
        raise NotImplementedError('Abstract method get_data_object()')

