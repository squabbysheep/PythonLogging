#!/usr/bin/env python
# coding:utf-8
"""
@Name   : first.py
@Author : myLove
@Email  : 17859717522@163.com
@Time   : 2019/7/26
"""
import logging

# 修改默认级别,并修改log文件地址
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, filename='coder.log', filemode='a')

logging.debug('崔庆才丨静觅、韦世东丨奎因')
logging.warning('邀请你关注微信公众号【进击的 Coder】')
logging.info('和大佬一起coding、共同进步')
