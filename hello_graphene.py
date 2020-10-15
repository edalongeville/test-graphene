from graphene import ObjectType, String, Schema, Int, Field, List
import collections

User = collections.namedtuple("User", [ 'id', 'email', 'password', 'first_name', 'last_name', 'company'])

data = {
    1: User('1', 'jane@doe.com', 'qwerty', 'jane', 'doe', 'corpo'),
    2: User('2', 'john@doe.com', 'qwerty', 'john', 'doe', 'megacorp')
}


class UserType(ObjectType):
    # this defines a user account
    id = String()
    email = String()
    password = String()
    first_name = String()
    last_name = String()
    company = String()

    # Resolvers
    def resolve_id(user, info):
        return user.id
    
    def resolve_email(user, info):
        return user.email

    def resolve_password(user, info):
        return user.password

    def resolve_first_name(user, info):
        return user.first_name

    def resolve_last_name(user, info):
        return user.last_name

    def resolve_company(user, info):
        return user.company

class Query(ObjectType):
    user = Field(UserType, key=Int())
    users = List(UserType)

    def resolve_user(root, info, key):
        return data[key]

    def resolve_users(root, info):
        return data.values()

schema = Schema(query=Query)

# Open python3 and type:
# from hello_graphene import schema
# query = '{users {firstName, lastName} }'
# schema.execute(query).data
#
# Other queries:
# query = '{user(key: 1) {firstName, lastName} }'