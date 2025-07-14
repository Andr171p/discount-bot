
class ServiceError(Exception):
    pass


class RequestFailed(ServiceError):
    pass


class RepositoryError(Exception):
    pass


class CreationError(RepositoryError):
    pass


class ReadingError(RepositoryError):
    pass
