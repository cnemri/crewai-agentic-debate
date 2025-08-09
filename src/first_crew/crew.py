from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class FirstCrew():
    """FirstCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def proponent(self) -> Agent:
        return Agent(
            config=self.agents_config['proponent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def opponent(self) -> Agent:
        return Agent(
            config=self.agents_config['opponent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def judge(self) -> Agent:
        return Agent(
            config=self.agents_config['judge'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def proponent_opening_statement_task(self) -> Task:
        return Task(config=self.tasks_config['proponent_opening_statement_task'])

    @task
    def opponent_opening_statement_task(self) -> Task:
        return Task(
            config=self.tasks_config['opponent_opening_statement_task'],
            context=[self.proponent_opening_statement_task()]
        )

    @task
    def proponent_rebuttal_1_task(self) -> Task:
        return Task(
            config=self.tasks_config['proponent_rebuttal_1_task'],
            context=[self.opponent_opening_statement_task()]
        )

    @task
    def opponent_rebuttal_1_task(self) -> Task:
        return Task(
            config=self.tasks_config['opponent_rebuttal_1_task'],
            context=[self.proponent_rebuttal_1_task()]
        )

    @task
    def proponent_rebuttal_2_task(self) -> Task:
        return Task(
            config=self.tasks_config['proponent_rebuttal_2_task'],
            context=[self.opponent_rebuttal_1_task()]
        )

    @task
    def opponent_rebuttal_2_task(self) -> Task:
        return Task(
            config=self.tasks_config['opponent_rebuttal_2_task'],
            context=[self.proponent_rebuttal_2_task()]
        )

    @task
    def proponent_rebuttal_3_task(self) -> Task:
        return Task(
            config=self.tasks_config['proponent_rebuttal_3_task'],
            context=[self.opponent_rebuttal_2_task()]
        )

    @task
    def opponent_rebuttal_3_task(self) -> Task:
        return Task(
            config=self.tasks_config['opponent_rebuttal_3_task'],
            context=[self.proponent_rebuttal_3_task()]
        )

    @task
    def proponent_closing_statement_task(self) -> Task:
        return Task(
            config=self.tasks_config['proponent_closing_statement_task'],
            context=[self.opponent_rebuttal_3_task()]
        )

    @task
    def opponent_closing_statement_task(self) -> Task:
        return Task(
            config=self.tasks_config['opponent_closing_statement_task'],
            context=[self.proponent_closing_statement_task()]
        )

    @task
    def judge_task(self) -> Task:
        return Task(
            config=self.tasks_config['judge_task'],
            context=[
                self.proponent_opening_statement_task(),
                self.opponent_opening_statement_task(),
                self.proponent_rebuttal_1_task(),
                self.opponent_rebuttal_1_task(),
                self.proponent_rebuttal_2_task(),
                self.opponent_rebuttal_2_task(),
                self.proponent_rebuttal_3_task(),
                self.opponent_rebuttal_3_task(),
                self.proponent_closing_statement_task(),
                self.opponent_closing_statement_task()
            ],
            output_file='debate_verdict.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the FirstCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
