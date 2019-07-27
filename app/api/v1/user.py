"""
    Created by  on 2019-07-26.
"""

__author__ = 'TinsFox'

from flask import Blueprint
from app.libs.redprint import Redprint

# blueprint
# redprint
# book = Blueprint('book', __name__)
api = Redprint('user')


@api.route('/get')
def get_user():
    return "get user"


@api.route('/create')
def create_user():

    return "get user"

# 用户 注册