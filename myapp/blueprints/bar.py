from flask import Blueprint
from myapp.api_result import ApiResult
# import os

from myapp.models.db import db
from myapp.models.Foos import Foo


bp = Blueprint('demo', __name__)

@bp.route('/foo')
def foo():
    # os.environ.get('var')
    new_foo = Foo(name='Potato')
    db.session.add(new_foo)
    db.session.commit()
    return ApiResult({'foo_id': new_foo.id})
