{%- if cookiecutter.arduino == "esp32s2" %}
{%- include "esp32s2/sketch.ino" %}
{%- elif cookiecutter.arduino == "esp32" %}
{%- include "esp32/sketch.ino" %}
{%- if cookiecutter.arduino == "esp32c3" %}
{%- include "esp32c3/sketch.ino" %}
{%- elif cookiecutter.arduino == "esp32s3" %}
{%- include "esp32s3/sketch.ino" %}
{%- elif cookiecutter.arduino == "nano" %}
{%- include "nano/sketch.ino" %}
{% endif %}