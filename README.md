# Symantec Endpoint Protection Manager

## Tech Preview

This is the [Ansible
Collection](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections.html)
provided by the [Ansible Security Automation
Team](https://github.com/ansible-security) for automating actions in [Symantec
Endpoint Protection Manager](https://www.symantec.com/products/endpoint).

This Collection is meant for distribution via
[Ansible Galaxy](https://galaxy.ansible.com/) as is available for all
[Ansible](https://github.com/ansible/ansible) users to utilize, contribute to,
and provide feedback about.

### Using Symantec Endpoint Protection Manager Collection

An example for using this collection to manage FIXME FIXME FIXME with
[Symantec Endpoint Protection Manager](https://www.symantec.com/products/endpoint)
is as follows.

`inventory.ini` (Note the password should be managed by a [Vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html) for a production environment.
```
[epm]
epm.example.com

[epm:vars]
ansible_network_os=symantec.epm.epm
ansible_user=admin
ansible_httpapi_pass=SuperSekretPassword
ansible_httpapi_use_ssl=yes
ansible_httpapi_validate_certs=yes
ansible_connection=httpapi
```

Alternatively this can be done with an authentication token. FIXME FIXME FIXME


`inventory.ini` (Note the password should be managed by a [Vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html) for a production environment.
```
[epm]
epm.example.com

[epm:vars]
ansible_network_os=symantec.epm.epm
ansible_user=admin
ansible_httpapi_pass=SuperSekretPassword
ansible_httpapi_use_ssl=yes
ansible_httpapi_validate_certs=yes
ansible_connection=httpapi
```

#### Using the modules with Fully Qualified Collection Name (FQCN)

With [Ansible
Collections](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections.html)
there are various ways to utilize them either by calling specific Content from
the Collection, such as a module, by it's Fully Qualified Collection Name (FQCN)
as we'll show in this example or by defining a Collection Search Path as the
examples below will display.

`epm_with_collections_example.yml`
```
FIXME FIXME FIXME
```

#### Define your collection search path at the Play level

Below we specify our collection at the
[Play](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html)
level which allows us to use the `FIXME` module without
the need for the FQCN for each task.

`epm_with_collections_example.yml`
```
FIXME FIXME FIXME
```

#### Define your collection search path at the Block level

Another option for Collection use is below. Here we use the
[`block`](https://docs.ansible.com/ansible/latest/user_guide/playbooks_blocks.html)
level keyword instead of [Play](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html)
level as with the previous example. In this scenario we are able to use the
`FIXME` module without the need for the FQCN for each
task but with an optionally more specific scope of Collection Search Path than
specifying at the Play level.

`epm_with_collections_block_example.yml`
```
EPM
```
