#include "{{ cookiecutter.project_name }}.h"

namespace esphome {
namespace {{ cookiecutter.project_name }} {

static const char *TAG = "empty_component.component";

void EmptyComponent::setup() {

}

void EmptyComponent::loop() {

}

void EmptyComponent::dump_config(){
    ESP_LOGCONFIG(TAG, "Empty component");
}


}  // namespace empty_component
}  // namespace esphome