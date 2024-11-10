import subprocess
from pyto.installer import install_package

# Simulates a case where the package install with sucess
def test_install_package_sucess(mocker) -> None:
    mocker.patch("subprocess.run", return_value=True)
    assert (
        install_package("echo 'command install'", "test_package") is True
    )  # Should return False

# Simulates a case where the package no install because have Erros
def test_install_package_failed(mocker) -> None:
    mocker.patch(
        "subprocess.run", side_effect=subprocess.CalledProcessError(1, "test command")
    )
    assert (
        install_package("invalid command", "invalid_package") is False
    )  # Should return False
