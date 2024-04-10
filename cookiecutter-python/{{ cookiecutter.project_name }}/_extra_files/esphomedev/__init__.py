import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID

empty_component_ns = cg.esphome_ns.namespace('{{ cookiecutter.project_name }}')
EmptyComponent = empty_component_ns.class_("{{ cookiecutter.project_name[0]|upper }}{{ cookiecutter.project_name[1:] }}", cg.Component)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id({{ cookiecutter.project_name[0]|upper }}{{ cookiecutter.project_name[1:] }})
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)