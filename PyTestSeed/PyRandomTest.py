import pytest
import random
import string

# Fixture to generate a random username
@pytest.fixture
def fixture_a():
    # Generate a random username
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    return username

# Fixture to perform setup using the generated username
@pytest.fixture
def fixture_b(fixture_a):
    # Use the generated username from fixture_a
    setup_data = {
        'username': fixture_a,
        # Add more setup logic if needed
    }
    print(f"Performing setup with username: {fixture_a}")
    return setup_data

# Test function that uses fixture_b
def test_using_fixture_b(fixture_b):
    # Access setup_data returned by fixture_b
    assert 'username' in fixture_b
    print(f"Testing with setup data: {fixture_b}")