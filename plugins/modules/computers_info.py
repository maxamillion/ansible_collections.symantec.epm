#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2019, Adam Miller (admiller@redhat.com)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}
DOCUMENTATION = """
---
module: computers_info
short_description: Obtain information about Symantec Endpoint Protection Manager computers
description:
  - Obtain information about Symantec Endpoint Protection Manager computers
version_added: "2.9"
options:
  name:
    description:
     - The host name of computer. Wild card is supported as '*'.
    required: false
    type: str
  domain:
    description:
     - The domain from which to get computer information.
    required: false
    type: str
  mac:
    description:
     - The MAC address of computer. Wild card is supported as '*'.
    required: false
    type: str
  os:
    description:
     - The list of OS to filter.
    choices:
     - CentOs
     - Debian
     - Fedora
     - MacOSX
     - Oracle
     - OSX
     - RedHat
     - SUSE
     - Ubuntu
     - Win10
     - Win2K
     - Win7
     - Win8
     - Win81
     - WinEmb7
     - WinEmb8
     - WinEmb81
     - WinFundamental
     - WinNT
     - Win2K3
     - Win2K8
     - Win2K8R2
     - Win2K12
     - Win2K12R2
     - Win2K16
     - WinVista
     - WinXP
     - WinXPEmb
     - WinXPProf64
    required: false
    type: str
notes:
  - This module returns a dict of group data and is meant to be registered to a
    variable in a Play for conditional use or inspection/debug purposes.

author: Ansible Security Automation Team (@maxamillion) <https://github.com/ansible-security>"
"""


# FIXME - provide correct example here
RETURN = """
"""

EXAMPLES = """
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_text

from ansible.module_utils.urls import Request
from ansible.module_utils.six.moves.urllib.parse import urlencode
from ansible.module_utils.six.moves.urllib.error import HTTPError
from ansible_collections.symantec.epm.plugins.module_utils.epm import EPMRequest

import copy
import json


def main():

    argspec = dict(
        name=dict(required=False, type="str"),
        domain=dict(required=False, type="str"),
        mac=dict(required=False, type="str"),
        os=dict(
            required=False,
            type="str",
            choices=[
                "CentOs",
                "Debian",
                "Fedora",
                "MacOSX",
                "Oracle",
                "OSX",
                "RedHat",
                "SUSE",
                "Ubuntu",
                "Win10",
                "Win2K",
                "Win7",
                "Win8",
                "Win81",
                "WinEmb7",
                "WinEmb8",
                "WinEmb81",
                "WinFundamental",
                "WinNT",
                "Win2K3",
                "Win2K8",
                "Win2K8R2",
                "Win2K12",
                "Win2K12R2",
                "Win2K16",
                "WinVista",
                "WinXP",
                "WinXPEmb",
                "WinXPProf64",
            ],
        ),
    )

    module = AnsibleModule(argument_spec=argspec, supports_check_mode=True)

    epm_request = EPMRequest(module, headers={"Content-Type": "application/json"})

    query_params = {
        'pageSize': 100
    }

    if module.params['name']:
        query_params['computerName'] = module.params['name']

    if module.params['domain']:
        query_params['domain'] = module.params['domain']

    if module.params['mac']:
        query_params['mac'] = module.params['mac']

    if module.params['os']:
        query_params['os'] = module.params['os']

    rest_endpoint = 'sepm/api/v1/computers'

    request_out = epm_request.get(
        '{0}?{1}'.format(rest_endpoint, urlencode(query_params))
    )

    if 'content' in request_out:
        list_of_computers = request_out['content']
        if isinstance(request_out.get('totalPages'), int) and request_out['totalPages'] > 1:
            for page_num in range(2, request_out['totalPages']+1):
                query_params['pageIndex'] = page_num
                page_request_out = epm_request.get(
                    '{0}?{1}'.format(rest_endpoint, urlencode(query_params))
                )
                if 'content' in page_request_out:
                    list_of_computers.append(page_request_out['content'])

        id_list = ""
        try:
            id_list += ",".join([comp["id"] for comp in list_of_computers])
        except KeyError:
            module.warn("Unable to compile id_list")
        module.exit_json(computers=list_of_computers, id_list=id_list, changed=False)
    else:
        module.fail_json(msg="Unable to query Computers data", sepm_data=computers)


if __name__ == "__main__":
    main()
