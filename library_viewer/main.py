import pkg_resources as pr
import sys
import subprocess
from Package_Checker import Package_Checker

def get_package_list():
	pkgs = pr.working_set
	pkg_list = sorted(["%s" % i.key for i in pkgs]+list(sys.stdlib_module_names))

	count = 0
	for p_id in range(0,len(pkg_list)):
    		if '_' in pkg_list[p_id]:
        		count += 1
        
	if count > 0:
    		for id in range(0,count):
        		pkg_list.pop(0)

	for i in range(0, len(pkg_list)):
    		print(f'{i} {pkg_list[i]}')


	selection = int(input('\nEnter package number you want to look into: '))
	package = Package_Checker().pkge_check(pkg_list[selection])
	
	return package

def write_package(package):
	file = open('package.py', 'w')
	file.writelines(f'import {package}\n')
	file.writelines(f'print(dir({package}))\n')
	file.close()

def list_pkg_directory(package):
	pkg_run = subprocess.Popen(['python3', 'package.py'], stdout=subprocess.PIPE)
	pkg_sublist = pkg_run.communicate()[0].decode('utf-8')
	pkg_sublist = pkg_sublist.replace("['", "").replace("']", "").replace("\n", "").split("', '")
	print(f'\n{package}:')
	for sub in pkg_sublist:
    		if '__' not in sub and sub != 'main':
        		print('\t' + sub) 

if __name__ == "__main__":
	package = get_package_list()
	write_package(package)
	list_pkg_directory(package)
