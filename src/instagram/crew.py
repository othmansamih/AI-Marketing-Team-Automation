from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from instagram.tools.search_tools import SearchTools

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Instagram():
	"""Instagram crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def market_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['market_researcher'],
			tools=[
				SearchTools.search_internet,
				SearchTools.search_instagram,
				SearchTools.open_webpage
			],
			verbose=True
		)

	@agent
	def copy_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['copy_writer'],
			verbose=True
		)
	
	@agent
	def visual_artist(self) -> Agent:
		return Agent(
			config=self.agents_config['visual_artist'],
			allow_delegation=False,
			verbose=True
		)

	@agent
	def content_strategist(self) -> Agent:
		return Agent(
			config=self.agents_config['content_strategist'],
			verbose=True
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def market_research_task(self) -> Task:
		return Task(
			config=self.tasks_config['market_research_task'],
			agent=self.market_researcher(),
			output_file="tasks/1_market_research_task.md"
		)
	
	@task
	def content_calendar_task(self) -> Task:
		return Task(
			config=self.tasks_config['content_calendar_task'],
			agent=self.content_strategist(),
			output_file="tasks/2_content_calendar_task.md"
		)
	
	@task
	def copy_writing_task(self) -> Task:
		return Task(
			config=self.tasks_config['copy_writing_task'],
			agent=self.copy_writer(),
			output_file="tasks/3_copy_writing_task.md"
		)
	
	@task
	def image_description_task(self) -> Task:
		return Task(
			config=self.tasks_config['image_description_task'],
			agent=self.visual_artist(),
			output_file="tasks/4_image_description_task.md"
		)
	
	@task
	def compile_weekly_content_task(self) -> Task:
		return Task(
			config=self.tasks_config['compile_weekly_content_task'],
			agent=self.content_strategist(),
			output_file="tasks/5_compile_weekly_content_task.md"
		)


	@crew
	def crew(self) -> Crew:
		"""Creates the Instagram crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
