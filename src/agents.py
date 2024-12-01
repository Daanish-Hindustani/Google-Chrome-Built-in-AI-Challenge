import os
from crewai import Agent
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import tools 
from crewai_tools import (
    SerperDevTool,
)
load_dotenv()
#os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')
os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')

# inititlaize the tool for internet searching capabilities
# search_tool = SerperDevTool()



# call gemini model
llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash',
                            verbose=True,
                            temperature=0.5,
                            goggle_api_key=os.getenv('GOOGLE_API_KEY'))               

# create a senior researcher agent with memory and verbose mode

resume_advisor = Agent(
        role="Resume Advisor",
        goal="Give feedback on potential improvements to a resume given {resume_path}.",
        verbose=True,
        memory=True,
        backstory=( """
                        You're a seasoned recruiter with a keen eye for the latest trends 
                        and best practices in resume writing. Renowned for your ability to 
                        identify relevant strengths and suggest impactful adjustments, 
                        you excel at presenting information in a clear, concise manner 
                        tailored to each individual's career goals.
                   """
        ),
        tools=[tools.pdf_reader],
        llm=llm,
        allow_delegation=True
)

# creating a write agent with custom tools responsible in writing news blog

resume_writer = Agent(
    role="Resume Writer ",
    goal="""
            Craft a polished resume incorporating the suggested improvements 
            while ensuring consistent formatting and ATS compatibility. Use {template_path} as an reference.
         """,
    verbose=True,
    memory=True,
    backstory=("""
                    You are a meticulous analyst with a sharp eye for detail, 
                    recognized for your ability to transform complex information
                    into clear and concise documents. Your expertise ensures that 
                    resumes not only highlight key qualifications effectively but also 
                    meet the stringent requirements of Applicant Tracking Systems (ATS),
                    making it easier for candidates to stand out in the hiring process.
                    Please write it back to the resume {resume_path}.
               """
    ),
    tools=[],
    llm=llm,
    allow_delegation=False
)