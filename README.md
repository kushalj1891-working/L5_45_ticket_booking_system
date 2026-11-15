# Movie Theater Ticket Booking System

A compact Python project that demonstrates seat reservations, ticket pricing, and basic theater inventory management. The program runs a short demonstration when started, and its functions can also be imported and used individually.

## Project overview

The seating map includes standard and premium seats, each with a price and a sold or available status. The booking functions reserve and cancel seats, check availability, calculate a promotional price, count sold seats, generate ticket identifiers, and export the seating map to a text file.

## Features

- Reserve an available seat and record a booking message
- Cancel a reservation and check seat availability
- Apply a discount rate from `0` to `1` to a seat's price
- Count sold seats in the theater
- Generate a SHA-256 ticket digest and a secure four-digit booking PIN
- Export the seating chart as UTF-8 text

## Project files

```text
.
├── ticket_booking_system.py
├── issues.md
├── reflection.md
└── reports/
    ├── before/
    │   ├── pylint_report.txt
    │   ├── bandit_report.txt
    │   ├── flake8_report.txt
    │   └── program_output.txt
    └── after/
        ├── pylint_report.txt
        ├── bandit_report.txt
        ├── flake8_report.txt
        └── program_output.txt
```

The issue log records the original findings and their fixes. The reflection summarizes what the analysis work showed. The `before` and `after` folders preserve the tool output from each stage.

## Requirements

- Python 3
- Pylint, Bandit, and Flake8 for static analysis

The application itself uses only Python's standard library.

## Run the demonstration

From the project directory, run:

```bash
python ticket_booking_system.py
```

The script prints example booking, price, ticket, PIN, and theater summary information, then writes `seating_chart.txt` in the current directory.

## Use the booking functions

The discount argument is a decimal fraction: `0.20` means a 20% discount. Values outside the range `0` to `1` and unknown seat IDs raise `ValueError`.

```python
from ticket_booking_system import compute_discounted_price, reserve_seat

reserve_seat("A1", "Avery")
price = compute_discounted_price("B1", 0.20)
print(price)
```

Importing the module does not start the demonstration; it runs only when the file is executed directly.

## Run static analysis

Install the tools with:

```bash
python -m pip install pylint bandit flake8
```

Run them from the project directory:

```bash
python -m pylint ticket_booking_system.py
python -m bandit -r ticket_booking_system.py
python -m flake8 ticket_booking_system.py
```

## Results

The final version scored **10.00/10 with Pylint**, had **no Bandit findings**, and produced **no Flake8 findings**. The saved reports are included under `reports/after/`; the original reports are under `reports/before/`.

