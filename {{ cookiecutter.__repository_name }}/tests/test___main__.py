from {{ cookiecutter.__package_name }}.__main__ import main


async def test_main() -> None:
    """
    Tests the main function.

    :return: None
    """
    # setup
    text = "Hello, World!"
    exit_code = 0

    # test
    result = await main(text=text)

    # assert
    assert result == exit_code
