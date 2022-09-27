from bot import get_joke, get_last_seen, update_last_seen


# Test data
TEST_FILE_NAME = "test_last_seen.txt"
TEST_ID = 1234567890


def test_get_joke():
    """
    Tests that the get_joke function returns a string
    """
    assert isinstance(get_joke(), str)


def test_get_last_seen():
    """
    Tests that the get_last_seen function returns an integer
    """
    assert isinstance(get_last_seen(TEST_FILE_NAME), int)
    assert get_last_seen(TEST_FILE_NAME) == TEST_ID


def test_update_last_seen():
    """
    Tests that the update_last_seen function updates the last seen ID
    """
    update_last_seen(TEST_FILE_NAME, TEST_ID)
    assert get_last_seen(TEST_FILE_NAME) == TEST_ID
    assert isinstance(get_last_seen(TEST_FILE_NAME), int)
