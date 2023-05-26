#!/usr/bin/env python3
# Copyright 2021-2023 The Wazo Authors  (see the AUTHORS file)
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
            'commonconf = wazo_sysconfd_client.commands.commonconf:CommonConfCommand',
            'dhcpd = wazo_sysconfd_client.commands.dhcpd:DhcpdCommand',
            'exec_request_handlers = wazo_sysconfd_client.commands.exec_request_handlers:ExecRequestHandlersCommand',
            'ha = wazo_sysconfd_client.commands.ha:HAConfigCommand',
            'hosts = wazo_sysconfd_client.commands.hosts:HostsCommand',
            'voicemail = wazo_sysconfd_client.commands.voicemail:VoicemailCommand',
            'resolv_conf = wazo_sysconfd_client.commands.resolv_conf:ResolvConfCommand',
            'services = wazo_sysconfd_client.commands.services:ServicesCommand',
            'status = wazo_sysconfd_client.commands.status:StatusCommand',
            'wazoctl = wazo_sysconfd_client.commands.wazoctl:WazoCtlCommand',
        ]
    },
)
