def verify_status_code(response, expected_code):
    assert response.status_code == expected_code, (
        f"Expected {expected_code}, "
        f"but got {response.status_code}"
    )


def verify_key_exists(response_json, key):
    assert key in response_json, (
        f"{key} not found in response"
    )


def verify_response_time(response, max_time=2):
    assert response.elapsed.total_seconds() < max_time, (
        f"Response exceeded {max_time} seconds"
    )