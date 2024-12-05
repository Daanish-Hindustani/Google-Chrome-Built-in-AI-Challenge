from crewai import Task
from agents import resume_advisor, resume_writer

# researcher task
resume_review_task = Task(
    description=( """
                        Conduct a thorough analysis of the resume from {resume_path}. 
                        Research similar resumes and relevant information pertaining to the topics 
                        included in the resume. Based on insights from external sources and critiques 
                        of the current resume, construct a CRITIQUED RESUME.
                 """
    ),
    expected_output="""Give a rewritten resume text to the resume_writer agent, 
                        the output should hold the same context as the original 
                        resume but impoved. There so be no other TEXT THAT IS NOT RELATED TO THE RESUME
                    """
    ,
    
    agent=resume_advisor
)

# writing task with language model configuration
resume_writing_task = Task(
    description=( """
                    Given input from another agent, format the information into a clean, organized, stylish, and centered resume using HTML and CSS.

                        Requirements:
                        Background and Layout:

                        Overlay a subtle, professional gradient or pattern as the background.
                        Use a centered container for the resume content, with a light box-shadow and rounded edges.
                        Ensure consistent padding around the resume for visual appeal.
                        Typography:

                        Use Times New Roman for the entire resume.
                        Section titles and job titles should be bold, with a font size of 14px.
                        Descriptions and other text should have a font size of 12px.
                        Styling Sections:

                        Separate sections with a horizontal line or a styled divider.
                        Keep the content within each section left-aligned for readability while the overall resume remains centered.
                        Add some line spacing (e.g., line-height: 1.6) for clarity.
                        Header/Footer:

                        Center-align the header, including the name and contact details.
                        Use icons or links for contact methods (LinkedIn, GitHub, etc.).
                        Include a professional footer with the applicant's name and copyright information.
                        Responsive Design:

                        Ensure the resume looks polished on various screen sizes.
                        Keep margins proportional to the screen width for mobile-friendliness.


                 """
    ),
    expected_output=""" A fully developed resume with each section complete and containing all necessary information. 
                        The resume should be a formatted html file.
                    """,
    agent=resume_writer,
    output_file='my_resume.html'
)