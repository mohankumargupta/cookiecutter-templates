#pragma once

#include "esphome/core/component.h"
#include "esphome/core/log.h"

namespace esphome {
namespace {{ cookiecutter.project_name }} {

class {{ cookiecutter.project_name[0]|upper }}{{ cookiecutter.project_name[1:] }}Component : public Component {
 public:
  void setup() override;
  void loop() override;
  void dump_config() override;
};


}  // namespace empty_component
}  // namespace esphome