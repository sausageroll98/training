# Ansible Kevin Bacon

## Reference

* [Ansible homepage](https://www.ansible.com/)
* [Ansible Docs](https://docs.ansible.com/ansible/latest/collections/ansible/)
* [Ansible Patch Management](https://youtu.be/VRoQLVHdNHE)
* [Ansible community projects](https://galaxy.ansible.com/docs/)

## Setup

1. Update the tooling to include `software-properties-common`

    ``` bash
    sudo apt update && sudo apt install software-properties-common
    ```

1. Add the ansible repository

    ``` bash
    sudo add-apt-repository --yes --update ppa:ansible/ansible
    ```

1. Install ansible

    ``` bash
    sudo apt install ansible
    ```

1. Setup ansible galaxy collection install

    ``` bash
    ansible-galaxy collection install community.general
    ```

---

## Sample Playbook locally

Install
 * ENGB locale
 * Update tooling


run with `localhost` setup:

``` ansible
  hosts: localhost
  connection: local
```


Run the command `sudo ansible-playbook localhost.yaml`

for more diagnostics add `-v` or `-vv` to the command e.g. `ansible-playbook localhost.yaml -vv`