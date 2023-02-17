import strawberry


@strawberry.type
class AuthorMutations:
    @strawberry.field
    def add_author(self, name: str) -> str:
        return name
