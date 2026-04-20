from typing import List, Dict

def validate_logs(tests_input: str, log_content: str) -> List[Dict[str, str]]:
    """
    Parses a multiline string of tests and checks if they exist in the log content.
    """
    if not tests_input or not tests_input.strip():
        return []

    # Split by newline, strip whitespace, and filter out empty strings
    tests = [test.strip() for test in tests_input.split('\n') if test.strip()]
    
    results = []
    for test in tests:
        # Check if the test string exists anywhere in the log content
        exists = test in log_content
        results.append({
            "Test Name": test,
            "Status": "OK" if exists else "NOT OK"
        })
        
    return results