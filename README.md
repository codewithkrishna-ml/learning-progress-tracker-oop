# Learning Progress Tracker 📊🎓

An enterprise-grade console application built in Python using core **Object-Oriented Programming (OOP)** principles to monitor student milestones. The system tracks academic points across specialized paths (Python, Java, Data Science), visualizes metrics in aligned matrices, and handles complete data persistence through structural file exports.

---

## 🌟 About the Developer

*   **Age/Class:** 16 Years Old (Class 10th) 🎯
*   **Future Goal:** B.Tech in Artificial Intelligence and Machine Learning (AI-ML).
*   **Milestone:** Successfully completed the **100 Days of Code** challenge!
*   **Current Focus:** Learning Data Structures & Algorithms (DSA) and data science libraries like **NumPy** and **Pandas**.

---

## ✨ Key Features

*   **Automated Validation Filters:** Employs Regular Expressions (`re` module) to parse and validate structural email patterns, completely preventing duplicate registrations.
*   **Progress Metrics Engine:** Evaluates active user points against path thresholds (e.g., Python 600, Java 500, DS 400), dynamically compiling completion percentages locked up to `100.0%`.
*   **Formatted Matrix Dashboard:** Renders clean, tabular column reports directly on the command line, showing full names alongside individual subject standing weights.
*   **Dual Data Persistence Protocols:** 
    *   **CSV Exporter:** Structurally writes runtime records into clean spreadsheets (`.csv`) for analytical processing.
    *   **JSON Tree Saver:** Serializes the complete active database state into formatted, indented nesting matrices (`.json`).

---

## 🛠️ OOP Concepts & Architecture Demonstrated

This system prioritizes clean separation of structural layers, safe data mutation, and explicit error parsing:
*   **Classes & Component Blueprints:** Models the platform around highly isolated nodes: `Course` (metadata tracker), `Student` (profile & point host), and `TrackerSystem` (master validation & persistence engine).
*   **Data Structure Aggregation:** Maps active entries inside nested dictionary trees keyed against self-incrementing serial IDs starting from `10001`.
*   **Robust Input Defense:** Shields runtime calculations against fatal crashes through structural `try-except ValueError` blocks guarding interactive float inputs.

---

## 🚀 How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone https://github.com
    ```
2.  **Navigate to the project folder:**
    ```bash
    cd learning-progress-tracker-oop
    ```
3.  **Run the interactive tracking portal:**
    ```bash
    python main.py
    ```

---

## 📝 Prerequisites
*   **Python 3.x** installed on your machine.
*   Standard utilities (`re`, `csv`, `json` are bundled natively within standard Python runtimes).
