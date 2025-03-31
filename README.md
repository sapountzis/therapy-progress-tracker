# Therapy Progress Tracker

## Overview

This repository contains a Proof of Concept (POC) for tracking therapy progress, designed as part of the Machine Learning Engineer assignment. The project aims to provide an intuitive interface and a robust AI-driven backend to analyze therapy sessions and assess a patient's progress over time.

---

## Features

### 1. **User Interface**
   - A simple, user-friendly web interface built with **FastAPI** and **Jinja2** templates.
   - Allows therapists to:
     - Create and manage client profiles.
     - Upload structured therapy session data in JSON format.
     - Compare sessions to assess progress.

### 2. **AI-Powered Progress Assessment**
   - Employs advanced AI techniques to:
     - Analyze session data.
     - Generate meaningful insights into therapy progress.
     - Present results in a structured and actionable format.

### 3. **Documentation-Driven Design**
   - Based on predefined therapy templates: GAD-7, PHQ-9, BDI-II, HADS, PSS, WHO-5, PANSS, PSQI, AUDIT, CGI-S, Y-BOCS, BAI, MADRS, SF-36
   - Leverages **LangChain**, **LangFuse**, and **OpenAI GPT** models for assessing and tracking client progress.

---

## Technology Stack

| **Component**       | **Technology**                                 |
|----------------------|-----------------------------------------------|
| Backend Framework    | FastAPI                                       |
| Database             | PostgreSQL (via SQLModel)                     |
| AI Tools             | LangChain, LangGraph, LangFuse, OpenAI GPT    |
| Frontend             | Jinja2 Templates, Vanilla JS, CSS             |
| Containerization     | Docker, Docker Compose                        |

---

## Key Components

### 1. **Therapy Progress Tracker UI**
- **Tabs**:
  - Manage Sessions: Create clients, upload sessions, and view session details.
  - Compare Progress: Select two sessions and generate progress insights.
- **Interactive Forms**:
  - Client creation.
  - Session upload.
  - Session comparison.
- **Dynamic Features**:
  - Fetch and display client sessions.
  - Display detailed session summaries and clinical assessments.

### 2. **AI Workflow**
- **Agents**:
  - An `Agent` class implemented as a singleton to ensure efficient and consistent AI interactions.
  - Uses a state graph to manage AI workflows.
- **Session Comparison**:
  - Extracts and compares session data to identify trends in symptom severity and frequency.
  - Produces structured outputs, including a progress summary and reasoning.

---

## File Structure

```
progress_tracker/
├── app/
│   ├── core/                     # Core application logic
│   │   ├── agent/                # AI Agents and State Management
│   │   ├── settings.py           # Environment settings
│   ├── models/                   # Database models
│   ├── routes/                   # FastAPI routes
│   ├── schemas/                  # Data validation schemas
│   ├── static/                   # JavaScript and CSS
│   ├── templates/                # HTML templates
│   ├── dependencies.py           # Dependency injections
│   ├── main.py                   # Application entry point
├── .dockerignore                 # Docker ignore file
├── Dockerfile                    # Docker build configuration
├── pyproject.toml                # Project dependencies
├── docker-compose.yml            # Docker Compose configuration
```

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-private-repo/therapy-tracker.git
cd therapy-tracker
```

### 2. Configure Environment
- Create a `.env` file in the root directory with the following:
- Create a `progress_tracker.env` file in the `progress_tracker/` directory with the following:

### 3. Build and Run Services
Use Docker Compose to build and start the application.
```bash
docker-compose up --build
```

### 4. Access the Application
Visit [http://localhost:8000](http://localhost:8000) in your browser.

---

## Usage

### 1. **Manage Sessions**
- Create a new client.
- Upload structured JSON files for client sessions.
- View details of all uploaded sessions.

### 2. **Compare Progress**
- Select a client and two of their sessions.
- Submit the comparison form to generate progress insights.

---

## Technical Approach

### 1. **AI Model**
- **Session Analysis**:
  - Decomposes session data into meaningful components using LangChain and LangGraph.
  - Scores symptom metrics (e.g., severity, frequency).
- **Progress Evaluation**:
  - Analyzes trends across sessions using predefined templates and prompts.
  - Outputs progress assessments with reasoning.

### 2. **Multi-Agent System**
- **State Management**:
  - Implements a state graph for structured workflow execution.
- **Node Functions**:
  - `process_sessions`: Prepares session data for analysis.
  - `generate_score`: Computes symptom scores.
  - `compare_progress`: Synthesizes insights into overall progress.

### 3. **Frontend**
- Implements tab-based navigation for simplicity.
- Employs dynamic session rendering with JavaScript.

---

## Contact

For any questions or feedback, please reach out to:

- Andreas Sapountzis  
- Email: [sapountzis.andreas@gmail.com](mailto:sapountzis.andreas@gmail.com)

---

### License

This project is for evaluation purposes only and is not intended for production use.

