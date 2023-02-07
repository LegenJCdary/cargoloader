from copy import deepcopy

import pytest

from cargoloader.modules.misc.arguments import CliInput


class TestArgumentParsingVerification(CliInput):

    parser = CliInput().create_parser()

    def test_verification_true(self):
        assert self.validate_arguments(self.parser.parse_args([]))["verification"] is True

    @pytest.mark.parametrize("option", CliInput.option_names["verification"])
    def test_verification_false(self, option):
        assert self.validate_arguments(self.parser.parse_args([option]))["verification"] is False


class TestArgumentParsingInExLists(CliInput):

    single_list = ["AB1234"]
    double_list = ["AB1234", "CD1234"]

    options = deepcopy(CliInput.option_names)
    options.pop("verification")
    parser = CliInput().create_parser()

    # @staticmethod
    # @pytest.fixture(scope="function", params=current_option)
    # def check_input_list_true(request):
    #     return request.param

    # TODO opt_names to mark.parametrize, so pytest runs tests separately
    @pytest.mark.parametrize("input_list", [single_list, double_list])
    @pytest.mark.parametrize("option", [*options.items()])
    def test_input_list_true(self, input_list, option):
        opt_type, opt_names = option
        # opt_type = list(self.options.keys())[list(self.options.values()).index(option)]
        for opt_name in opt_names:
            assert isinstance(self.validate_arguments(self.parser.parse_args([opt_name, *input_list]
                                                                             ))[opt_type], list)

    def test_input_list_false(self):
        arguments = self.validate_arguments(self.parser.parse_args([]))
        assert arguments["exclude"] is False
        assert arguments["include"] is False

    def test_lists_exclusive(self):
        with pytest.raises(TypeError) as exc:
            self.validate_inex_lists(self.double_list, self.double_list)

        assert str(exc.value) == "[CRITICAL]: Mutually exclusive lists were provided, use --help."\
                                 " Program will exit now."
