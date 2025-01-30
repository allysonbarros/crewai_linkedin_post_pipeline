from crew import LinkedInContentCrew
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

def streamlit_app():
    st.title("LinkedIn Content Creation and Posting")
    
    topic = st.text_input("Enter the topic for your LinkedIn post:")
    
    if st.button("Generate Content"):
        if topic:
            content_crew = LinkedInContentCrew()
            
            with st.spinner("Generating..."):
                result = content_crew.run(topic)
            
                st.write(f"\nGenerated Content:")
                st.markdown((result['content']), unsafe_allow_html=True)
                        
            st.success("Process completed successfully!")
        else:
            st.error("Please enter the topic.")

if __name__ == "__main__":
    streamlit_app()