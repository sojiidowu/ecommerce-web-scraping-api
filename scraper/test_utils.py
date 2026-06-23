def clean_price_string(price_str):
    cleaned = price_str.replace("$", '').replace(",", "")
    return float(cleaned)

def test_clean_price_string_success():
    # Arrange: Setup our inputs
    raw_input = "$1,249.99"
    expected_output = 1249.99

    # Act: Run the code we want to test
    actual_output = clean_price_string(raw_input)

    # Assert: Check if the result matches our expectations
    assert actual_output == expected_output