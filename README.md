# 🌱 Tiny Tasks

## Introduction

**Tiny Tasks** was created as part of Tech Sister's October 2024 AI Challenge, which was aimed at exploring **Large Language Models (LLMs)** and experimenting with the **Google Gemini API**. As someone who usees to-do lists every day, I developed **Tiny Tasks** to help boost my productivity with the help of **Generative AI**.

## Project Overview

**Tiny Tasks** is a productivity app that uses **generative AI** to break break-down high-level tasks that are input by the user into smaller, actionable subtasks. Functionalities include allowing users to add, view, edit, and delete both tasks and AI-generated subtasks. It was built using **Python**, **Google Gemini API**, and **Streamlit**.

You can access the Tiny Tasks app [here](https://tinytasks.streamlit.app/)!

## Getting Started

Follow these steps to locally run the Tiny Tasks app:

### Prerequisites

Make sure you have the following installed:
- Python (version 3.7 or higher) 🐍
- pip (Python package installer) 📦

### Steps to Locally Set Up App

1. **Clone this Repository** 💻
   - Open your terminal (or command prompt) and run the following command:
     ```bash
     git clone https://github.com/maggienegm/tech-sisters-ai-challenge.git
     ```

2. **Create a Virtual Environment** 🌱
   - Navigate to the root of the project directory:
     ```bash
     cd tech-sisters-ai-challenge
     ```
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

3. **Install Requirements** 📜
    - Before installing the necessary packages, make sure to navigate to the `/app` directory. You can do this by running the following command in your terminal:
        ```bash
        cd app
        ```
   - Install the necessary packages by running:
        ```bash
        pip install -r requirements.txt
        ```

4. **Run the Streamlit App** 🚀
    - To run the Streamlit application, use the following command in your terminal:
      ```bash
      streamlit run app.py
      ```
    - Once the app is running, you can access it in your web browser at http://localhost:8501.

## Future Improvements

- **UI Framework**: While Streamlit is great for rapid prototyping, it refreshes the entire app on each interaction, which can hinder the user experience. To address this, I would use a frontend framework like React or Vue.js, which would offer better control over UI components, efficient state management, and a more smoother, dynamic user interface without full page reloads.

- **Storage**: Currently, Streamlit's ```session_state``` doesn't persist data across sessions, meaning that users lose their progress after refreshing the page. To address this, I would implement persistent storage using a backend database or local storage to ensure data is retained between page sessions.