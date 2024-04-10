#include "{{ cookiecutter.project_name }}.h"

namespace esphome {
namespace {{ cookiecutter.project_name }} {

static const char *TAG = "empty_component.component";

void {{ cookiecutter.project_name[0]|upper }}{{ cookiecutter.project_name[1:] }})Component::setup() {

}

void EmptyComp{{ cookiecutter.project_name[0]|upper }}{{ cookiecutter.project_name[1:] }})Componentonent::loop() {

}

void {{ cookiecutter.project_name[0]|upper }}{{ cookiecutter.project_name[1:] }})Component::dump_config(){
    ESP_LOGCONFIG(TAG, "Empty component");
}


}  // namespace empty_component
}  // namespace esphome