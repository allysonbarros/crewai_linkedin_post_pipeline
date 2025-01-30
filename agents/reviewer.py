from crewai import Agent, LLM
from langchain.tools import Tool

class ReviewerAgent:
    def __init__(self, groq_api_key, llm):
        self.llm = LLM(
            model="ollama/gemma2:2b",
            base_url="http://localhost:11434"
        )

    def create(self):
        review_tool = Tool(
            name="Review LinkedIn Post",
            func=self.review_post,
            description="Reviews and refines LinkedIn posts for maximum impact"
        )

        return Agent(
            role='Content Reviewer',
            goal="""Review and optimize LinkedIn posts for maximum engagement and professionalism.
            Review and improve this LinkedIn post:
        {content}
        
        Analyze and improve the following aspects:
        1. Hook strength and opening impact
        2. Content clarity and flow
        3. Professional tone and language
        4. Emoji usage and placement
        5. Hashtag relevance and quantity
        6. Call-to-action effectiveness
        7. Overall engagement potential
        
        Provide the refined version of the post with your improvements.
        Keep the core message but enhance its impact and engagement potential.
        Ensure it remains under 2000 characters.
        DONOT PROVIDE EEXPLANATION OF THE IMPROVEMENTS.""",
            backstory="""You are an expert content reviewer specializing in LinkedIn posts. 
            You have a deep understanding of what makes content go viral on LinkedIn and 
            how to maintain professional standards while maximizing engagement. Your role 
            is to critique, refine, and enhance posts to ensure they achieve their maximum potential.""",
            llm=self.llm,
            #tools=[review_tool],
            verbose=True
        )

    async def review_post(self, content: str) -> str:
        """Review and refine the LinkedIn post"""
        prompt = f"""Review and improve this LinkedIn post:
        {content}
        
        Analyze and improve the following aspects:
        1. Hook strength and opening impact
        2. Content clarity and flow
        3. Professional tone and language
        4. Emoji usage and placement
        5. Hashtag relevance and quantity
        6. Call-to-action effectiveness
        7. Overall engagement potential
        
        Provide the refined version of the post with your improvements.
        Keep the core message but enhance its impact and engagement potential.
        Ensure it remains under 1300 characters."""

        response = await self.groq_llm.ainvoke(prompt)
        print("\nRefined LinkedIn post:")
        print(response.content)
        return response.content 