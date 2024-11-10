import pytest
from typing import Dict
from unittest.mock import patch
from pyto.package_installer import PackageInstaller


command_mock: Dict[str, str] = {
    "package_name_example_1": "echo 'installing package_name_example_1'",
    "package_name_example_2": "echo 'installing package_name_example_2'",
}


@pytest.fixture
def package_installer() -> PackageInstaller:
    return PackageInstaller("package_name_example_1", command_mock)


# Simulates if is package installed  on system
def test_package_installed(package_installer: PackageInstaller) -> None:
    with patch.object(PackageInstaller, "_is_package_installed") as mock_is_installed:
        mock_is_installed.return_value= True
        result: bool = package_installer.install()
        assert result is False


# Simulates if is not package installed on system
def test_package_not_installed(package_installer: PackageInstaller) -> None:
    with patch.object(PackageInstaller, "_is_package_installed") as mock_is_installed:
        mock_is_installed.return_value = False
        result: bool = package_installer.install()
        assert result is True


# Simulates if is package installed  on system and then not excute method install
def test_install_package_already_installed(package_installer: PackageInstaller) -> None:
    with patch.object(PackageInstaller, "_is_package_installed", return_value=True):
        result: bool = package_installer.install()
    assert result is False


# Simulates if is not package installed  on system and then method excute install
def test_install_package_not_installed(package_installer: PackageInstaller) -> None:
    with patch.object(
        PackageInstaller, "_is_package_installed", return_value=False
    ), patch.object(PackageInstaller, "execute", return_value=True) as mock_execute:
        result: bool = package_installer.install()
        mock_execute.assert_called_once()  # Vefify if excute was called
        assert result is True  # Should True
