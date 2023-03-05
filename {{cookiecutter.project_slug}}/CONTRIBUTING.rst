.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://gitlab.com/{{ cookiecutter.gitlab_username }}/{{ cookiecutter.project_slug }}/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the Gitlab issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the Gitlab issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

{{ cookiecutter.project_name }} could always use more documentation, whether as part of the
official {{ cookiecutter.project_name }} docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://gitlab.com/{{ cookiecutter.gitlab_username }}/{{ cookiecutter.project_slug }}/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `{{ cookiecutter.project_slug }}` for local development.

#. Start from an issue (create one if it does not exist) at https://gitlab.com/{{ cookiecutter.gitlab_username }}/{{ cookiecutter.project_slug }}/issues.
#. Then go into the issue and create a merge request from it. This will automates a few things.
    * creates a new branch with the issue number and title
    * adds the issue link to the MR description
    * automatallically closes the issue with the MR is merged.

#. Clone the repo locally::

    $ git clone https://gitlab.com/{{ cookiecutter.gitlab_username }}/{{ cookiecutter.project_slug }}.git

#. Make sure that you have `pull.rebase` set to true. If not, run this::

    $ git config pull.rebase true

#. Create a branch for local development::

    $ git checkout -b name-of-your-branch-from-step-2

#. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv {{ cookiecutter.project_slug }}
    $ cd {{ cookiecutter.project_slug }}/
    $ pip install -e ".[dev]"

   Now you can make your changes locally.

#. When you're done making changes, check that your changes pass flake8 and the
   tests, including testing other Python versions with tox::

    $ flake8 {{ cookiecutter.project_slug }} tests
    $ python setup.py test or pytest
    $ tox

   To get flake8 and tox, just pip install them into your virtualenv.

#. Commit your changes and push your branch to Gitlab::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

#. Submit a merge request through the Gitlab website.

Merge Request Guidelines
-----------------------

Before you mark a merge request as ready, check that it meets these guidelines:

1. The merge request should include tests.
2. If the merge request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The merge request should work for Python 3.5, 3.6, 3.7 and 3.8, and for PyPy. Check
{% if cookiecutter.use_pypi_deployment_with_travis== 'y' %}
   https://travis-ci.com/{{ cookiecutter.gitlab_username }}/{{ cookiecutter.project_slug }}/pull_requests
{% endif %}
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

{% if cookiecutter.use_pytest == 'y' -%}
    $ pytest tests.test_{{ cookiecutter.project_slug }}
{% else %}
    $ python -m unittest tests.test_{{ cookiecutter.project_slug }}
{%- endif %}

Deploying
---------

TODO:: Fix bump2version

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.rst).
Then run::

$ bump2version patch # possible: major / minor / patch
$ git push
$ git push --tags
