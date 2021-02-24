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
            'delete_voicemail = wazo_sysconfd_client.commands.delete_voicemail:DeleteVoicemailCommand',
            'commonconf_apply = wazo_sysconfd_client.commands.commonconf:CommonConfApplyCommand',
            'commonconf_generate = wazo_sysconfd_client.commands.commonconf:CommonConfGenerateCommand',
            'exec_request_handlers = wazo_sysconfd_client.commands.exec_request_handlers:ExecRequestHandlersCommand',
            'hosts = wazo_sysconfd_client.commands.hosts:HostsCommand',
            'resolv_conf = wazo_sysconfd_client.commands.resolv_conf:ResolvConfCommand',
            'ha_config = wazo_sysconfd_client.commands.ha_config:HAConfigCommand',
            'services = wazo_sysconfd_client.commands.services:ServicesCommand',
        ]
    },
)
