from bluebirdlib.data import get_distinct_users, get_db, add_to_mongo

def main():

    connection = get_db("teenspirit")

    # Get unique user id from tweets
    users = get_distinct_users(connection=connection)

    # Insert all users in users db
    query = map(lambda x: {
        "user_id": x,
        "controls": []
    }, users)

    add_to_mongo(query, collection="users", connection=connection)


if __name__ == '__main__':
    main()
