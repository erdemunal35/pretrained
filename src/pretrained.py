#!/usr/bin/env python
import click
import requests
import torch
import torchvision

version = 1.01

def search_tf(search_str):
	headers = {'Content-Type': 'application/json'}
	data = '["cma:po",'+search_str+',"",-1,true,[],null,[],null,[]]'
	response = requests.post('https://tfhub.dev/s/list', headers=headers, data=data)
	r = response.text
	cmaip = '"cma:ip"'
	tf_modules = find_all_modules(r,cmaip)
	for a in range(len(tf_modules)):
		tf_modules[a] += " [tfhub.dev]"
	return tf_modules

def search_pytorch(search_str):
	torch_models = torch.hub.list('pytorch/vision', force_reload=True)
	res = [i for i in torch_models if search_str in i]
	for a in range(len(res)):
		res[a] += " [pytorch/vision]"
	return res

def find_all_modules(input_str, search_str):
    l1 = []
    length = len(input_str)
    index = 0
    main_char = '"'
    while index < length:
        i = input_str.find(search_str, index)
        if i == -1:
            return l1
        for a in range(5):
        	main_index = input_str.find(main_char, i)
        	i = main_index+1
        main_index2 = input_str.find(main_char, i)
        main_str = input_str[main_index+1:main_index2]
        l1.append(main_str)
        index = i+1
    return l1

@click.group()
def cli():
    pass

@click.command()
@click.argument("argument")
def search(argument):
	""" --- Searchs for the given argument"""
	click.echo("Searching " + argument +" at tfhub.dev and pyTorch/hub...")
	tf_models = search_tf(argument)
	pyt_models = search_pytorch(argument)
	all_models = tf_models+pyt_models
	all_models.sort()
	for model in all_models:
		click.echo(model)
	click.echo(click.style("Total number of found models: " + str(len(all_models)) + "("+str(len(tf_models))+" tensorflow, "+str(len(pyt_models)) +" pytorch/vision)", fg='bright_yellow'))

@click.command()
def install():
	""" --- Installs the given weights (NOT IMPLEMENTED YET)"""
	click.echo("Install command")

@click.command()
def version():
	""" --- Prints the current version of the program"""
	click.echo("Version: "+str(version))

cli.add_command(search)
cli.add_command(install)
cli.add_command(version)

if __name__ == '__main__':
    cli()
