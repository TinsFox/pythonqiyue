"""
    Created by  on 2019-07-26.
"""

__author__ = 'TinsFox'

from app.libs.redprint import Redprint

api = Redprint('book')


@api.route('/', methods=["GET"])
def get_book():
    return "get book"


@api.route('/', methods=["POST"])
def create_book():
    return "create book"
