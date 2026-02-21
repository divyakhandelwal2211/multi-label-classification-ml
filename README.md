# Multi-Label Classification ML Pipeline

## 📌 Project Overview

This project demonstrates an end-to-end implementation of a **Multi-Label Classification** system using classical Machine Learning.

Unlike multi-class problems where each instance belongs to only one class, this business scenario allows **multiple labels per instance**.

The solution is built using:

- Logistic Regression (Base Model)
- One-vs-Rest Strategy (Binary Relevance Approach)
- Micro F1-score for evaluation
- Modular ML architecture

---

## 🧠 Problem Statement

The business requirement allows multiple labels per instance.  
However, a traditional multi-class model assumes mutually exclusive classes.

To address this:

- The problem was reformulated as a **Multi-Label Classification** task.
- Each label is treated as an independent binary classification problem.

---

## ⚙️ Solution Approach

### 1️⃣ Modeling Strategy

We used:
OneVsRestClassifier(LogisticRegression)


This trains:

- One binary classifier per label
- Each classifier predicts whether a specific label is present or not

This approach is also known as the **Binary Relevance Method**.

---

### 2️⃣ Evaluation Metrics

Since this is a multi-label problem:

- **Micro F1 Score** → Measures global precision & recall balance
- **Accuracy Score** → Subset accuracy (strict match of all labels)

Micro F1 is preferred because subset accuracy can be overly strict.

---


