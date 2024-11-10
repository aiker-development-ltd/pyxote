import pytest
from pyto.command_serializer import CommandSerializer
from typing import Dict
from unittest.mock import patch, call, _Call


# Simulates command for install package
command_mock: Dict[str, str] = {
    "package_name_example_1": "echo 'installing package_name_example_1'",
    "package_name_example_2": "echo 'installing package_name_example_2'",
}


# Mock class CommandSerializer
@pytest.fixture
def command_serializer() -> CommandSerializer:
    return CommandSerializer(command_mock)


# Simulates if execute method fish with sucess
def test_execute_finish_sucess(command_serializer: CommandSerializer) -> None:
    execute_method: bool = command_serializer.execute()
    assert execute_method is True  # Should return true


# Simulates if execute method was executed with sucess
def test_execute_success(command_serializer: CommandSerializer) -> None:
    with patch.object(
        CommandSerializer, "_install", wraps=command_serializer._install
    ) as mock_install:
        execute_method: bool = command_serializer.execute()
        expected_calls: list[_Call] = [
            call("echo 'installing package_name_example_1'", "package_name_example_1"),
            call("echo 'installing package_name_example_2'", "package_name_example_2"),
        ]
        mock_install.assert_has_calls(expected_calls, any_order=True)
        assert execute_method is True  # Should return true


# Simulates if excute method with on install package
def test_execute_failure(command_serializer: CommandSerializer) -> None:
    with patch.object(CommandSerializer, "_install") as mock_install:
        # side effect function make a error on first package install
        def side_effect(command, package_name):
            if package_name == "package_name_example_1":
                raise Exception(f"Error installing {package_name}")
            return True

        mock_install.side_effect = side_effect
        with pytest.raises(Exception, match="Error installing package_name_example_1"):
            command_serializer.execute()
