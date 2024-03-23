{%- if cookiecutter.project_template == "cli" %}
{%- include "main-cli.py" %}
{%- else %}
{%- include "main-template.py" %}
{% endif %}