# test app
from app import app, db, SUser, write_user_sqlalchemy
from faker import Faker
import logging as log

# app = create_app already ran
fake = Faker()
app.app_context().push()


def test_make_db():
    db.create_all()
    assert True # don't know how to check
def test_add_users(clean_after=True):
    x = 10
    for i in range(x):
        log.info(i)
        name = fake.first_name()
        log.info(name)
        write_user_sqlalchemy(name, 'password')
    assert len(SUser.query.all()) == x
    if clean_after:
        nuke_db()

def nuke_db():
    db.drop_all()
    return True