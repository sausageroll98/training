import requests
import argparse

def get_superhero(host, port, name):
    url = f'http://{host}:{port}/superhero/{name}'
    response = requests.get(url)
    if response.status_code<300:
        return response.json()
    return False 
    
def get_superheroes(host, port):
    url = f'http://{host}:{port}/superheroes'
    response = requests.get(url)
    if response.status_code<300:
        return response.json()
    return False 


def post_superhero_name(host, port, name):
    url = f'http://{host}:{port}/superheroes'
    response = requests.post(url, json=name)
    if response.status_code<300:
        return response.json()
    return False 

def put_superhero_attributes(name, attribute, value):
    url = f'http://{host}:{port}/superhero/{name}'
    params = {'name':name, 'attribute':attribute, 'value':value}
    response = requests.put(url, json=params)
    if response.status_code<300:
        return response.json()
    return False 

def delete_superhero(host, port, name):
    url = f'http://{host}:{port}/superhero/{name}'
    response = requests.delete(url, json=name)
    if response.status_code<300:
        return response.json()
    return False 


parser = argparse.ArgumentParser(description='tool to test superhero server')
parser.add_argument('-p', default=5000, type=int)
parser.add_argument('--host', default="127.0.0.1", type=str)
args = parser.parse_args()


new_superhero = "Bitcoin man"
post_superhero_name(args.host, args.p, new_superhero)
superhero_list = get_superheroes(args.host, args.p)
assert new_superhero in superhero_list

superhero_list = delete_superhero(args.host, args.p, new_superhero)
assert new_superhero not in superhero_list

print(f'Successfully added and removed {new_superhero} from server running off {args.host}/:{args.p}')

