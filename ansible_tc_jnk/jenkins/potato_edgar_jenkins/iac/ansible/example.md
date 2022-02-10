``` bash
    export ANSIBLE_HOST_KEY_CHECKING=False
```

location of `private key`: ansible_key

``` bash
    ansible all -i hosts -u ansible --key-file ./ansible_key -m ping
```

setup the ip addresses for the `hosts` file

``` bash
ansible-galaxy collection install community.general
ansible-playbook  -i hosts --key-file ./ansible_key -u ansible generic.yaml

```

## locally

sudo  ansible-galaxy collection install community.general
sudo  ansible-playbook localhost.yaml
