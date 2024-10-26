from crewai import Task
from agents import resume_advisor, resume_writer

# researcher task
resume_review_task = Task(
    description=( """
                        Conduct a thorough analysis of the resume. 
                        Research similar resumes and relevant information pertaining to the topics 
                        included in the resume. Based on insights from external sources and critiques 
                        of the current resume, construct a detailed response.
                 """
    ),
    expected_output="""A list of 10 detailed bullet points outlining the necessary improvements 
                        for the resume and recommendations on how it should be structured.
                    """
    ,
    
    agent=resume_advisor
)

# writing task with language model configuration
resume_writing_task = Task(
    description=( """
                    Review the provided feedback and expand each topic into a comprehensive section for the resume. 
                    Ensure that the resume is detailed, includes all relevant information, and maintains a cohesive structure.
                 """
    ),
    expected_output=""" A fully developed resume with each section complete and containing all necessary information. 
                        The resume should be properly formatted PDF file and free of any code blocks.
                    """,
    agent=resume_writer,
    output_file='Resume.pdf'
)