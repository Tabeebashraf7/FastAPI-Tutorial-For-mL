# FastAPI for Machine Learning 🚀

## 📌 About This Repository

This repository contains my learning notes, code implementations, and practical exercises while following the **FastAPI for Machine Learning** YouTube playlist by CampusX.

The objective is to understand backend development using FastAPI and learn how to build APIs that can serve machine learning models.

## 🎯 Learning Objectives

- Understand the fundamentals of FastAPI.
- Learn how REST APIs work.
- Understand HTTP methods (GET, POST, PUT, DELETE).
- Work with API endpoints and path parameters.
- Handle query parameters and request bodies.
- Understand data validation using Pydantic.
- Learn how to handle API requests and responses.
- Integrate machine learning models with FastAPI.
- Build backend services for machine learning applications.
- Understand how to test and deploy APIs.

## 🛠️ Technologies Used

- **Python** – Programming language.
- **FastAPI** – Modern Python web framework for building APIs.
- **Uvicorn** – ASGI server for running FastAPI applications.
- **Pydantic** – Data validation and serialization.
- **Jupyter Notebook / VS Code** – Development environment.

## 📂 Repository Structure

```text
FastAPI-for-Machine-Learning/
│
├── notebooks/
│   └── Learning_Notebooks.ipynb
│
├── code/
│   ├── basics/
│   ├── api_endpoints/
│   ├── request_response/
│   └── ml_model_api/
│
├── models/
│   └── model.pkl
│
├── requirements.txt
│
└── README.md
```

## ⚙️ Installation and Setup

**1. Clone the repository**

```bash
git clone <your-repository-url>
```

**2. Navigate to the project directory**

```bash
cd FastAPI-for-Machine-Learning
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the virtual environment**

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

**5. Install dependencies**

```bash
pip install fastapi uvicorn
```

## ▶️ Running a FastAPI Application

Start the development server:

```bash
uvicorn main:app --reload
```

Open the following URL in your browser:

- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 📚 Learning Resource

**YouTube Playlist:** FastAPI for Machine Learning – CampusX

[Watch the Complete Playlist](https://www.youtube.com/playlist?list=PLKnIA16_RmvZ41tjbKB2ZnwchfniNsMuQ)

## 💡 Why FastAPI?

FastAPI is useful for creating backend services that expose machine learning models through HTTP endpoints.

For example:

1. Train a machine learning model using Scikit-learn.
2. Save the trained model.
3. Load the model into a FastAPI application.
4. Create an API endpoint to accept user input.
5. Generate predictions and return them as JSON responses.

This makes it possible to integrate machine learning models into real-world applications.

## 📈 Learning Progress

- [ ] Understand FastAPI fundamentals.
- [ ] Learn HTTP methods and API endpoints.
- [ ] Understand request and response handling.
- [ ] Learn Pydantic and data validation.
- [ ] Build CRUD APIs.
- [ ] Integrate a machine learning model.
- [ ] Build a complete ML prediction API.

## 👨‍💻 Author
Syed Tabib Ashraf

Created as part of my journey towards becoming an AI/ML Engineer.

**Learning by doing, one concept at a time!** 🚀
