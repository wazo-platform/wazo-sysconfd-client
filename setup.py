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
            'commonconf_apply = wazo_sysconfd_client.commands.commonconf:CommonConfApplyCommand',
            'commonconf_generate = wazo_sysconfd_client.commands.commonconf:CommonConfGenerateCommand',
            'delete_voicemail = wazo_sysconfd_client.commands.voicemail:DeleteVoicemailCommand',
            'dhcpd_update = wazo_sysconfd_client.commands.dhcpd_update:DhcpdUpdateCommand',
            'exec_request_handlers = wazo_sysconfd_client.commands.exec_request_handlers:ExecRequestHandlersCommand',
            'ha_config = wazo_sysconfd_client.commands.ha_config:HAConfigCommand',
            'hosts = wazo_sysconfd_client.commands.hosts:HostsCommand',
            'move_voicemail = wazo_sysconfd_client.commands.voicemail:MoveVoicemailCommand',
            'resolv_conf = wazo_sysconfd_client.commands.resolv_conf:ResolvConfCommand',
            'services = wazo_sysconfd_client.commands.services:ServicesCommand',
            'status_check = wazo_sysconfd_client.commands.status_check:StatusCheckCommand',
            'xivoctl = wazo_sysconfd_client.commands.xivoctl:XivoCtlCommand',
        ]
    },
)
