import pytest

pytest_plugins = ("pytest_jupyter.jupyter_server",)


@pytest.fixture
def jp_server_config(jp_server_config):
    return {"ServerApp": {"jpserver_extensions": {"gcs_jupyter_plugin": True}}}
