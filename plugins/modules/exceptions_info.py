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
module: exceptions_info
short_description: Obtain information about Symantec Endpoint Protection Manager exceptions
description:
  - Obtain information about Symantec Endpoint Protection Manager exceptions
version_added: "2.9"
options:
  id:
    description:
      - Obtain only information of the Rule with provided ID
    required: false
    type: int
notes:
  - You may provide many filters and they will all be applied, except for C(id)
    as that will return only the Rule identified by the unique ID provided.
  - FIXME FIXME FIXME ---> not sure about filters yet

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
from ansible.module_utils.six.moves.urllib.parse import quote
from ansible.module_utils.six.moves.urllib.error import HTTPError
from ansible_collections.symantec.epm.plugins.module_utils.epm import (
    EPMRequest,
)

import copy
import json


def main():

    argspec = dict(
        id=dict(required=False, type="int"),
#       name=dict(required=False, type="str"),
#       owner=dict(required=False, type="str"),
#       type=dict(
#           required=False, choices=["EVENT", "FLOW", "COMMON", "USER"], type="str"
#       ),
#       origin=dict(required=False, choices=["SYSTEM", "OVERRIDE", "USER"], type="str"),
    )

    module = AnsibleModule(argument_spec=argspec, supports_check_mode=True)

    epm_request = EPMRequest(
        module, headers={"Content-Type": "application/json"}
    )

    if module.params["id"]:
        rules = epm_request.get_by_path(
            "api/v1/policies/summary/exceptions/{0}".format(module.params["id"])
        )

    else:
        rules = epm_request.get_by_path("api/v1/policies/summary/exceptions")

        module.exit_json(rules=rules, changed=False)


if __name__ == "__main__":
    main()
