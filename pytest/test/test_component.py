#No need of ../component as pytest automatically adds project's root directory to Python's path when you run it
from component import add, divide, get_weather
import pytest

def test_add():
    assert add(2, 3) == 5, "2 plus 3 is equal to 5"

def test_divide():
    with pytest.raises(ValueError, match="Cannot divide by 0"):
        divide(6, 0) 
    assert divide(6, 3) == 2, "6 divided by 3 is equal to 2"

def test_weather(mocker):
    # Given
    mock_get = mocker.patch("component.requests.get") #See how we mock requests invocations inside component.py
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"temperature" : 25, "condition" : "Sunny"}
    # When
    result = get_weather("Dubai")
    # then
    assert result == {"temperature" : 25, "condition" : "Sunny"}
    mock_get.assert_called_once_with("https://api.weather.com/v1/Dubai")


