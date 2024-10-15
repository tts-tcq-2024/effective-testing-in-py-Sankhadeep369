# Project: Strengthened Tests and Bug Identification

This project involves improving the existing tests in three modules: `tshirts.py`, `misaligned.py`, and `alerter.py`. The original tests were weak and did not expose certain bugs in the implementation. This README explains the changes made to strengthen the tests and highlights the issues identified in the code.

---

## 1. **Module: `tshirts.py`**

### Problem:
The original code does not handle the exact input value `38`. It skips directly from `cms < 38` to `cms > 38`.

### Changes Made:
- Added a test case to handle the edge case where the input is exactly `38`.
- The test for this value (`38`) will fail due to the lack of proper handling in the code logic.

### Bug Identified:
- The code does not classify `38` correctly. The correct size category for `38` should be `M` but is left unhandled.

### Strengthened Test:
- Added an assertion: `assert(size(38) == 'M')`.

---

## 2. **Module: `misaligned.py`**

### Problem:
The function tries to print a map from numbers to colors, but the numeric values and the separator (`|`) are misaligned. Additionally, the functionality depends on human inspection, making automated testing difficult.

### Changes Made:
- Separated concerns by creating a `get_color_map()` function to generate the sequence of color mappings separately from the print logic.
- Strengthened the test by verifying if the numeric sequence generated is correct.
- Added an inspection mechanism to flag format misalignments based on visual output and sequence correctness.

### Bug Identified:
- Misalignment in the color map values and separator (`|`) in the print output, which is hard to catch through automated tests.

### Strengthened Test:
- Added checks to ensure the numeric sequence in the generated color map matches the expected sequence.
- Introduced sequence-based tests for alignment.

---

## 3. **Module: `alerter.py`**

### Problem:
The code doesn't correctly update the failure count when the `network_alert_stub` returns a non-200 status. Also, the alerting and test logic are mixed with production code, making it difficult to swap out the stub for real network communication.

### Changes Made:
- Modified the test to simulate a failure case by returning a 500 status code in the `network_alert_stub`.
- Strengthened the test by adding an assertion to check that the `alert_failure_count` is incremented when the network alert fails.
- For the extra challenge, introduced dependency injection to separate the network alert function from the core logic, enabling us to switch between test and real implementations without modifying the production code.

### Bug Identified:
- The failure count (`alert_failure_count`) is not correctly incremented when the alert fails.
- Mixed test and production code logic in the original implementation.

### Strengthened Test:
- Added a test to verify that `alert_failure_count` is correctly incremented when the network alert fails.

---

## Extra Challenge

### Problem:
The `alerter.py` module mixes the stub and test code with the production logic, which makes it hard to switch to real network communication without modifying the code.

### Solution:
- Used dependency injection for the network alert function. This allows us to pass in either the stub or the real network function without modifying the core logic.

---

## Conclusion

These changes improve the testing coverage and expose hidden bugs in the original implementations. By adding edge case tests, separating concerns, and improving the error handling logic, we ensure that the system behaves as expected under all conditions.

---

