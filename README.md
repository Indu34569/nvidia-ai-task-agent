# NVIDIA AI Task Agent

An AI-powered command-line task assistant built with Python and NVIDIA AI.

The project accepts natural-language requests and uses an LLM to generate practical responses, study plans, project ideas, and task guidance. It also maintains a local history of previous tasks.

## Features

- Natural-language task input
- AI-powered responses using NVIDIA AI
- Command-line interface
- Persistent task history
- `history` command to review previous tasks
- `exit` / `quit` commands
- Simple Python implementation
- Environment-variable based API key configuration

## Tech Stack

- Python
- NVIDIA AI API
- OpenAI Python SDK
- `openai/gpt-oss-20b`
- Git & GitHub
- Command-line interface

## How It Works

```text
User
  ↓
Command-line interface
  ↓
Python task agent
  ↓
NVIDIA AI API
  ↓
GPT-OSS model
  ↓
AI-generated response
  ↓
Task history
Project Structure
switch-practice/
├── task_agent.py
├── README.md
├── requirements.txt
├── .gitignore
└── task_history.txt

Setup
1. Clone the repository
git clone https://github.com/Indu34569/nvidia-ai-task-agent.git
cd nvidia-ai-task-agent

2. Install dependencies
python3 -m pip install -r requirements.txt

3. Configure your NVIDIA API key
Set your API key as an environment variable.
export NVIDIA_API_KEY="your-real-nvidia-api-key"

For permanent configuration on macOS with zsh, add the variable to ~/.zshrc.

Never commit your API key to GitHub.
4. Run the agent
python3 task_agent.py

Example
What do you need help with? help me make a Python study plan

Thinking...

[AI-generated study plan]

You can also type:
history

to view previous tasks.

Use:
exit

or:
quit

to close the application.
Why I Built This
This project was created as a hands-on learning project to explore:
- Python development
- AI/LLM API integration
- Command-line applications
- Prompt design
- Environment variables and API security
- Git and GitHub workflows
- Building practical AI agents
Future Improvements
- Streaming AI responses
- Better error handling and retry logic
- Configurable AI models
- Structured task categories
- Exportable task history
- Web interface
- Automated tests
- Docker support
Learning Project
This project is part of my journey into Python, AI agents, and practical LLM application development.

