# LinkedIn Content Crew

This project is designed to automate the creation of LinkedIn content using AI agents. The agents are responsible for researching a topic, writing an article, reviewing the content, and generating relevant code examples to enrich the article.

## Technologies Used

- **Python**: The main programming language used for the project.
- **CrewAI**: A framework for creating and managing AI agents.
- **LangChain**: A library for building language model applications.
- **LLM (Large Language Model)**: Used for generating content and code examples.
- **Tavily API**: Used for research purposes.
- **Groq API**: Used for writing and reviewing content.

## Project Structure

- **src/crew.py**: Contains the main class `LinkedInContentCrew` which orchestrates the content creation process.
- **src/ai_agents.py**: Contains the implementation of various AI agents including `ResearcherAgent`, `WriterAgent`, `ReviewerAgent`, and `CoderAgent`.
- **src/utils/__init__.py**: Utility functions and classes used across the project.
- **requirements.txt**: Lists the dependencies required for the project.
- **README.md**: This file.

## How to Run the Application

1. **Clone the repository**:
    ```bash
    git clone https://github.com/allysonbarros/crewai_linkedin_post_pipeline
    cd crewai_linkedin_post_pipeline
    ```

2. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:
    Create a [.env](http://_vscodecontentref_/2) file in the root directory and add your API keys:
    ```env
    TAVILY_API_KEY=your_tavily_api_key
    GROQ_API_KEY=your_groq_api_key
    ```

4. **Run the application**:
    ```bash
    streamlit main.py
    ```