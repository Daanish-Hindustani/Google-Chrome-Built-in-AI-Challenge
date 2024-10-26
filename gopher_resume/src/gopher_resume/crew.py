from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from gopher_resume.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

# Importing crewAI tools
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
	FileWriterTool,
    SerperDevTool,
    WebsiteSearchTool
)

# Instantiate tools
dir_tool = DirectoryReadTool("../resumes")
file_tool = FileReadTool()
write_tool = FileWriterTool()
search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()


@CrewBase
class GopherResumeCrew():
	"""GopherResume crew"""

	@agent
	def resume_advisor(self) -> Agent:
		return Agent(
			config=self.agents_config['resume_advisor'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			tools=[web_rag_tool, search_tool, file_tool, dir_tool],
			verbose=True
		)

	@agent
	def resume_writter(self) -> Agent:
		return Agent(
			config=self.agents_config['resume_writter'],
			tools=[file_tool, dir_tool, write_tool],
			verbose=True
		)

	@task
	def resume_review_task(self) -> Task:
		return Task(
			config=self.tasks_config['resume_review_task'],
		)

	@task
	def resume_writing_task(self) -> Task:
		return Task(
			config=self.tasks_config['resume_writing_task'],
			output_file='Resume.pdf'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the GopherResume crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)