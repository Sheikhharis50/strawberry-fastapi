import strawberry

from .author.mutations import AuthorMutations
from .author.queries import AuthorQueries


@strawberry.type
class Query(
    AuthorQueries,
):
    """Query class inherit all the queries provided by this app"""

    ...


@strawberry.type
class Mutation(
    AuthorMutations,
):
    """Mutation class inherit all the queries provided by this app"""

    ...


schema = strawberry.Schema(query=Query, mutation=Mutation)
