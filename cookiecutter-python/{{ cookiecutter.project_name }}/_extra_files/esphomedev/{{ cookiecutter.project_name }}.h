#pragma once

#include "esphome.h"

namespace esphome {
namespace {{ cookiecutter.project_name }} {

class EmptyComponent : public Component {
 public:
  void setup() override;
  void loop() override;
  void dump_config() override;
};


}  // namespace empty_component
}  // namespace esphome