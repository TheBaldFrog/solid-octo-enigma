from utils.db_api.sqlite import Database

db = Database()


def test():
    db.create_table_users()
    users = db.select_all_users()

    print(f"until add users: {users}")
    db.add_user(1, "One", "email1")
    db.add_user(2, "Two", "email2")
    db.add_user(3, "Three", "email3")
    db.add_user(4, "Four", "email4")
    db.add_user(5, "Five", "email5")

    users = db.select_all_users()
    print(f"after add users: {users}")

    user = db.select_user(Name="Five", id=5)
    print(f"user: {user}")


test()
