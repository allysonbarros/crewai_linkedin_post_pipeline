from crewai import Agent, LLM
from langchain.tools import Tool

class WriterAgent:
    def __init__(self, groq_api_key, llm):
        self.llm = LLM(
            model="ollama/gemma2:2b",
            base_url="http://localhost:11434"
        )

    def create(self):
        writing_tool = Tool(
            name="Write LinkedIn Post",
            func=self.write_post,
            description="Creates an engaging LinkedIn post from research findings"
        )

        return Agent(
            role='Content Writer',
            goal="""Create engaging LinkedIn posts from research briefs.
            Create a LinkedIn post based on this research: {research_brief}
        
        Follow these guidelines:
        - Keep it under 2000 characters
        - Include relevant hashtags
        - Use engaging hooks
        - Add engaging emojis
        - Add clear call-to-actions
        - Format with appropriate line breaks
        - Make it professional and thought-provoking
        - Add reference URLs if any in the {research_brief}""",
            backstory="""You are an expert LinkedIn content creator who knows 
            how to craft viral, engaging posts that drive professional discussions.
            Your goal is to create content that resonates with professionals and 
            generates meaningful engagement.""",
            llm=self.llm,
            #tools=[writing_tool],
            verbose=True
        )

    async def write_post(self, research_brief: str) -> str:
        """Transform research brief into LinkedIn post"""
        prompt = f"""Create a LinkedIn post based on this research:
        {research_brief}
        
        Follow these guidelines:
        - Keep it under 1300 characters
        - Include relevant hashtags
        - Use engaging hooks
        - Add engaging emojis
        - Add clear call-to-actions
        - Format with appropriate line breaks
        - Make it professional and thought-provoking"""

        response = self.llm(prompt)
        print("\nGenerated LinkedIn post:")
        print(response.content)
        return response.content 