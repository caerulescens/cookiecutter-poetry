import asyncio


async def main(text: str) -> int:
    """
    Run the main function.

    :param text:
    :return:
    """
    exit_code = 0
    print(text)
    return exit_code


if __name__ == "__main__":
    asyncio.run(main=main(text="Hello, World"))
