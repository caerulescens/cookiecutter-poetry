from pathlib import Path
from typing import Any

import pytest


class TestCookiecutterPoetry:
    """Tests the cookiecutter-poetry template."""

    @pytest.fixture
    def template(self) -> Path:
        """
        Test fixture providing the template file path.

        :return: pathlib.Path
        """
        return Path(__file__).parent.parent

    @pytest.mark.parametrize(
        argnames="license_", argvalues=["none", "mit", "bsd2", "bsd3", "isc"]
    )
    def test_license(self, cookies: Any, template: Path, license_: str) -> None:
        """
        Tests template options for license.

        :return: None
        """
        # test
        result = cookies.bake(
            template=str(template), extra_context={"license": license_}
        )

        # assert
        assert result.exit_code == 0
        assert result.exception is None

    @pytest.mark.parametrize(argnames="editor", argvalues=["none", "emacs", "pycharm"])
    def test_editor(self, cookies: Any, template: Path, editor: str) -> None:
        """
        Tests template options for editor.

        :return: None
        """
        # test
        result = cookies.bake(template=str(template), extra_context={"editor": editor})

        # assert
        assert result.exit_code == 0
        assert result.exception is None
