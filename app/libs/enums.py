"""
    Created by  on 2019-07-26.
"""

__author__ = 'TinsFox'
from enum import Enum


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201
    pass
