# AWS S3 Operations Assignment (Boto3 + Moto Testing)

## 📌 Overview

This project demonstrates AWS S3 automation using Python `boto3` with complete CRUD-style operations on S3 objects.

It includes:
- Uploading 2500 S3 objects
- Adding tags and metadata
- Fetching objects using tags
- Fetching objects using metadata
- Deleting objects using tags
- Deleting objects using metadata
- Unit testing using `unittest` + `moto` (AWS mocking)

---

## 📁 Project Structure
S3_Assignment_2/
│
├── s3_operation.py # S3 operations class
├── test_s3_operation.py # Unit tests using moto
├── requirements.txt # Dependencies
├── output/ # Filtered results stored here
└── README.md # Documentation


---

## ⚙️ Features

### 1. Add S3 Objects
- Uploads **2500 objects** to S3 bucket
- Each object:
  - Key: `number_i.txt`
  - Body: `Natural Number: i`
  - Metadata:
    - `number`: i
    - `group`: natural
  - Tags:
    - `type=even`
    - `type=odd`
    - `type=prime` (rotating pattern)

---

### 2. Fetch Objects by Tags
- Uses `get_object_tagging`
- Filters objects by tag key/value
- Saves output to:


---
output/filtered_by_tags.txt

### 3. Fetch Objects by Metadata
- Uses `head_object`
- Filters objects based on metadata
- Saves output to:

output/filtered_by_metadata.txt

---

### 4. Delete Objects by Tags
- Deletes all objects matching given tag filter
- Returns count of deleted objects

---

### 5. Delete Objects by Metadata
- Deletes all objects matching metadata filter
- Returns count of deleted objects

---

## 🧪 Testing

This project uses:

- `unittest` (Python built-in framework)
- `moto` (for mocking AWS S3)

---

## ▶️ Run Tests

```bash id="t8wq1k"
pip install -r requirements.txt
python -m unittest test_s3_operation.py -v

Test Cases Covered
test_add_s3_objects
Verifies 2500 objects are created
test_fetch_s3_objects_by_tag
Validates filtered results (even-type objects)
test_fetch_s3_objects_by_metadata
Ensures all 2500 objects match metadata filter
test_delete_s3_objects_by_tags
Deletes objects based on tags and validates remaining count
test_delete_s3_objects_by_metadata
Deletes all objects based on metadata
🚀 How to Run Project
python s3_operation.py
📦 Installation
pip install boto3 moto

or

pip install -r requirements.txt
🔄 CI/CD Pipeline

GitHub Actions automatically:

Sets up Python environment
Installs dependencies
Runs all unit tests

Workflow file:

.github/workflows/ci.yml
🛠️ Tech Stack
Python 3.x
AWS S3 (boto3)
moto (mock AWS services)
unittest
GitHub Actions
👨‍💻 Author

AWS S3 Assignment Project
