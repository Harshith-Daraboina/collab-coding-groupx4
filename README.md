# Cafe Management System

A modular Python CLI application to manage cafe operations, developed by a collaborative team.

## Team Structure

| Role | Responsibility |
|------|----------------|
| **Admin / Integrator** | Repository setup, starter file, merges, driver function |
| **Contributor 1** | Menu Management |
| **Contributor 2** | Order Processing |
| **Contributor 3** | Billing & Payment |
| **Contributor 4** | Display & Reporting |

## Project Structure
```
collab-coding-groupID/
│
├── cafe_management/   # Source code
│   ├── menu.py
│   ├── order.py
│   ├── billing.py
│   ├── display.py
│   └── main.py
│
├── tests/             # Unit tests
│   ├── test_menu.py
│   ├── test_order.py
│   ├── test_billing.py
│   └── test_display.py
│
├── README.md          # This file
├── CONTRIBUTING.md    # Contribution guidelines
└── Experience_Report.md
```

## How to Run

1. Navigate to the project root `collab-coding-groupID`.
2. Run the application:
   ```bash
   python cafe_management/main.py
   ```
   *Note: Ensure python path is set correctly if running from root, or `cd cafe_management` and run `python main.py`.*

## Running Tests
To run the automated test suite:
```bash
python -m unittest discover tests
```
