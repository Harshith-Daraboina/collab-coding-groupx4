# Contributing to Cafe Management System

Welcome to the Cafe Management System project! This document outlines the team roles and contribution workflow.

## Team Structure

| Role | Responsibility |
|------|----------------|
| **Admin / Integrator** | Repository setup, starter file, merges, driver function |
| **Contributor 1** | Menu Management |
| **Contributor 2** | Order Processing |
| **Contributor 3** | Billing & Payment |
| **Contributor 4** | Display & Reporting |

## Development Workflow

1.  **Clone the repository**:
    ```bash
    git clone <repo_url>
    ```
2.  **Create a feature branch**:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3.  **Implement your module**:
    - Follow conventions in `cafe_management/`.
    - Add tests in `tests/`.
4.  **Run tests**:
    ```bash
    python -m unittest discover tests
    ```
5.  **Submit a Pull Request**.

## Coding Standards
- Use Python 3.x.
- Follow PEP 8 guidelines.
- Ensure all tests pass before submitting.
