import strawberry


@strawberry.type
class AuthorQueries:
    @strawberry.field
    def all_authors(self) -> list[str]:
        return ["Haris Zahid", "Azhar Iqbal"]
