# Static Analysis Issue Log

**Assigned program:** `ticket_booking_system.py`  
**Baseline:** original repository version, analyzed with Pylint 4.1.4, Bandit 1.9.4, and Flake8 7.5.0. Line numbers below refer to that original file. Findings are ordered by security severity, then correctness and style.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Weak MD5 ticket digest (B324) | High / Security | 47 | MD5 is unsuitable where collision resistance matters. | Use SHA-256 for the ticket digest. |
| Shell command uses filename input (B605) | High / Security | 58 | Concatenating a filename into `os.system` can allow shell metacharacters to execute. | Remove the shell call and print the export confirmation directly. |
| Dynamic `eval` of promotion expression (B307) | Medium / Security | 42 | A caller-controlled expression can execute arbitrary Python code. | Accept a numeric discount rate, validate it from 0 through 1, and calculate the price directly. |
| Mutable default order history | Bug / Correctness | 14 | The default list is shared across calls, leaking booking history between callers. | Default to `None` and create a new list inside the function. |
| Non-cryptographic booking PIN (B311) | Low / Security | 51 | `random.randint` is predictable and unsuitable for PIN generation. | Generate the four-digit PIN with `secrets.randbelow`. |
| Silent broad exception (B110) | Low / Reliability | 23–26 | A bare `except` suppresses all failures and gives no result for unknown seats. | Check whether the seat exists; return `False` when it does not. |
| Unused and misleading logic | Quality / Correctness | 30–32, 41, 60–63 | The booking fee and a local price variable were unused; the status check and summary loop could be simpler. | Remove dead variables, return the availability condition directly, and count sold seats with `sum`. |
| File handling and output | Quality / Reliability | 52–55 | The file was opened without an encoding and closed manually. | Use a context manager and specify UTF-8 encoding. |
| PEP 8 and naming violations | Style | 6, 15, 19, 82 | Unused import, camelCase name, long formatting expression, and missing final newline were reported. | Remove the import, use `reserve_seat`, use an f-string, and end the file with a newline. |

**Verification:** the final reports show Pylint 10.00/10, no Bandit issues, and no Flake8 findings. The before and after reports are in `reports/before/` and `reports/after/`.
