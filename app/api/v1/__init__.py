"""
    Created by  on 2019-07-26.
"""

__author__ = 'TinsFox'


from flask import Blueprint
from app.api.v1 import user, book, client


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    user.api.register(bp_v1)
    book.api.register(bp_v1)
    client.api.register(bp_v1)
    return bp_v1
