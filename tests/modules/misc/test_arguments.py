import pytest

from cargoloader.modules.misc.arguments import CliInput


class TestArgumentParsingVerification(CliInput):

    parser = CliInput().create_parser()

    def test_verification_true(self):
        assert self.validate_arguments(self.parser.parse_args([]))["verification"] is True

    @pytest.mark.parametrize("option", CliInput.option_names["verification"])
    def test_verification_false(self, option):
        assert self.validate_arguments(self.parser.parse_args([option]))["verification"] is False
