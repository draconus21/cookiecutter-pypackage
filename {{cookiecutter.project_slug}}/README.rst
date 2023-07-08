{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
{%- if cookiecutter.add_pypi_badge== 'y' -%}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}
{% endif %}

{%- if cookiecutter.use_pypi_deployment_with_travis== 'y' -%}
.. image:: https://img.shields.io/travis/{{ cookiecutter.gitlab_username }}/{{ cookiecutter.project_slug }}.svg
        :target: https://travis-ci.com/{{ cookiecutter.gitlab_username }}/{{ cookiecutter.project_slug }}
{% endif %}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status
{%- endif %}

{% if cookiecutter.add_pyup_badge == 'y' %}
.. image:: https://pyup.io/repos/gitlab/{{ cookiecutter.gitlab_username }}/{{ cookiecutter.project_slug }}/shield.svg
     :target: https://pyup.io/repos/gitlab/{{ cookiecutter.gitlab_username }}/{{ cookiecutter.project_slug }}/
     :alt: Updates
{% endif %}


{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}

Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `draconus21/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`draconus21/cookiecutter-pypackage`: https://gitlab.com/draconus21/cookiecutter-pypackage
