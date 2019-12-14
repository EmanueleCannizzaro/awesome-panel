"""Test of the pages"""
import pytest
import awesome_panel.express as pnx
from awesome_panel.express.testing import TestApp
from src.pages import home, resources

pnx.bootstrap.extend()


@pytest.mark.panel
def test_home():
    """Test that we can see the home page

    """
    return TestApp(test_home, home.view())


@pytest.mark.panel
def test_resources():
    """Test that we can see the resources page

    """
    return TestApp(test_resources, resources.view())


if __name__.startswith("bk"):
    test_home().servable()
    test_resources().servable()
