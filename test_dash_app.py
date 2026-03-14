import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

from regionwise_dash_app import app_3


def test_header_present(dash_duo):
    """Test that the H1 header is present with the correct text."""
    dash_duo.start_server(app_3)
    dash_duo.wait_for_element("h1", timeout=10)
    assert dash_duo.find_element("h1").text == "Regional Sales Dashboard"


def test_visualisation_present(dash_duo):
    """Test that the Graph visualisation component is present."""
    dash_duo.start_server(app_3)
    dash_duo.wait_for_element("#region-wise-graph", timeout=10)
    assert dash_duo.find_element("#region-wise-graph")


def test_region_picker_present(dash_duo):
    """Test that the RadioItems region picker is present."""
    dash_duo.start_server(app_3)
    dash_duo.wait_for_element("#region-wise-radio", timeout=10)
    assert dash_duo.find_element("#region-wise-radio")
