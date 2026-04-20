from validator import validate_logs

SAMPLE_LOG = """
[INFO] Starting test execution...
[DEBUG] Running test_login_module
[SUCCESS] test_login_module completed successfully
[DEBUG] Running test_payment_gateway
[ERROR] test_payment_gateway failed due to timeout
[INFO] Shutting down.
"""

def test_validate_logs_found():
    tests = "test_login_module\ntest_payment_gateway"
    results = validate_logs(tests, SAMPLE_LOG)
    assert results == [
        {"Test Name": "test_login_module", "Status": "OK"},
        {"Test Name": "test_payment_gateway", "Status": "OK"}
    ]

def test_validate_logs_missing():
    tests = "test_user_registration"
    results = validate_logs(tests, SAMPLE_LOG)
    assert results == [
        {"Test Name": "test_user_registration", "Status": "NOT OK"}
    ]

def test_validate_logs_mixed():
    tests = "test_login_module\nmissing_test"
    results = validate_logs(tests, SAMPLE_LOG)
    assert results == [
        {"Test Name": "test_login_module", "Status": "OK"},
        {"Test Name": "missing_test", "Status": "NOT OK"}
    ]

def test_handle_empty_lines_and_spaces():
    tests = "\n  test_login_module  \n\n  test_payment_gateway  \n"
    results = validate_logs(tests, SAMPLE_LOG)
    assert len(results) == 2
    assert results[0]["Test Name"] == "test_login_module"
    assert results[1]["Test Name"] == "test_payment_gateway"

def test_empty_input_returns_empty_list():
    assert validate_logs("   \n   ", SAMPLE_LOG) == []
    assert validate_logs("", SAMPLE_LOG) == []