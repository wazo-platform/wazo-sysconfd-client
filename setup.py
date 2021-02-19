#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import setup, find_packages

setup(
    name='wazo_sysconfd_client',
    version='0.1',
    description='a simple client library for the wazo-sysconfd HTTP interface',
    author='Wazo Authors',
    author_email='dev@wazo.community',
    url='http://wazo.community',
    packages=find_packages(),
    entry_points={
        'wazo_sysconfd_client.commands': [
            'dhcpd_update = wazo_sysconfd_client.commands.dhcpd_update:DhcpdUpdateCommand',
        ]
    },
)
