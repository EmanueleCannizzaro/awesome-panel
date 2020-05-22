"""Test of the app services"""
from application.pages.bootstrap_dashboard import bootstrap_dashboard
from awesome_panel.utils import module_to_github_url


def test_module_to_github_url():
    """An extrac test of the module_to_github_url function as I had problems making it work"""
    # When
    actual = module_to_github_url.module_to_github_url(bootstrap_dashboard)
    # Then
    assert actual == (
        "https://github.com/MarcSkovMadsen/awesome-panel/blob/master/"
        "application/pages/bootstrap_dashboard/bootstrap_dashboard.py"
    )
