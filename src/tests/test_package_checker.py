from pyxote.package_checker import is_package_installed


# Simulates the return of `shutil.which` as if the package exists
def test_package_installed_by_shutil(mocker) -> None:
    mocker.patch("shutil.which", return_value="/usr/bin/example_package")
    mocker.patch("os.path.exists", return_value=False)  # Ignores default_path
    assert is_package_installed("example_package")  # Should return True


# Simulates a case where the package is not in PATH, but default_path exists
def test_package_installed_by_path(mocker) -> None:
    mocker.patch("shutil.which", return_value=None)
    mocker.patch("os.path.exists", return_value=True)
    assert is_package_installed(
        "nonexistent_package", "/path/to/package"
    )  # Should return True


# Simulates a case where the package is neither in PATH nor in default_path
def test_package_not_installed(mocker) -> None:
    mocker.patch("shutil.which", return_value=None)
    mocker.patch("os.path.exists", return_value=False)
    assert not is_package_installed("nonexistent_package")  # Should return False
