from crewai import Crew, Process
from tasks import resume_review_task, resume_writing_task
from agents import resume_advisor, resume_writer


# forming the tech focused crew with some enhanced configuration
crew = Crew(
    agents=[resume_advisor, resume_writer],
    tasks=[resume_review_task, resume_writing_task],
    process=Process.sequential,
)

# starting the task execution process with enhanced feedback

result = crew.kickoff(inputs={'topic': 'AI in healthcare'})
print(result)