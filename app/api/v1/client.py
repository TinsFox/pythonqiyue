"""
    Created by  on 2019-07-26.
"""
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

__author__ = 'TinsFox'
api = Redprint('client')


@api.route('/register', methods=['GET', 'POST'])
def create_client():
    data = request.json
    form = ClientForm(data=data)
    if form.validate():
        print("eee")
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_user_by_email
        }
        promise[form.type.data]()
    print("e")
    return 'success'


def __register_user_by_email():
    form = UserEmailForm(data=request.json)
    if form.validate():
        User.register_by_email(form.nickname.data, form.account.data, form.secret.data)
