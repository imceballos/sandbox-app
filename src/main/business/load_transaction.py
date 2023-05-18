import yaml
f = open('main/business/file.json', 'r') 
f = f.read()
import yaml


my_dict = yaml.safe_load(f)
print(my_dict)

