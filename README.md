# CustomLogValidator (Python & Streamlit)

CustomLogValidator is a lightweight web application built with Python and Streamlit. It allows users to paste a multiline list of test names and cross-reference them against a raw log file to verify which tests actually executed.

## Features
* **Modern Web UI:** Built entirely in Python using Streamlit (no HTML/CSS required).
* **Responsive Layout:** Side-by-side inputs and a polished data table for results.
* **Metrics Dashboard:** Instantly see total, passed, and failed test counts.
* **Tested:** High reliability backed by Pytest.
* **Dockerized:** Easy to deploy and run anywhere.

---

## 🛠️ Prerequisites
* **Python 3.9+**
* **Docker** (optional, for containerized execution)

---

## 🚀 Local Setup & Installation

1. **Clone the repository**:
   \`\`\`bash
   git clone https://github.com/yourusername/CustomLogValidator.git
   cd CustomLogValidator
   \`\`\`

2. **Create a Virtual Environment (Recommended)**:
   \`\`\`bash
   python -m venv venv
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\\Scripts\\activate
   \`\`\`

3. **Install dependencies**:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

---

## 💻 Running the Application

To launch the Streamlit UI locally, run:
\`\`\`bash
streamlit run app.py
\`\`\`
*This will automatically open your default web browser to `http://localhost:8501`.*

---

## 🧪 Running Tests

This project uses **Pytest** for unit testing the core validation logic.
To run the test suite:
\`\`\`bash
pytest tests/
\`\`\`

---

## 🐳 Dockerization

You can run this application entirely within Docker without installing Python on your host machine.

### 1. Build the Docker Image
From the root of the project, run:
\`\`\`bash
docker build -t custom-log-validator-ui .
\`\`\`

### 2. Run the Docker Container
Launch the container and map port 8501 to your host machine:
\`\`\`bash
docker run -p 8501:8501 custom-log-validator-ui
\`\`\`

Once running, navigate to `http://localhost:8501` in your web browser to use the application.