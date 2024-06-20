#include "{{ cookiecutter.project_name }}.h"

namespace esphome {
namespace {{ cookiecutter.project_name }} {

static const char *TAG = "{{ cookiecutter.project_name }}.component";

void {{ cookiecutter.project_name[0]|upper }}{{ cookiecutter.project_name[1:] }}::setup() {

}

void {{ cookiecutter.project_name[0]|upper }}{{ cookiecutter.project_name[1:] }}::loop() {

}

void {{ cookiecutter.project_name[0]|upper }}{{ cookiecutter.project_name[1:] }}::dump_config(){
    ESP_LOGI(TAG, "Empty component");
}


}  // namespace {{ cookiecutter.project_name }}
}  // namespace esphome