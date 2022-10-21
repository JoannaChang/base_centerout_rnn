#%%
import os
import params
from config_manager import base_configuration
from simulation.config_template import ConfigTemplate
import numpy as np


#%%
MAIN_FILE_PATH = os.path.dirname(os.path.realpath(__file__))

def create_config(config_num, property_name = None, property_value = None, changes_dict = None, base_config =None):
    assert(((property_name is not None) & (property_value is not None)) or (changes_dict is not None))
    if base_config is None:
        base_config = 'base_config.yaml'
    config_path = os.path.join(MAIN_FILE_PATH, 'configs/' + base_config)

    configuration = base_configuration.BaseConfiguration(
        configuration= config_path, template = ConfigTemplate.base_config_template)

    if changes_dict is None:
        configuration.amend_property(property_name=property_name, new_property_value=property_value)
    else:
        for property_name in changes_dict.keys():
            property_value = changes_dict[property_name]
            configuration.amend_property(property_name=property_name, new_property_value=property_value)
    
    save_dir = params.PROJ_DIR + params.CONFIGS_DIR
    file_name = 'config_' + str(config_num) + '.yaml'
    configuration.save_configuration(folder_path=save_dir, file_name = file_name)


#%%
#Examples:

#1: original, same as config.yaml
create_config(1,'optimizer', 'Adam')

#2-3: beta
for i, val in enumerate([0.1,0.3]):
    create_config(2 + i,'beta1', float(val))

