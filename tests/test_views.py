from typing import OrderedDict

from usaddress import RepeatedLabelError
import pytest
from parserator_web.views import AddressParse


def test_api_parse_succeeds(client):
    address_string = '123 main st chicago il'
    assert AddressParse().parse(address_string) == (OrderedDict(
        [('AddressNumber', '123'), ('StreetName', 'main'), ('StreetNamePostType', 'st'), ('PlaceName', 'chicago'), ('StateName', 'il')]), 'Street Address')


def test_api_parse_raises_error(client):
    address_string = '123 main st chicago il 123 main st'
    with pytest.raises(RepeatedLabelError) as exception_info:
        AddressParse().parse(address_string)
    assert "RepeatedLabelError" in str(exception_info.type)
