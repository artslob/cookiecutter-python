from {{ cookiecutter.project_slug }} import __version__


def test_version():
    assert isinstance(__version__, str)
    assert __version__.strip() == __version__
    assert " " not in __version__
