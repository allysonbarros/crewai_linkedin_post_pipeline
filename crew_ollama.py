import os
from crewai import Crew, Task, LLM

from agents.researcher import ResearcherAgent
from agents.writer import WriterAgent
from agents.reviewer import ReviewerAgent

class LinkedInContentCrew:
    def __init__(self):
        # Initialize clients
        self.tavily_api_key = os.getenv('TAVILY_API_KEY')
        self.groq_api_key = os.getenv('GROQ_API_KEY')
        self.llm = LLM(
            model="ollama/deepseek-r1",
            base_url="http://localhost:11434"
        )

       
        # Initialize agents
        self.researcher = ResearcherAgent(self.tavily_api_key, self.llm).create()
        self.writer = WriterAgent(self.groq_api_key, self.llm).create()
        self.reviewer = ReviewerAgent(self.groq_api_key, self.llm).create()
        

    def create_content(self, topic):
        """Create LinkedIn content without posting"""
        # Define research and writing tasks
        research_task = Task(
            description=f"Research this topic thoroughly: {topic}",
            agent=self.researcher,
            expected_output="Detailed research findings including key insights, trends, and statistics about the topic"
        )

        writing_task = Task(
            description="""
                Create an engaging LinkedIn Article from the research. 
                You approach serious topics related to business, and productivity in a professional way to make them more accessible to the general public.
                You must use emojis in each paragraph.
                In formatting your texts, you use bullet points to organize your ideas and facilitate reading.
                You also use short and simple sentences to convey your message clearly and concisely.
                Overall, your tone is optimistic and encouraging, with a touch of humor.
                Use a question at the end of your text to engage your audience and elicit their reaction. You consistently encourage interaction by inviting your audience to comment and share their own experiences.
                Include six relevant hashtags at the end of the post.
            """,
            agent=self.writer,
            expected_output="A well-crafted LinkedIn Article in Markdown with hashtags, engaging emojis and clear call-to-actions."
        )

        review_task = Task(
            description="Review and optimize the LinkedIn Article for maximum impact",
            agent=self.reviewer,
            expected_output="A refined and optimized version of the post with improved engagement potential while maintaining professionalism only and no furtherreasoning or explanation"
        )

        # Create and run content creation crew
        content_crew = Crew(
            agents=[self.researcher, self.writer, self.reviewer],
            tasks=[research_task, writing_task, review_task]
        )

        return content_crew.kickoff()

   

    def run(self, topic):
        """Complete workflow: Create and post content"""
        # First create the content
        print("\nPhase 1: Creating and reviewing LinkedIn content...")
        content = self.create_content(topic)
        print("\nContent created and reviewed successfully!")
        
        # # Then post it
        # print("\nPhase 2: Posting to LinkedIn...")
        # result = self.post_content(content)
        # print("\nPosting completed!")
        
        return {
            'content': content,
            #'posting_result': result
        } 